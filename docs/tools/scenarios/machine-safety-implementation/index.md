---
layout: default
title: "Scenario 06 — Practical Machine Safety Implementation"
description: "10-step machine builder workflow for SIL/PL implementation: risk assessment through validation, with hardware selection and architecture examples."
breadcrumb:
  - name: "Scenarios"
    url: "/tools/scenarios/"
  - name: "Machine Safety Implementation"
related_standards:
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61508"
    url: "/standards/functional-safety/iec-61508/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
redirect_from:
  - /implementation/scenarios/machine-safety-implementation/
  - /scenarios/machine-safety-implementation/
  - /scenarios/machine-safety-implementation/index.html
---

<div class="page-header">
  <span class="page-header__label">Scenario 06</span>
  <h1>Practical Machine Safety Implementation</h1>
  <p>A structured engineering workflow for machine builders implementing SIL or PL — from risk assessment through hardware validation.</p>
</div>

## Workflow Overview

Implementing SIL or PL on a machine is not a single decision. It flows through four layers:

| Layer | Activity |
|-------|----------|
| 1 | Risk Assessment |
| 2 | Safety Function Definition |
| 3 | Hardware Architecture Selection |
| 4 | Validation (hardware + software) |

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
    A[Risk Assessment] --> B[Safety Functions]
    B --> C[Architecture Selection]
    C --> D[Device Selection]
    D --> E[Wiring]
    E --> F[Safety Logic]
    F --> G[Validation]

    A -.-> A1[ISO 13849 / IEC 62061]
    B -.-> B1[Safety function register]
    C -.-> C1[Category B/1/2/3/4]
    D -.-> D1[SIL/PL-certified devices]
    F -.-> F1[Certified function blocks]
    G -.-> G1[SISTEMA / validation report]
</pre>
</div>

---

## Step 1 — Perform a Risk Assessment

Before choosing hardware, determine the **required safety level**.

| Standard | Method | Output |
|----------|--------|--------|
| ISO 13849-1 | Risk graph (S/F/P parameters) | PLr (Performance Level required) |
| IEC 62061 | Risk estimation | SILCL (SIL Claim Limit) |

### Risk Graph Parameters (ISO 13849-1)

| Parameter | Meaning |
|-----------|---------|
| **S** | Severity of injury (S1 = reversible, S2 = irreversible) |
| **F** | Frequency of exposure (F1 = seldom, F2 = frequent) |
| **P** | Possibility of avoiding hazard (P1 = possible, P2 = scarcely) |

Example:

| Hazard | S | F | P | PLr |
|--------|---|---|---|-----|
| Crushing hazard (press) | S2 | F2 | P2 | **PLd** |
| Guard door bypass | S2 | F1 | P1 | PLc |

---

## Step 2 — SIL/PL Equivalence

Both standards target the same safety levels. Choose one standard and apply it consistently for each safety function.

| PL (ISO 13849-1) | SIL (IEC 62061 / IEC 61508) | PFHd range |
|------------------|-----------------------------|-----------|
| PL a | — | ≥ 10⁻⁵ |
| PL b | SIL 1 | 3×10⁻⁶ – 10⁻⁵ |
| PL c | SIL 1 | 10⁻⁶ – 3×10⁻⁶ |
| **PL d** | **SIL 2** | **10⁻⁷ – 10⁻⁶** |
| **PL e** | **SIL 3** | **10⁻⁸ – 10⁻⁷** |

**PL d / SIL 2 is the most common target for industrial machine guarding.**

---

## Step 3 — Define Safety Functions

A safety function is the behavior the system must perform when danger occurs.

| Safety Function | Trigger | Action |
|----------------|---------|--------|
| Emergency Stop | E-stop pressed | Remove power to all hazards |
| Guard Door Interlock | Guard opened | Stop machine, disable outputs |
| Safe Torque Off | Safety demand | Disable motor torque via drive STO |
| Hydraulic Pressure Dump | Safety demand | Open dump valve, remove pressure |
| Chemical Pump Shutoff | Safety demand | Close dosing valve |

Each function must be documented as:

```
Input device → Safety logic → Output device
```

Example:

```
E-Stop Button (dual NC contacts)
         ↓
   Safety PLC (Category 3)
         ↓
Safety Contactor → Motor power removed
```

---

## Step 4 — Choose Architecture Category (ISO 13849-1)

| Category | Description | Typical PL Achievable |
|----------|-------------|----------------------|
| B | Basic single channel, no redundancy | PLa–PLb |
| 1 | Reliable components (well-tried parts) | PLb–PLc |
| 2 | Single channel with periodic test | PLc |
| **3** | **Dual channel, detected single fault** | **PLd** |
| **4** | **Dual channel, all faults detected** | **PLe** |

Most industrial machines with moving parts require **Category 3 or 4**.

---

