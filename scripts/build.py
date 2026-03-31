import os
import requests
import shutil
from datetime import datetime
import time

# --- KONFIGURATION ---
# Diese Dateien müssen im Ordner "sources/" liegen!
CATEGORIES = {
    "ads": "sources/ads.raw",
    "tracking": "sources/tracking.raw",
    "malware": "sources/malware.raw",
    "phishing": "sources/phishing.raw",
    "threat_intel": "sources/threat_intel.raw",
    "fakeshops": "sources/fakeshops.raw",
    "gambling": "sources/gambling.raw",
    "crypto": "sources/crypto.raw",
    "dating": "sources/dating.raw",
    "spam": "sources/spam.raw",
    "fake_science": "sources/fake_science.raw",
    "bypass": "sources/bypass.raw",
    "native_tracker": "sources/native_tracker.raw",
    "popups": "sources/popups.raw",
    "domain_squatting": "sources/domain_squatting.raw",
    "jugendschutz": "sources/jugendschutz.raw",
    # NEU: Newly Registered Domains
    "nrd": "sources/newly_registered_domains.raw" 
}

OUTPUT_DIR = "blocklists"
WL_DIR = "Whitelists"
LOCAL_WHITELIST = "sources/whitelist.raw"
REMOTE_WHITELIST = "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/whitelist-referral.txt"

# Pfade für IP-Liste
MANUAL_IP_SRC = "manual_sources/deny-ip-list.txt"
IP_OUTPUT = os.path.join(OUTPUT_DIR, "techrzn_ips.txt")

# WICHTIG: User-Agent verhindert 403-Fehler
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) TechRZN-Bot/1.1'
}

def clean_domain(line):
    line = line.strip().lower()
    # Kommentare und AdBlock-Metadaten ignorieren
    if not line or line.startswith(('#', '!', '[')):
        return None
    if '://' in line:
        line = line.split('://')[-1]
    line = line.split('/')[0]
    line = line.replace('*.', '').replace('*', '')
    # Säuberung von AdBlock-Syntax (||domain.com^)
    domain = line.replace('@@||', '').replace('^$important', '').replace('||', '').replace('^', '')
    if ' ' in domain or not domain:
        return None
    if domain.startswith('www.'):
        domain = domain[4:]
    domain = domain.split('#')[0].split('!')[0].strip()
    return domain if domain and '.' in domain else None

def main():
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")
    print(f"🚀 TechRZN Update-Prozess gestartet: {timestamp}")
    
    # 1. Ordner vorbereiten
    for folder in [OUTPUT_DIR, WL_DIR]:
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
            print(f"📁 Ordner {folder} erstellt.")

    # 2. Whitelist aufbauen
    whitelist = set()
    print("⚪ Baue Whitelist auf...")
    if os.path.exists(LOCAL_WHITELIST):
        with open(LOCAL_WHITELIST, 'r', encoding='utf-8') as f:
            for line in f:
                d = clean_domain(line)
                if d: whitelist.add(d)
    
    try:
        r = requests.get(REMOTE_WHITELIST, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            for line in r.text.splitlines():
                d = clean_domain(line)
                if d: whitelist.add(d)
        print(f"✅ Whitelist bereit: {len(whitelist)} Einträge.")
    except Exception as e:
        print(f"⚠️ Warnung: Remote Whitelist konnte nicht geladen werden: {e}")

    # Whitelist-Datei speichern
    wl_file = os.path.join(WL_DIR, "techrzn_whitelist.txt")
    with open(wl_file, 'w', encoding='utf-8') as f:
        f.write(f"### TechRZN Master Whitelist ###\n### Stand: {timestamp} ###\n\n")
        for d in sorted(list(whitelist)):
            f.write(f"{d}\n")

    # 3. Manuelle IP-Liste (Marius Hosting)
    if os.path.exists(MANUAL_IP_SRC):
        print(f"⚙️ Verarbeite IP-Quelle: {MANUAL_IP_SRC}")
        ip_count = 0
        with open(MANUAL_IP_SRC, "r", encoding="utf-8") as f_in:
            lines = f_in.readlines()
        with open(IP_OUTPUT, "w", encoding="utf-8") as f_out:
            f_out.write(f"### TechRZN - Deny IP List ###\n### Stand: {timestamp} ###\n\n")
            for line in lines:
                line = line.strip()
                if line and not line.startswith(('#', '!', '/')):
                    f_out.write(f"{line}\n")
                    ip_count += 1
        print(f"✅ IP-Liste erstellt: {ip_count} Einträge.")

    # 4. Domain-Blocklisten bauen
    for cat_name, src_path in CATEGORIES.items():
        if not os.path.exists(src_path):
            print(f"❌ Quelldatei fehlt: {src_path} - Überspringe {cat_name}")
            continue
        
        print(f"🔍 Erstelle Liste: techrzn_{cat_name}.txt ...")
        category_domains = set()
        
        with open(src_path, 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        
        for url in urls:
            try:
                fetch_url = url
                # GitHub/JsDelivr URLs anpassen
                if "cdn.jsdelivr.net" in url:
                    fetch_url = url.replace("cdn.jsdelivr.net/gh/", "raw.githubusercontent.com/").replace("@latest/", "/main/")
                
                # Request mit User-Agent und ausreichend Timeout
                r = requests.get(fetch_url, headers=HEADERS, timeout=30)
                if r.status_code == 200:
                    for line in r.text.splitlines():
                        domain = clean_domain(line)
                        if domain and domain not in whitelist:
                            category_domains.add(domain)
                else:
                    print(f"   ❌ Fehler {r.status_code} bei URL: {url}")
            except Exception as e:
                print(f"   ❌ Timeout/Fehler bei URL {url}: {e}")
                continue

        # Datei nur schreiben, wenn Domains gefunden wurden
        if category_domains:
            output_path = os.path.join(OUTPUT_DIR, f"techrzn_{cat_name}.txt")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"### TechRZN - {cat_name.upper()} ###\n")
                count_str = "{:,}".format(len(category_domains)).replace(',', '.')
                f.write(f"### Stand: {timestamp} | Regeln: {count_str} ###\n\n")
                for d in sorted(list(category_domains)):
                    f.write(f"||{d}^\n")
            print(f"   ✅ Fertig! {len(category_domains)} Domains in techrzn_{cat_name}.txt gespeichert.")
        else:
            print(f"   ⚠️ Warnung: Keine Domains für {cat_name} gefunden.")

    print(f"\n✨ Alle Listen wurden im Ordner '{OUTPUT_DIR}' aktualisiert.")

if __name__ == "__main__":
    main()
