import re
import os
import requests

CATEGORIES = {
    "malware": "sources/malware.raw",
    "phishing": "sources/phishing.raw",
    "fakeshops": "sources/fakeshops.raw",
    "ads": "sources/ads.raw",
    "tracking": "sources/tracking.raw",
    "jugendschutz": "sources/jugendschutz.raw",
    "porn": "sources/porn.raw",  # Wird gesplittet
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
CHUNK_SIZE = 700000  # Sicher unter 100MB pro Datei

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

    # Jede Kategorie verarbeiten
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
            except: continue

        if category_domains:
            final_list = sorted(list(category_domains))
            
            # SPEZIALFALL: Porn-Liste splitten und in blocklists/ speichern
            if cat_name == "porn" and len(final_list) > CHUNK_SIZE:
                # Alte Riesendatei löschen, um Fehler zu vermeiden
                old_file = os.path.join(OUTPUT_DIR, "techrzn_porn.txt")
                if os.path.exists(old_file):
                    os.remove(old_file)
                
                for i in range(0, len(final_list), CHUNK_SIZE):
                    part_num = (i // CHUNK_SIZE) + 1
                    chunk = final_list[i:i + CHUNK_SIZE]
                    filename = f"techrzn_porn_part{part_num}.txt"
                    file_path = os.path.join(OUTPUT_DIR, filename) # Pfad zum Ordner
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(f"### TechRZN - PORN PART {part_num} ###\n\n")
                        for d in chunk:
                            f.write(f"||{d}^\n")
                print(f"✅ Porn in {part_num} Teile in {OUTPUT_DIR}/ aufgeteilt.")
            
            # NORMALFALL: Alle anderen Listen
            else:
                output_path = os.path.join(OUTPUT_DIR, f"techrzn_{cat_name}.txt")
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(f"### TechRZN - {cat_name.upper()} ###\n\n")
                    for d in final_list:
                        f.write(f"||{d}^\n")
                print(f"✅ {cat_name} fertig.")
