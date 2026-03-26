import requests
import os

# Deine 11 Quellen
SOURCES = {
    "hagezi_pro": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_48.txt",
    "hagezi_bypass": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_52.txt",
    "hagezi_threat": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_44.txt",
    "techrzn_ips": "https://raw.githubusercontent.com/SmokingBull/malicious-ip-blocklist/refs/heads/main/deny-ip-list.txt",
    "hagezi_windows": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_63.txt",
    "smart_tv": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_7.txt",
    "urlhaus_malicious": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_11.txt",
    "hagezi_gambling": "https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/gambling.mini.txt",
    "hagezi_fake": "https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/fake.txt",
    "adguard_german": "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_6_German/filter.txt",
    "dan_pollock": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_4.txt"
}

# NEU: Die HaGeZi Whitelist URL
HAGEZI_WHITELIST_URL = "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/whitelist-referral.txt"

def clean_line(line):
    line = line.strip()
    if line and not line.startswith(('#', '!', '[', ' ')):
        return line.split('#')[0].split('!')[0].strip()
    return None

def main():
    combined_set = set()
    whitelist = set()

    # 1. Deine eigene lokale Whitelist laden
    if os.path.exists("whitelist.txt"):
        with open("whitelist.txt", "r") as f:
            for line in f:
                domain = clean_line(line)
                if domain: whitelist.add(domain)

    # 2. Die externe HaGeZi Whitelist laden
    try:
        print("Lade HaGeZi Referral Whitelist...")
        r_white = requests.get(HAGEZI_WHITELIST_URL, timeout=15)
        for line in r_white.text.splitlines():
            domain = clean_line(line)
            if domain: whitelist.add(domain)
    except Exception as e:
        print(f"Hinweis: HaGeZi Whitelist konnte nicht geladen werden: {e}")

    if not os.path.exists("lists"):
        os.makedirs("lists")

    for name, url in SOURCES.items():
        try:
            r = requests.get(url, timeout=20)
            lines = r.text.splitlines()
            individual_list = []
            for line in lines:
                cleaned = clean_line(line)
                # Nur hinzufügen, wenn NICHT auf der kombinierten Whitelist
                if cleaned and cleaned not in whitelist:
                    individual_list.append(cleaned)
                    combined_set.add(cleaned)
            
            with open(f"lists/{name}.txt", "w") as f:
                f.write(f"# TechRZN {name}\n\n")
                for item in sorted(set(individual_list)):
                    f.write(f"{item}\n")
        except Exception as e:
            print(f"Fehler bei {name}: {e}")

    with open("combined_blocklist.txt", "w") as f:
        f.write(f"# TechRZN Combined Masterlist\n\n")
        for item in sorted(combined_set):
            f.write(f"{item}\n")

if __name__ == "__main__":
    main()
