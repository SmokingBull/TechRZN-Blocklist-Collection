import requests
import os

# Definition der Quellen mit Kategorien
SOURCES = {
    "adguard_main": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_48.txt",
    "adguard_security": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_52.txt",
    "threat_intel": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_44.txt",
    "techrzn_custom": "https://raw.githubusercontent.com/SmokingBull/malicious-ip-blocklist/refs/heads/main/deny-ip-list.txt",
    "windows_telemetry": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_63.txt",
    "german_filter": "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_6_German/filter.txt",
    "hagezi_gambling": "https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/gambling.mini.txt",
    "hagezi_fake": "https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/fake.txt",
    "smart_tv": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_4.txt"
}

def clean_line(line):
    line = line.strip()
    if line and not line.startswith(('#', '!', '[', ' ')):
        return line.split('#')[0].split('!')[0].strip()
    return None

def main():
    combined_set = set()
    
    # Ordner für Einzel-Listen erstellen falls nicht da
    if not os.path.exists("lists"):
        os.makedirs("lists")

    for name, url in SOURCES.items():
        try:
            print(f"Verarbeite: {name}")
            r = requests.get(url, timeout=15)
            lines = r.text.splitlines()
            
            individual_list = []
            for line in lines:
                cleaned = clean_line(line)
                if cleaned:
                    individual_list.append(cleaned)
                    combined_set.add(cleaned)
            
            # Einzelne Liste speichern
            with open(f"lists/{name}.txt", "w") as f:
                f.write(f"# TechRZN {name} Blocklist\n# Einträge: {len(individual_list)}\n\n")
                for item in sorted(set(individual_list)):
                    f.write(f"{item}\n")
                    
        except Exception as e:
            print(f"Fehler bei {name}: {e}")

    # Die große kombinierte Liste speichern
    with open("combined_blocklist.txt", "w") as f:
        f.write(f"# TechRZN Combined Masterlist\n# Einträge gesamt: {len(combined_set)}\n\n")
        for item in sorted(combined_set):
            f.write(f"{item}\n")

    print(f"Fertig! Masterliste und {len(SOURCES)} Einzellisten erstellt.")

if __name__ == "__main__":
    main()
