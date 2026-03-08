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

> **Edition adoption caveat:** The NEC is published every three years, but each state or municipality adopts a specific edition independently. Always verify the applicable NEC edition with the **local Authority Having Jurisdiction (AHJ)** before beginning design work — especially on multi-state or retrofit projects.

---

## Use This Page For

**Use NEC for:**
- Feeder sizing and branch circuit protection
- Grounding and bonding requirements
- Disconnecting means location and sizing
- Electrical installation rules for the facility
- Wiring methods (conduit, cable tray, etc.)
- Verifying panel SCCR against available fault current

**Do not use NEC alone for:**
- Machine internal wiring details — use **NFPA 79**
- Panel construction method and component ratings — use **UL 508A**
- Functional safety validation (SIL, PL) — use **ISO 13849-1** or **IEC 62061**
- Risk reduction architecture — use **ISO 12100**

---

## What the NEC Does Not Cover

The NEC does **not** determine:

- Performance Level (PL) or Safety Integrity Level (SIL) targets
- Safety controller architecture or category selection
- Stop category selection
- Guarding strategy
- Machine risk assessment method

These are handled by ISO 12100, ISO 13849-1, IEC 62061, and related functional safety standards.

---

## Key Articles for Industrial Control Systems

| Article | Topic | Relevance |
|---------|-------|-----------|
| **250** | Grounding and bonding | Foundation for all electrical installations; protective grounding for equipment and panels |
| **300** | Wiring methods | Installation rules for cables, conduits, and raceways |
| **310** | Conductors for general wiring | Conductor sizing and insulation ratings |
| **409** | Industrial control panels | Panel installation; SCCR marking requirement (409.110) |
| **409.70** | Surge protection | Surge protection requirements for industrial control panels (NEC 2023) |
| **430** | Motors, motor circuits, and controllers | Motor protection, overcurrent, disconnects |
| **440** | Air-conditioning equipment | HVAC-related motor control |
| **670** | Industrial machinery | Installation requirements for machines; references NFPA 79 for machine electrical design |
| **670.6** | Overvoltage protection | Overvoltage protection for industrial machinery supply circuits |
| **725** | Class 1, 2, 3 remote-control circuits | Control and signaling circuit wiring methods |

---

## Article 409 — Industrial Control Panels

NEC Article 409 governs **industrial control panels installed in facilities**.

Key requirements include:

- Panels must be properly marked
- The **Short-Circuit Current Rating (SCCR)** must be determined and displayed (409.110)
- The panel must be installed within its marked SCCR
- The marked SCCR must meet or exceed the available fault current at the installation point

**On SCCR determination:** NEC Article 409 requires SCCR to be established by an approved method. UL 508A Supplement SB is a commonly used approved method for determining SCCR. A listed/labeled assembly satisfies this requirement; a field-evaluated panel may use other approved methods. Avoid stating that UL 508A listing is the only path — it is one approved method among others.

**On 409.70 — Surge Protection (NEC 2023):** Where industrial control panels contain electronic components or safety circuits sensitive to transient voltage events, surge protective devices (SPDs) may be required. This is particularly relevant where safety relay modules, PLCs, or safety controllers are housed in the panel.

---

## Article 670 — Industrial Machinery

Article 670 applies to **industrial machines installed in facilities**.

It primarily addresses:
- Machine disconnecting means
- Supply circuit requirements and feeder sizing
- Overcurrent protection at the machine supply

**NEC / NFPA 79 relationship:** For industrial machinery, NEC Article 670 points engineers toward **NFPA 79** for many machine electrical design details, while NEC remains the enforceable installation code.

In practice:
- **NEC governs how electrical systems are installed in the facility**
- **NFPA 79 governs machine electrical design**

**On 670.6 — Overvoltage Protection:** Industrial machinery supply circuits may require overvoltage protection per 670.6, particularly where safety system components are sensitive to supply voltage transients.

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

NEC is the **enforceable installation code**. It works in combination with design and construction standards:

| Standard | Scope |
|----------|-------|
| **NEC (NFPA 70)** | Electrical installation — enforced by AHJ |
| **NFPA 79** | Machine electrical design |
| **UL 508A** | Industrial control panel construction |
| **ISO 12100** | Machine risk assessment |
| **ISO 13849-1** | Safety control system Performance Levels |
| **IEC 60204-1** | Electrical equipment of machinery (international) |

> **NEC is the enforceable installation code.**
> **Article 409** governs industrial control panel installation and marking, including SCCR marking.
> **Article 670** applies to industrial machinery as installed equipment and points to NFPA 79 for many machine electrical design details.
> **UL 508A** is commonly used to construct and evaluate panels, including SCCR determination by approved method.
> Functional safety requirements such as PL/SIL are handled separately through standards such as **ISO 13849-1** and **IEC 62061**.

---

## Typical Machine Builder Workflow

When designing a machine for the US market:

1. Perform machine **risk assessment** (ISO 12100)
2. Determine required **PL or SIL** level (ISO 13849-1 / IEC 62061)
3. Design the **safety architecture**
4. Design machine electrical system (**NFPA 79**)
5. Build control panel (**UL 508A**)
6. Verify **SCCR** against available fault current (UL 508A SB)
7. Install equipment per **NEC** requirements
8. Pass **AHJ inspection**

---

## Machine Builder Compliance Checklist

Before installing a machine in a facility, verify the following:

- [ ] Determine available fault current at the installation point
- [ ] Verify panel SCCR meets or exceeds available fault current (409.110)
- [ ] Feeder and branch circuit conductors properly sized (Articles 310, 430)
- [ ] Motor branch circuit short-circuit and ground-fault protection verified (430.52)
- [ ] Motor overload protection verified (430.32)
- [ ] Machine disconnecting means location and sizing verified (Article 670)
- [ ] Equipment grounding and bonding verified (Article 250)
- [ ] Surge and overvoltage protection evaluated where safety circuits are present (409.70, 670.6)

---

<a href="{{ '/standards/us-electrical/' | relative_url }}" class="card__link">&larr; US Electrical family overview</a>
