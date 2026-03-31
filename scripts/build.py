import re
import os
import requests

# Alle Quellen für die Einzel-Listen
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
    "domain_squatting": "sources/domain_squatting.raw",
    "threat_intel": "sources/threat_intel.raw",
    "bypass": "sources/bypass.raw",
    "popups": "sources/popups.raw",
    "native_tracker": "sources/native_tracker.raw"
}

OUTPUT_DIR = "blocklists"
WHITELIST_RAW = "allowlist.raw"

def is_valid_domain(domain):
    if not domain or len(domain) > 80: return False
    pattern = r'^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$'
    return re.match(pattern, domain.lower()) is not None

def clean_domain(line):
    line = line.strip().lower()
    if not line or line.startswith(('#', '!', '[')): return None
    domain = line.replace('http://', '').replace('https://', '').split('/')[0]
    domain = domain.replace('@@||', '').replace('^$important', '').replace('||', '').replace('^', '')
    domain = domain.replace('127.0.0.1 ', '').replace('0.0.0.0 ', '')
    if domain.startswith('www.'): domain = domain[4:]
    return domain.split('#')[0].strip()

if __name__ == "__main__":
    # Whitelist laden
    whitelist = set()
    if os.path.exists(WHITELIST_RAW):
        with open(WHITELIST_RAW, 'r') as f:
            for line in f:
                d = clean_domain(line)
                if d: whitelist.add(d)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Jede Kategorie einzeln verarbeiten
    for cat_name, src_file in CATEGORIES.items():
        if not os.path.exists(src_file): continue
        
        category_domains = set()
        with open(src_file, 'r') as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        
        for url in urls:
            try:
                r = requests.get(url, timeout=15)
                for line in r.text.splitlines():
                    domain = clean_domain(line)
                    if domain and is_valid_domain(domain) and domain not in whitelist:
                        category_domains.add(domain)
            except:
                continue

        if category_domains:
            output_path = os.path.join(OUTPUT_DIR, f"techrzn_{cat_name}.txt")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"### TechRZN - {cat_name.upper()} ###\n\n")
                for d in sorted(list(category_domains)):
                    f.write(f"||{d}^\n")
            print(f"✅ {cat_name} fertig: {len(category_domains)} Domains.")
