<p align="center">
  <img src="techrzn-dns.png" width="400" alt="TechRZN DNS Logo">
</p>

<p align="center">
  Sprache: 🇩🇪 <b>[Deutsch]</b> | 🇺🇸 <a href="README.en.md">[English]</a>
</p>

# 🛡️ TechRZN-Blocklist-Collection
### High-Performance Blocklists • Täglich aktualisiert • 100% Bereinigt

<p align="left">
  <a href="https://github.com/TechRZN-DNS/TechRZN-Blocklist-Collection/actions/workflows/main.yml">
    <img src="https://github.com/TechRZN-DNS/TechRZN-Blocklist-Collection/actions/workflows/main.yml/badge.svg" alt="Blocklist Update">
  </a>
  <img src="https://img.shields.io/github/last-commit/TechRZN-DNS/TechRZN-Blocklist-Collection?style=flat-square&color=blue" alt="Last Commit">
  <img src="https://img.shields.io/badge/Total_Rules-1M+-success?style=flat-square" alt="Rules">
  <img src="https://img.shields.io/badge/Service-Automated-orange?style=flat-square" alt="Status">
</p>

Willkommen beim **TechRZN Filter-Hub**. Dieses Repository bietet eine täglich aktualisierte "All-in-One" Blocklist für **AdGuard Home**, **Pi-hole** und **Technitium**. Alle Listen werden automatisch von Duplikaten bereinigt und gegen eine intelligente, mehrstufige Whitelist geprüft.

---

## 🚀 Die Master-Liste (Empfohlen)
Die ultimative Lösung für dein Setup. Enthält alle **14 unten aufgeführten Module** in einer einzigen, performanten Datei.

**Link für deinen DNS-Filter:**
> `https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/combined_blocklist.txt`

---

## 🧩 Modulare Filter-Architektur (Die 14 Core-Module)
| Modul | Fokus / Schutzbereich | Raw-Link |
| :--- | :--- | :--- |
| 🥇 **HaGeZi Pro** | Weltweiter Schutz (Gold Standard) | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_pro.txt) |
| 🔐 **Bypass Filter** | VPN & Proxy Schutz | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_bypass.txt) |
| 🏴‍☠️ **Threat Intel** | Botnets & Cyber-Abwehr | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_threat.txt) |
| 🇩🇪 **German Filter** | Optimierung DE / AT / CH | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/adguard_german.txt) |
| 📺 **Smart-TV** | TV-Tracking & Werbung | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/smart_tv.txt) |
| 🦠 **URLHaus** | Malware & Phishing Intelligence | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/urlhaus_malicious.txt) |
| 💻 **Windows Spy** | MS Telemetrie & Office Opt. | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_windows.txt) |
| 🎮 **Gambling** | Glücksspiel & Wetten | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_gambling.txt) |
| ⚠️ **Fake DNS** | Scam & Fake-Shops (DNS-Ebene) | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_fake.txt) |
| 📜 **Dan Pollock** | Hosts-File Klassiker | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/dan_pollock.txt) |
| 📍 **TechRZN IPs** | Kuratierte IP-Blocklist | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/techrzn_ips.txt) |
| 🛍️ **Anti-Fakeshop** | Abofallen & Betrug (RPiList) | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/notserious.txt) |
| 🏦 **Banking-Schutz** | Phishing (DE-Banken - RPiList) | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/phishing_de.txt) |
| 🔬 **Fake-Science** | Pseudo-Wissenschaft (RPiList) | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/fake_science.txt) |

---

## ⚪ Intelligente Whitelist (Erlaubnisliste)
Um "Overblocking" zu vermeiden und eine reibungslose User-Experience (z.B. bei Telekom/1&1 Logins oder Gaming) zu garantieren, nutzt TechRZN eine kombinierte Master-Whitelist.

* **Inhalt:** Persönliche TechRZN-Ausnahmen + HaGeZi's Referral-Allowlist.
* **Technik:** Das Python-Backend erkennt Subdomains automatisch und bereinigt alle 14 Blocklisten in Echtzeit.

### 📋 Link für AdGuard Home (DNS-Erlaubnislisten):
```text
[https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/whitelist.txt](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/whitelist.txt)

---

## ⚙️ Optimale AdGuard Home Einstellungen
Für maximale Performance mit 1M+ Regeln (getestet auf **UGREEN NAS / 2,5 Gbit/s**):

### 1️⃣ DNS-Cache & TTL
* **Cache-Größe:** `104.857.600` (100 MB) ✅
* **Optimistisches Caching:** Aktiviert ✅
* **TTL-Minimalwert:** `3600` (1 Stunde) 💡

### 2️⃣ Sicherheit & Filterung
* **DNSSEC:** Aktiviert ✅
* **Sperrmodus:** `Standard` ✅
* **Gültigkeitsdauer blockierter Antwort:** `300` Sekunden ✅

---

## 🙏 Danksagung & Quellen
Dieses Projekt basiert auf der großartigen Arbeit von:
* 🛡️ **HaGeZi:** Der weltweite Gold-Standard.
* 🚀 **RPiList:** Spezialisierter Schutz (Fakeshops, Phishing).
* 🌐 **AdGuard Team:** Deutsche Sprachfilter.
* 🦠 **Abuse.ch (URLHaus):** Malware Intelligence.

---

## ☕ Support & Infrastruktur
Die tägliche Pflege der über 1 Million Regeln und der Betrieb der **2,5 Gbit/s Test-Infrastruktur** in Kleve erfordern Zeit und Ressourcen. Wenn dir meine Arbeit hilft:

* **Feedback:** Eröffne ein Issue oder gib dem Projekt einen ⭐.
* **Support:** Kontaktiere mich bei Interesse an einer Unterstützung einfach direkt.

*Gepflegt mit ❤️ in Kleve • Stand: März 2026*
