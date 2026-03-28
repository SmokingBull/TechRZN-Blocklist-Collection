<p align="center">
  <img src="techrzn-dns.png" width="400" alt="TechRZN DNS Logo">
</p>

<p align="center">
  Language: 🇺🇸 <b>[English]</b> | 🇩🇪 <a href="README.md">[Deutsch]</a>
</p>

# 🛡️ TechRZN-Blocklist-Collection
### High-Performance Blocklists • Updated Daily • 100% Cleaned

<p align="left">
  <a href="https://github.com/TechRZN-DNS/TechRZN-Blocklist-Collection/actions/workflows/main.yml">
    <img src="https://github.com/TechRZN-DNS/TechRZN-Blocklist-Collection/actions/workflows/main.yml/badge.svg" alt="Blocklist Update">
  </a>
  <img src="https://img.shields.io/github/last-commit/TechRZN-DNS/TechRZN-Blocklist-Collection?style=flat-square&color=blue" alt="Last Commit">
  <img src="https://img.shields.io/badge/Total_Rules-1M+-success?style=flat-square" alt="Rules">
  <img src="https://img.shields.io/badge/Service-Automated-orange?style=flat-square" alt="Status">
</p>

Welcome to the **TechRZN Filter-Hub**. This repository provides a daily updated "All-in-One" blocklist for **AdGuard Home**, **Pi-hole**, and **Technitium**. All lists are automatically deduplicated and cross-checked against a multi-stage whitelist.

---

## 🚀 The Master-List (Recommended)
The ultimate solution for your setup. Contains all **11 listed modules** in a single, high-performance file.

**Link for your DNS-Filter:**
> `https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/combined_blocklist.txt`

---

## 🧩 Modular Filter Architecture (The 14 Core Modules)
| Module | Focus / Protection Area | Raw Link |
| :--- | :--- | :--- |
| 🥇 **HaGeZi Pro** | Global All-in-One Protection (Gold Standard) | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/hagezi_pro.txt) |
| 🔐 **Bypass Filter** | VPN, Proxy, Tor & Bypass Methods | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/bypass.txt) |
| 🏴‍☠️ **Threat Intel** | Defense against Cyber Attacks & Botnets | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/threat_intel.txt) |
| 🇩🇪 **German Filter** | **Special Optimization for DE / AT / CH** | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/german_filter.txt) |
| 📺 **Smart TV** | Prevents TV Tracking & Advertising | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/smart_tv.txt) |
| 🦠 **URLHaus** | Malware URLs & Phishing (Real-time) | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/urlhaus.txt) |
| 💻 **Windows Spy** | Hardening for MS Telemetry & Office | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/windows_spy.txt) |
| 🎮 **Gambling** | Blocking of Gambling & Betting Sites | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/gambling.txt) |
| ⚠️ **Fake DNS** | Protection against Scams & Fake Shops | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/fake_dns.txt) |
| 📜 **Dan Pollock** | Legendary Hosts File Classic | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/dan_pollock.txt) |
| 📍 **TechRZN IPs** | Custom List of Malicious IP Addresses | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/techrzn_ips.txt) |
| 🛍️ **Anti-Fakeshop** | Defense against Scam Shops & Subs (RPiList) | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/notserious.txt) |
| 🏦 **Banking Protection** | Phishing Shield (DE/AT/CH Banks - RPiList) | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/phishing_de.txt) |
| 🧪 **Fake Science** | Blocks Predatory Publishers & Scam Portals (RPiList) | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/fake_science.txt) |

---

## ⚪ Intelligent Whitelists
To prevent "overblocking," TechRZN uses a two-stage process:

1. **HaGeZi Referral Whitelist:** Automatically integrated to prevent global false positives.
2. **TechRZN Custom Whitelist:** Manual list (`whitelist.txt`) for personal exceptions (e.g., **UGREEN Updates**, **FRITZ!Box Services**, **Microsoft**).

---

## ⚙️ Optimal AdGuard Home Settings
For best performance with this collection (1M+ rules), we recommend configuring your AdGuard Home as follows:

### 1️⃣ DNS Cache Settings
* **Cache Size:** `104,857,600` (100 MB) ✅
* **Optimistic Caching:** Enabled ✅
* **TTL Minimum:** `3600` (1 hour) 💡
* **TTL Maximum:** `86400` (24 hours) 💡

### 2️⃣ DNS Server Configuration
* **DNSSEC:** Enabled ✅
* **Blocking Mode:** `Default` ✅
* **Blocking Response TTL:** `300` seconds ✅

### 3️⃣ Private Inverse DNS Servers
* **Use private reverse DNS resolvers:** Enabled ✅
* **Enable hostname resolution for clients:** Enabled ✅
* **Upstream Timeout:** `2` seconds ✅
* **DNS Server:** Please enter your **local router's DNS IP** (e.g., FRITZ!Box).

---

## 🙏 Credits & Copyright (TechRZN)
Special thanks to the sources that make this project possible:

* **[HaGeZi](https://github.com/hagezi/dns-blocklists):** The gold standard of blocklists.
* **[AdGuard Team](https://github.com/AdguardTeam):** German language filters & registry.
* **[Abuse.ch (URLHaus)](https://urlhaus.abuse.ch/):** Malware Intelligence.
* **[Dan Pollock](https://someonewhocares.org/hosts/):** The legendary hosts classic.

---
*Maintained with ❤️ by TechRZN in Kleve • Last Update: March 2026*

---

## ❤️ Support TechRZN
Maintaining 1M+ rules daily and running the 2.5 Gbit/s test infrastructure on my UGREEN NAS (64 GB RAM) takes time and resources. If my work helps you, I would appreciate your support!

[![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://www.patreon.com/cw/TechRZN_DNS)

---

## ☕ Support & Infrastructure
Running a **2.5 Gbit/s test environment** (UGREEN NAS with **64 GB RAM**) and maintaining over 1 million rules daily takes time and resources. 

If my work helps you:
* **Feedback:** Open an issue or give the project a ⭐.
* **Support:** Since my Patreon is currently under review, please contact me directly if you're interested in supporting the project.

*Maintained with ❤️ in Kleve • Status: March 2026*
