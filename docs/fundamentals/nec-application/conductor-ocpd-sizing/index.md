---
layout: training-module
title: "Conductor and OCPD Sizing Worked Examples"
description: "Step-by-step NEC sizing calculations for motor branch circuits and feeders, with worked examples for 10 HP and 25 HP motors and a quick-reference table."
breadcrumb:
  - name: "Training"
    url: "/fundamentals/"
  - name: "NEC for Machines and Panels"
    url: "/fundamentals/nec-application/"
repo_path: "control-standards/rag/training_modules/nec_application/conductor_ocpd_sizing_examples.md"
related_standards:
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
redirect_from:
  - /training/nec-application/conductor-ocpd-sizing/
review:
  standard: "NEC (NFPA 70) — article scope per the module"
  edition: "taught against the NEC 2023 corpus basis; the locally enforceable edition governs — verify with the AHJ"
  status: "Review pending"
  coverage: "Training module: Conductor and OCPD Sizing Worked Examples — worked as education, not a code determination; the AHJ and enforceable edition govern."
  last_reviewed: "July 2026"
---

## Purpose

This module walks through complete sizing calculations for motor branch-circuit conductors and overcurrent protective devices (OCPDs), starting from the correct NEC table and finishing with equipment grounding conductor (EGC) selection. Two worked examples — 10 HP and 25 HP motors — illustrate the full sequence.

---

## Key tables used in motor sizing

Four NEC tables drive most branch-circuit sizing decisions.

| Table | What it gives you | When you use it |
|---|---|---|
| 430.250 | Full-load current (FLC) for three-phase AC motors | Always the starting point — use the table value, not the nameplate |
| 310.15(B)(16) | Conductor ampacity for 60 °C and 75 °C terminations in free air or conduit | Conductor sizing after applying the 125 % multiplier |
| 430.52 | Maximum rating or setting of branch-circuit SCPD by type and motor type | OCPD selection — inverse-time breaker (ITB), dual-element fuse, etc. |
| 250.122 | Equipment grounding conductor sizing based on upstream OCPD rating | EGC sizing — always based on OCPD ampere rating, not load current |

> **Rule from Art 430.6(A):** Use Table 430.250 to find FLC for sizing conductors, overloads, and OCPDs. Do not use the nameplate full-load ampere (FLA) rating for these calculations.

---

## Worked example 1 — 10 HP, 480 V, three-phase motor

### Given

- Motor: 10 HP, 480 V, three-phase, squirrel-cage induction
- Service factor: 1.15 (nameplate)
- Wiring method: THHN copper in conduit, 75 °C terminations
- OCPD type: inverse-time circuit breaker (ITB)

### Step 1 — Find table FLC (Art 430.6 + Table 430.250)

Table 430.250 for a 10 HP, 460 V motor gives **FLC = 14 A**.

*(The table column is 460 V; the 480 V system voltage does not change the table value.)*

### Step 2 — Size the branch-circuit conductor (Art 430.22)

Minimum conductor ampacity = 125 % × FLC = 1.25 × 14 = **17.5 A**

From Table 310.15(B)(16), 12 AWG Cu at 75 °C = 20 A ampacity.

**Select 12 AWG THHN copper.**

### Step 3 — Size the overload relay (Art 430.32)

For a motor with a service factor ≥ 1.15 or temperature rise ≤ 40 °C:

Maximum overload setting = 125 % × FLC = 1.25 × 14 = **17.5 A**

Set the overload relay at or below 17.5 A. If that setting causes nuisance tripping, Art 430.32(C) allows up to 140 % for motors with a service factor ≥ 1.15 (1.40 × 14 = 19.6 A maximum).

### Step 4 — Size the branch-circuit SCPD (Art 430.52 + Table 430.52)

Table 430.52, inverse-time circuit breaker, squirrel-cage motor: **250 % maximum**.

Maximum ITB rating = 2.50 × 14 = 35 A

Standard breaker sizes per Art 240.6: 30, 35, 40 …

**Select a 35 A inverse-time circuit breaker.**

(A 30 A breaker is also acceptable and is the next size down. The table gives the maximum, not the required size.)

