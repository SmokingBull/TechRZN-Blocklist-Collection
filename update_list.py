import requests
import os
import sys
from multiprocessing import Pool, cpu_count
from datetime import datetime

# Deine Quellen (identisch mit deinem Setup)
SOURCES = {
    "techrzn_tracking": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_tracking.txt", "TechRZN Tracking"),
    "hagezi_pro": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_48.txt", "HaGeZi Pro"),
    "hagezi_bypass": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_52.txt", "HaGeZi Bypass"),
    "hagezi_threat": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_44.txt", "HaGeZi Threat"),
    "techrzn_ips": ("https://raw.githubusercontent.com/SmokingBull/malicious-ip-blocklist/main/deny-ip-list.txt", "TechRZN IPs"),
    "hagezi_windows": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_63.txt", "HaGeZi Windows"),
    "smart_tv": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_7.txt", "Smart TV"),
    "urlhaus_malicious": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_11.txt", "URLHaus"),
    "hagezi_gambling": ("https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/gambling.mini.txt", "HaGeZi Gambling"),
    "hagezi_fake": ("https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/fake.txt", "HaGeZi Fake"),
    "adguard_german": ("https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_6_German/filter.txt", "AdGuard German"),
    "dan_pollock": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_4.txt", "Dan Pollock"),
    "notserious": ("https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/notserious", "Anti-Fakeshop"),
    "phishing_de": ("https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Phishing-Angriffe", "Banking-Schutz"),
    "fake_science": ("https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Fake-Science", "Fake-Science")
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
    # Whitelist Logik (bleibt gleich)
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

    tasks = [(name, url, credit, final_whitelist) for name, (url, credit) in SOURCES.items()]
    
    with Pool(processes=cpu_count()) as pool:
        results_data = pool.map(process_source, tasks)

    all_domains = []
    total_raw_lines = 0
    for domains, raw_count in results_data:
        all_domains.extend(domains)
        total_raw_lines += raw_count

    # Master Deduplizierung
    combined_set = set(all_domains)
    duplicates_removed = total_raw_lines - len(combined_set)
    timestamp = datetime.now().strftime("%d. %B %Y um %H:%M")

    try:
        with open("combined_blocklist.txt", "w", encoding='utf-8') as f:
            f.write("############################################################\n")
            f.write("# TechRZN Master Blocklist - All-in-One\n")
            f.write(f"# Aktualisiert: {timestamp}\n")
            f.write(f"# Roh-Einträge: ca. {total_raw_lines:,}\n".replace(',', '.'))
            f.write(f"# Einzigartige Regeln: {len(combined_set):,}\n".replace(',', '.'))
            f.write(f"# Entfernte Duplikate: {duplicates_removed:,}\n".replace(',', '.'))
            f.write("############################################################\n\n")
            f.write("\n".join(sorted(combined_set)))
        print(f"✨ Master-Liste erstellt: {len(combined_set)} Regeln (Dedupliziert).")
    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    main()
