---
layout: training-module
title: "Practical Article 430 Workflow"
description: "A routing guide to Article 430's internal structure and a step-by-step sizing sequence from FLA lookup to disconnect selection, with a worked example for a 25 HP motor."
breadcrumb:
  - name: "Training"
    url: "/fundamentals/"
  - name: "NEC for Machines and Panels"
    url: "/fundamentals/nec-application/"
repo_path: "control-standards/rag/training_modules/nec_application/article_430_practical_workflow.md"
related_standards:
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
redirect_from:
  - /training/nec-application/article-430-workflow/
review:
  standard: "NEC (NFPA 70) — article scope per the module"
  edition: "taught against the NEC 2023 corpus basis; the locally enforceable edition governs — verify with the AHJ"
  status: "Review pending"
  coverage: "Training module: Practical Article 430 Workflow — worked as education, not a code determination; the AHJ and enforceable edition govern."
  last_reviewed: "July 2026"
---

## Purpose

Article 430 is the primary NEC article for motors, motor circuits, and controllers. It is long, internally subdivided, and cross-references other articles. This module provides a routing map to Article 430's internal structure and a repeatable five-step sizing sequence, demonstrated with a full worked example for a 25 HP motor.

---

## Article 430 internal structure

Article 430 is organized into lettered Parts. Each Part governs a specific protective or sizing function. Navigating the article becomes straightforward once you know which Part handles the question you are answering.

| Part | Scope | Key sections |
|---|---|---|
| Part I | General requirements and definitions | 430.1–430.14: scope, location, markings |
| Part II | Motor circuit conductors | 430.17–430.32: conductor sizing for branch circuits and feeders |
| Part III | Motor and branch-circuit overload protection | 430.31–430.44: overload relay selection and setting |
| Part IV | Motor branch-circuit short-circuit and ground-fault protection | 430.51–430.58: OCPD selection, Table 430.52 |
| Part V | Motor feeder short-circuit and ground-fault protection | 430.61–430.63: feeder OCPD, Art 430.62 |
| Part VI | Motor control circuits | 430.71–430.75: control circuit conductors and protection |
| Part VII | Motor controllers | 430.81–430.91: controller ratings and interrupting capacity |
| Part IX | Disconnecting means | 430.101–430.113: disconnect location, rating, and marking |
| Part X | Adjustable-speed drives (VFDs) | 430.120–430.128: VFD supply conductors and protection |
| Part F (within Part X) | Motor control centers | 430.92–430.98: MCC assembly requirements |

> **Tip:** When you have a motor question, first identify whether you are dealing with branch-circuit conductors (Part II), overload (Part III), branch-circuit SCPD (Part IV), or the disconnect (Part IX). Go directly to that Part rather than reading the article sequentially.

---

## The Art 430.6(A) rule — always use the table

Before entering the sizing sequence, Art 430.6(A) establishes the foundational rule:

> For the purpose of determining conductor ampacity, overload protection, and short-circuit and ground-fault protection, the values given in Tables 430.247, 430.248, 430.249, and 430.250 shall be used instead of the motor nameplate full-load current (FLC) rating.

This means the nameplate FLA is used only for the overload relay's actual setting (which the relay manufacturer uses as the starting point). Conductor, OCPD, and disconnect sizing all begin from the table value.

---

## Article 430 circuit question routing flowchart

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
  Q([Motor circuit question]) --> W{What are you sizing?}
  W --> C[Branch-circuit\nconductors]
  W --> OL[Overload\nprotection]
  W --> OCPD[Branch-circuit\nSCPD]
  W --> F[Feeder\nconductors / OCPD]
  W --> DISC[Disconnecting\nmeans]
  W --> VFD[VFD supply\nand protection]
  C --> P2[Part II\nArt 430.22\n125% × table FLC]
  OL --> P3[Part III\nArt 430.32\n115%–125% × table FLC]
  OCPD --> P4[Part IV\nArt 430.52\nTable 430.52]
  F --> P5[Part V\nArt 430.24 / 430.62]
  DISC --> P9[Part IX\nArt 430.110\n≥115% table FLC]
  VFD --> P10[Part X\nArt 430.122\n125% input current]
</pre>
</div>

---

## Standard five-step sizing sequence

For a typical squirrel-cage induction motor on a branch circuit, the sizing sequence is:

| Step | Action | Article reference | Key multiplier / table |
|---|---|---|---|
| 1 | Look up table FLC | Art 430.6(A) + Table 430.250 | — |
| 2 | Size branch-circuit conductor | Art 430.22 | 125 % × FLC |
| 3 | Select and set overload relay | Art 430.32 | 115 % (SF < 1.15) or 125 % (SF ≥ 1.15) × FLC |
| 4 | Select branch-circuit OCPD | Art 430.52 + Table 430.52 | Per table by OCPD type |
| 5 | Select disconnecting means | Art 430.110 | ≥ 115 % × table FLC |

The sequence is designed so that each step feeds naturally into the next. Steps 3 and 4 are independent of each other (the overload relay and the OCPD are separate protective functions with separate sizing rules), but both depend on the table FLC from Step 1.

---

## Worked example — 25 HP, 460 V, three-phase motor

### Given

- Motor: 25 HP, 460 V, three-phase, squirrel-cage induction
- Service factor: 1.0 (nameplate)
- Wiring: THHN copper conductors, 75 °C terminations
- OCPD type: inverse-time circuit breaker (ITB)
- Disconnect type: molded-case switch or circuit breaker

---

### Step 1 — Table FLC (Art 430.6 + Table 430.250)

