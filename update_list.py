import requests
import os
import sys
from multiprocessing import Pool, cpu_count
from datetime import datetime

# --- GRUPPE 1: MASTER SOURCES (Diese landen in der kombinierten Liste) ---
MASTER_SOURCES = {
    "techrzn_ads": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_ads.txt", "TechRZN Ads"),
    "techrzn_tracking": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_tracking.txt", "TechRZN Tracking"),
    "techrzn_malware": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_malware.txt", "TechRZN Malware"),
    "techrzn_phishing": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_phishing.txt", "TechRZN Phishing"),
    "techrzn_threat_intel": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_threat_intel.txt", "TechRZN Threat Intel"),
    "techrzn_fakeshops": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_fakeshops.txt", "TechRZN Fakeshops"),
    "techrzn_squatting": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_domain_squatting.txt", "TechRZN Squatting"),
    "techrzn_gambling": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_gambling.txt", "TechRZN Gambling"),
    "techrzn_crypto": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_crypto.txt", "TechRZN Crypto"),
    "techrzn_dating": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_dating.txt", "TechRZN Dating"),
    "techrzn_spam": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_spam.txt", "TechRZN Spam"),
    "techrzn_fake_science": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_fake_science.txt", "TechRZN Fake Science"),
    "techrzn_bypass": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_bypass.txt", "TechRZN Bypass"),
    "techrzn_ips": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/techrzn_ips.txt", "TechRZN IPs"),
    "hagezi_pro": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_48.txt", "HaGeZi Pro"),
    "urlhaus_malicious": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_11.txt", "URLHaus"),
    "adguard_german": ("https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_6_German/filter.txt", "AdGuard German"),
    "dan_pollock": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_4.txt", "Dan Pollock"),
    "notserious": ("https://raw.githubusercontent.com/notserious/Anti-FakeShop/main/fakeshops.txt", "Anti-Fakeshop")
}

# --- GRUPPE 2: SPECIAL SOURCES (Werden einzeln verarbeitet, NICHT im Master) ---
SPECIAL_SOURCES = {
    "techrzn_porn": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_porn.txt", "TechRZN Porn"),
    "techrzn_jugendschutz": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_jugendschutz.txt", "TechRZN Jugendschutz")
}

REMOTE_WHITELIST_URL = "https://raw.githubusercontent.com/hagezi/dns-blocklists/refs/heads/main/adblock/whitelist-referral.txt"

def clean_line(line):
    if not line: return None
    line = line.strip()
    if line and not line.startswith(('#', '!', '[', ' ')):
        cleaned = line.replace('||', '').replace('^', '')
        return cleaned.split('#')[0].split('!')[0].strip()
    return None

def process_source(args):
    name, url, credit, whitelist_set = args
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        lines = r.text.splitlines()
        raw_count = len(lines)
        
        individual_set = set()
        for line in lines:
            cleaned = clean_line(line)
            if cleaned and cleaned not in whitelist_set:
                individual_set.add(cleaned)
        
        os.makedirs("lists", exist_ok=True)
        with open(os.path.join("lists", f"{name}.txt"), "w", encoding='utf-8') as f:
            f.write(f"# TechRZN Module: {name} | Source: {credit}\n\n")
            f.write("\n".join(sorted(individual_set)))
            
        return list(individual_set), raw_count
    except Exception:
        return [], 0

def main():
    final_whitelist = set()
    try:
        if os.path.exists("whitelist.txt"):
            with open("whitelist.txt", "r", encoding='utf-8', errors='ignore') as f:
                for line in f:
                    d = clean_line(line)
                    if d: final_whitelist.add(d.replace('*.', ''))
        r_white = requests.get(REMOTE_WHITELIST_URL, timeout=15)
        if r_white.status_code == 200:
            for line in r_white.text.splitlines():
                d = clean_line(line)
                if d: final_whitelist.add(d)
    except: pass

    # --- Verarbeitung beider Gruppen ---
    # Wir werfen alles in den Pool, damit die Einzel-Listen in /lists/ erstellt werden
    ALL_SOURCES = {**MASTER_SOURCES, **SPECIAL_SOURCES}
    tasks = [(name, url, credit, final_whitelist) for name, (url, credit) in ALL_SOURCES.items()]
    
    with Pool(processes=cpu_count()) as pool:
        results_map = pool.map(process_source, tasks)
        # Erstelle ein Mapping von Name zu Ergebnis
        results_dict = dict(zip(ALL_SOURCES.keys(), results_map))

    # --- Master Deduplizierung (Nur MASTER_SOURCES) ---
    master_domains = []
    total_raw_lines = 0
    for name in MASTER_SOURCES.keys():
        domains, raw_count = results_dict[name]
        master_domains.extend(domains)
        total_raw_lines += raw_count

    combined_set = set(master_domains)
    duplicates_removed = total_raw_lines - len(combined_set)
    timestamp = datetime.now().strftime("%d. %B %Y um %H:%M")

    # Speichern der Master-Liste
    try:
        with open("combined_blocklist.txt", "w", encoding='utf-8') as f:
            f.write("############################################################\n")
            f.write("# TechRZN Master Blocklist - All-in-One (Performance)\n")
            f.write("# Ohne Jugendschutz / Porn - für maximale Kompatibilität\n")
            f.write(f"# Aktualisiert: {timestamp}\n")
            f.write(f"# Roh-Einträge: ca. {total_raw_lines:,}\n".replace(',', '.'))
            f.write(f"# Einzigartige Regeln: {len(combined_set):,}\n".replace(',', '.'))
            f.write("############################################################\n\n")
            f.write("\n".join(sorted(combined_set)))
        print(f"✨ Master-Liste erstellt: {len(combined_set)} Regeln.")
    except Exception as e:
        print(f"Fehler Master-Liste: {e}")

    # --- Spezial-Listen (Jugendschutz / Porn separat speichern) ---
    for name in SPECIAL_SOURCES.keys():
        domains, raw_count = results_dict[name]
        if domains:
            output_file = f"techrzn_{name.split('_')[1]}.txt" # Ergibt techrzn_porn.txt etc.
            with open(output_file, "w", encoding='utf-8') as f:
                f.write(f"# TechRZN Special Module: {name.upper()}\n")
                f.write(f"# Stand: {timestamp} | Regeln: {len(domains)}\n\n")
                f.write("\n".join(sorted(domains)))
            print(f"🔞 Spezial-Liste erstellt: {output_file}")

if __name__ == "__main__":
    main()
