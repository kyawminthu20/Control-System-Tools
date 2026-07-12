---
layout: default
title: "NFPA 79 ↔ IEC 60204-1 Crosswalk"
description: "Topic-by-topic equivalency matrix between NFPA 79:2024 and IEC 60204-1:2016+AMD1:2021 for dual-market machinery."
breadcrumb:
  - name: "Crosswalks"
    url: "/tools/crosswalks/"
  - name: "NFPA 79 ↔ IEC 60204-1"
repo_path: "control-standards/rag/standards_intelligence/tools/crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md"
related_standards:
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
redirect_from:
  - /crosswalks/nfpa79-iec60204/
  - /crosswalks/nfpa79-iec60204/index.html
---

<div class="page-header">
  <span class="page-header__label">Crosswalk</span>
  <h1>NFPA 79:2024 ↔ IEC 60204-1:2016+AMD1:2021</h1>
  <p>Equivalency matrix for dual-market machinery (US + EU). Source: <code>rag/tools/crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md</code></p>
</div>

## Purpose

Use this crosswalk when designing machinery for both US and EU markets. Both standards cover the electrical equipment of machines with the same technical scope but differ in structure, wiring requirements, and some specifics.

**Strategy:** Design to the **most restrictive** requirement from each standard. Document compliance to both.

---

## Topic-Based Equivalency Matrix

| Topic Area | NFPA 79 | IEC 60204-1 | Equivalence | Notes |
|------------|---------|-------------|-------------|-------|
| Scope boundary | Ch. 1 | Clause 1 | High | Same connection point definition |
| Incoming supply / Disconnect | **Ch. 5** | **Clause 5** | **Very High** | Direct equivalent |
| Protection against electric shock | Ch. 7 | Clause 6 | High | IEC leads internationally |
| Equipment protection (overcurrent) | Ch. 6 | Clause 7 | High | Both cover overcurrent and environmental |
| **Grounding / Bonding** | **Ch. 8** | **Clause 8** | **Very High** | Direct equivalent; terminology differs (US: "grounding", IEC: "equipotential bonding") |
| **Control circuits / E-stop** | **Ch. 9** | **Clause 9** | **Very High** | Direct equivalent; stop categories (0, 1, 2) |
| Operator interface | Ch. 10 | Clause 10 | High | HMI, pushbuttons, indicators |
| Control equipment / Enclosures | Ch. 11 | Clause 11 | High | Panel design, environmental ratings |
| Motors and drives | Ch. 12 | Clause 12 | High | VFDs, motor protection |
| Wiring / Conductors | Ch. 14 | Clause 12 | Medium | Wire sizing methods differ |
| Accessories and lighting | Ch. 13, 14 | Clause 13 | Medium | IEC combines; NFPA separates |
| Marking and documentation | **Ch. 19** | **Clause 17** | High | IEC more prescriptive |
| Verification and testing | Ch. 20 | Clause 15 | High | IEC has explicit verification clause |

---

## Critical Differences

### Wire Colors

| Conductor | NFPA 79 | IEC 60204-1 |
|-----------|---------|-------------|
| Protective Earth (PE) | Green or bare | **Yellow-green** (required) |
| Neutral | White or gray | Blue |
| Phase conductors | Black, red, blue | Brown, black, gray |
| AC control | Red | Red |
| DC control | Blue | Dark blue |

**Implication for global machines:** Use yellow-green for PE (IEC 60204-1 takes precedence; NFPA 79 allows it).

### Voltage Scope

| Aspect | NFPA 79 | IEC 60204-1 |
|--------|---------|-------------|
| AC voltage ceiling | 1000 V (current edition; the 600 V figure is out of date) | 1000 V (1500 V DC) |
| DC voltage ceiling | — | 1500 V |

**Implication:** IEC 60204-1 covers higher voltages. For standard 480V / 400V machinery, both apply equally.

### Neutral Conductor Treatment

IEC 60204-1 provides more explicit requirements for neutral conductor sizing and protection. Review Clause 5 of IEC 60204-1 for neutral-specific requirements when designing for international markets.

---

## Highly Equivalent Sections (Direct Equivalents)

These sections have very high equivalence — compliance with one standard's requirements generally satisfies the other:

| Topic | NFPA 79 | IEC 60204-1 |
|-------|---------|-------------|
| Disconnecting means | Chapter 5 | Clause 5 |
| Grounding/bonding | Chapter 8 | Clause 8 |
| Control circuits | Chapter 9 | Clause 9 |
| Operator interface | Chapter 10 | Clause 10 |

---

## Recommended Approach for Global Machinery

1. Start with IEC 60204-1 as the base (EU requires it; US does not prohibit it)
2. Add NFPA 79 overlay checks for US-specific requirements (voltage rating, wire colors)
3. Document which standard's requirement is more restrictive for each topic
4. Use yellow-green PE wiring throughout (IEC requirement; compatible with NFPA 79)
5. Size conductors to the more restrictive of both standards
