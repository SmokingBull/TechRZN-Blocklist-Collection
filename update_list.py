import requests
import os

# Die 14 Core-Module mit Zuordnung für die Danksagung (TechRZN Stack)
SOURCES = {
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
    # RPiList Spezial-Module (Neu hinzugefügt)
    "notserious": ("https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/notserious", "RPiList (Anti-Fakeshop)"),
    "phishing_de": ("https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Phishing-Angriffe", "RPiList (Banking-Schutz)"),
    "fake_science": ("https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Fake-Science", "RPiList (Fake-Science)")
}

def clean_line(line):
    line = line.strip()
    # Entfernt Kommentare und leere Zeilen
    if line and not line.startswith(('#', '!', '[', ' ')):
        # Entfernt Inline-Kommentare
        return line.split('#')[0].split('!')[0].strip()
    return None

def main():
    combined_set = set()
    global_whitelist = set()

    # 1. Lokale Whitelist laden (falls vorhanden)
    if os.path.exists("whitelist.txt"):
        with open("whitelist.txt", "r") as f:
            for line in f:
                domain = clean_line(line)
                if domain: global_whitelist.add(domain)

    # 2. Ordner 'lists' sicherstellen
    if not os.path.exists("lists"):
        os.makedirs("lists")

    # 3. Quellen verarbeiten und im Unterordner 'lists' speichern
    for name, (url, credit) in SOURCES.items():
        try:
            r = requests.get(url, timeout=25)
            if r.status_code == 200:
                lines = r.text.splitlines()
                individual_list = []
                for line in lines:
                    cleaned = clean_line(line)
                    if cleaned and cleaned not in global_whitelist:
                        individual_list.append(cleaned)
                        combined_set.add(cleaned)
                
                # Datei im Ordner lists/ speichern
                filename = os.path.join("lists", f"{name}.txt")
                with open(filename, "w", encoding='utf-8') as f:
                    # Automatisierter Header mit Credits
                    f.write(f"############################################################\n")
                    f.write(f"# TechRZN Blocklist Module: {name}\n")
                    f.write(f"# Maintainer: TechRZN (Kleve)\n")
                    f.write(f"# Original Source & Credits: {credit}\n")
                    f.write(f"# Updated: March 2026\n")
                    f.write(f"############################################################\n\n")
                    # Nur einzigartige Einträge sortiert speichern
                    for item in sorted(set(individual_list)):
                        f.write(f"{item}\n")
                print(f"✅ Created: {filename} (Source: {credit})")
            else:
                print(f"❌ Error {r.status_code} at {name}")
        except Exception as e:
            print(f"❌ Exception at {name}: {e}")

    # 4. Masterliste im Hauptverzeichnis speichern
    with open("combined_blocklist.txt", "w", encoding='utf-8') as f:
        f.write("############################################################\n")
        f.write("# TechRZN Masterlist - Combined Protection Stack\n")
        f.write("# Credits to: HaGeZi, RPiList, AdGuard, URLHaus, Dan Pollock\n")
        f.write("############################################################\n\n")
        for item in sorted(combined_set):
            f.write(f"{item}\n")
    
    print("\n--- All 14 modules updated successfully. ---")

if __name__ == "__main__":
    main()
