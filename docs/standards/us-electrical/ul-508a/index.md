---
layout: default
title: "UL 508A — Industrial Control Panels"
description: "UL 508A:2022 — panel construction, SCCR, listing requirements, and relationship to NEC and NFPA 79."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "US Electrical"
    url: "/standards/us-electrical/"
  - name: "UL 508A"
repo_path: "control-standards/rag/standards_intelligence/us/ul_508a/"
related_standards:
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
crosswalk_refs:
  - name: "UL 508A / NEC / NFPA 79 Overlap"
    url: "/crosswalks/ul508a-nec-nfpa79/"
lifecycle_stage:
  - name: "Detailed Design"
    slug: "detailed-design/"
  - name: "Build"
    slug: "build/"
---

<div class="page-header">
  <span class="page-header__label">US Electrical Standards · UL 508A</span>
  <h1>UL 508A:2022 — Industrial Control Panels</h1>
</div>

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | UL 508A |
| **Edition** | 2022 |
| **Publisher** | UL (Underwriters Laboratories) |
| **Jurisdiction** | United States |
| **Scope** | Construction and performance of industrial control panels |
| **Repository** | `rag/us/ul_508a/` — 11 sections |
| **Status in Corpus** | Complete |

**Purpose:** UL 508A defines requirements for the construction, materials, and performance of industrial control panels. A UL-listed panel means it has been evaluated and certified to meet UL 508A requirements. Insurance requirements and many AHJs require UL-listed panels for industrial installations.

---

## Why UL Listing Matters

| Driver | Requirement |
|--------|------------|
| Insurance | Often requires UL-listed panels |
| AHJ approval | Many jurisdictions require listed equipment |
| NEC compliance | NEC Article 409 references listed equipment |
| Customer specification | OEM customers frequently specify UL listing |

---

## Key Sections

| Section | Topic |
|---------|-------|
| 5 | Conductors — wire sizing, ampacity |
| 7 | Grounding and bonding requirements |
| 8 | Spacing — creepage and clearance |
| 9 | Marking and identification |
| 10 | Component ratings |
| 11 | Enclosed control equipment |
| 12 | Marking of industrial control panels |
| SB | Short-circuit current rating (SCCR) — critical section |

---

## Short-Circuit Current Rating (SCCR)

SCCR is one of the most important outputs of a UL 508A panel design. The panel must be rated for the available fault current at the point of installation.

**Key requirements:**
- Calculate SCCR for the panel assembly
- SCCR must match or exceed available fault current at the service
- NEC Article 409.110 requires the marked SCCR on the panel
- Component selection must support the required SCCR

**Calculation path:** UL 508A Section SB provides the method for determining panel SCCR based on component ratings.

---

## Topic Routing

| Topic | UL 508A Section | Also Covered By |
|-------|----------------|-----------------|
| Wire sizing | Sec. 5 | NEC Art. 310 |
| Grounding | Sec. 7 | NEC Art. 250, NFPA 79 Ch. 8 |
| SCCR | Sec. SB | NEC Art. 409.110 |
| Clearance/creepage | Sec. 8 | IEC 60204-1 Clause 11 |
| Panel marking | Sec. 12 | NFPA 79 Ch. 19 |

---

## Relationship to Other Standards

- **NEC Article 409** — Requires listed industrial control panels; UL 508A is the listing standard
- **NFPA 79** — Governs electrical design of the machine; UL 508A governs the panel construction within that machine
- **IEC 60204-1 Clause 11** — International equivalent for enclosed control equipment; no listing scheme, but similar technical requirements

<a href="{{ '/crosswalks/ul508a-nec-nfpa79/' | relative_url }}" class="card__link">View UL 508A / NEC / NFPA 79 overlap table &rarr;</a>
