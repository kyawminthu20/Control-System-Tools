---
layout: default
title: "IEC 60204-1 — Electrical Equipment of Machines"
description: "IEC 60204-1:2016+AMD1:2021 — scope, key clauses, lifecycle stage, and relationship to NFPA 79."
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
review:
  standard: "IEC 60204-1"
  edition: "IEC 60204-1:2016 (Ed. 6.0) + AMD1:2021 — consolidated CSV Ed. 6.1"
  status: "Review pending"
  coverage: "Clause-level summary of the 18 clauses; per-clause depth pass pending. Edition, scope voltages, clause structure and emergency-stop categories corrected July 2026"
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">International Machinery · IEC 60204-1</span>
  <h1>IEC 60204-1:2016+AMD1:2021 — Electrical Equipment of Machines</h1>
</div>

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | IEC 60204-1 |
| **Edition** | IEC 60204-1:2016 (Ed. 6.0) + AMD1:2021 — consolidated as CSV Ed. 6.1, 2021-09-15 |
| **Publisher** | International Electrotechnical Commission (IEC) |
| **Jurisdiction** | Global; harmonized in EU under Machinery Directive |
| **Scope** | Electrical and electronic equipment on industrial machines |
| **Repository** | `rag/international/machinery/iec_60204_1/` |
**Purpose:** IEC 60204-1 applies to the electrical, electronic and programmable electronic
equipment and systems of machines not portable by hand while working. Its requirements begin
at the point of connection of the supply to the electrical equipment of the machine.

**Scope limits (official Clause 1):** the standard applies to electrical equipment operating
with nominal supply voltages **not exceeding 1 000 V AC or 1 500 V DC**, and nominal supply
frequencies **not exceeding 200 Hz**.

> **There is no lower voltage threshold in the scope.** An earlier version of this page stated
> that IEC 60204-1 "applies to circuits above 25 V AC or 60 V DC". That is incorrect and has
> been removed — no such lower bound exists in Clause 1. (The 25 V AC / 60 V DC figures belong
> to PELV/extra-low-voltage requirements inside Clause 6, which is a different question from
> the standard's scope.)

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

IEC 60204-1:2016+AMD1:2021 has **18 clauses**. Clauses 1–3 are scope, normative references,
and terms; the technical requirements run from Clause 4 to Clause 18.

| Clause | Topic | NFPA 79 Crosswalk |
|--------|-------|------------------|
| 4 | General requirements | Ch 4 |
| 5 | Incoming supply conductor terminations and devices for disconnecting and switching off | Ch 5 |
| 6 | Protection against electric shock | Ch 7 |
| 7 | Protection of equipment | Ch 6 |
| 8 | Equipotential bonding | Ch 8 |
| 9 | Control circuits and control functions | Ch 9 |
| 10 | Operator interface and machine-mounted control devices | Ch 10 |
| 11 | Controlgear: location, mounting, and enclosures | Ch 11 |
| 12 | Conductors and cables | Ch 12 |
| 13 | Wiring practices | Ch 13 |
| 14 | Electric motors and associated equipment | Ch 14 |
| 15 | Socket-outlets and lighting | Ch 15 |
| 16 | Marking, warning signs and reference designations | Ch 16 |
| 17 | Technical documentation | Ch 19 |
| 18 | Verification | — |

> **Corrected July 2026.** An earlier version of this page claimed "all 15 clauses" while
> listing a table that ran 4–17, duplicated technical documentation, and omitted **Clause 18
> (Verification)** entirely. The reference library behind it had the same defect — it was
> drafted against the superseded **2005** edition (its Clause 15 was titled "Accessories and
> lighting", the Ed. 5.0 title) and skipped Clauses 12 and 13 altogether. The clause structure
> above is taken from the official IEC 60204-1:2016+AMD1:2021 contents, and the corpus has been
> renumbered to match. Clauses 12, 13 and 17 now exist but carry only principles — a depth pass
> is still pending.

---

## Stop Functions and Emergency Stop (Clause 9)

**Stop categories are not all emergency-stop categories.** IEC 60204-1 Clause 9 defines three
stop categories for machine stop functions:

| Stop category | Behaviour | Valid for emergency stop? |
|---|---|---|
| **Category 0** | Immediate removal of power to the machine actuators (uncontrolled stop) | **Yes** |
| **Category 1** | Controlled stop with power available to the actuators to achieve the stop, then power removed once stopped | **Yes** |
| **Category 2** | Controlled stop with power **left available** to the machine actuators | **No** |

An **emergency-stop function shall be either a Category 0 or a Category 1 stop**, selected on
the basis of the machine risk assessment. **Category 2 is not an emergency-stop category** —
it leaves power on the actuators, which is incompatible with the purpose of an emergency stop.
General (non-emergency) stop functions may be Category 0, 1 or 2.
<span class="badge badge--verify">confirm against the published Clause 9.2 text</span>

> **Sourcing note.** The correction above (removing Category 2 from the emergency-stop
> options) is the conservative reading and is consistent with ISO 13850, but the body of
> Clause 9 is behind the IEC paywall — the free official preview truncates before it. It has
> **not** been confirmed word-for-word against the published text. Confirm against the
> purchased standard before relying on it for a design decision.
>
> Note also that the emergency-stop material sits under **9.2.2 / 9.2.3** and **10.7** in the
> 2016 edition. Any document citing "9.2.5.4.2" is citing the superseded **2005** edition.

For formal safety function design, this clause works with:

- [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) — Performance Level (PL) approach
- [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}) — SIL approach for machinery
- ISO 13850 — Emergency stop devices (referenced by both)

---

## Global Machine Projects

For machines sold in both US and EU markets, use **both** IEC 60204-1 and NFPA 79 and design to the most restrictive requirement from each.

Key differences to watch for:
- **Wire colors**: IEC 60204-1 requires yellow-green for PE; NFPA 79 allows green or bare
- **Voltage rating**: both are now 1000 V — IEC 60204-1 covers to 1000 V AC / 1500 V DC; NFPA 79's current scope is 1000 V or less (its older 600 V ceiling is out of date)
- **Neutral conductor** requirements differ in detail

<a href="{{ '/tools/crosswalks/nfpa79-iec60204/' | relative_url }}" class="card__link">View NFPA 79 ↔ IEC 60204-1 full crosswalk &rarr;</a>
