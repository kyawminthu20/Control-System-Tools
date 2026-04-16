---
layout: default
title: "IEC 60204-1 — Electrical Equipment of Machines"
description: "IEC 60204-1:2018 — scope, key clauses, lifecycle stage, and relationship to NFPA 79."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "International Machinery"
    url: "/standards/machinery/"
  - name: "IEC 60204-1"
repo_path: "control-standards/rag/standards_intelligence/international/machinery/iec_60204_1/"
related_standards:
  - name: "NFPA 79 (US equivalent)"
    url: "/standards/us-electrical/nfpa-79/"
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
crosswalk_refs:
  - name: "NFPA 79 ↔ IEC 60204-1 Overlap"
    url: "/tools/crosswalks/nfpa79-iec60204/"
lifecycle_stage:
  - name: "Standards Selection"
    slug: "standards-selection/"
  - name: "Detailed Design"
    slug: "detailed-design/"
  - name: "Build"
    slug: "build/"
---

<div class="page-header">
  <span class="page-header__label">International Machinery · IEC 60204-1</span>
  <h1>IEC 60204-1:2018 — Electrical Equipment of Machines</h1>
</div>

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | IEC 60204-1 |
| **Edition** | 2018 |
| **Publisher** | International Electrotechnical Commission (IEC) |
| **Jurisdiction** | Global; harmonized in EU under Machinery Directive |
| **Scope** | Electrical and electronic equipment on industrial machines |
| **Repository** | `rag/international/machinery/iec_60204_1/` — 15 clauses |
| **Status in Corpus** | Complete |

**Purpose:** IEC 60204-1 applies to electrical, electronic, and programmable electronic equipment and systems to machines not portable by hand while working. It applies to circuits above 25 V AC or 60 V DC and up to 1000 V AC / 1500 V DC.

---

## Lifecycle Stages

| Stage | Application |
|-------|------------|
| **Standards Selection** | Confirm IEC 60204-1 applies (machine type, voltage, market) |
| **Detailed Design** | Wire sizing, circuit design, control panel layout |
| **Build** | Compliance verification during panel construction |
| **Commissioning** | Documentation requirements (Clause 17) |

---

## Key Clauses

| Clause | Topic | NFPA 79 Crosswalk |
|--------|-------|------------------|
| 4 | General requirements | — |
| 5 | Incoming supply / disconnects | Ch 5 |
| 6 | Protection against electric shock | Ch 6 |
| 7 | Protection of equipment | Ch 7 |
| 8 | Equipotential bonding (grounding) | Ch 8 |
| 9 | Control circuits and functions | Ch 9 |
| 10 | Operator interface and mounted control devices | Ch 10 |
| 11 | Control equipment — enclosures and mounting | Ch 11 |
| 12 | Conductors and cables | Ch 14 |
| 13 | Motor and associated equipment | Ch 12 |
| 14 | Accessories and lighting | — |
| 15 | Marking | Ch 19 |
| 16 | Technical documentation | Ch 19 |
| 17 | Technical documentation (detailed) | Ch 19 |

---

## Emergency Stop (Clause 9)

IEC 60204-1 Clause 9 addresses emergency stop (Category 0, 1, 2) and safety-related stop functions. For formal safety function design, this clause works with:

- [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) — Performance Level (PL) approach
- [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}) — SIL approach for machinery
- ISO 13850 — Emergency stop devices (referenced by both)

---

## Global Machine Projects

For machines sold in both US and EU markets, use **both** IEC 60204-1 and NFPA 79 and design to the most restrictive requirement from each.

Key differences to watch for:
- **Wire colors**: IEC 60204-1 requires yellow-green for PE; NFPA 79 allows green or bare
- **Voltage rating**: IEC 60204-1 covers to 1000 V AC; NFPA 79 is 600 V
- **Neutral conductor** requirements differ in detail

<a href="{{ '/tools/crosswalks/nfpa79-iec60204/' | relative_url }}" class="card__link">View NFPA 79 ↔ IEC 60204-1 full crosswalk &rarr;</a>
