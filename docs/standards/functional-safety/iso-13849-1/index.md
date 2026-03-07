---
layout: default
title: "ISO 13849-1 — Safety of Machinery, Control Systems (PL)"
description: "ISO 13849-1:2023 — Performance Level approach for safety-related control systems in machinery."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Functional Safety"
    url: "/standards/functional-safety/"
  - name: "ISO 13849-1"
repo_path: "control-standards/rag/standards_intelligence/international/functional_safety/iso_13849_1/"
related_standards:
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
  - name: "IEC 62061 (alternative SIL path)"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
lifecycle_stage:
  - name: "Risk Assessment"
    slug: "risk-assessment/"
  - name: "Safety Architecture"
    slug: "safety-architecture/"
  - name: "Commissioning"
    slug: "commissioning/"
---

<div class="page-header">
  <span class="page-header__label">Functional Safety · ISO 13849-1</span>
  <h1>ISO 13849-1:2023 — Safety-Related Parts of Control Systems (PL)</h1>
  <span class="badge badge--complete">Phase 3 Complete</span>
</div>

## Quick Start

- **Get PLr before starting** — obtain the required Performance Level from an ISO 12100 S/F/P risk analysis before selecting any architecture or components
- **Three decisions drive everything:** Category (architecture/fault tolerance), MTTFd (component reliability), and DC (diagnostic coverage) together determine the achieved PL
- **PLd is the most common target** for industrial guarding, E-stop, and light curtain applications — most industrial machinery land here
- **Category 3 + MTTFd High + DC Medium achieves PLd** — this is the standard dual-channel safety relay or safety PLC topology for PLd
- **If complex electronics or software are in the safety path**, consider [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}) (SIL path) as an alternative or complementary approach

---

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | ISO 13849-1 |
| **Edition** | 2023 |
| **Publisher** | International Organization for Standardization (ISO) |
| **Jurisdiction** | Global; harmonized under EU Machinery Directive and Machinery Regulation 2023/1230 |
| **Scope** | Safety-related parts of control systems — PL determination and verification |
| **Repository** | `rag/international/functional_safety/iso_13849_1/` |
| **Status in Corpus** | Phase 3 Complete <span class="badge badge--complete">COMPLETE</span> |

**Purpose:** ISO 13849-1 provides requirements for design and validation of safety-related parts of control systems (SRP/CS). The standard uses Performance Levels (PLa–PLe) to quantify the ability of a safety-related control system to perform a safety function. It covers electromechanical, electronic, and programmable electronic systems, as well as pneumatic and hydraulic safety elements (via ISO 13849-2 for validation methods).

---

## PLr Determination — From ISO 12100 Risk Assessment

PLr (required Performance Level) is determined from the ISO 12100 Annex A risk graph using three parameters: **S** (severity), **F** (frequency/exposure), **P** (possibility of avoidance). Perform this analysis before starting any ISO 13849-1 design work.

| S | F | P | PLr |
|---|---|---|-----|
| S1 (reversible) | F1 (seldom) | P1 (possible) | PLa |
| S1 (reversible) | F1 (seldom) | P2 (scarcely possible) | PLb |
| S1 (reversible) | F2 (frequent) | P1 (possible) | PLb |
| S1 (reversible) | F2 (frequent) | P2 (scarcely possible) | PLc |
| S2 (irreversible) | F1 (seldom) | P1 (possible) | PLc |
| S2 (irreversible) | F1 (seldom) | P2 (scarcely possible) | PLd |
| S2 (irreversible) | F2 (frequent) | P1 (possible) | PLd |
| S2 (irreversible) | F2 (frequent) | P2 (scarcely possible) | PLe |

**Note:** This table represents the ISO 13849-1 Annex A risk graph. The normative source is the graph itself — borderline cases may permit one-step adjustment with documented justification. PLr cannot be assumed or guessed; it must be derived from a documented risk assessment.

---

## PL Levels and PFHd

| PL | PFHd Range | Typical Application |
|----|-----------|---------------------|
| PLa | ≥ 10⁻⁵ /hr to < 10⁻⁴ /hr | Very low risk; auxiliary functions, simple indicators |
| PLb | ≥ 3×10⁻⁶ /hr to < 10⁻⁵ /hr | Low–medium risk; simple single-channel protections |
| PLc | ≥ 10⁻⁶ /hr to < 3×10⁻⁶ /hr | Medium risk; infrequent-access guarding, basic interlocks |
| PLd | ≥ 10⁻⁷ /hr to < 10⁻⁶ /hr | High risk; E-stop, light curtains, guard interlocks on most industrial machinery |
| PLe | < 10⁻⁷ /hr | Highest risk; collaborative robot nearest-person zones, some specialized press guarding |

