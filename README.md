# 🛡️ Advanced DNS Filter & Security Stack
### Curated Blocklist Collection for AdGuard Home, Pi-hole & Technitium

![GitHub last commit](https://img.shields.io/github/last-commit/TechRZN/dns-blocklists?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)

Diese Sammlung enthält eine sorgfältig zusammengestellte Auswahl an Filterlisten, die darauf optimiert sind, Werbung, Telemetrie, Phishing und bösartige IP-Adressen effektiv zu blockieren, ohne das Surferlebnis durch "Overblocking" zu beeinträchtigen.

---

## 📊 Filter-Übersicht

| Kategorie | Name der Liste | Einträge | Dokumentation / Quelle |
| :--- | :--- | :---: | :--- |
| **Main Engine** | HaGeZi's Pro Blocklist | ~185k | [Link](https://adguardteam.github.io/HostlistsRegistry/assets/filter_48.txt) |
| **Security** | HaGeZi's Threat Intelligence | ~737k | [Link](https://adguardteam.github.io/HostlistsRegistry/assets/filter_44.txt) |
| **Privacy** | HaGeZi's Windows/Office Tracker | 385 | [Link](https://adguardteam.github.io/HostlistsRegistry/assets/filter_63.txt) |
| **Malicious** | TechRZN-malicious-ip-blocklist | ~60k | [Link](https://raw.githubusercontent.com/SmokingBull/malicious-ip-blocklist/refs/heads/main/deny-ip-list.txt) |
| **Network** | HaGeZi's Encrypted DNS/VPN/TOR | ~16k | [Link](https://adguardteam.github.io/HostlistsRegistry/assets/filter_52.txt) |
| **Media** | Smart-TV Blocklist (Perflyst) | 159 | [Link](https://adguardteam.github.io/HostlistsRegistry/assets/filter_7.txt) |
| **Regional** | AdGuard German Filter | ~11k | [Link](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_6_German/filter.txt) |
| **Misc** | HaGeZi's Gambling / Fake DNS | ~70k | [Link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/gambling.mini.txt) |

---

## ⚙️ Implementierung

### AdGuard Home
1. Navigiere zu **Filter** -> **DNS-Sperrlisten**.
2. Klicke auf **Sperrliste hinzufügen** -> **Benutzerdefinierte Liste hinzufügen**.
3. Kopiere die gewünschte URL aus der Tabelle oben in das Feld "URL der Liste".

### Pi-hole
1. Gehe zu **Group Management** -> **Adlists**.
2. Füge den Link im Feld **Address** ein.
3. Führe danach ein `pihole -g` (Update Gravity) aus.

### Technitium DNS
1. Gehe zu **Settings** -> **Block Lists**.
2. Klicke auf **Add New Block List** und füge die URL ein.

---

## 🛠️ Tech Stack & Integration
Dieses Setup ist Teil einer optimierten Netzwerk-Infrastruktur. Die Listen sind kompatibel mit:
- **Unbound** (als rekursiver DNS-Resolver)
- **Tailscale** (für sicheren Remote-Zugriff)
- **UGREEN NAS / Docker** Umgebungen

---

## 📜 Lizenz & Disclaimer
Die Urheberrechte der einzelnen Listen liegen bei den jeweiligen Maintainern (HaGeZi, AdGuard, etc.). Diese Repository dient der Kuration und einfachen Bereitstellung für die Community.

---
*Zuletzt aktualisiert: März 2026*
