<div align="center">

<br>

<p align="center">
  <img src="techrzn.png" width="650" alt="TechRZN DNS Filter-Hub" />
</p>

<p align="center">
  Language: 🇩🇪 <a href="README.md">[German]</a> | 🇺🇸 <b>[English]</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-INFRASTRUCTURE_ACTIVE-00C853?style=for-the-badge&logo=statuspage&logoColor=white" />
  <img src="https://img.shields.io/badge/DATABASE-1M%2B_RULES-FF6B6B?style=for-the-badge&logo=databricks&logoColor=white" />
  <img src="https://img.shields.io/badge/UPLINK-2.5_GBIT_BACKBONE-7957d5?style=for-the-badge&logo=wi-fi&logoColor=white" />
</p>

---

## 🛰️ Mission & Vision
> **High-Performance Blocklists • Updated Daily • 100% Cleaned**

Welcome to the **TechRZN Filter Hub**. This repository provides a highly optimized "All-in-One" solution for **AdGuard Home, Pi-hole, and Technitium**. Through automated deduplication and an intelligent whitelist, we guarantee protection without "overblocking".

---

## 🚀 Quick Deployment
> **All-in-One Solution:** The Master List already includes all **14 modules listed below** in a single file. One link for complete protection.

<p align="center">
  <a href="https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/combined_blocklist.txt">
    <img src="https://img.shields.io/badge/MASTER_LIST-COPY_LINK-7957d5?style=for-the-badge&logo=adguard&logoColor=white" height="45" />
  </a>
  &nbsp;&nbsp;
  <a href="https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/whitelist.txt">
    <img src="https://img.shields.io/badge/WHITELIST-COPY_LINK-blue?style=for-the-badge&logo=github&logoColor=white" height="45" />
  </a>
</p>

---

## 🧩 The 14 Core Modules (Individual Access)
*For manual selection – all of these are already included in the **Master List** above.*

| Status | Module | Focus / Protection Area | Link |
| :--- | :--- | :--- | :---: |
| 🥇 | **HaGeZi Pro** | Global Protection (Gold Standard) | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_pro.txt) |
| 🔐 | **Bypass Filter** | VPN, Proxy, Tor & Bypass Methods | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_bypass.txt) |
| 🏴‍☠️ | **Threat Intel** | Cyber Attacks & Botnets | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_threat.txt) |
| 🇩🇪 | **German Filter** | Optimization for DE / AT / CH | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/adguard_german.txt) |
| 📺 | **Smart TV** | Tracking & TV Advertising | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/smart_tv.txt) |
| 🦠 | **URLHaus** | Malware & Phishing (Real-time) | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/urlhaus_malicious.txt) |
| 💻 | **Windows Spy** | MS Telemetry & Office Hardening | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_windows.txt) |
| 🎮 | **Gambling** | Blocking of Gambling & Betting Sites | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_gambling.txt) |
| ⚠️ | **Fake DNS** | Protection against Scams & Fake Shops | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_fake.txt) |
| 📜 | **Dan Pollock** | Legendary Hosts File Classic | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/dan_pollock.txt) |
| 📍 | **TechRZN IPs** | Custom List of Malicious IP Addresses | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/techrzn_ips.txt) |
| 🛍️ | **Anti-Fakeshop** | Scam Shops & Subscription Traps | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/notserious.txt) |
| 🏦 | **Banking Protect** | Phishing Shield (DE-Banks) | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/phishing_de.txt) |
| 🧪 | **Fake Science** | Blocks Predatory Publishers | [🔗](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/fake_science.txt) |

---

## 🛠️ Setup & Optimization

<details>
<summary><b>📖 Step-by-Step Installation (AdGuard & Pi-hole)</b></summary>
<br>
<blockquote>
<h3>🛡️ AdGuard Home</h3>
1. Navigate to <b>Filters</b> ➔ <b>DNS Blocklists</b>.<br>
2. Click <b>Add Blocklist</b> ➔ <b>Add a custom list</b>.<br>
3. Name: <code>TechRZN Master</code> | URL: Use the buttons above.<br>

<h3>🥧 Pi-hole</h3>
1. Navigate to <b>Adlists</b> in the left sidebar.<br>
2. Paste the URL into the <b>Address</b> field and click <b>Add</b>.<br>
3. <b>Important:</b> Run <i>Tools</i> ➔ <i>Update Gravity</i> to load the new rules.
</blockquote>
</details>

<details>
<summary><b>⚙️ Optimal AdGuard Home Settings (Recommended)</b></summary>
<br>
<blockquote>
For maximum performance with 1M+ rules (tested on <b>UGREEN NAS / 2.5 Gbit/s</b>):<br><br>
<b>1. DNS Cache & TTL</b><br>
* Cache Size: <code>104,857,600</code> (100 MB)<br>
* Optimistic Caching: <b>Enabled</b> ✅<br>
* TTL Minimum: <code>3600</code> (1 hour)<br><br>
<b>2. Security & Filtering</b><br>
* DNSSEC: <b>Enabled</b> ✅<br>
* Blocking Mode: <code>Default</code><br>
* Blocked Response TTL: <code>300</code> sec.
</blockquote>
</details>

---

## 🏗️ Hardware Backbone (Kleve, Germany)
*Validation on enterprise hardware for absolute reliability.*

<table align="center" width="100%" style="border-collapse: collapse; background-color: #0d1117; border-radius: 12px; overflow: hidden; border: 1px solid #30363d;">
  <tr>
    <td align="left" style="padding: 20px;">
      <b>CORE NODE</b><br>UGREEN NAS DXP4800 Plus<br>
      <img src="https://img.shields.io/badge/64_GB_DDR5_ECC-7957d5?style=flat-square" />
    </td>
    <td align="left" style="padding: 20px;">
      <b>ACCELERATION</b><br>2x Samsung 990 Pro RAID<br>
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

## 🙏 Credits & Sources
This project is built upon the great work of: **HaGeZi**, **RPiList**, **AdGuard Team**, and **Abuse.ch**.

**Maintained with ❤️ by Jörg Berns in Kleve • Status: March 2026**
<br>
<img src="https://capsule-render.vercel.app/render?type=soft&color=7957d5&height=30&section=footer" width="100%" />

</div>
