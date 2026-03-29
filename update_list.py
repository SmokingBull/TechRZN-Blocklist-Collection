import requests
import os
import sys
from multiprocessing import Pool, cpu_count

# Die TechRZN Module inkl. dem neuen Tracking-Modul
SOURCES = {
    "techrzn_tracking": ("https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/blocklists/techrzn_tracking.txt", "TechRZN (Tracking Master)"),
    "hagezi_pro": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_48.txt", "HaGeZi (Gold Standard)"),
    "hagezi_bypass": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_52.txt", "HaGeZi (VPN/Proxy)"),
    "hagezi_threat": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_44.txt", "HaGeZi (Threat Intel)"),
    "techrzn_ips": ("https://raw.githubusercontent.com/SmokingBull/malicious-ip-blocklist/main/deny-ip-list.txt", "SmokingBull / TechRZN"),
    "hagezi_windows": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_63.txt", "HaGeZi (Windows Telemetry)"),
    "smart_tv": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_7.txt", "AdGuard / TechRZN"),
    "urlhaus_malicious": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_11.txt", "Abuse.ch (URLHaus)"),
    "hagezi_gambling": ("https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/gambling.mini.txt", "HaGeZi (Gambling)"),
    "hagezi_fake": ("https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/fake.txt", "HaGeZi (Fake DNS)"),
    "adguard_german": ("https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_6_German/filter.txt", "AdGuard Team"),
    "dan_pollock": ("https://adguardteam.github.io/HostlistsRegistry/assets/filter_4.txt", "Dan Pollock (Classic)"),
    "notserious": ("https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/notserious", "RPiList (Anti-Fakeshop)"),
    "phishing_de": ("https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Phishing-Angriffe", "RPiList (Banking-Schutz)"),
    "fake_science": ("https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Fake-Science", "RPiList (Fake-Science)")
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
    """Verarbeitet eine einzelne Quelle parallel."""
    name, url, credit, whitelist_set = args
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        lines = r.text.splitlines()
        
        individual_set = set()
        for line in lines:
            cleaned = clean_line(line)
            if cleaned and cleaned not in whitelist_set:
                individual_set.add(cleaned)
        
        # Datei lokal speichern
        os.makedirs("lists", exist_ok=True)
        with open(os.path.join("lists", f"{name}.txt"), "w", encoding='utf-8') as f:
            f.write(f"# TechRZN Module: {name} | Source: {credit}\n\n")
            f.write("\n".join(sorted(individual_set)))
            
        print(f"✅ Finished: {name} ({len(individual_set)} unique domains)")
        return individual_set
    except Exception as e:
        print(f"❌ Error in {name}: {e}")
        return set()

def main():
    final_whitelist = set()

    # 1. Whitelists laden (wie gehabt)
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
        
        # Whitelist speichern
        with open("whitelist.txt", "w", encoding='utf-8') as f:
            f.write("# TechRZN-DNS - Master Whitelist\n\n")
            f.write("\n".join(sorted(final_whitelist)))
    except Exception as e:
        print(f"⚠️ Whitelist Error: {e}")

    # 2. Multiprocessing Vorbereitung
    tasks = [(name, url, credit, final_whitelist) for name, (url, credit) in SOURCES.items()]
    
    print(f"🚀 Starting parallel processing with {cpu_count()} cores...")
    
    # 3. Parallel alle Quellen abarbeiten
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(process_source, tasks)

    # 4. Master-Liste erstellen (Deduplizierung)
    print("🧹 Deduplicating all lists to Master...")
    combined_set = set().union(*results)

    try:
        with open("combined_blocklist.txt", "w", encoding='utf-8') as f:
            f.write("# TechRZN Master Blocklist - All-in-One\n")
            f.write(f"# Total unique entries: {len(combined_set)}\n\n")
            f.write("\n".join(sorted(combined_set)))
        print(f"\n✨ Success! Master list contains {len(combined_set)} entries.")
    except Exception as e:
        print(f"❌ Final Save Error: {e}")

if __name__ == "__main__":
    main()
