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

The National Electrical Code (NEC), published as **NFPA 70**, is the primary electrical installation code used in the United States. It defines minimum safety requirements for **installation of electrical systems and equipment** in buildings and industrial facilities.

The NEC governs **how electrical equipment is installed** — not how industrial machines are designed internally. For machine electrical design, see **NFPA 79**. For control panel construction, see **UL 508A**. NEC is the legally enforced installation baseline; those standards add requirements on top.

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
| **240** | Overcurrent protection | Circuit breaker and fuse sizing rules for feeders and branch circuits |
| **250** | Grounding and bonding | Foundation for all electrical installations; protective grounding for equipment and panels |
| **300** | Wiring methods | Installation rules for cables, conduits, and raceways |
| **310** | Conductors for general wiring | Conductor sizing and insulation ratings |
| **409** | Industrial control panels | Panel installation; SCCR marking requirement (409.110) |
| **409.70** | Surge protection | Surge protective devices (SPDs) for control panels with electronic or safety components (NEC 2023) |
| **430** | Motors, motor circuits, and controllers | Motor protection, overcurrent, disconnects |
| **440** | Air-conditioning equipment | HVAC-related motor control |
| **670** | Industrial machinery | Connection of machines to facility electrical systems; disconnecting means and supply circuit requirements |
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

**The critical rule:** The control panel SCCR must be **greater than or equal to the available fault current at the installation point**. A panel installed where available fault current exceeds its marked SCCR is a code violation and a safety hazard.

**On SCCR determination:** NEC Article 409 requires SCCR to be established by an approved method. Common approaches include:

- **UL 508A Supplement SB calculation** — the most common method for industrial control panels
- **Fully rated components** — all devices individually rated for the available fault current
- **Current-limiting devices** — upstream fuses or breakers that reduce let-through current
- **Tested/listed assemblies** — factory-tested panels with a marked SCCR

A listed/labeled assembly satisfies this requirement; a field-evaluated panel may use other approved methods. UL 508A listing is one approved path — not the only one.

**On 409.70 — Surge Protection (NEC 2023):** Where industrial control panels contain electronic components or safety circuits sensitive to transient voltage events, surge protective devices (SPDs) may be required. This is particularly relevant where safety relay modules, PLCs, or safety controllers are housed in the panel.

---

## Article 670 — Industrial Machinery

Article 670 governs how industrial machinery is **connected to facility electrical systems** — including supply circuits, disconnecting means, and installation considerations. It does **not** define the machine's internal electrical design; that is the role of **NFPA 79**.

It primarily addresses:
- Machine disconnecting means (location and sizing)
- Supply circuit requirements and feeder sizing
- Overcurrent protection at the machine supply

**NEC / NFPA 79 boundary:**
- **NEC Art. 670** — how the machine connects to the facility electrical system
- **NFPA 79** — how the machine's internal electrical system is designed and built

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

> **Adoption status:** The 2026 NEC is a finalized edition, published in 2025. Most jurisdictions are still enforcing the 2020 or 2023 edition. Always confirm the adopted edition with the **local AHJ** before applying 2026 references to a live project.

**What changed at a glance:**

| Article | Change type | Topic | Impact |
|---------|-------------|-------|--------|
| **206** | New | Non-power-limited control circuits | High — line-voltage control wiring reclassified |
| **725** | Narrowed | Now Class 2 / Class 3 only | High — Class 1 citations in existing docs become incorrect |
| **120** | Relocated | Load calculations (was Art. 220) | Low — rules unchanged, article number only |
| **130** | Relocated | Energy management (was Art. 750) | Low — relevant for demand-response installations only |

---

### Art. 206 (New) — Non-Power-Limited Control and Signaling Circuits

**Impact:** High &nbsp;|&nbsp; **Affects:** Panel designers, anyone citing Art. 725 for line-voltage control wiring

