<div align="center">

<br>

<p align="center">
  <img src="social-preview.png" width="650" alt="TechRZN DNS Filter-Hub" />
</p>

<p align="center">
  Sprache: 🇩🇪 <b>[Deutsch]</b> | 🇺🇸 <a href="README.en.md">[English]</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-INFRASTRUKTUR_AKTIV-00C853?style=for-the-badge&logo=statuspage&logoColor=white" />
  <img src="https://img.shields.io/badge/DATENBANK-1M%2B_REGELN-FF6B6B?style=for-the-badge&logo=databricks&logoColor=white" />
  <img src="https://img.shields.io/badge/UPLINK-2.5_GBIT_BACKBONE-7957d5?style=for-the-badge&logo=wi-fi&logoColor=white" />
</p>

---

## 🛰️ Mission & Vision
> **High-Performance Blocklisten • Täglich aktualisiert • 100% Bereinigt**

Willkommen beim **TechRZN Filter-Hub**. Dieses Repository bietet eine hochoptimierte "All-in-One" Lösung für **AdGuard Home, Pi-hole und Technitium**. Durch automatisierte Deduplizierung und eine intelligente Whitelist garantieren wir Schutz ohne "Overblocking".

---

## 🚀 Direkt-Einbindung (Schnellzugriff)
> **All-in-One Lösung:** Die Master-Liste enthält bereits alle **14 unten aufgeführten Module** in einer einzigen Datei. Ein Link für den kompletten Schutz.

<p align="center">
  <a href="https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/combined_blocklist.txt">
    <img src="https://img.shields.io/badge/MASTER_LISTE-LINK_KOPIEREN-7957d5?style=for-the-badge&logo=adguard&logoColor=white" height="45" />
  </a>
  &nbsp;&nbsp;
  <a href="https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/whitelist.txt">
    <img src="https://img.shields.io/badge/WHITELIST-LINK_KOPIEREN-blue?style=for-the-badge&logo=github&logoColor=white" height="45" />
  </a>
</p>

---

## 🧩 Die 14 Core-Module (Einzelzugriff)
*Zur manuellen Auswahl – alle bereits in der **Master-Liste** enthalten.*

| Status | Modul | Fokus / Schutzbereich | Link |
| :--- | :--- | :--- | :---: |
| 🥇 | **HaGeZi Pro** | Weltweiter Schutz (Gold Standard) | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_pro.txt) |
| 🔐 | **Bypass Filter** | VPN, Proxy, Tor & Bypass-Methoden | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_bypass.txt) |
| 🏴‍☠️ | **Threat Intel** | Schutz vor Cyberangriffen & Botnetzen | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_threat.txt) |
| 🇩🇪 | **German Filter** | Optimierung für DE / AT / CH | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/adguard_german.txt) |
| 📺 | **Smart TV** | Unterbindet TV-Tracking & Werbung | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/smart_tv.txt) |
| 🦠 | **URLHaus** | Malware-URLs & Phishing (Echtzeit) | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/urlhaus_malicious.txt) |
| 💻 | **Windows Spy** | Härtung für MS-Telemetrie & Office | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_windows.txt) |
| 🎮 | **Gambling** | Sperrung von Glücksspiel & Wetten | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_gambling.txt) |
| ⚠️ | **Fake DNS** | Schutz vor Betrug & Fake-Shops | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_fake.txt) |
| 📜 | **Dan Pollock** | Legendärer Hosts-File Klassiker | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/dan_pollock.txt) |
| 📍 | **TechRZN IPs** | Eigene Liste bösartiger IP-Adressen | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/techrzn_ips.txt) |
| 🛍️ | **Anti-Fakeshop** | Abwehr von Fake-Shops & Abofallen | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/notserious.txt) |
| 🏦 | **Banking-Schutz** | Phishing-Schild (DE-Banken) | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/phishing_de.txt) |
| 🧪 | **Fake Science** | Blockiert Pseudo-Wissenschaft | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/fake_science.txt) |

---

## 🛠️ Einrichtung & Optimierung

<details>
<summary><b>📖 Schritt-für-Schritt Installation (AdGuard & Pi-hole)</b></summary>
<br>
<blockquote>
<h3>🛡️ AdGuard Home</h3>
1. Gehe zu <b>Filter</b> ➔ <b>DNS-Sperrlisten</b>.<br>
2. Klicke auf <b>Sperrliste hinzufügen</b> ➔ <b>Benutzerdefinierte Liste</b>.<br>
3. Name: <code>TechRZN Master</code> | URL: Button oben nutzen.<br>

<h3>🥧 Pi-hole</h3>
1. Gehe zu <b>Adlists</b> im linken Menü.<br>
2. Füge die URL in das Feld <b>Address</b> ein und klicke auf <b>Add</b>.<br>
3. <b>Wichtig:</b> Führe unter <i>Tools</i> ➔ <i>Update Gravity</i> ein Update aus.
</blockquote>
</details>

<details>
<summary><b>⚙️ Optimale AdGuard Home Einstellungen (Empfohlen)</b></summary>
<br>
<blockquote>
Für maximale Performance mit 1M+ Regeln (getestet auf <b>UGREEN NAS / 2,5 Gbit/s</b>):<br><br>
<b>1. DNS-Cache & TTL</b><br>
* Cache-Größe: <code>104.857.600</code> (100 MB)<br>
* Optimistisches Caching: <b>Aktiviert</b> ✅<br>
* TTL-Minimalwert: <code>3600</code> (1 Stunde)<br><br>
<b>2. Sicherheit & Filterung</b><br>
* DNSSEC: <b>Aktiviert</b> ✅<br>
* Sperermodus: <code>Standard</code><br>
* Gültigkeitsdauer blockierter Antwort: <code>300</code> Sek.
</blockquote>
</details>

---

## 🏗️ Hardware Backbone (Kleve, NRW)
*Validierung auf Enterprise-Hardware für absolute Zuverlässigkeit.*

<table align="center" width="100%" style="border-collapse: collapse; background-color: #0d1117; border-radius: 12px; overflow: hidden; border: 1px solid #30363d;">
  <tr>
    <td align="left" style="padding: 20px;">
      <b>CORE NODE</b><br>UGREEN NAS DXP4800 Plus<br>
      <img src="https://img.shields.io/badge/64_GB_DDR5_ECC-7957d5?style=flat-square" />
    </td>
    <td align="left" style="padding: 20px;">
      <b>BESCHLEUNIGUNG</b><br>2x Samsung 990 Pro RAID<br>
      <img src="https://img.shields.io/badge/NVMe_Gen4_RAID_1-FF6B6B?style=flat-square" />
    </td>
  </tr>
  <tr>
    <td align="left" style="padding: 20px;">
      <b>NETWORK</b><br>2.5 Gbit Hybrid-Power<br>
      <img src="https://img.shields.io/badge/Zyxel_Managed_Switch-00D2FF?style=flat-square" />
    </td>
    <td align="left" style="padding: 20px;">
      <b>STORAGE</b><br>80 TB WD Red Pro (12G SAS)<br>
      <img src="https://img.shields.io/badge/RAID_5_ZFS-00C853?style=flat-square" />
    </td>
  </tr>
</table>

---

## 🙏 Danksagung & Quellen
Dieses Projekt basiert auf der Arbeit von: **HaGeZi**, **RPiList**, **AdGuard Team** und **Abuse.ch**.

**Gepflegt mit ❤️ von Jörg Berns in Kleve • Stand: März 2026**
<br>
<img src="https://capsule-render.vercel.app/render?type=soft&color=7957d5&height=30&section=footer" width="100%" />

</div>