PLd is the level most industrial machinery designers target. PLe adds significant architecture cost (Category 4) and should be confirmed by risk assessment before committing.

---

## Design Parameters

| Parameter | Definition | Levels / Values | How to Determine |
|-----------|-----------|----------------|-----------------|
| **Category** (B, 1–4) | Architecture type — defines fault tolerance and detection capability | B, 1, 2, 3, 4 | Selected based on PLr and fault tolerance needed (Clause 6) |
| **MTTFd** | Mean Time To Dangerous Failure — per channel reliability | Low (<10 yr), Medium (10–30 yr), High (30–100 yr) | From manufacturer B10d datasheet data; or Annex C/D default tables |
| **DC** | Diagnostic Coverage — fraction of dangerous failures detected | None (<60%), Low (60–90%), Medium (90–99%), High (≥99%) | From diagnostic measures implemented; Annex E reference values |
| **CCF** | Common Cause Failure resistance — scored 0–100 | Must score ≥ 65 for Categories 2, 3, 4 | Annex F scoring: separation, diversity, environment, competence |

**Critical notes:**
- MTTFd is not the same as MTBF. MTTFd counts only dangerous failure modes; MTBF counts all failures.
- CCF is not optional for Categories 2, 3, and 4. A score below 65 invalidates the Category claim.
- DC is a design property, not a component property — it depends on what diagnostic measures are implemented in the system.

---

## Category Architecture

| Category | Architecture | Fault Tolerance | DC Required | Max Achievable PL | Typical Use |
|----------|-------------|-----------------|-------------|-------------------|-------------|
| B | Single channel, basic safety principles | None | None | PLb | Very low risk; auxiliary functions |
| 1 | Single channel, well-tried components | None | None | PLc | Infrequent access, low severity hazards |
| 2 | Single main channel + periodic test function | Detected at next scheduled test | Low–Medium | PLd | Periodic-demand safety functions; lower frequency access |
| 3 | Dual channel with cross-monitoring | Single fault tolerated; detected at or before next demand | Low–High | PLd | Most industrial guarding, E-stop, light curtains — the standard PLd choice |
| 4 | Dual channel, high DC throughout | Single fault detected before or at next demand; accumulation ruled out by design | High (≥99%) | PLe | Highest risk applications; cobot nearest-person safety; specialized press guarding |

For Category 2: test frequency must be ≥ 100× the demand rate. For Categories 3 and 4: both channels must be independent with no shared single-point failure that defeats both channels.

---

## Worked Example: E-Stop for Robot Cell

**Scenario:** Industrial robot cell with operator loading/unloading parts every production cycle.

**Hazard:** Robot arm contact — potential for serious crushing or fracture injury.

**PLr determination (ISO 12100 Annex A):**
- S = S2 — irreversible injury (crush, fracture) if robot arm strikes operator
- F = F2 — operator enters zone every cycle; frequent exposure
- P = P1 — operator can hear the restart warning signal and has a clear sightline to the hazard zone; avoidance is possible under specific conditions

**Result: PLr = PLd** (S2 / F2 / P1 → PLd)

**Architecture to achieve PLd:**

| Design Decision | Selection | Rationale |
|----------------|-----------|-----------|
| Category | 3 (dual-channel) | Fault tolerance required; PLd ceiling at Cat 3 with High MTTFd + Medium DC |
| MTTFd per channel | High (≥30 yr) | Select E-stop device with published B10d data; calculate MTTFd ≥ 30 yr |
| DC | Medium (90–99%) | Cross-monitoring by safety relay detects cross-channel faults |
| Achieved PL | PLd | Category 3 + MTTFd High + DC Medium → PLd (Clause 5 table) |
| CCF | ≥ 65 points | Separate cable routing (15 pts) + diverse input devices (20 pts) + independent supplies + competence records |

**Validation:** FMEA at component level; functional test of E-stop initiation; cross-fault injection test; SISTEMA calculation report retained in Technical File.

---

## PL vs SIL — When To Choose This Standard

| Aspect | ISO 13849-1 (PL) | IEC 62061 (SIL) |
|--------|-----------------|----------------|
| **Metric** | PLa–PLe | SIL 1–SIL 3 |
| **Equivalent levels** | PLd ≈ SIL 2, PLe ≈ SIL 3 | SIL 2 ≈ PLd |
| **Best for** | Mechanical and electromechanical safety devices; most typical industrial machinery | Complex SRECS with programmable logic; safety instrumented systems |
| **Software handling** | Limited — prefers proven components and well-tried designs; complex software needs additional evidence | Full software integrity requirements (SIL-rated development process) |
| **Quantitative basis** | Category + MTTFd + DC combination table | PFHd sum across subsystems |
| **Tools** | SISTEMA (free, published by IFA/TÜV) | SISTEMA or custom spreadsheet calculation |
| **Scope** | Includes mechanical, pneumatic, hydraulic elements (via ISO 13849-2) | Electrical/electronic/programmable only |

