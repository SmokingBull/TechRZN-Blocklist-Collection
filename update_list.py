import requests
import os
import sys

# Die 14 TechRZN Core-Module
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

REMOTE_WHITELIST_URL = "https://raw.githubusercontent.com/hagezi/dns-blocklists/refs/heads/main/adblock/whitelist-referral.txt"

def clean_line(line):
    if not line: return None
    line = line.strip()
    if line and not line.startswith(('#', '!', '[', ' ')):
        cleaned = line.replace('||', '').replace('^', '')
        return cleaned.split('#')[0].split('!')[0].strip()
    return None

def is_whitelisted(domain, whitelist_set):
    if not domain: return False
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

    # 1. Lokale Whitelist laden
    try:
        if os.path.exists("whitelist.txt"):
            with open("whitelist.txt", "r", encoding='utf-8', errors='ignore') as f:
                for line in f:
                    d = clean_line(line)
                    if d: final_whitelist.add(d.replace('*.', ''))
            print(f"📂 Lokale Whitelist geladen.")
    except Exception as e:
        print(f"⚠️ Fehler beim Lesen von whitelist.txt: {e}")

    # 2. Externe HaGeZi Whitelist laden
    try:
        print("⏳ Lade HaGeZi Referral-Liste...")
        r_white = requests.get(REMOTE_WHITELIST_URL, timeout=15)
        r_white.raise_for_status()
        for line in r_white.text.splitlines():
            d = clean_line(line)
            if d: final_whitelist.add(d)
        print(f"✅ HaGeZi-Whitelist integriert.")
    except Exception as e:
        print(f"⚠️ Fehler bei Remote Whitelist: {e}")

    # 3. Whitelist.txt neu schreiben (TechRZN Branding)
    try:
        with open("whitelist.txt", "w", encoding='utf-8') as f:
            f.write("############################################################\n")
            f.write("# TechRZN-DNS - Master Whitelist (Kombiniert)\n")
            f.write("# Repository: TechRZN-DNS / TechRZN-Blocklist-Collection\n")
            f.write("############################################################\n\n")
            for domain in sorted(final_whitelist):
                f.write(f"{domain}\n")
        print(f"✅ whitelist.txt erfolgreich aktualisiert.")
    except Exception as e:
        print(f"❌ Kritischer Fehler beim Schreiben der Whitelist: {e}")
        sys.exit(1)

    # 4. Blocklisten verarbeiten
    if not os.path.exists("lists"):
        os.makedirs("lists")

    for name, (url, credit) in SOURCES.items():
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            lines = r.text.splitlines()
            individual_list = []
            for line in lines:
                cleaned = clean_line(line)
                if cleaned and not is_whitelisted(cleaned, final_whitelist):
                    individual_list.append(cleaned)
                    combined_set.add(cleaned)
            
            with open(os.path.join("lists", f"{name}.txt"), "w", encoding='utf-8') as f:
                f.write(f"# TechRZN Module: {name} | Source: {credit}\n\n")
                for item in sorted(set(individual_list)):
                    f.write(f"{item}\n")
            print(f"✅ Created: lists/{name}.txt")
        except Exception as e:
            print(f"❌ Fehler bei Quelle {name}: {e}")

    # 5. Master-Blockliste speichern
    try:
        with open("combined_blocklist.txt", "w", encoding='utf-8') as f:
            f.write("# TechRZN Master Blocklist - All-in-One\n\n")
            for item in sorted(combined_set):
                f.write(f"{item}\n")
        print("\n🚀 Alle TechRZN-DNS Listen erfolgreich aktualisiert!")
    except Exception as e:
        print(f"❌ Fehler beim Speichern der Master-Liste: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