## Step 5 — Category 3 Architecture Example

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
    ES[E-stop / Guard] --> |CH1 NC| IA[Safety Input A]
    ES --> |CH2 NC| IB[Safety Input B]
    IA --> PLC[Safety PLC]
    IB --> PLC
    PLC --> OA[Output A → Contactor A]
    PLC --> OB[Output B → Contactor B]
    OA --> |Feedback NC| FB[Feedback to PLC]
    OB --> |Feedback NC| FB
</pre>
</div>

Key features:
- Dual-channel NC contact wiring
- Cross-channel monitoring (short-circuit detection)
- Contactor feedback loop (welded contact detection)
- Manual reset required after safety demand

---

## Step 6 — Select Safety-Certified Devices

Only use devices with published safety data (PFHd, B10d, or MTTF values).

| Device | Certification Required | Example Vendors |
|--------|----------------------|-----------------|
| Safety PLC | SIL 2 or SIL 3 certified | GuardLogix (Rockwell), Siemens F-CPU, Pilz PNOZmulti |
| Safety relay module | SIL 3 | Pilz PNOZ, Schmersal, Omron |
| Safety contactor | Mechanically linked contacts | Schneider TeSys, ABB AF series |
| Safety light curtain | PLe / SIL 3 | SICK C4000, Banner EZ-SCREEN |
| Safety interlock switch | PLd / PLe | Schmersal, EUCHNER, Rockwell Guardmaster |
| E-stop button | PLd / PLe, positive-opening NC contacts | Pilz, Schmersal, Rockwell |

---

## Step 7 — Example Machine Safety Stack

For a hydraulic + chemical dosing machine:

| Safety Function | Input Device | Logic | Output Device |
|----------------|-------------|-------|---------------|
| Emergency Stop | Dual NC E-stop | Safety PLC | Safety contactors |
| Guard Interlock | Coded safety switch | Safety PLC | Drive STO + contactors |
| Hydraulic pressure relief | Pressure safety switch | Safety PLC | Safety-rated dump valve |
| Pump shutdown | Dual NC process switch | Safety PLC | Safety contactor |
| Servo Safe Torque Off | Safety PLC output | Drive STO channel 1 + 2 | Motor torque disabled |

**Safety PLC handles all logic.** Individual contactors and valves never need to be SIL-rated because the PLC + dual-channel architecture provides the required reliability.

---

## Step 8 — Safety Wiring Practices

Refer to the [Safety Wiring Practices]({{ '/lifecycle/safety-wiring/' | relative_url }}) lifecycle page for detailed wiring guidance.

Key principles:
- 24 VDC for all safety control circuits (SELV — IEC 61140)
- Dual-channel separation: CH1 and CH2 never paralleled
- NC contacts (fail-safe: wire break = safety demand)
- 18 AWG stranded copper as practical default for machine control
- Blue: ungrounded DC control conductors (NFPA 79 / UL 508A)
- Ferrules and spring-clamp terminals for vibration resistance
- Discrepancy time 20–100 ms (configure per controller and device)

---

## Step 9 — Programming Safety Logic

Safety PLC programming must use **certified function blocks** (IEC 61131-3 safety libraries).

```
IF
  EStop_OK
AND
  GuardDoorClosed
AND
  LightCurtainClear
THEN
  SafetyEnable = TRUE
ELSE
  SafetyEnable = FALSE
```

Safety programming rules:
- No bypass paths
- No unsafe reset (reset must be manual and supervised)
- All safety outputs de-energize on any faulted input
- Reset only after all safety devices are clear

---

## Step 10 — Validation

Validation is required by both ISO 13849-1 (Clause 10) and IEC 62061 (Clause 8).

| Activity | Tool / Method |
|----------|--------------|
| PL / PFHd calculation | SISTEMA (free, TÜV Rheinland) |
| Safety function testing | Functional test per safety plan |
| Fault injection | Simulate wire breaks, short circuits, welded contacts |
| Response time measurement | Verify safety response time ≤ required |
| Documentation | Validation report, safety function register |

**SISTEMA** is the standard calculation tool for ISO 13849-1. Libraries of certified component data are available from major device manufacturers.

---

## Standards Referenced

| Standard | Role |
|----------|------|
| ISO 13849-1 | PLr determination, Category selection, PFHd calculation |
| IEC 62061 | SILCL determination, subsystem PFHD calculation |
| IEC 61508 | Underlying reliability framework for IEC 62061 |
| NFPA 79 | Machine electrical wiring (US) |
| IEC 60204-1 | Machine electrical equipment (international) |
| IEC 61140 | SELV definition (24 VDC justification) |

## See Also

- [Safety Architecture — Lifecycle Stage 4]({{ '/lifecycle/safety-architecture/' | relative_url }})
- [Safety Wiring Practices — Lifecycle Stage]({{ '/lifecycle/safety-wiring/' | relative_url }})
- [ISO 13849-1 Standard Reference]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }})
- [IEC 62061 Standard Reference]({{ '/standards/functional-safety/iec-62061/' | relative_url }})
