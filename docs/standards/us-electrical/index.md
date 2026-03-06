---
layout: default
title: "US Electrical Standards"
description: "NEC, NFPA 79, and UL 508A — the three US standards for industrial control panels and machinery electrical design."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "US Electrical"
repo_path: "control-standards/rag/standards_intelligence/us/"
related_standards:
  - name: "IEC 60204-1 (International equivalent)"
    url: "/standards/machinery/iec-60204-1/"
  - name: "NFPA 79 ↔ IEC 60204-1 Crosswalk"
    url: "/crosswalks/nfpa79-iec60204/"
  - name: "UL 508A / NEC / NFPA 79 Crosswalk"
    url: "/crosswalks/ul508a-nec-nfpa79/"
crosswalk_refs:
  - name: "UL 508A / NEC / NFPA 79 Overlap"
    url: "/crosswalks/ul508a-nec-nfpa79/"
  - name: "NFPA 79 ↔ IEC 60204-1"
    url: "/crosswalks/nfpa79-iec60204/"
---

<div class="page-header">
  <span class="page-header__label">US Electrical Standards Family</span>
  <h1>NEC · NFPA 79 · UL 508A</h1>
  <p>Three interlocking standards that cover US-market industrial control panels and machinery electrical design.</p>
</div>

## How They Relate

The three US electrical standards are not alternatives — they work together:

| Role | Standard | Authority |
|------|----------|-----------|
| Legal electrical code | NEC (NFPA 70) | Adopted by AHJ; legally enforced in most US jurisdictions |
| Machinery electrical design | NFPA 79 | Contractual / customer-required; referenced by NEC Article 670 |
| Panel construction and listing | UL 508A | Required for UL listing; insurance and AHJ commonly require it |

**Typical US panel project:** UL 508A governs construction details + NEC Article 409 covers panel installation + NFPA 79 adds machinery context if the panel is part of a machine.

---

## Standards in This Family

### NEC (NFPA 70) — 2023 Edition

**Scope:** National Electrical Code. The US electrical installation standard, adopted as law in most US jurisdictions. Controls all electrical wiring and equipment installations.

**Key articles for industrial control:**
- Article 409 — Industrial control panels
- Article 430 — Motors and motor controllers
- Article 670 — Industrial machinery
- Article 250 — Grounding and bonding
- Article 725 — Control circuits

**Repo path:** `rag/us/nec/` (10 articles)

<a href="{{ '/standards/us-electrical/nec/' | relative_url }}" class="card__link">NEC detail page &rarr;</a>

---

### NFPA 79 — 2024 Edition

**Scope:** Electrical Standard for Industrial Machinery. Covers the electrical design of industrial machines — motor control, safety circuits, documentation requirements, and electrical enclosures for machinery.

**Key chapters:**
- Chapter 5 — Incoming supply / disconnects
- Chapter 8 — Grounding and bonding
- Chapter 9 — Control circuits, control functions, operator interface
- Chapter 12 — Motors and motor control
- Chapter 19 — Technical documentation

**Repo path:** `rag/us/nfpa79/` (20 chapters)

<a href="{{ '/standards/us-electrical/nfpa-79/' | relative_url }}" class="card__link">NFPA 79 detail page &rarr;</a>

---

### UL 508A — 2022 Edition

**Scope:** Standard for Industrial Control Panels. Governs the construction, marking, and listing of industrial control panels for the US market. Addresses short-circuit current rating (SCCR), wiring methods, and component spacing.

**Key sections:**
- Section 5 — Wire sizing
- Section 7 — Grounding
- Section SB — Short-circuit current rating (SCCR)
- Section 12 — Marking and documentation

**Repo path:** `rag/us/ul_508a/` (11 sections)

<a href="{{ '/standards/us-electrical/ul-508a/' | relative_url }}" class="card__link">UL 508A detail page &rarr;</a>

---

## Topic Routing

| Topic | NEC | NFPA 79 | UL 508A |
|-------|-----|---------|---------|
| Panel construction | Art. 409 | Ch 11 | All sections |
| Grounding / bonding | Art. 250 | Ch 8 | Sec. 7 |
| Motor protection | Art. 430 | Ch 12 | — |
| Emergency stop | — | Ch 9 | — |
| Wire sizing | Art. 310 | — | Sec. 5 |
| Short-circuit rating (SCCR) | Art. 409.110 | — | Sec. SB |
| Marking / documentation | Art. 110 | Ch 19 | Sec. 12 |
| Control circuits | Art. 725 | Ch 9 | — |

---

## Crosswalk References

- [UL 508A / NEC / NFPA 79 overlap table]({{ '/crosswalks/ul508a-nec-nfpa79/' | relative_url }})
- [NFPA 79 ↔ IEC 60204-1 comparison]({{ '/crosswalks/nfpa79-iec60204/' | relative_url }}) — for global machinery projects
