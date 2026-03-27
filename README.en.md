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

## 🧩 All 11 Filter Modules (Individual)
You can subscribe to these filters separately by category.

| Module | Focus / Protection Area | Raw-Link |
| :--- | :--- | :--- |
| **🥇 HaGeZi Pro** | All-in-One Protection | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_pro.txt) |
| **🔐 Bypass Filter** | VPN/Proxy/Tor/Bypass | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_bypass.txt) |
| **🏴‍☠️ Threat Intel** | Cyber Attacks & Botnets | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_threat.txt) |
| **🇩🇪 German Filter** | DE/AT/CH Optimization | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/adguard_german.txt) |
| **📺 Smart-TV** | TV Tracking & Ads | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/smart_tv.txt) |
| **🦠 URLHaus** | Malware URLs & Phishing | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/urlhaus_malicious.txt) |
| **💻 Windows Spy** | MS Telemetry & Office | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_windows.txt) |
| **🎮 Gambling** | Gambling & Betting | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_gambling.txt) |
| **⚠️ Fake DNS** | Scam & Fake Shops | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/hagezi_fake.txt) |
| **📜 Dan Pollock** | Hosts-File Classic | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/dan_pollock.txt) |
| **📍 TechRZN IPs** | Custom Malicious IP List | [Link](https://raw.githubusercontent.com/TechRZN-DNS/TechRZN-Blocklist-Collection/main/lists/techrzn_ips.txt) |

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
