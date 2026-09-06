
# Linkguard

A URL safety scanner that checks links for malicious intent before you click them — combining multiple detection layers into a single risk score.

## Why I built this

Most people click links without thinking twice, and shortened or disguised URLs make it easy to hide where a link actually leads. I wanted to build something that pulls together several real detection techniques — the kind actual browsers and security tools use — into one accessible tool, rather than relying on any single check.

## Features

- **URL shortener detection** — flags when a link uses a known shortening service (bit.ly, tinyurl, etc.), since these hide the real destination
- **Domain reputation heuristics** — flags structurally suspicious domains (unusual TLDs, excessive digits/hyphens, unusually long names)
- **VirusTotal integration** — checks a URL against VirusTotal's aggregated results from dozens of security vendors
- **Google Safe Browsing integration** — checks a URL against Google's live database of known malware and phishing sites
- **Risk scoring system** — combines all signals into a single 0-100 score and a clear Low/Medium/High risk rating
- **Custom detection rules** — lets you maintain your own banned domain and keyword lists
- **Scan history** — keeps a local log of every scan performed
- **Exportable reports** — generates a readable `.txt` report for any scan

## How the risk score works

Each detection layer contributes to a weighted score:
- Shortened URLs add a baseline risk (they hide the destination, which is inherently a red flag)
- Domain reputation flags each add incrementally
- VirusTotal detections are weighted by how many vendors flagged the URL as malicious or suspicious
- A Google Safe Browsing match adds a significant risk weight, since it's a direct match against a known threat database
- Custom rule matches (your own banned domains/keywords) are weighted heavily, since they represent known, specific threats to you

Scores are capped at 100 and mapped to Low (0-24), Medium (25-59), or High (60-100) risk.

## Usage

```bash
python linkguard.py
```

Run it and choose from the menu: scan a URL, view scan history, export a report, or add a custom detection rule.

**API keys (optional but recommended):** VirusTotal and Google Safe Browsing checks require free API keys, added at the top of the script. Without them, Linkguard still runs fully using shortener detection, domain heuristics, and custom rules — it just skips those two checks gracefully.

## What I'd improve next

- Add a proper WHOIS-based domain age check (very new domains are a strong phishing signal)
- Batch scanning — check a list of URLs at once instead of one at a time
- A simple web interface instead of a CLI menu
- Weight tuning based on real-world testing rather than initial estimates

## Tech stack

Python, `requests`

## ⚠️ Note on ethical use

This tool checks publicly available threat intelligence data about URLs. It does not access, scrape, or store any private information about websites or their owners beyond what's already used for security screening.

---

Part of my ongoing work toward Cloud AI Architecture, focused on building practical, layered security tooling.