import requests
import os

# Deine 14 Sperrlisten
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
    "notserious": ("https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/notserious", "RPiList (Anti-Fakeshop)"),
    "phishing_de": ("https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Phishing-Angriffe", "RPiList (Banking-Schutz)"),
    "fake_science": ("https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Fake-Science", "RPiList (Fake-Science)")
}

# Quelle für die HaGeZi-Whitelist
REMOTE_WHITELIST_URL = "https://raw.githubusercontent.com/hagezi/dns-blocklists/refs/heads/main/adblock/whitelist-referral.txt"

def clean_line(line):
    line = line.strip()
    if line and not line.startswith(('#', '!', '[', ' ')):
        cleaned = line.replace('||', '').replace('^', '')
        return cleaned.split('#')[0].split('!')[0].strip()
    return None

def is_whitelisted(domain, whitelist_set):
    if domain in whitelist_set:
        return True
    parts = domain.split('.')
    for i in range(len(parts) - 1):
        parent = '.'.join(parts[i+1:])
        if parent in whitelist_set:
            return True
    return False

def main():
    combined_set = set()
    final_whitelist = set()

    # 1. Deine persönlichen Einträge aus 'whitelist.txt' laden
    if os.path.exists("whitelist.txt"):
        with open("whitelist.txt", "r", encoding='utf-8') as f:
            for line in f:
                d = clean_line(line)
                if d: final_whitelist.add(d.replace('*.', ''))
        print(f"📂 Persönliche whitelist.txt eingelesen.")

    # 2. HaGeZi Whitelist laden und hinzufügen
    try:
        print("⏳ Lade HaGeZi Referral-Liste...")
        r_white = requests.get(REMOTE_WHITELIST_URL, timeout=15)
        if r_white.status_code == 200:
            for line in r_white.text.splitlines():
                d = clean_line(line)
                if d: final_whitelist.add(d)
    except Exception as e:
        print(f"⚠️ Fehler bei HaGeZi Whitelist: {e}")

    # 3. Die kombinierte MASTER-WHITELIST speichern (neue Datei)
    with open("generated_whitelist.txt", "w", encoding='utf-8') as f:
        f.write("############################################################\n")
        f.write("# TechRZN Master Whitelist (Personal + HaGeZi Referral)\n")
        f.write("# Nutze diese URL in AdGuard Home!\n")
        f.write("############################################################\n\n")
        for domain in sorted(final_whitelist):
            f.write(f"{domain}\n")
    print(f"✅ Master-Whitelist erstellt: generated_whitelist.txt ({len(final_whitelist)} Einträge)")

    # 4. Blocklisten verarbeiten
    if not os.path.exists("lists"): os.makedirs("lists")

    for name, (url, credit) in SOURCES.items():
        try:
            r = requests.get(url, timeout=25)
            if r.status_code == 200:
                lines = r.text.splitlines()
                individual_list = []
                for line in lines:
                    cleaned = clean_line(line)
                    if cleaned and not is_whitelisted(cleaned, final_whitelist):
                        individual_list.append(cleaned)
                        combined_set.add(cleaned)
                
                with open(os.path.join("lists", f"{name}.txt"), "w", encoding='utf-8') as f:
                    f.write(f"# TechRZN Module: {name}\n\n")
                    for item in sorted(set(individual_list)):
                        f.write(f"{item}\n")
        except Exception as e:
            print(f"❌ Fehler bei {name}")

    # 5. Master-Blockliste speichern
    with open("combined_blocklist.txt", "w", encoding='utf-8') as f:
        f.write("# TechRZN Master Blocklist\n\n")
        for item in sorted(combined_set):
            f.write(f"{item}\n")
    print("🚀 Setup in Kleve erfolgreich aktualisiert!")

if __name__ == "__main__":
    main()
