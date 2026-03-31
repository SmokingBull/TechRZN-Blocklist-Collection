import os
import requests
import shutil
import time  # Neu für die Entlastung
from datetime import datetime

# --- KONFIGURATION ---
CATEGORIES = {
    "ads": "sources/ads.raw",
    "tracking": "sources/tracking.raw",
    "malware": "sources/malware.raw",
    "phishing": "sources/phishing.raw",
    "threat_intel": "sources/threat_intel.raw",
    "fakeshops": "sources/fakeshops.raw",
    "gambling": "sources/gambling.raw",
    "dating": "sources/dating.raw",
    "spam": "sources/spam.raw",
    "fake_science": "sources/fake_science.raw",
    "bypass": "sources/bypass.raw",
    "native_tracker": "sources/native_tracker.raw",
    "popups": "sources/popups.raw",
    "domain_squatting": "sources/domain_squatting.raw",
    "jugendschutz": "sources/jugendschutz.raw",
    "nrd": "sources/newly_registered_domains.raw"
}

OUTPUT_DIR = "blocklists"
WL_DIR = "Whitelists"
LOCAL_WHITELIST = "sources/whitelist.raw"
HEADERS = {'User-Agent': 'Mozilla/5.0 TechRZN-Bot/1.2'}

def clean_domain(line):
    line = line.strip().lower()
    if not line or line.startswith(('#', '!', '[')): return None
    if '://' in line: line = line.split('://')[-1]
    line = line.split('/')[0].replace('*.', '').replace('*', '')
    domain = line.replace('@@||', '').replace('^$important', '').replace('||', '').replace('^', '')
    if ' ' in domain or not domain: return None
    if domain.startswith('www.'): domain = domain[4:]
    return domain.split('#')[0].split('!')[0].strip() if '.' in domain else None

def main():
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")
    print(f"🚀 TechRZN Update gestartet: {timestamp}")
    
    for folder in [OUTPUT_DIR, WL_DIR]:
        os.makedirs(folder, exist_ok=True)

    # Whitelist laden
    whitelist = set()
    if os.path.exists(LOCAL_WHITELIST):
        with open(LOCAL_WHITELIST, 'r', encoding='utf-8') as f:
            for line in f:
                d = clean_domain(line)
                if d: whitelist.add(d)
    
    # Session starten für bessere Performance
    session = requests.Session()
    session.headers.update(HEADERS)
    
    for cat_name, src_path in CATEGORIES.items():
        if not os.path.exists(src_path):
            print(f"⚠️ Überspringe {cat_name} (Quelle fehlt)")
            continue
        
        category_domains = set()
        with open(src_path, 'r', encoding='utf-8') as f:
            urls = [l.strip() for l in f if l.strip() and not l.startswith('#')]
        
        print(f"📦 Verarbeite Kategorie: {cat_name} ({len(urls)} Quellen)")
        
        for url in urls:
            try:
                # URL Normalisierung
                fetch_url = url.replace("cdn.jsdelivr.net/gh/", "raw.githubusercontent.com/").replace("@latest/", "/main/") if "jsdelivr" in url else url
                
                r = session.get(fetch_url, timeout=20)
                if r.status_code == 200:
                    for line in r.text.splitlines():
                        domain = clean_domain(line)
                        if domain and domain not in whitelist:
                            category_domains.add(domain)
                
                # KLEINE PAUSE: Entlastet Router und AdGuard (DNS-Latenz-Fix)
                time.sleep(0.2) 
                
            except Exception as e:
                print(f"❌ Fehler bei URL {url}: {e}")
                continue

        if category_domains:
            output_path = os.path.join(OUTPUT_DIR, f"techrzn_{cat_name}.txt")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"### TechRZN - {cat_name.upper()} ###\nStand: {timestamp}\n\n")
                for d in sorted(list(category_domains)): 
                    f.write(f"||{d}^\n")
            print(f"✅ {cat_name} mit {len(category_domains)} Domains erstellt.")

if __name__ == "__main__":
    main()