**What changed**
- Art. 206 is entirely new in the 2026 NEC
- It covers line-voltage control wiring that is not a branch circuit and does not originate from a Class 2 or Class 3 power source
- This wiring previously had no dedicated article and was often (incorrectly) cited under Art. 725

**Why it matters**
- Motor control circuits at 120 V AC from a control transformer → now **Art. 206**
- PLC I/O at 24 VDC from a listed Class 2 supply → remains **Art. 725**
- Safety relay inputs at 24 VDC → depends on power supply classification; verify

**Engineer takeaway**
> Audit any design document or wiring diagram that cites Art. 725 for line-voltage control circuits — reclassify to Art. 206 for 2026 compliance.

---

### Art. 725 (Changed) — Now Class 2 and Class 3 Only

**Impact:** High &nbsp;|&nbsp; **Affects:** Engineers with existing panel drawings or specs citing Art. 725 for motor control wiring

**What changed**
- Class 1 circuits removed from Art. 725
- Art. 725 now covers only Class 2 and Class 3 low-energy circuits
- Class 1 line-voltage control wiring moves to new Art. 206

**Why it matters**
- Citing Art. 725 for line-voltage motor control circuits is **incorrect under the 2026 NEC**
- 24 VDC sensor and PLC I/O wiring from a Class 2 supply is unaffected — it stays in Art. 725

**Engineer takeaway**
> If you cite Art. 725 for anything other than low-energy Class 2 / Class 3 wiring, that reference needs to be updated to Art. 206.

---

### Art. 120 (Relocated) — Load Calculations

**Impact:** Low &nbsp;|&nbsp; **Affects:** Electrical designers writing load calculation reports

**What changed**
- Load calculations for branch circuits, feeders, and services moved from **Art. 220 → Art. 120**
- Rules are identical; only the article number changed

**Why it matters**
- Design documents referencing Art. 220 are still correct under 2023 NEC
- Documents targeting 2026 compliance should be updated to reference Art. 120

**Engineer takeaway**
> No design rule changes — update article number references in any 2026-targeted document.

---

### Art. 130 (Relocated) — Energy Management Systems

**Impact:** Low &nbsp;|&nbsp; **Affects:** Facilities with demand-response or building energy management integrated with industrial power distribution

**What changed**
- Energy management system requirements moved from **Art. 750 → Art. 130**
- Rules are unchanged

**Why it matters**
- Niche scope: relevant only where energy management systems connect to industrial distribution
- Existing Art. 750 references should be updated in 2026-targeted documents

**Engineer takeaway**
> Only relevant if energy management systems are in your project scope — update Art. 750 references to Art. 130.

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
| **ISO 13849-1 / IEC 62061** | Functional safety of control systems (PL and SIL) |
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
- [ ] Feeder overcurrent protection properly sized **(Art. 240)**
- [ ] Feeder and branch circuit conductors properly sized **(Art. 310, 430)**
- [ ] Wiring methods (conduit, cable tray, supports) comply with installation rules **(Art. 300)**
- [ ] Motor branch circuit short-circuit and ground-fault protection verified **(Art. 430.52)**
- [ ] Motor overload protection verified **(Art. 430.32)**
- [ ] Machine disconnecting means location and sizing verified **(Art. 670)**
- [ ] Equipment grounding and bonding verified **(Art. 250)**
- [ ] Surge and overvoltage protection evaluated where safety circuits are present **(Art. 409.70, 670.6)**

---

<details>
<summary><strong>Standard metadata</strong></summary>

| Field | Value |
|-------|-------|
| **Standard** | NFPA 70 |
| **Common name** | National Electrical Code (NEC) |
| **Latest edition** | 2023 |
| **Published by** | National Fire Protection Association (NFPA) |
| **Enforced by** | Authority Having Jurisdiction (AHJ) |
| **Update cycle** | Every 3 years |
| **Scope** | Electrical installation safety in the United States |

</details>

---

<a href="{{ '/standards/us-electrical/' | relative_url }}" class="card__link">&larr; US Electrical family overview</a>