### Step 5 — Size the equipment grounding conductor (Art 250.122 + Table 250.122)

EGC is sized from the upstream OCPD rating, which is 35 A.

Table 250.122: OCPD up to 60 A → **10 AWG copper EGC**.

### Summary — 10 HP motor

| Item | Calculation | Result |
|---|---|---|
| Table FLC | Table 430.250 | 14 A |
| Branch conductor | 125 % × 14 A → 17.5 A min | 12 AWG Cu THHN |
| Overload setting | 125 % × 14 A | ≤ 17.5 A |
| ITB breaker (max) | 250 % × 14 A | 35 A |
| EGC | Table 250.122, 35 A OCPD | 10 AWG Cu |

---

## Worked example 2 — 25 HP, 460 V, three-phase motor

### Given

- Motor: 25 HP, 460 V, three-phase, squirrel-cage induction
- Service factor: 1.0 (nameplate)
- Wiring method: THHN copper in conduit, 75 °C terminations
- OCPD type: inverse-time circuit breaker (ITB)

### Step 1 — Find table FLC (Table 430.250)

Table 430.250 for a 25 HP, 460 V motor: **FLC = 34 A**

### Step 2 — Size the branch-circuit conductor (Art 430.22)

Minimum ampacity = 125 % × 34 = **42.5 A**

Table 310.15(B)(16): 8 AWG Cu at 75 °C = 50 A ampacity.

**Select 8 AWG THHN copper.**

### Step 3 — Size the overload relay (Art 430.32)

Service factor = 1.0 (not ≥ 1.15), so maximum overload = 115 % × FLC:

115 % × 34 = **39.1 A**

Set overload relay at or below 39.1 A. If nuisance tripping occurs, Art 430.32(C) permits up to 130 % for service factor < 1.15 (1.30 × 34 = 44.2 A absolute maximum).

### Step 4 — Size the branch-circuit SCPD (Art 430.52)

Table 430.52, ITB, squirrel-cage: 250 % maximum.

Maximum ITB = 2.50 × 34 = 85 A → next standard size = **90 A ITB**

**If the motor will not start reliably at 90 A**, Art 430.52 Exception No. 2 permits increasing the ITB to the next standard size that allows starting, up to a maximum of **400 %** for ITB breakers (4.00 × 34 = 136 A → 150 A is the next standard size).

Maximum permitted ITB under the exception: **150 A** (400 % of 34 A = 136 A, so 150 A is the first standard size that exceeds that — verify local AHJ interpretation, some cap at exactly 400 %).

### Step 5 — Size the EGC (Table 250.122)

OCPD = 90 A (normal case). Table 250.122: OCPD up to 100 A → **8 AWG copper EGC**.

If the exception is applied and a 150 A breaker is used: Table 250.122, OCPD up to 200 A → **6 AWG copper EGC**.

### Summary — 25 HP motor

