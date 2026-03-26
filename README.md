<p align="center">
  <img src="techrzn-dns.png" width="400" alt="TechRZN DNS Logo">
</p>

# 🛡️ Advanced DNS Filter & Security Stack
### Powered by TechRZN • High-Performance Blocklist Collection

![GitHub last commit](https://img.shields.io/github/last-commit/SmokingBull/my-blocklist-collection?style=flat-square&color=blue)
![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)
![Rules](https://img.shields.io/badge/Rules-1M+-success?style=flat-square)
![Status](https://img.shields.io/badge/Service-Automated-orange?style=flat-square)

Diese Repository bietet eine sorgfältig kuratierte und täglich aktualisierte "All-in-One" Blocklist. Sie kombiniert die weltweit besten Filterquellen für DNS-basierte Sicherheit, Telemetrie-Unterbindung und Werbefreiheit.

---

## ⚡ Quick Install (Recommended)
Für maximale Performance und einfachste Wartung nutzt du am besten diesen kombinierten Link. Er enthält alle unten aufgeführten Listen, bereinigt um Duplikate.

**Kopiere diesen Link in deinen DNS-Filter:**
> `https://raw.githubusercontent.com/SmokingBull/my-blocklist-collection/main/combined_blocklist.txt`

> [!IMPORTANT]
> **Update-Intervall:** Die Liste wird automatisch alle 24 Stunden durch GitHub Actions aktualisiert.

---

## 📊 Enthaltene Filter-Module
Diese Liste speist sich aus den folgenden hochqualitativen Quellen:

| Modul | Quelle | Fokus |
| :--- | :--- | :--- |
| **Main Engine** | HaGeZi Pro | Umfassender Schutz vor Adware & Trackern |
| **Cyber Security** | Threat Intel | Schutz vor Malware, Phishing & Botnets |
| **IP-Security** | TechRZN Custom | Spezifische Liste bösartiger IP-Adressen |
| **Privacy** | Windows Tracker | Unterbindung von Microsoft Telemetrie |
| **Regional** | German Filter | Optimierte Filter für DE/AT/CH |
| **Hardware** | Smart-TV List | Reduziert Tracking auf TV-Geräten |
| **Safety** | Gambling/Fake | Filtert Glücksspiel & Fake-Shops |

---

## ⚙️ Installation & Setup

### 🔵 AdGuard Home
1. Gehe zu **Filter** -> **DNS-Sperrlisten**.
2. Klicke auf **Sperrliste hinzufügen** -> **Benutzerdefinierte Liste hinzufügen**.
3. Name: `TechRZN Combined`, URL: Link von oben einfügen.

### ⚪ Pi-hole
1. Navigiere zu **Group Management** -> **Adlists**.
2. Füge den Link im Feld **Address** ein und klicke auf **Add**.
3. Führe in der Konsole `pihole -g` aus, um die Liste zu laden.

### 🟢 Technitium DNS
1. Gehe zu **Settings** -> **Block Lists**.
2. Klicke auf **Add New Block List** und füge den Link ein.

---

## 🛠️ Automatisierung & Technik
Die Listen-Zusammenführung erfolgt über ein Python-Skript (`update_list.py`), welches über GitHub Actions gesteuert wird. Dabei werden:
1. Alle Quellen heruntergeladen.
2. Kommentare und Metadaten bereinigt.
3. Duplikate entfernt, um die Systemlast deines DNS-Servers zu minimieren.

---
*Maintained with ❤️ in Kleve • Stand: März 2026*
