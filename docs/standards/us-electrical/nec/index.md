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

> **NEC at a glance:** Art. 409 → control panel SCCR marking. Art. 670 → machine disconnecting means. Art. 430 → motor protection. Art. 250 → grounding and bonding. NEC governs facility installation; NFPA 79 governs machine internal wiring design.

---

## Contents

- [Standard Overview](#standard-overview)
- [Scope and Limitations](#scope-and-limitations)
- [Key Articles](#key-articles-for-industrial-control-systems)
- [Article 409 — Industrial Control Panels](#article-409--industrial-control-panels)
- [Article 670 — Industrial Machinery](#article-670--industrial-machinery)
- [Article 430 — Motors](#article-430--motors)
- [2026 NEC Changes](#2026-nec--key-changes-for-control-engineers)
- [Relationship to Other Standards](#relationship-to-other-standards)
- [Typical Machine Builder Workflow](#typical-machine-builder-workflow)
- [Machine Builder Compliance Checklist](#machine-builder-compliance-checklist)

---

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | NEC (NFPA 70) |
| **Edition** | 2023 |
| **Publisher** | National Fire Protection Association (NFPA) |
| **Jurisdiction** | United States (adopted by most states and local jurisdictions) |
| **Scope** | All electrical installations in the US |
| **Repository** | `rag/us/nec/` — 19 articles |
| **Status in Corpus** | Complete |
| **Legal status** | Adopted as law in most US jurisdictions; enforced by AHJ |

**Purpose:** NEC is the minimum standard for electrical installations. For industrial control systems, it is the legally enforced baseline — NFPA 79 and UL 508A add additional requirements on top.

> **Edition adoption caveat:** The NEC is published every three years, but each state or municipality adopts a specific edition independently. Always verify the applicable NEC edition with the **local Authority Having Jurisdiction (AHJ)** before beginning design work — especially on multi-state or retrofit projects.

---

## Scope and Limitations

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

**NEC does not determine:**
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
| **725** | Class 2 and 3 remote-control circuits | Low-energy control and signaling wiring (Class 1 moved to Art. 206 in 2026 NEC) |

---

## Article 409 — Industrial Control Panels

NEC Article 409 governs **industrial control panels installed in facilities**.

Key requirements include:

- Panels must be properly marked
- The **Short-Circuit Current Rating (SCCR)** must be determined and displayed **(409.110)**
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

- Branch circuit protection sizing **(430.52)**
- Motor overload protection **(430.32)**
- Disconnecting means **(430.102)**
- Multi-motor applications **(430.53)**
- HVAC / air conditioning motors cross-reference to Article 440

---

## 2026 NEC — Key Changes for Control Engineers

<details>
<summary><strong>Expand — 2026 NEC changes (most jurisdictions are still on 2020 or 2023)</strong></summary>

> **Adoption status:** The 2026 NEC was published in 2025. Most jurisdictions are still enforcing the 2020 or 2023 edition. Confirm the adopted edition with the local AHJ before applying these changes to a live project.

The 2026 edition restructures how control and signaling circuits are classified — directly affecting control panel design:

### Art. 206 (New) — Non-Power-Limited Remote Control and Signaling Circuits

**Article 206 is new in the 2026 NEC.** It covers line-voltage remote control, signaling, and power-limited circuits that do not originate from a Class 2 or Class 3 power source. In practical terms: line-voltage control wiring inside a panel that is not a branch circuit and is not powered by a Class 2/3 source now belongs in **Article 206**, not Article 725.

This is significant for control panel designers:
- Motor control circuits fed from a control transformer at 120 V AC → **Article 206**
- PLC I/O wiring at 24 VDC from a Class 2 power supply → **Article 725**
- Safety relay input circuits at 24 VDC from a dedicated safety power supply → confirm power supply classification

### Art. 725 (Changed) — Now Class 2 and Class 3 Only

In the 2026 NEC, **Class 1 circuits are removed from Article 725**. Article 725 now exclusively covers Class 2 and Class 3 circuits — the low-energy, limited-power wiring used for sensors, communication, and instrumentation. Class 1 line-voltage control wiring moves to the new Article 206.

If you currently cite Article 725 for line-voltage motor control circuits, that reference is incorrect under the 2026 NEC.

### Art. 120 (Relocated) — Load Calculations

Load calculations for branch circuits, feeders, and services have moved from Article 220 to **Article 120**. The rules are the same; only the article number changed. If your design documents reference Article 220 for load calculations, they will still be correct under 2023 NEC but should be updated to Article 120 for 2026 compliance.

### Art. 130 (Relocated) — Energy Management Systems

Energy management system requirements moved from Article 750 to **Article 130**. Relevant for installations with demand-response controls or building energy management integrated with industrial power distribution.

</details>

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

**Phase 1 — Safety Design**

1. Perform machine **risk assessment** (ISO 12100)
2. Determine required **PL or SIL** level (ISO 13849-1 / IEC 62061)
3. Design the **safety architecture**

**Phase 2 — Electrical Design and Construction**

4. Design machine electrical system (**NFPA 79**)
5. Build control panel (**UL 508A**)
6. Verify **SCCR** against available fault current (UL 508A SB)

**Phase 3 — Installation and Compliance**

7. Install equipment per **NEC** requirements
8. Pass **AHJ inspection**

---

## Machine Builder Compliance Checklist

Before installing a machine in a facility, verify the following:

- [ ] Determine available fault current at the installation point
- [ ] Verify panel SCCR meets or exceeds available fault current **(Art. 409.110)**
- [ ] Feeder and branch circuit conductors properly sized **(Art. 310, 430)**
- [ ] Motor branch circuit short-circuit and ground-fault protection verified **(Art. 430.52)**
- [ ] Motor overload protection verified **(Art. 430.32)**
- [ ] Machine disconnecting means location and sizing verified **(Art. 670)**
- [ ] Equipment grounding and bonding verified **(Art. 250)**
- [ ] Surge and overvoltage protection evaluated where safety circuits are present **(Art. 409.70, 670.6)**

---

<a href="{{ '/standards/us-electrical/' | relative_url }}" class="card__link">&larr; US Electrical family overview</a>
