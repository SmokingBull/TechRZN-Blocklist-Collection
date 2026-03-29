import re
import os
import requests

# Konfiguration: Name der Kategorie -> Pfad zur Eingabe-Datei (sources/)
CATEGORIES = {
    "malware": "sources/malware.raw",
    "phishing": "sources/phishing.raw",
    "fakeshops": "sources/fakeshops.raw",
    "ads": "sources/ads.raw",
    "tracking": "sources/tracking.raw",
    "jugendschutz": "sources/jugendschutz.raw",
    "porn": "sources/porn.raw",
    "dating": "sources/dating.raw",
    "crypto": "sources/crypto.raw",
    "gambling": "sources/gambling.raw",
    "spam": "sources/spam.raw",
    "fake_science": "sources/fake_science.raw",
    "domain_squatting": "sources/domain_squatting.raw"
}

# Hier landen die fertigen Dateien
OUTPUT_DIR = "blocklists"

def is_valid_domain(domain):
    pattern = r'^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$'
    return re.match(pattern, domain.lower()) is not None

def clean_domain(line):
    line = line.strip().lower()
    if not line or line.startswith(('#', '!', '[')): return None
    domain = line.replace('http://', '').replace('https://', '').split('/')[0]
    domain = domain.replace('@@||', '').replace('^$important', '').replace('||', '').replace('^', '').replace('127.0.0.1 ', '').replace('0.0.0.0 ', '')
    if domain.startswith('www.'): domain = domain[4:]
    return domain

def build_whitelist():
    raw_file = 'allowlist.raw'
    output_file = 'whitelist.txt'
    all_domains = set()
    if os.path.exists(raw_file):
        with open(raw_file, 'r') as f:
            for line in f:
                domain = clean_domain(line)
                if domain and is_valid_domain(domain):
                    all_domains.add(domain)
    if all_domains:
        with open(output_file, 'w') as f:
            f.write("### TechRZN - MASTER WHITELIST ###\n\n")
            for d in sorted(list(all_domains)):
                f.write(f"@@||{d}^$important\n")

def fetch_and_build_blocklist(cat_name, source_file):
    all_domains = set()
    if not os.path.exists(source_file): return
    with open(source_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    if not urls: return

    for url in urls:
        try:
            print(f"📥 {cat_name.upper()}: Lade {url}...")
            r = requests.get(url, timeout=15)
            for line in r.text.splitlines():
                domain = clean_domain(line)
                if domain and is_valid_domain(domain):
                    all_domains.add(domain)
        except Exception as e:
            print(f"❌ Fehler bei {url}: {e}")

    if all_domains:
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        
        output_path = os.path.join(OUTPUT_DIR, f"techrzn_{cat_name}.txt")
        with open(output_path, 'w') as f:
            f.write(f"### TechRZN - {cat_name.upper()} BLOCKLIST ###\n")
            f.write(f"# Einträge: {len(all_domains)}\n\n")
            for d in sorted(list(all_domains)):
                f.write(f"||{d}^\n")
        print(f"✅ {output_path} erstellt.")

if __name__ == "__main__":
    build_whitelist()
    for cat, src in CATEGORIES.items():
        fetch_and_build_blocklist(cat, src)
