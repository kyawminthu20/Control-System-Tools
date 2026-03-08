---
layout: default
title: "NEC (NFPA 70) — National Electrical Code"
description: "NEC 2023 — key articles for industrial control panels and machinery: 409, 409.70, 430, 670, 670.6, 250, 725."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "US Electrical"
    url: "/standards/us-electrical/"
  - name: "NEC"
repo_path: "control-standards/rag/standards_intelligence/us/nec/"
related_standards:
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
  - name: "UL 508A"
    url: "/standards/us-electrical/ul-508a/"
lifecycle_stage:
  - name: "Detailed Design"
    slug: "detailed-design/"
  - name: "Installation"
    slug: "installation/"
last_reviewed: "2026-03-08"
primary_audience: "Panel designers, machine builders, controls engineers, AHJ-facing documentation"
edition_note: "Always verify the edition adopted by the local AHJ. Many jurisdictions are not on the current NEC cycle."
companion_standards:
  - "NFPA 79"
  - "UL 508A"
  - "ISO 12100"
  - "ISO 13849-1"
  - "IEC 60204-1"
---

<div class="page-header">
  <span class="page-header__label">US Electrical Standards · NEC</span>
  <h1>NEC (NFPA 70):2023 — National Electrical Code</h1>
</div>

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | NEC (NFPA 70) |
| **Edition** | 2023 |
| **Publisher** | National Fire Protection Association (NFPA) |
| **Jurisdiction** | United States (adopted by most states and local jurisdictions) |
| **Scope** | All electrical installations in the US |
| **Repository** | `rag/us/nec/` — 10 articles |
| **Status in Corpus** | Complete |
| **Legal status** | Adopted as law in most US jurisdictions; enforced by AHJ |

**Purpose:** NEC is the minimum standard for electrical installations. For industrial control systems, it is the legally enforced baseline — NFPA 79 and UL 508A add additional requirements on top.

---

## Key Articles for Industrial Control Systems

| Article | Topic | Relationship |
|---------|-------|-------------|
| **250** | Grounding and bonding | Foundation for all electrical installations |
| **310** | Conductors for general wiring | Wire sizing basis |
| **409** | Industrial control panels | Panel installation; requires UL listing or field evaluation |
| **430** | Motors, motor circuits, and controllers | Motor protection, overcurrent, disconnects |
| **440** | Air-conditioning equipment | HVAC-related motor control |
| **670** | Industrial machinery | References NFPA 79 for electrical design |
| **725** | Class 1, 2, 3 remote-control circuits | Control circuit wiring methods |

---

## Article 409 — Industrial Control Panels

NEC Article 409 is the primary article for industrial control panels:

- Requires listed equipment or field evaluation
- Requires marked SCCR (409.110) — must match available fault current
- Covers installation requirements for the panel enclosure
- Specifies marking requirements

**SCCR requirement:** `409.110` requires the panel to be marked with the SCCR. This is calculated per UL 508A Section SB and must meet or exceed the available fault current at the installation point.

---

## Article 670 — Industrial Machinery

Article 670 covers industrial machinery as a complete unit:

- References NFPA 79 for electrical design requirements of the machine
- Covers supply conductor sizing for the machine feeder
- Addresses disconnecting means for the machine

**Important:** Article 670 makes NFPA 79 the effective electrical design standard for industrial machinery in the US market.

---

## Article 430 — Motors

Critical for motor control panel designs:

- Branch circuit protection sizing (430.52)
- Motor overload protection (430.32)
- Disconnecting means (430.102)
- Multi-motor applications (430.53)
- HVAC / air conditioning motors cross-reference to Article 440

---

## Relationship to Other Standards

```
NEC (legally enforced)
    ├── Article 409  →  requires UL 508A listing for panels
    └── Article 670  →  references NFPA 79 for machine design
                              ↓
                         NFPA 79 applies
```

<a href="{{ '/standards/us-electrical/' | relative_url }}" class="card__link">&larr; US Electrical family overview</a>
