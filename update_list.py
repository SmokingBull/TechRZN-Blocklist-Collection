import requests
import os

# Die 14 Core-Module für TechRZN
SOURCES = {
    "hagezi_pro": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_48.txt",
    "bypass": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_52.txt",
    "threat_intel": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_44.txt",
    "techrzn_ips": "https://raw.githubusercontent.com/SmokingBull/malicious-ip-blocklist/main/deny-ip-list.txt",
    "windows_spy": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_63.txt",
    "smart_tv": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_7.txt",
    "urlhaus": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_11.txt",
    "gambling": "https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/gambling.mini.txt",
    "fake_dns": "https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/fake.txt",
    "german_filter": "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_6_German/filter.txt",
    "dan_pollock": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_4.txt",
    "notserious": "https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/notserious",
    "phishing_de": "https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Phishing-Angriffe",
    "fake_science": "https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Fake-Science"
}

def clean_line(line):
    line = line.strip()
    if line and not line.startswith(('#', '!', '[', ' ')):
        return line.split('#')[0].split('!')[0].strip()
    return None

def main():
    combined_set = set()
    global_whitelist = set()

    # 1. Lokale Whitelist laden
    if os.path.exists("whitelist.txt"):
        with open("whitelist.txt", "r") as f:
            for line in f:
                domain = clean_line(line)
                if domain: global_whitelist.add(domain)

    # 2. Quellen verarbeiten und direkt im Hauptverzeichnis speichern
    for name, url in SOURCES.items():
        try:
            r = requests.get(url, timeout=20)
            if r.status_code == 200:
                lines = r.text.splitlines()
                individual_list = []
                for line in lines:
                    cleaned = clean_line(line)
                    if cleaned and cleaned not in global_whitelist:
                        individual_list.append(cleaned)
                        combined_set.add(cleaned)
                
                # Speichert die Datei direkt als name.txt (z.B. notserious.txt)
                filename = f"{name}.txt"
                with open(filename, "w", encoding='utf-8') as f:
                    f.write(f"# TechRZN Blocklist Module: {name}\n")
                    f.write(f"# Source: {url}\n\n")
                    for item in sorted(set(individual_list)):
                        f.write(f"{item}\n")
                print(f"✅ Created: {filename}")
            else:
                print(f"❌ Error {r.status_code} at {name}")
        except Exception as e:
            print(f"❌ Exception at {name}: {e}")

    # 3. Masterliste speichern
    with open("combined_blocklist.txt", "w", encoding='utf-8') as f:
        f.write("# TechRZN Masterlist - Combined Protection Stack\n\n")
        for item in sorted(combined_set):
            f.write(f"{item}\n")
    
    print("\n--- All 14 files updated in root directory. ---")

if __name__ == "__main__":
    main()
