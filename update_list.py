import requests

# Deine Quellen
urls = [
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_48.txt",
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_52.txt",
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_44.txt",
    "https://raw.githubusercontent.com/SmokingBull/malicious-ip-blocklist/refs/heads/main/deny-ip-list.txt",
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_63.txt",
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_7.txt",
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_11.txt",
    "https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/gambling.mini.txt",
    "https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/fake.txt",
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_6_German/filter.txt",
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_4.txt"
]

def main():
    combined_set = set()
    for url in urls:
        try:
            print(f"Lade: {url}")
            r = requests.get(url, timeout=10)
            lines = r.text.splitlines()
            for line in lines:
                # Kommentare und leere Zeilen ignorieren
                line = line.strip()
                if line and not line.startswith(('#', '!', '[', ' ')):
                    combined_set.add(line)
        except Exception as e:
            print(f"Fehler bei {url}: {e}")

    # Sortieren und Speichern
    with open("combined_blocklist.txt", "w") as f:
        f.write("# TechRZN Combined DNS Blocklist\n")
        f.write("# Letztes Update: automated by GitHub Actions\n\n")
        for item in sorted(combined_set):
            f.write(f"{item}\n")

if __name__ == "__main__":
    main()
