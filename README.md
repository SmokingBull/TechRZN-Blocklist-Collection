<p align="center">
  <img src="techrzn-dns.png" width="400" alt="TechRZN DNS Logo">
</p>

# 🛡️ TechRZN-Blocklist-Collection
### High-Performance Blocklists • Täglich aktualisiert • 100% Bereinigt

<p align="left">
  <a href="https://github.com/SmokingBull/TechRZN-Blocklist-Collection/actions">
    <img src="https://github.com/SmokingBull/TechRZN-Blocklist-Collection/actions/workflows/main.yml/badge.svg" alt="Blocklist Update">
  </a>
  <img src="https://img.shields.io/github/last-commit/SmokingBull/TechRZN-Blocklist-Collection?style=flat-square&color=blue" alt="Last Commit">
  <img src="https://img.shields.io/badge/Total_Rules-1M+-success?style=flat-square" alt="Rules">
  <img src="https://img.shields.io/badge/Service-Automated-orange?style=flat-square" alt="Status">
</p>

Willkommen beim **TechRZN Filter-Hub**. Diese Repository bietet eine täglich aktualisierte "All-in-One" Blocklist für **AdGuard Home**, **Pi-hole** und **Technitium**. Alle Listen werden automatisch von Duplikaten bereinigt und gegen eine mehrstufige Whitelist geprüft.

---

## 🚀 Die Master-Liste (Empfohlen)
Die ultimative Lösung für dein Setup. Enthält alle **11 unten aufgeführten Listen** in einer einzigen, performanten Datei.

**Link für deinen DNS-Filter:**
> `https://raw.githubusercontent.com/SmokingBull/TechRZN-Blocklist-Collection/main/combined_blocklist.txt`

---

## 🧩 Alle 11 Filter-Module einzeln
Hier kannst du die Filter nach Kategorien getrennt abonnieren.

| Modul | Fokus / Schutzbereich | Raw-Link |
| :--- | :--- | :--- |
| **🥇 HaGeZi Pro** | All-in-One Schutz | [Link](https://raw.githubusercontent.com/SmokingBull/TechRZN-Blocklist-Collection/main/lists/hagezi_pro.txt) |
| **🔐 Bypass Filter** | VPN/Proxy/Tor/Bypass | [Link](https://raw.githubusercontent.com/SmokingBull/TechRZN-Blocklist-Collection/main/lists/hagezi_bypass.txt) |
| **🏴‍☠️ Threat Intel** | Cyber-Angriffe & Botnets | [Link](https://raw.githubusercontent.com/SmokingBull/TechRZN-Blocklist-Collection/main/lists/hagezi_threat.txt) |
| **🇩🇪 German Filter** | DE/AT/CH Optimierung | [Link](https://raw.githubusercontent.com/SmokingBull/TechRZN-Blocklist-Collection/main/lists/adguard_german.txt) |
| **📺 Smart-TV** | TV-Tracking & Werbung | [Link](https://raw.githubusercontent.com/SmokingBull/TechRZN-Blocklist-Collection/main/lists/smart_tv.txt) |
| **🦠 URLHaus** | Malware URLs & Phishing | [Link](https://raw.githubusercontent.com/SmokingBull/TechRZN-Blocklist-Collection/main/lists/urlhaus_malicious.txt) |
| **💻 Windows Spy** | MS Telemetrie & Office | [Link](https://raw.githubusercontent.com/SmokingBull/TechRZN-Blocklist-Collection/main/lists/hagezi_windows.txt) |
| **🎮 Gambling** | Glücksspiel & Wetten | [Link](https://raw.githubusercontent.com/SmokingBull/TechRZN-Blocklist-Collection/main/lists/hagezi_gambling.txt) |
| **⚠️ Fake DNS** | Scam & Fake-Shops | [Link](https://raw.githubusercontent.com/SmokingBull/TechRZN-Blocklist-Collection/main/lists/hagezi_fake.txt) |
| **📜 Dan Pollock** | Hosts-File Klassiker | [Link](https://raw.githubusercontent.com/SmokingBull/TechRZN-Blocklist-Collection/main/lists/dan_pollock.txt) |
| **📍 TechRZN IPs** | Eigene Malicious IP-Liste | [Link](https://raw.githubusercontent.com/SmokingBull/TechRZN-Blocklist-Collection/main/lists/techrzn_ips.txt) |

---

## ⚪ Intelligente Whitelists (Erlaubnislisten)
Um "Overblocking" zu vermeiden und sicherzustellen, dass wichtige Dienste funktionieren, nutzt TechRZN ein zweistufiges Verfahren:

1. **HaGeZi Referral Whitelist:** Automatische Integration zur Vermeidung globaler Fehlblockierungen.
2. **TechRZN Custom Whitelist:** Eine manuelle Liste (`whitelist.txt`) für persönliche Ausnahmen (z.B. **UGREEN Updates**, **FRITZ!Box Services**, **Microsoft**).

---

## ⚙️ Optimale AdGuard Home Einstellungen
Basierend auf dem TechRZN-Setup (für 1M+ Regeln optimiert):

### DNS-Cache Konfiguration
* **Größe des Cache:** `104857600` (Bytes)
* **TTL-Minimalwert:** `300` (Sekunden)
* **TTL-Höchstwert:** `14400` (Sekunden)
* **Optimistisches Caching:** Aktiviert ✅

### DNS-Serverkonfiguration
* **DNSSEC:** Aktiviert ✅
* **Sperrmodus:** `Standard`
* **Gültigkeitsdauer blockierter Antwort:** `10` (Sekunden)
* **Upstream-Timeout:** `6` (Sekunden)

---

## 🙏 Danksagung & Urheberrecht
Ein Projekt wie dieses wäre ohne die Arbeit der Community nicht möglich. Besonderer Dank gilt:

* **[HaGeZi](https://github.com/hagezi/dns-blocklists):** Für die exzellenten Block- und Whitelists.
* **[AdGuard Team](https://github.com/AdguardTeam):** Für den deutschen Sprachfilter und die Hostlist-Registry.
* **[Abuse.ch (URLHaus)](https://urlhaus.abuse.ch/):** Für kritische Malware-Daten.
* **[Dan Pollock](https://someonewhocares.org/hosts/):** Für den legendären Hosts-Klassiker.

---
*Maintained with ❤️ by Madleen (TechRZN) in Kleve • Stand: März 2026*