**FLC = 34 A**

This value is used for all subsequent calculations in Steps 2–5.

---

### Step 2 — Branch-circuit conductor (Art 430.22)

Minimum conductor ampacity = 125 % × 34 = **42.5 A**

From Table 310.15(B)(16), 75 °C copper:

- 10 AWG = 35 A — insufficient
- 8 AWG = 50 A — adequate

**Select 8 AWG THHN copper.** (50 A ≥ 42.5 A required)

Apply derating for conduit fill or ambient temperature correction factors if applicable to the installation.

---

### Step 3 — Overload relay (Art 430.32)

Service factor (SF) = 1.0 (nameplate), which is less than 1.15, so:

Maximum overload setting = 115 % × FLC = 1.15 × 34 = **39.1 A**

Set the overload relay at or below 39.1 A.

If nuisance tripping occurs after proper investigation, Art 430.32(C) permits increasing the setting to:

- 130 % × FLC for SF < 1.15: 1.30 × 34 = 44.2 A absolute maximum
- After that, an engineering review of the starting conditions is required before further increase

---

### Step 4 — Branch-circuit SCPD (Art 430.52 + Table 430.52)

Table 430.52, inverse-time circuit breaker, Design B squirrel-cage motor: **250 % maximum**

Maximum ITB = 2.50 × 34 = 85 A

Standard breaker sizes (Art 240.6): … 70, 80, 90 …

Next standard size at or below 85 A is 80 A. Art 430.52(C)(1) permits selecting the next standard size up when the calculated maximum does not correspond to a standard size, so **90 A ITB** is acceptable (90 A is the next standard size above 85 A).

**Normal selection: 90 A ITB.**

**Won't-start exception (Art 430.52 Exception No. 2):** If the motor fails to start reliably with a 90 A breaker, the ITB rating may be increased up to **400 %** of table FLC:

400 % × 34 = 136 A → next standard size = **150 A ITB** (maximum permitted under the exception for an ITB)

The won't-start exception requires that the OCPD size is selected no larger than necessary to allow starting, not simply the maximum permitted.

---

### Step 5 — Disconnecting means (Art 430.110)

The motor disconnecting means must have a rating of at least **115 % of the table FLC**:

Minimum disconnect ampere rating = 1.15 × 34 = **39.1 A**

A 30 A disconnect is insufficient. A standard 60 A molded-case switch or circuit breaker easily satisfies this requirement.

Art 430.110(A) also requires the disconnect to be rated for the motor's horsepower or be a circuit breaker rated for the available fault current. For 25 HP at 460 V, a listed HP-rated switch of 25 HP or greater is required if using a motor-circuit switch.

**Minimum disconnect rating: 40 A ampere rating (next standard size above 39.1 A), HP-rated for 25 HP at 460 V.**

---

### Complete sizing summary — 25 HP, 460 V motor

| Step | Item | Calculation | Result |
|---|---|---|---|
| 1 | Table FLC | Table 430.250 | 34 A |
| 2 | Branch conductor | 125 % × 34 = 42.5 A min → 8 AWG Cu = 50 A | 8 AWG THHN Cu |
| 3 | Overload setting (SF=1.0) | 115 % × 34 | ≤ 39.1 A |
| 4 | ITB breaker (normal) | 250 % × 34 = 85 A → next standard | 90 A ITB |
| 4a | ITB breaker (won't-start) | 400 % × 34 = 136 A → next standard | 150 A ITB max |
| 5 | Disconnect | 115 % × 34 = 39.1 A min; HP-rated | 40 A, 25 HP rated |

---

## The 430.52 exception in practice

The won't-start exception is sometimes misapplied. The correct procedure is:

1. Start with the normal maximum from Table 430.52 (250 % for ITB).
2. If the motor does not start — confirmed, not assumed — increment the breaker size one standard size at a time.
3. Stop at the first size that allows starting. Do not go to the maximum permitted by the exception as the default choice.
4. Document the selection, as an AHJ may ask why the breaker exceeds the table maximum.

The maximum limits under the exception for ITB breakers are **250 % standard, 400 % with the exception**. For dual-element (time-delay) fuses the standard maximum is 175 %, exception maximum is 225 %. For non-time-delay fuses the standard maximum is 300 %, exception maximum is 400 %.

---

## NFPA 79 alignment

NFPA 79 (Electrical Standard for Industrial Machinery) applies Art 430 of the NEC by reference for motor protection on industrial machinery (NFPA 79 Chapter 12). The Art 430 sizing sequence described in this module is fully applicable to NFPA 79 machines.

NFPA 79 adds specific requirements for motor short-circuit protection coordination with the machine's supply (NFPA 79 12.4), motor overtemperature protection for motors that may stall (NFPA 79 12.5), and control circuit protection (NFPA 79 9.1.4.3). These supplement, rather than replace, the Art 430 sequence.

---

## Practical takeaway

Article 430's internal structure maps directly to the five-step sizing sequence. When you know which step you are on, you know which Part of Art 430 to consult. The foundational rule is Art 430.6(A): always start from the table FLC, not the nameplate. The won't-start exception for OCPDs is a last resort, not a default, and requires documentation.

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/nec-application/class1-class2-circuits/' | relative_url }}">&larr; Class 1, Class 2, and Remote-Control Circuits</a>
  <a href="{{ '/fundamentals/nec-application/' | relative_url }}">↑ NEC for Machines and Panels</a>
  <a href="{{ '/fundamentals/nec-application/article-409-workflow/' | relative_url }}">Practical Article 409 Workflow &rarr;</a>
</div>
