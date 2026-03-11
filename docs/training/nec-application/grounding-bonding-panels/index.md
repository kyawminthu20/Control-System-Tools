---
layout: training-module
title: "Grounding and Bonding for Control Panels"
description: "The difference between grounding and bonding, EGC sizing from Table 250.122, and why the neutral and ground buses must stay separate in downstream panels."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "NEC for Machines and Panels"
    url: "/training/nec-application/"
repo_path: "control-standards/rag/training_modules/nec_application/grounding_bonding_control_panels.md"
related_standards:
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
  - name: "UL 508A"
    url: "/standards/us-electrical/ul-508a/"
---

## Purpose

This module clarifies the distinction between grounding and bonding, explains how to size the equipment grounding conductor (EGC) using Table 250.122, and covers why the neutral and ground buses must remain separate in downstream (sub) panels and industrial control panels.

---

## Grounding vs. bonding — the distinction

These two terms are often used interchangeably in the field, but the NEC treats them as separate functions with different purposes.

| Concept | NEC term | Purpose |
|---|---|---|
| **Grounding** | Connecting to earth via grounding electrode | Stabilizes system voltage relative to earth; limits lightning and surge overvoltages |
| **Bonding** | Connecting conductive parts together | Creates a **low-impedance fault-current path** back to the source, enabling the OCPD to operate |

> **Critical rule:** A grounding electrode rod driven into the earth is **not** the fault-current return path. Its impedance is far too high (typically hundreds of ohms) to carry enough fault current to trip an OCPD. The equipment grounding conductor (EGC) is the fault-current return path — the earth rod is not.

This distinction matters for panel design. A control panel that bonds motor frames and enclosures to the EGC ensures that a fault between a live conductor and the enclosure causes a large fault current that trips the OCPD quickly. If only an earth rod were connected (no EGC), the fault current would be too low to trip the OCPD, leaving energized metalwork.

---

## EGC sizing — Table 250.122

The **equipment grounding conductor** is sized from **NEC Table 250.122** based on the rating of the upstream overcurrent protective device, **not** the load current or conductor ampacity.

**Rule:** Size the EGC by the OCPD, not the load.

### EGC sizing reference table

| Upstream OCPD rating | Minimum copper EGC | AWG |
|---|---|---|
| 15 A | 14 AWG | 14 |
| 20 A | 12 AWG | 12 |
| 60 A | 10 AWG | 10 |
| 100 A | 8 AWG | 8 |
| 200 A | 6 AWG | 6 |
| 300 A | 4 AWG | 4 |
| 400 A | 3 AWG | 3 |
| 600 A | 1 AWG | 1 |

These are **minimum** sizes. The EGC may always be increased in size for longer runs or for EMI noise reasons.

**Example:** A 10 HP motor protected by a 60 A branch-circuit OCPD requires a minimum 10 AWG copper EGC, regardless of the fact that the motor conductors are 10 AWG or 12 AWG.

---

## Neutral and ground separation in downstream panels

At the **main service panel**, the neutral (grounded conductor) and the equipment ground (EGC) are intentionally bonded together at one point — the main bonding jumper (MBJ). This is the only permitted bonding point in a standard premises wiring system.

At all **downstream panels and subpanels** (and industrial control panels fed from a separate source), the neutral bus and the ground bus must be **kept separate and isolated from each other**.

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TB
  UTIL["Utility"]
  SVC["Service Panel\n(Main Bonding Jumper here)"]
  GRND["Grounding Electrode\n(Earth rod, water pipe, etc.)"]
  SUB["Downstream Panel\nor ICP"]
  N_BUS["Neutral Bus\n(isolated from enclosure)"]
  G_BUS["Ground Bus\n(bonded to enclosure)"]

  UTIL --> SVC
  SVC -- "MBJ bonds N to G\nat this point only" --> GRND
  SVC -->|"4-wire feeder\n(L1, L2, L3, N, EGC)"| SUB
  SUB --> N_BUS
  SUB --> G_BUS
  N_BUS -. "NOT connected here" .- G_BUS

  style SVC fill:#f5f5dc,stroke:#999
  style N_BUS fill:#dce8f5,stroke:#999
  style G_BUS fill:#dce8f5,stroke:#999
</pre>
</div>

**Why must they stay separate downstream?**

If the neutral and ground are bonded at a downstream panel, neutral current will flow on both the neutral conductor and the grounding conductors and metallic enclosures back to the source. This creates:

- Objectionable current on grounding paths (NEC 250.6)
- Shock hazard on normally non-current-carrying metal parts
- Interference with ground-fault circuit interrupter (GFCI) operation

For industrial control panels fed by a feeder from a main service, the ICP ground bus bonds to the enclosure and to the incoming EGC. The neutral (if present) must land on a separate, isolated bus.

---

## Panel enclosure bonding

The metal enclosure of every industrial control panel must be bonded to the EGC system. NEC 250.96 and UL 508A both require that the enclosure be part of the effective fault-current path.

Bonding methods for ICP enclosures:

| Method | Notes |
|---|---|
| Main ground bus bolted to enclosure | Most common; direct metal-to-metal contact required |
| Bonding jumper from DIN rail to ground bus | Required if DIN rail is not inherently bonded to enclosure |
| Bonding jumper from subpanel within enclosure | Interior panels separated by paint must be jumpered |

**Paint:** Painted surfaces break the bonding path. Hardware used to mount the ground bus must cut through any paint or use star washers to make direct metal-to-metal contact.

---

## VFD grounding notes

VFDs require careful attention to grounding because:

1. VFD output creates high-frequency PWM currents that can return on the EGC, causing noise in adjacent circuits.
2. VFD manufacturers typically require a **dedicated EGC** run with the motor power conductors inside shielded cable, with the shield bonded at both ends.
3. The motor frame must be directly bonded to the panel ground bus via the EGC, not solely through conduit fittings.

Follow VFD manufacturer bonding requirements in addition to NEC Table 250.122 minimums. Manufacturer requirements for conductor shielding and bonding are enforceable under NEC 110.3(B) (listed equipment installed per instructions).

---

## Common mistakes

| Mistake | Impact | Correct approach |
|---|---|---|
| EGC sized by load current instead of OCPD | Undersized EGC; fault current may damage conductor | Size from Table 250.122 by OCPD rating |
| Neutral and ground bonded in downstream panel | Objectionable current on metal parts; GFCI nuisance tripping | Keep neutral isolated from ground bus downstream |
| Earth rod used as fault-current return | OCPD will not trip; energized enclosure during fault | Install EGC from source; earth rod supplements, does not replace |
| Ground bus not making metal-to-metal contact | High-impedance bond; ineffective fault path | Remove paint; use star washers or bonding bushings |
| No EGC with motor cable inside conduit | Conduit fittings are not a reliable EGC | Pull dedicated EGC or use listed EGC-rated cable |

---

## Practical takeaway

- Grounding stabilizes voltage to earth; bonding provides the fault-current return path.
- The earth rod is not the fault-current path — the EGC is.
- Size the EGC from Table 250.122 using the upstream OCPD rating.
- Neutral and equipment ground may only be bonded at one point: the main service panel's main bonding jumper.
- Downstream panels and ICPs must keep neutral and ground buses separate.

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/training/nec-application/disconnecting-means/' | relative_url }}">&larr; Disconnecting Means for Machinery</a>
  <a href="{{ '/training/nec-application/' | relative_url }}">↑ NEC for Machines and Panels</a>
  <a href="{{ '/training/nec-application/sccr-workflow/' | relative_url }}">SCCR Workflow &rarr;</a>
</div>
