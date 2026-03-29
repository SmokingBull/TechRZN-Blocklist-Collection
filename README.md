<div align="center">

<br>

<p align="center">
  <img src="techrzn.png" width="650" alt="TechRZN DNS Filter-Hub" />
</p>

<p align="center">
  Sprache: 🇩🇪 <b>[Deutsch]</b> | 🇺🇸 <a href="README.en.md">[English]</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-INFRASTRUKTUR_AKTIV-00C853?style=for-the-badge&logo=statuspage&logoColor=white" />
  <img src="https://img.shields.io/badge/DATENBANK-2.2M%2B_REGELN-FF6B6B?style=for-the-badge&logo=databricks&logoColor=white" />
  <img src="https://img.shields.io/badge/UPLINK-2.5_GBIT_BACKBONE-7957d5?style=for-the-badge&logo=wi-fi&logoColor=white" />
</p>

---

## 🛰️ Mission & Vision
> **High-Performance Blocklisten • Täglich aktualisiert • 100% Bereinigt**

Willkommen beim **TechRZN Filter-Hub**. Aufgrund der massiven Größe unserer Datenbank von über **2,2 Millionen hocheffektiven Regeln** haben wir die Master-Liste in zwei Teile aufgeteilt. Dies garantiert maximale Kompatibilität mit GitHub und schnellere Ladezeiten in deinem AdGuard/Pi-hole System.

---

## ❤️ Support & Community
Wenn dir der **TechRZN Filter-Hub** hilft, dein Netzwerk sicherer zu machen, freue ich mich über deine Unterstützung auf Patreon!

<p align="center">
  <a href="https://patreon.com/TechRZN">
    <img src="https://img.shields.io/badge/PATREON-UNTERSTÜTZER_WERDEN-orange?style=for-the-badge&logo=patreon&logoColor=white" height="45" />
  </a>
</p>

---

## 🚀 Direkt-Einbindung (Schnellzugriff)
> **WICHTIG:** Um den vollen Schutz zu erhalten, abonniere bitte **beide** Teile der Master-Liste.

<p align="center">
  <a href="https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/combined_part1.txt">
    <img src="https://img.shields.io/badge/MASTER_TEIL_1-LINK_KOPIEREN-7957d5?style=for-the-badge&logo=adguard&logoColor=white" height="45" />
  </a>
  &nbsp;&nbsp;
  <a href="https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/combined_part2.txt">
    <img src="https://img.shields.io/badge/MASTER_TEIL_2-LINK_KOPIEREN-7957d5?style=for-the-badge&logo=adguard&logoColor=white" height="45" />
  </a>
</p>

<p align="center">
  <a href="https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/whitelist.txt">
    <img src="https://img.shields.io/badge/WHITELIST-LINK_KOPIEREN-blue?style=for-the-badge&logo=github&logoColor=white" height="35" />
  </a>
</p>

> [!TIP]
> **Performance-Hinweis:** Durch die Aufteilung in zwei Dateien umgehen wir das 100MB-Limit von GitHub. Dein DNS-Server (AdGuard/Pi-hole) führt beide Listen im Arbeitsspeicher automatisch wieder zusammen.

---

## 🛡️ Optionale Zusatz-Module (Nicht in der Master-Liste)
*Diese Listen sind bewusst **nicht** Teil der Master-Liste, um Overblocking zu vermeiden. Sie können bei Bedarf zusätzlich abonniert werden.*

| Modul | Fokus | Link |
| :--- | :--- | :---: |
| **TechRZN Porn** | Umfassende Sperre expliziter & erotischer Inhalte. | [🔗 Kopieren](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/techrzn_porn.txt) |
| **TechRZN Jugendschutz** | Family-Safety: Schutz vor Inhalten für Erwachsene & Gewalt. | [🔗 Kopieren](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/techrzn_jugendschutz.txt) |

---

<details>
<summary><b>📦 Was steckt in der Master-Liste? (Inhaltsverzeichnis)</b></summary>
<br>

| Modul | Schutzwirkung | Icon |
| :--- | :--- | :---: |
| **Tracking & Ads** | Stoppt Datensammler & aggressive Werbung (Win/Android/iOS/TV). | 📱 |
| **Security Core** | Malware, Phishing, C2-Server & Threat Intelligence. | 🛡️ |
| **Einkaufsschutz** | Sperrt Fakeshops, Abofallen & Scam-Seiten. | 🛒 |
| **Tech-Schutz** | Blockiert Crypto-Miner, Spam-Domains & VPN-Bypass. | 🔓 |
| **Society** | Filtert Gambling, Dating & Fake Science (Desinformation). | 🎰 |
| **Global Core** | Enthält HaGeZi Pro, URLHaus, AdGuard German & Dan Pollock. | 🏆 |

</details>

---

## 🛠️ Einrichtung & Optimierung

<details>
<summary><b>📖 Schritt-für-Schritt Installation (AdGuard & Pi-hole)</b></summary>
<br>
<blockquote>
<h3>🛡️ AdGuard Home</h3>
1. Gehe zu <b>Filter</b> ➔ <b>DNS-Sperrlisten</b>.<br>
2. Klicke auf <b>Sperrliste hinzufügen</b>.<br>
3. Füge <b>zuerst Part 1</b> und dann <b>Part 2</b> hinzu.<br>

<h3>🥧 Pi-hole</h3>
1. Gehe zu <b>Adlists</b>.<br>
2. Füge beide URLs (Part 1 & 2) nacheinander ein.<br>
3. Führe <code>pihole -g</code> (Update Gravity) aus.
</blockquote>
</details>

<details>
<summary><b>⚙️ Optimale Hardware-Power (Kleve Backbone)</b></summary>
<br>
Diese Listen werden auf einem <b>UGREEN NAS DXP4800 Plus</b> mit 64GB RAM und 2.5 Gbit/s Anbindung validiert. Für eine reibungslose Verarbeitung von >2 Mio. Regeln empfehlen wir im AdGuard einen DNS-Cache von mindestens 100 MB.
</details>

---

**Gepflegt mit ❤️ von Madleen Berns in Kleve • Stand: März 2026**
<br>
<img src="https://capsule-render.vercel.app/render?type=soft&color=7957d5&height=30&section=footer" width="100%" />

</div>
