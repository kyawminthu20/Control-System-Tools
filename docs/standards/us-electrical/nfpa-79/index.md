---
layout: default
title: "NFPA 79 — Electrical Standard for Industrial Machinery"
description: "NFPA 79:2024 — scope, key chapters, lifecycle stage, and relationship to NEC and IEC 60204-1."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "US Electrical"
    url: "/standards/us-electrical/"
  - name: "NFPA 79"
repo_path: "control-standards/rag/standards_intelligence/us/nfpa79/"
related_standards:
  - name: "IEC 60204-1 (International equivalent)"
    url: "/standards/machinery/iec-60204-1/"
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
  - name: "UL 508A"
    url: "/standards/us-electrical/ul-508a/"
crosswalk_refs:
  - name: "NFPA 79 ↔ IEC 60204-1 Overlap"
    url: "/tools/crosswalks/nfpa79-iec60204/"
lifecycle_stage:
  - name: "Detailed Design"
    slug: "detailed-design/"
  - name: "Build"
    slug: "build/"
  - name: "Installation"
    slug: "installation/"
---

<div class="page-header">
  <span class="page-header__label">US Electrical Standards · NFPA 79</span>
  <h1>NFPA 79:2024 — Electrical Standard for Industrial Machinery</h1>
</div>

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | NFPA 79 |
| **Edition** | 2024 |
| **Publisher** | National Fire Protection Association (NFPA) |
| **Jurisdiction** | United States |
| **Scope** | Electrical/electronic equipment for industrial machines |
| **Repository** | `rag/us/nfpa79/` — 20 chapters |
| **Status in Corpus** | Complete |

**Purpose:** NFPA 79 covers the electrical and electronic equipment, apparatus, and wiring of industrial machinery operating from a nominal voltage not exceeding 600 V. It applies to the point of connection of the supply conductor(s) to the machine and covers all electrical equipment after that point.

---

## Lifecycle Stages

NFPA 79 is primarily applied during:

| Stage | Application |
|-------|------------|
| **Standards Selection** | Determine if machinery scope applies |
| **Detailed Design** | Wire sizing, circuit design, panel layout, safety circuits |
| **Build** | Panel construction compliance check |
| **Installation** | Handoff requirements; NEC Article 670 governs installation |

---

## Key Chapters

| Chapter | Topic | Crosswalk (IEC 60204-1) |
|---------|-------|------------------------|
| 5 | Incoming supply / disconnects | Clause 5 |
| 6 | Protection against electric shock | Clause 6 |
| 7 | Protection of equipment | Clause 7 |
| 8 | Grounding and bonding | Clause 8 |
| 9 | Control circuits, emergency stop, interlocking | Clause 9, 10 |
| 10 | Operator interface / control devices | Clause 10 |
| 11 | Control equipment — general | Clause 11 |
| 12 | Motors, motor drives, motor controls | Clause 12 |
| 14 | Wiring practices | Clause 13 |
| 17 | Electronic equipment | Clause 14 |
| 19 | Technical documentation | Clause 17 |

---

## Relationship to NEC and UL 508A

```
NEC Article 670 (Industrial Machinery) references NFPA 79
        ↓
NFPA 79 governs machine electrical design
        ↓
UL 508A governs panel construction if UL listing required
        ↓
NEC Article 409 governs panel installation
```

**When all three apply:** Machine in US market with UL-listed control panel. NFPA 79 defines the electrical design requirements; UL 508A governs the panel construction and listing; NEC covers installation.

---

## PL / SIL Relevance

NFPA 79 Chapter 9 addresses safety-related control circuits and emergency stop functions. For formal safety function design (Performance Level or SIL), NFPA 79 provides the electrical implementation requirements — the safety architecture and PL/SIL calculation comes from [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) or [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}).

---

## Related Standards

- [IEC 60204-1]({{ '/standards/machinery/iec-60204-1/' | relative_url }}) — International equivalent; use for CE-marked machinery
- [NEC]({{ '/standards/us-electrical/nec/' | relative_url }}) — Installation code; Article 670 references NFPA 79
- [UL 508A]({{ '/standards/us-electrical/ul-508a/' | relative_url }}) — Panel listing; applies alongside NFPA 79
- [NFPA 79 ↔ IEC 60204-1 crosswalk]({{ '/tools/crosswalks/nfpa79-iec60204/' | relative_url }})