| Item | Calculation | Result |
|---|---|---|
| Table FLC | Table 430.250 | 34 A |
| Branch conductor | 125 % × 34 A → 42.5 A min | 8 AWG Cu THHN |
| Overload setting (SF=1.0) | 115 % × 34 A | ≤ 39.1 A |
| ITB breaker (normal max) | 250 % × 34 A | 90 A |
| ITB breaker (won't-start exception) | up to 400 % × 34 A | 150 A max |
| EGC (90 A OCPD) | Table 250.122 | 8 AWG Cu |

---

## Feeder sizing for multiple motors (Art 430.24)

When one feeder supplies two or more motors, Art 430.24 sets the minimum feeder conductor ampacity as:

> **125 % of the largest motor FLC + 100 % of all other motor FLCs**

### Example — feeder for three motors

| Motor | HP | FLC (Table 430.250) | Factor |
|---|---|---|---|
| Motor A | 25 HP, 460 V | 34 A | 125 % (largest) |
| Motor B | 10 HP, 460 V | 14 A | 100 % |
| Motor C | 5 HP, 460 V | 7.6 A | 100 % |

Minimum feeder ampacity = (1.25 × 34) + (1.00 × 14) + (1.00 × 7.6) = 42.5 + 14 + 7.6 = **64.1 A**

Table 310.15(B)(16): next conductor above 64.1 A at 75 °C = **4 AWG Cu THHN** (85 A ampacity).

Feeder OCPD is sized based on the largest motor OCPD + other motor FLCs (Art 430.62). Feeder OCPD ≤ largest branch-circuit OCPD + sum of other FLCs = 90 + 14 + 7.6 = 111.6 A → select **110 A** (or the next standard size at or below 111.6 A, which is 110 A).

---

## Quick-reference sizing table — common HP at 460/480 V

This table shows common values for squirrel-cage, three-phase motors using THHN copper conductors in conduit at 75 °C, ITB breakers, and copper EGC. Verify against current code edition for your project.

| HP | FLC (A) | Min conductor ampacity (A) | Conductor AWG | Max ITB (A) | EGC AWG (at max ITB) |
|---|---|---|---|---|---|
| 1 | 2.1 | 2.6 | 14 AWG | 15 | 14 AWG |
| 1.5 | 3.0 | 3.8 | 14 AWG | 15 | 14 AWG |
| 2 | 3.4 | 4.3 | 14 AWG | 15 | 14 AWG |
| 3 | 4.8 | 6.0 | 14 AWG | 15 | 14 AWG |
| 5 | 7.6 | 9.5 | 14 AWG | 20 | 12 AWG |
| 7.5 | 11 | 13.8 | 14 AWG | 30 | 10 AWG |
| 10 | 14 | 17.5 | 12 AWG | 35 | 10 AWG |
| 15 | 21 | 26.3 | 10 AWG | 60 | 10 AWG |
| 20 | 27 | 33.8 | 8 AWG | 70 | 8 AWG |
| 25 | 34 | 42.5 | 8 AWG | 90 | 8 AWG |
| 30 | 40 | 50.0 | 8 AWG | 100 | 8 AWG |
| 40 | 52 | 65.0 | 4 AWG | 150 | 6 AWG |
| 50 | 65 | 81.3 | 3 AWG | 175 | 6 AWG |

> Conductor AWG based on 75 °C Cu ampacity from Table 310.15(B)(16). EGC AWG from Table 250.122 at the maximum ITB rating shown. Derating for conduit fill or ambient temperature not applied — recalculate when those factors apply.

---

## Common mistakes

| Mistake | Consequence | Correct approach |
|---|---|---|
| Using nameplate FLA instead of Table 430.250 | Under- or over-sized conductors and OCPDs | Always use Art 430.6 + Table 430.250 for sizing |
| Sizing EGC from load current instead of OCPD rating | Undersized EGC — fault path fails to clear | Size EGC from Table 250.122 using the OCPD ampere rating |
| Applying 125 % multiplier to overload as well as conductor | Overload set too high — motor thermal damage | Overload multiplier is 115 % or 125 % per Art 430.32, not always 125 % |
| Selecting standard breaker size below 250 % without checking start capability | Motor fails to start, nuisance tripping | Start with 250 % maximum, then invoke the won't-start exception if needed |
| Omitting feeder OCPD coordination per Art 430.62 | Feeder OCPD trips before branch OCPD on motor fault | Feeder OCPD ≤ largest branch OCPD + other FLCs |

---

## Practical takeaway

Motor branch-circuit sizing follows a fixed five-step sequence: (1) look up table FLC from Art 430.250, (2) apply 125 % for the conductor, (3) apply 115 % or 125 % for the overload relay, (4) apply Table 430.52 for the OCPD, and (5) size the EGC from Table 250.122 based on the OCPD.

The single most common error is substituting the nameplate FLA for the code table FLC. Art 430.6(A) prohibits that substitution for the purposes of conductor, overload, and OCPD sizing.

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/nec-application/sccr-workflow/' | relative_url }}">&larr; SCCR Workflow</a>
  <a href="{{ '/fundamentals/nec-application/' | relative_url }}">↑ NEC for Machines and Panels</a>
  <a href="{{ '/fundamentals/nec-application/class1-class2-circuits/' | relative_url }}">Class 1, Class 2, and Remote-Control Circuits &rarr;</a>
</div>