Both standards can be used in the same machine: ISO 13849-1 for electromechanical elements (E-stop device, safety relay), IEC 62061 for the programmable safety controller. The PFHd outputs from each are summed to produce the overall safety function PFHd.

See [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}) for the SIL path.

---

## Common Mistakes

1. **Specifying PLd without running ISO 12100 S/F/P analysis** — guessing PLr based on what "sounds right" or what a competitor used. PLr must be derived from a documented risk assessment; an undocumented PLr cannot be defended in a CE audit or after an incident.

2. **Using Category 3 without achieving 65 CCF points** — implementing dual-channel hardware and cross-monitoring relay, then failing to score and document CCF. The dual-channel architecture is not considered valid without the Annex F score. Most common root cause: routing both channel cables in the same duct (loses 15 separation points) and using same-manufacturer devices on both channels (loses 20 diversity points).

3. **Confusing MTTFd with MTBF** — using MTBF from a datasheet or manufacturer's MTBF claim directly in SISTEMA or hand calculations. MTBF counts all failures; MTTFd counts only dangerous failures. A component with high MTBF may still have a low MTTFd if most failures are dangerous.

4. **Ignoring DC — high MTTFd with zero DC only achieves PLb at best** — a single-channel design (Category 1) with very high-reliability components still tops out at PLc; without diagnostics, no amount of component reliability reaches PLd. DC is what separates Category 3/PLd from Category 1/PLc.

5. **Missing that software in the safety path needs additional validation per Clause 7** — if a safety PLC, configurable safety relay, or other programmable device is in the SRP/CS, Clause 7 validation must address the software configuration. The safety PLC itself must be a validated safety device (IEC 61508 SIL-rated); the application program must be validated per the device manufacturer's safety manual.

6. **Not repeating PL verification after design changes** — modifying component types, changing wiring routes, updating firmware versions, or substituting equivalent components without re-running the SISTEMA calculation and CCF score. Any design change that affects the SRP/CS requires re-validation of the affected safety functions.

---

## Practical Checklist

- [ ] ISO 12100 risk assessment completed; PLr documented for each safety function
- [ ] Safety function specification written for each safety function (initiation event, response, PLr, response time)
- [ ] Category selected and justified based on PLr and fault tolerance requirement
- [ ] MTTFd calculated per channel using B10d datasheet data or Annex C/D defaults
- [ ] DC level identified and supported by specific diagnostic measures (Annex E reference)
- [ ] CCF scored using Annex F; score ≥ 65 documented for Categories 2, 3, 4
- [ ] Achieved PL confirmed from Category + MTTFd + DC lookup (Clause 5 table) or SISTEMA calculation
- [ ] Achieved PL ≥ PLr confirmed for every safety function
- [ ] Validation plan established before testing begins
- [ ] FMEA completed at component level; fault injection analysis documented
- [ ] Functional test of each safety function performed and recorded
- [ ] SISTEMA calculation report (or equivalent) included in Technical File
- [ ] Validation report completed and retained in Technical File

---

## Lifecycle Application

| Stage | ISO 13849-1 Activity |
|-------|---------------------|
| **Risk Assessment** | ISO 12100 Annex A analysis outputs PLr for each safety function; Annex A risk graph applied |
| **Safety Function Specification** | Clause 4: specify initiation event, response, PLr, response time for each function |
| **Safety Architecture Design** | Clause 6: select Category (B, 1, 2, 3, or 4) based on PLr and fault tolerance needed |
| **Detailed Design** | Clause 5: select components (MTTFd), implement diagnostics (DC), design CCF measures |
| **PL Verification** | Clause 5 + SISTEMA: confirm achieved PL ≥ PLr; iterate if not |
| **Validation Planning** | Clause 7: establish validation plan before testing; define scope, methods, acceptance criteria |
| **Validation Execution** | Clause 7: FMEA, fault injection analysis, functional testing; CCF score sheet completed |
| **Documentation** | Clause 7: validation report assembled; Technical File prepared for CE marking |
| **Commissioning** | Final validation test on installed machine; confirm response times and reset behavior |
| **Maintenance** | Periodic re-validation per validation plan; re-verification after any design change |

---

## Related Standards

- [ISO 12100]({{ '/standards/functional-safety/iso-12100/' | relative_url }}) — required first step: risk assessment outputs PLr for each safety function
- [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}) — alternative and complementary SIL path for complex programmable safety systems
- [IEC 60204-1]({{ '/standards/machinery/iec-60204-1/' | relative_url }}) — electrical implementation requirements for safety functions on machinery
- ISO 13849-2 — Validation methods: technology-specific annexes for electromechanical, pneumatic, hydraulic, and electronic elements
