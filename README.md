# UTM Campaign Governance Hub & Interactive Builder

> Create consistently tagged campaign links and reduce avoidable UTM classification errors. This tool cannot guarantee that GA4 will eliminate '(Other)' or 'Unassigned' traffic.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: STATIC_INTERACTIVE_TOOL](https://img.shields.io/badge/Format-STATIC--INTERACTIVE--TOOL-green.svg)](#)
[![Tier: 2](https://img.shields.io/badge/Tier-2-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**BOTH** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Build an open-source UTM governance hub: 1) Single-file responsive HTML/JS tool (`index.html`) running client-side with dropdown enforcement strictly adhering to GA4 Default Channel Grouping rules, 2) Python CLI (`utm_validator.py`) auditing CSV lists of live ad links, 3) Enterprise UTM policy document, 4) Integration cheat sheet for Slack/Teams.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `config/utm_taxonomy.json`
- `docs/utm-best-practices.md`
- `examples/sample_links_audit.csv`
- `index.html`
- `LICENSE`
- `policy/enterprise-utm-standards.md`
- `README.md`
- `src/url_cleaner.py`
- `src/utm_validator.py`
- `tests/test_cleaner.py`
- `tests/test_validator.py`
- `tools/index.html`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/url_cleaner.py --help
```

### Interactive Browser Tool
Open `index.html` directly in your web browser (Chrome, Edge, Safari) to use the local interactive calculator or dashboard. Operates 100% client-side with zero external network calls.

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "reporting",
  "repository": "utm-campaign-governance-hub",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Case Sensitivity & Normalization:** Enforces strict lowercase normalization on utm_source, utm_medium, and utm_campaign to prevent reporting fragmentation.
- **Delimiter Standard:** Replaces spaces with hyphens or underscores; flags unauthorized punctuation characters.
- **Encoding Compliance:** Ensures landing page URLs with Arabic query parameters or anchors are properly percent-encoded per RFC 3986.

---

## 📚 Primary Documentation & Verifiable References

- [Google Analytics Help: URL Builder & Traffic Sources](https://support.google.com/analytics/answer/10918840) - Official documentation on manual campaign tagging dimensions.
- [Google Analytics 4 Manual Tagging Best Practices](https://support.google.com/analytics/answer/10917952) - Standard naming conventions for source, medium, and campaign.
- [RFC 3986: Uniform Resource Identifier (URI) Generic Syntax](https://datatracker.ietf.org/doc/html/rfc3986) - Standard IETF specification for URI parameter encoding.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
