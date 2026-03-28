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

Willkommen beim **TechRZN Filter-Hub**. Dieses Repository bietet eine täglich aktualisierte "All-in-One" Blocklist für **AdGuard Home**, **Pi-hole** und **Technitium**. Alle Listen werden automatisch von Duplikaten bereinigt und gegen eine mehrstufige Whitelist geprüft.

---

## 🚀 Die Master-Liste (Empfohlen)
Die ultimative Lösung für dein Setup. Enthält alle **11 unten aufgeführten Listen** in einer einzigen, performanten Datei.

**Link für deinen DNS-Filter:**
> `https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/combined_blocklist.txt`

---

## 🧩 Alle 11 Filter-Module einzeln
Hier kannst du die Filter nach Kategorien getrennt abonnieren.

| Modul | Fokus / Schutzbereich | Raw-Link |
| :--- | :--- | :--- |
| **🥇 HaGeZi Pro** | All-in-One Schutz | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_pro.txt) |
| **🔐 Bypass Filter** | VPN/Proxy/Tor/Bypass | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_bypass.txt) |
| **🏴‍☠️ Threat Intel** | Cyber-Angriffe & Botnets | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_threat.txt) |
| **🇩🇪 German Filter** | DE/AT/CH Optimierung | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/adguard_german.txt) |
| **📺 Smart-TV** | TV-Tracking & Werbung | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/smart_tv.txt) |
| **🦠 URLHaus** | Malware URLs & Phishing | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/urlhaus_malicious.txt) |
| **💻 Windows Spy** | MS Telemetrie & Office | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_windows.txt) |
| **🎮 Gambling** | Glücksspiel & Wetten | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_gambling.txt) |
| **⚠️ Fake DNS** | Scam & Fake-Shops | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_fake.txt) |
| **📜 Dan Pollock** | Hosts-File Klassiker | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/dan_pollock.txt) |
| **📍 TechRZN IPs** | Eigene Malicious IP-Liste | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/techrzn_ips.txt) |

---

## ⚪ Intelligente Whitelists (Erlaubnislisten)
Um "Overblocking" zu vermeiden, nutzt TechRZN ein zweistufiges Verfahren:

1. **HaGeZi Referral Whitelist:** Automatische Integration zur Vermeidung globaler Fehlblockierungen.
2. **TechRZN Custom Whitelist:** Manuelle Liste (`whitelist.txt`) für persönliche Ausnahmen (z.B. **UGREEN Updates**, **FRITZ!Box Services**, **Microsoft**).

---

## 🛠️ Erweiterte Whitelist (Referral Fix)
Um zu verhindern, dass nützliche Weiterleitungen (z. B. aus E-Mails oder Preisvergleichen) geblockt werden, empfehle ich die Einbindung meiner Referral-Allowlist.

* **Format:** AdBlock / AdGuard Home
* **Quelle:** Basierend auf HaGeZi's Referral-Allowlist, optimiert für das TechRZN-Setup.

**Einbindung in AdGuard Home:**
Kopiere den Inhalt der [ALLOWLIST_REF.txt](./ALLOWLIST_REF.txt) direkt in deine **Benutzerdefinierten Filterregeln**.

---


## ⚙️ Optimale AdGuard Home Einstellungen
Für die beste Performance mit dieser Kollektion (1M+ Regeln) empfehlen wir, dein AdGuard Home wie folgt zu konfigurieren:

### 1️⃣ DNS-Cache Einstellungen
* **Cache-Größe:** `104.857.600` (100 MB) ✅
* **Optimistisches Caching:** Aktiviert ✅
* **TTL-Minimalwert:** `3600` (1 Stunde) 💡
* **TTL-Höchstwert:** `86400` (24 Stunden) 💡

### 2️⃣ DNS-Serverkonfiguration
* **DNSSEC:** Aktiviert ✅
* **Sperrmodus:** `Standard` ✅
* **Gültigkeitsdauer blockierter Antwort:** `300` Sekunden ✅

### 3️⃣ Private inverse DNS-Server
* **Private Reverse-DNS-Resolver verwenden:** Aktiviert ✅
* **Hostnamenauflösung der Clients aktivieren:** Aktiviert ✅
* **Upstream-Timeout:** `2` Sekunden ✅
* **DNS-Server:** Hier bitte die **lokale DNS-IP deines Routers** (z.B. FRITZ!Box) eintragen.

---

## 🙏 Danksagung & Urheberrecht (TechRZN)
Besonderer Dank gilt den Quellen, die dieses Projekt ermöglichen:

* **[HaGeZi](https://github.com/hagezi/dns-blocklists):** Gold-Standard der Blocklists.
* **[AdGuard Team](https://github.com/AdguardTeam):** Deutsche Sprachfilter & Registry.
* **[Abuse.ch (URLHaus)](https://urlhaus.abuse.ch/):** Malware Intelligence.
* **[Dan Pollock](https://someonewhocares.org/hosts/):** Legendärer Hosts-Klassiker.

---
*Maintained with ❤️ by TechRZN in Kleve • Stand: März 2026*

---

## ❤️ TechRZN unterstützen
Die tägliche Pflege der 1M+ Regeln und der Betrieb der 2,5 Gbit/s Test-Infrastruktur auf dem UGREEN NAS (64 GB RAM) kosten Zeit und Ressourcen. Wenn dir meine Arbeit hilft, freue ich mich über deine Unterstützung!

[![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://www.patreon.com/cw/TechRZN_DNS)

---

## ☕ Support & Infrastruktur
Der tägliche Betrieb der **2,5 Gbit/s Test-Umgebung** (UGREEN NAS mit **64 GB RAM**) und die Pflege von über 1 Million Regeln erfordern Zeit und Ressourcen. 

Wenn dir meine Arbeit hilft:
* **Feedback:** Eröffne ein Issue oder gib dem Projekt einen ⭐.
* **Support:** Da mein Patreon aktuell noch in der Prüfung ist, kontaktiere mich bei Interesse an einer Unterstützung einfach direkt.

*Gepflegt mit ❤️ in Kleve • Stand: März 2026*
