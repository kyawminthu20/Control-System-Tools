---
layout: default
title: "Lifecycle Stage 4 — Safety Architecture Definition"
description: "Decompose safety functions into subsystems, select category/architecture, calculate PL or SIL, and verify response time budgets."
breadcrumb:
  - name: "Lifecycle"
    url: "/lifecycle/"
  - name: "4. Safety Architecture"
related_standards:
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
  - name: "IEC 61508"
    url: "/standards/functional-safety/iec-61508/"
---

<div class="page-header">
  <span class="page-header__label">Lifecycle Stage 04</span>
  <h1>Safety Architecture Definition</h1>
  <strong>Confirm PL or SIL — Architecture Document</strong>
</div>

## 1. Purpose of This Stage

This stage translates the safety function register and PLr/SIL targets from Stage 3 into **concrete, calculable, verifiable safety architectures** — the specific arrangement of hardware and the quantitative parameters that determine whether each safety function achieves its required integrity level.

This is where safety engineering becomes quantitative. Stage 3 determined *what* safety functions are needed and *how much* risk reduction each must provide. This stage determines *how* that risk reduction is physically realized — what architecture, what components, what redundancy, what diagnostics, and what the numbers prove.

Every architecture decision made here has direct cost, complexity, and maintainability consequences. Over-specifying architecture wastes money and increases maintenance burden. Under-specifying means the safety function does not achieve its required PLr/SIL and the system is non-compliant.

This is also the **PL/SIL confirmation point**. The pathway selected in Stage 2 and the targets assigned in Stage 3 are now confirmed through calculation. If the architecture cannot achieve the target, the design must iterate — either by changing components, changing architecture, or (in rare cases) revisiting the risk assessment.

> **This stage answers: What specific architecture and components will achieve the required PLr/SIL for each safety function, and what is the quantitative proof?**

---

## 2. Entry Criteria

This stage begins when **Stage 3 (Risk Assessment) exit criteria are met**.

### Required Inputs

| Input | Source (Stage) | Why It Matters |
|-------|---------------|----------------|
| Safety function register | Stage 3 | Defines every safety function with its PLr/SIL target, safe state, response time, triggering event, and reset behavior — this is the design specification |
| PLr/SIL assignment record | Stage 3 | Confirms the integrity target each architecture must achieve |
| Standards register | Stage 2 | Determines which architectural methodology applies (ISO 13849-1 categories vs IEC 62061 subsystem architecture vs IEC 61511 SIS architecture) |
| PL vs SIL pathway confirmation | Stage 2 / Stage 3 | Determines calculation methodology |
| Type-C standard requirements | Stage 2 / Stage 3 | May impose specific architectural constraints (e.g., mandatory dual-channel for certain safety functions, specific component requirements) |
| System description and boundary | Stage 1 | Physical constraints that affect architecture choices (available space, cable routing, environment) |
| Operating mode definitions | Stage 1 | Architecture must function correctly across all defined modes, including mode transitions |
| Residual risk register | Stage 3 | Context for understanding what the safety function must protect against |

**If any safety function in the register does not have a confirmed PLr/SIL target, the architecture for that function cannot be designed. Resolve before proceeding.**

---

## 3. Standards Influence

| Standard | Role at This Stage |
|----------|-------------------|
| **ISO 13849-1:2023 §5, §6, §7, §8, Annex A–K** | Defines designated architectures (Categories B, 1, 2, 3, 4), reliability parameters (MTTFd, DC, CCF), PL calculation methodology, and validation requirements |
| **ISO 13849-2:2012** | Validation of safety-related parts — provides fault lists and fault exclusion criteria for specific technologies (electrical, pneumatic, hydraulic, mechanical). Critical for justifying fault exclusion assumptions in architecture design. |
| **IEC 62061:2021 §5, §6** | Defines subsystem architecture (1oo1, 1oo1D, 1oo2, 1oo2D, 2oo3), PFHD calculation methodology, hardware fault tolerance (HFT), safe failure fraction (SFF), and diagnostic coverage requirements |
| **IEC 61508:2010 Parts 1, 2, 6, 7** | Architectural constraints tables (HFT vs SFF), hardware reliability calculation methods, proven-in-use and prior-use justification requirements. Foundation for IEC 62061 and IEC 61511 architectural requirements. |
| **IEC 61511-1:2016 §11** | SIS architecture design requirements — defines minimum fault tolerance requirements (HFT), architectural constraints, and the conditions under which HFT can be reduced by one level |
| **IEC 62046:2018** | Application of protective equipment — muting, blanking, and reduced resolution requirements for safety devices (light curtains, laser scanners). Affects architecture when bypass/muting is required. |
| **ISO 14119:2013 §7, §8** | Interlocking device architecture — specific requirements for interlocking guard switches including fault exclusion criteria, coding levels, and actuator design |
| **ISO 13855:2010** | Safety device positioning — minimum safety distances based on approach speed and response time. Directly constrains the response time budget that the architecture must meet. |
| **Applicable type-C standards** | May impose specific architectural constraints — e.g., ISO 10218-2 requires specific safety-rated monitored stop or speed/separation monitoring for collaborative robots; ISO 16092 requires specific architectures for press safety functions |

---

## 4. Fundamental Architecture Concepts

### 4.1 The Safety Chain (Subsystem Decomposition)

Every safety function is physically realized as a chain of subsystems:

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   INPUT      │      │   LOGIC      │      │   OUTPUT     │
│  (Sensor)    │─────►│  (Solver)    │─────►│  (Actuator)  │
│              │      │              │      │              │
│  Examples:   │      │  Examples:   │      │  Examples:   │
│  • Guard     │      │  • Safety    │      │  • Contactor │
│    switch    │      │    relay     │      │  • Valve     │
│  • E-stop   │      │  • Safety    │      │  • Drive     │
│  • Light    │      │    PLC       │      │    STO input │
│    curtain  │      │  • Hardwired │      │  • Motor     │
│  • Pressure │      │    logic     │      │    starter   │
│    sensor   │      │              │      │              │
└─────────────┘      └─────────────┘      └─────────────┘

     SB1              SB2                   SB3
  (Subsystem 1)    (Subsystem 2)        (Subsystem 3)
```

**Each subsystem has its own:**
- Architecture (single channel, dual channel, with/without diagnostics)
- Reliability parameters (MTTFd or PFHd, DC)
- Component-level data (B10d, T10d, manufacturer safety data)

**The overall safety function achieves a PL or SIL that is determined by the combination of all subsystems in the chain.** The weakest subsystem limits the overall performance — you cannot achieve PLe with a Category B input subsystem, regardless of how good the logic and output subsystems are.

### 4.2 ISO 13849-1 Designated Architectures (Categories)

| Category | Architecture | Description | Behavior on Fault | Typical Achievable PL |
|----------|-------------|-------------|-------------------|----------------------|
| **B** | Single channel, no fault detection | Basic safety principles applied. Single fault can cause loss of safety function. | Loss of safety function | PL a — PL b |
| **1** | Single channel, well-tried components | Same as B but using well-tried components and well-tried safety principles. Single fault can still cause loss, but probability is reduced. | Loss of safety function (lower probability) | PL b — PL c |
| **2** | Single channel with periodic testing | Diagnostic function (test equipment, TE) checks the safety function at reasonable intervals. Fault between tests can cause loss. | Loss detected at next test cycle | PL b — PL d |
| **3** | Dual channel (redundant) | Two independent channels. Single fault in one channel does not cause loss of safety function. Some faults may be undetected. | Safety function maintained (single fault) | PL c — PL e |
| **4** | Dual channel with high diagnostics | Two independent channels with enhanced diagnostics. Single fault detected before or at next demand. Accumulation of undetected faults does not cause loss. | Safety function maintained (single and accumulated faults) | PL e |

#### Category Architecture Diagrams

```
Category B / 1:                    Category 2:
┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
│  I  │───►│  L  │───►│  O  │    │  I  │───►│  L  │───►│  O  │
└─────┘    └─────┘    └─────┘    └─────┘    └──┬──┘    └─────┘
                                               │
                                            ┌──▼──┐
                                            │ TE  │ (test/monitoring)
                                            └─────┘

Category 3 / 4:
┌─────┐    ┌─────┐    ┌─────┐
│ I1  │───►│ L1  │───►│ O1  │
└─────┘    └──┬──┘    └─────┘
              │ (cross-monitoring)
┌─────┐    └──┼──┐    ┌─────┐
│ I2  │───►│ L2  │───►│ O2  │
└─────┘    └─────┘    └─────┘
```

### 4.3 IEC 62061 Subsystem Architectures

| Architecture | HFT | Description | SFF Requirement |
|-------------|-----|-------------|-----------------|
| **1oo1** | 0 | Single channel, no redundancy | SFF ≥ 60% for SIL 1, ≥ 90% for SIL 2, not permitted for SIL 3 |
| **1oo1D** | 0 | Single channel with diagnostics | SFF ≥ 60% for SIL 1, ≥ 90% for SIL 2, ≥ 99% for SIL 3 |
| **1oo2** | 1 | Dual channel, either can trip | SFF ≥ 0% for SIL 1, ≥ 60% for SIL 2, ≥ 90% for SIL 3 |
| **1oo2D** | 1 | Dual channel with diagnostics | Most capable architecture — highest SIL achievable |
| **2oo3** | 1 | Triple channel, majority voting | Used in process safety and high-availability applications |

#### IEC 62061 Architectural Constraints (per IEC 61508 Table 2/3)

| SIL Target | Type A Element (well-known failure modes) | Type B Element (complex, not fully known) |
|-----------|----------------------------------------|----------------------------------------|
| | HFT = 0 | HFT = 1 | HFT = 2 | HFT = 0 | HFT = 1 | HFT = 2 |
| SIL 1 | SFF < 60% | SFF < 60% | SFF < 60% | SFF < 60% | SFF < 60% | SFF < 60% |
| SIL 2 | SFF ≥ 60% | SFF < 60% | SFF < 60% | SFF ≥ 90% | SFF ≥ 60% | SFF < 60% |
| SIL 3 | SFF ≥ 90% | SFF ≥ 60% | SFF < 60% | — | SFF ≥ 90% | SFF ≥ 60% |

**Type A elements:** Simple devices with well-known failure modes (electromechanical relays, contactors, simple sensors)

**Type B elements:** Complex devices (microprocessor-based safety PLCs, programmable sensors, smart actuators)

### 4.4 IEC 61511 SIS Architecture Requirements

| SIL Target | Minimum Hardware Fault Tolerance |
|-----------|-------------------------------|
| SIL 1 | HFT = 0 (1oo1) — may be reduced from HFT = 1 if prior use and SFF conditions met |
| SIL 2 | HFT = 1 (1oo2) — may be reduced to HFT = 0 if prior use and diagnostic conditions met per §11.4 |
| SIL 3 | HFT = 2 (1oo3 or 2oo3) — may be reduced to HFT = 1 if conditions met |
| SIL 4 | Special architecture — typically 2oo4 or equivalent |

**IEC 61511 HFT reduction rules (§11.4):** HFT may be reduced by one level if:
- The device has demonstrated prior use in a similar application, AND
- Diagnostic coverage is sufficient, AND
- The failure mode is well-characterized

**Document every HFT reduction with explicit justification.**

### 4.5 ISO 13849-1 vs IEC 62061 Architecture Mapping

For reference — approximate correspondence between the two frameworks:

| ISO 13849-1 Category | Approximate IEC 62061 Architecture | HFT |
|----------------------|-----------------------------------|-----|
| Category B | 1oo1 (no diagnostics) | 0 |
| Category 1 | 1oo1 (well-tried) | 0 |
| Category 2 | 1oo1D | 0 |
| Category 3 | 1oo2 | 1 |
| Category 4 | 1oo2D | 1 |

**These are approximations. The calculation methodologies are different and results may not be identical.**

---

## 5. Engineering Activities

### 5.1 Decompose Each Safety Function into Subsystems

For each safety function in the register from Stage 3, identify the physical subsystems:

| SF-ID | Input Subsystem (SB1) | Logic Subsystem (SB2) | Output Subsystem (SB3) | Additional Subsystems |
|-------|----------------------|----------------------|------------------------|----------------------|
| SF-01 | Guard switch (coded, dual-channel) | Safety relay module | Two contactors in series (redundant) | — |
| SF-02 | E-stop device (dual NC contacts) | Safety PLC, F-CPU | Two contactors in series | — |
| SF-03 | Type 4 light curtain (integral dual-channel) | Safety PLC, F-CPU | Drive STO input (dual-channel) | Muting sensor subsystem |
| SF-04 | Encoder (safe speed monitoring via safety PLC) | Safety PLC, F-CPU | Drive STO input | — |
| SF-05 | Pressure transmitter (1oo2 redundant) | SIS logic solver | Shutdown valve (1oo2 redundant) | — |

### 5.2 Select Architecture Category per Subsystem

For each subsystem, select the architecture category or hardware architecture based on the PLr/SIL target and the constraints of the standard:

#### For ISO 13849-1 (PL Pathway)

Use the relationship between Category, MTTFd, DC, and achievable PL:

| Target PLr | Minimum Category Options | Required MTTFd | Required DC | CCF Required? |
|-----------|------------------------|----------------|------------|--------------|
| PL a | Category B | Low | None | No |
| PL b | Category 1 or B (with high MTTFd) | Medium | None | No |
| PL c | Category 1 (high MTTFd), 2, or 3 | Low–Medium | Low–Medium | Yes (Cat 2, 3) |
| PL d | Category 2 (high MTTFd, medium DC), or Category 3 (medium–high MTTFd, low–medium DC) | Medium–High | Low–Medium | Yes |
| PL e | Category 3 (high MTTFd, high DC) or Category 4 | High | High | Yes |

**The most common industrial machinery safety architecture is Category 3 with high MTTFd components and medium DC, achieving PLd.** This covers the majority of guard interlocking, e-stop, and safety device applications.

#### For IEC 62061 (SIL Pathway)

Select architecture based on SIL target and architectural constraints:

| Target SIL | Typical Architecture | HFT | SFF Requirement (Type B) |
|-----------|---------------------|-----|-------------------------|
| SIL 1 | 1oo1D or 1oo2 | 0 or 1 | ≥ 60% (1oo1D) |
| SIL 2 | 1oo2 or 1oo2D | 1 | ≥ 60% (1oo2), ≥ 90% (1oo1D) |
| SIL 3 | 1oo2D | 1 | ≥ 90% |

### 5.3 Select Components

Component selection is driven by the architecture and the reliability data needed for calculation.

#### Component Data Requirements

| Parameter | ISO 13849-1 | IEC 62061 | Where to Get It |
|-----------|------------|-----------|-----------------|
| **MTTFd** (Mean Time to Dangerous Failure) | Required per subsystem | Used in PFHD calculation | Manufacturer safety data sheet, or calculated from B10d |
| **B10d** (Number of operations to 10% dangerous failure) | Used to calculate MTTFd for electromechanical devices | Used in PFHD calculation | Manufacturer data sheet |
| **DC** (Diagnostic Coverage) | Required per subsystem | Required per subsystem | Estimated per ISO 13849-1 Annex E or IEC 62061 Annex C |
| **CCF score** | Required for Category 2, 3, 4 | Required for all redundant architectures | Scored per ISO 13849-1 Annex F or IEC 62061 Annex F |
| **T10d** (Time to 10% dangerous failure) | Used for time-based components | — | Manufacturer data or estimated from B10d and demand rate |
| **PFHd** (Probability of Dangerous Failure per Hour) | Calculated result | Calculated result | SISTEMA, SILver, manual calculation |
| **SFF** (Safe Failure Fraction) | — | Required for architectural constraints | Manufacturer data or calculated from failure mode analysis |
| **λd** (Dangerous failure rate) | — | Used in PFHD calculation | Manufacturer data or failure rate databases (SN 29500, IEC 62380) |
| **Proof test interval (T1)** | — | Used in PFHD calculation for IEC 61511 | Defined by designer based on operational requirements |
| **Mission time (TM)** | 20 years default per ISO 13849-1 | 20 years default | May be shorter if justified and documented |

#### Component Selection Criteria

| Criterion | Requirement | Standard Reference |
|-----------|------------|-------------------|
| **Manufacturer provides safety data** | MTTFd, B10d, PFHd, SFF, failure modes must be available from the manufacturer — do not estimate if data is available | ISO 13849-1 §7, IEC 62061 §6.2 |
| **Well-tried component (Category 1)** | Must meet the definition of "well-tried" per ISO 13849-1 §6.2.4 and ISO 13849-2 — widely used in the past with good results, or made and verified to principles giving suitability and reliability | ISO 13849-1 §6.2.4 |
| **Proven-in-use / prior use** | For IEC 62061/61508: component must have documented operating history in a similar application with sufficient statistical confidence | IEC 62061 §6.2, IEC 61508-2 §7.4.7 |
| **Type A vs Type B element classification** | Simple devices with well-known failure modes (Type A) vs complex devices (Type B) — classification affects architectural constraint requirements | IEC 61508-2 §7.4.3 |
| **Environmental suitability** | Component rated for the operating environment (temperature, humidity, vibration, EMC, IP rating) | IEC 60204-1, IEC 61326 (EMC), IEC 60529 (IP) |
| **Mission time compatibility** | Component expected life must meet or exceed the mission time used in the calculation (default 20 years) — if not, mandatory replacement interval must be defined | ISO 13849-1 §7.1.4 |
| **Systematic capability (SC)** | For IEC 62061: complex subsystems must have a systematic capability rating ≥ the target SIL | IEC 62061 §6.3 |

#### Common Component Types and Typical Data

| Component Type | Typical Architecture Role | Typical MTTFd Range | Key Data to Obtain |
|---------------|--------------------------|--------------------|--------------------|
| Safety interlock switch (coded) | Input — guard monitoring | 50–150 years (varies by type) | B10d, operating rate, contact configuration |
| E-stop device | Input — emergency stop | 100+ years (low demand) | B10d, contact configuration (dual NC) |
| Type 4 light curtain | Input — presence detection | Manufacturer PFHd directly (complex device) | PFHd, response time, SIL/PL rating, resolution |
| Safety relay module | Logic — hardwired | Manufacturer MTTFd or PFHd directly | PFHd, category/SIL rating, input/output configuration |
| Safety PLC / F-CPU | Logic — programmable | Manufacturer PFHd directly | PFHd per safety function, response time, SIL/PL rating, systematic capability (SC) |
| Contactor (motor control) | Output — power switching | 20–100 years (depends on load and cycle rate) | B10d, utilization category (AC-1, AC-3, AC-4), operating rate |
| Safety-rated drive (STO, SS1, SLS) | Output — drive safety function | Manufacturer PFHd directly | PFHd per safety function, response time, SIL/PL rating |
| Solenoid valve (safety-rated) | Output — fluid power control | 50–150 years (varies by type and demand rate) | B10d, operating rate, failure mode data |
| Pressure transmitter | Input — process measurement | Manufacturer SFF and λd | λd, SFF, proof test interval sensitivity |

### 5.4 Calculate MTTFd from B10d (for Electromechanical Components)

For components where the manufacturer provides B10d instead of MTTFd:

```
MTTFd = B10d / (0.1 × nop)

Where:
  B10d = number of operations to 10% dangerous failure (from manufacturer)
  nop  = number of operations per year

  nop = dop × hop × 3600 / tcycle

Where:
  dop    = operating days per year
  hop    = operating hours per day
  tcycle = cycle time in seconds per operation
```

**Example:**
- Contactor B10d = 1,300,000 operations (from manufacturer)
- Machine operates 250 days/year, 16 hours/day
- Cycle time = 30 seconds (120 operations/hour)

```
nop = 250 × 16 × 3600 / 30 = 480,000 operations/year
MTTFd = 1,300,000 / (0.1 × 480,000) = 27.1 years
```

**Cap MTTFd at 2500 years per channel per ISO 13849-1 §C.2.**

### 5.5 Estimate Diagnostic Coverage (DC)

DC is the fraction of dangerous failures that are detected by automatic diagnostics.

#### ISO 13849-1 DC Estimation (Annex E — Selected Examples)

| Diagnostic Measure | Estimated DC |
|-------------------|-------------|
| No diagnostics | 0% (None) |
| Monitoring of input signals by safety logic (plausibility, cross-checking) | 60%–90% (Low–Medium) |
| Monitoring of output signals by safety logic (contactor feedback, EDM) | 99% (High) |
| Direct monitoring (e.g., mechanically linked contacts on guard switch) | 99% (High) |
| Cross-monitoring of redundant channels with dynamic testing | 99% (High) |
| Temporal monitoring (watchdog) | 60% (Low) |
| Redundant shutoff path with monitoring of both paths (EDM on both contactors) | 99% (High) |

#### DC Levels per ISO 13849-1

| DC Level | DC Range |
|----------|----------|
| None | DC < 60% |
| Low | 60% ≤ DC < 90% |
| Medium | 90% ≤ DC < 99% |
| High | DC ≥ 99% |

**Critical requirement:** For Category 2, 3, and 4, the diagnostic function itself must be designed to not cause a dangerous condition if it fails. The test equipment (TE) in Category 2, or the cross-monitoring in Category 3/4, must be evaluated for its own failure modes.

#### External Device Monitoring (EDM)

EDM is one of the most important and most commonly misunderstood diagnostic measures:

```
Safety Logic ──► Contactor K1 ──► Motor
                    │
                    ├──► K1 NC auxiliary contact ──► Safety Logic feedback input
                    │
Safety Logic ──► Contactor K2 ──► Motor
                    │
                    └──► K2 NC auxiliary contact ──► Safety Logic feedback input
```

**How it works:**
- After a stop command, the safety logic reads the NC auxiliary contacts of both contactors
- If a contactor welds (fails to open), its NC contact does not close → the safety logic detects the fault
- On next start command, the safety logic refuses to re-energize the circuit until the fault is cleared

**EDM provides DC = 99% for the output subsystem when properly implemented.** Without EDM, a welded contactor is an undetected dangerous failure, and DC for the output subsystem drops to 0%.

**EDM is not optional for Category 3 and 4 output subsystems. It is the primary mechanism that provides the diagnostic coverage required to achieve PLd and PLe.**

### 5.6 Score Common Cause Failure (CCF)

CCF analysis is required for:
- ISO 13849-1: Category 2, 3, and 4
- IEC 62061: All redundant architectures (1oo2, 1oo2D, 2oo3)
- IEC 61511: All redundant architectures

#### ISO 13849-1 CCF Scoring (Annex F)

| # | Measure | Score |
|---|---------|-------|
| 1 | **Separation / segregation** — physical separation of signal paths (routing, conduit, spacing) | 15 |
| 2 | **Diversity** — different technologies, different manufacturers, different physical principles | 20 |
| 3 | **Design / application / experience** — protection against overvoltage, overpressure, contamination, EMC per applicable standards | 20 |
| 4 | **Assessment / analysis** — documented CCF analysis performed during design | 5 |
| 5 | **Competence / training** — designers and maintainers are trained and competent | 5 |
| 6 | **Environmental** — protection against contamination, temperature, shock, humidity per manufacturer specifications | 25 |
| 7 | **Other influences** — immunity to common mode failures not covered above | 10 |

**Maximum possible score: 100**

**Minimum required score: 65 points**

**If the CCF score is below 65, the redundant architecture cannot claim the fault tolerance benefit of dual-channel design. The architecture effectively degrades to single-channel behavior.**

#### CCF Practical Implementation Measures

| CCF Measure | Practical Actions |
|-------------|------------------|
| **Separation** | Route redundant channel wiring in separate conduits or cable trays; physically separate redundant sensors on different mounting points; use separate power supplies for redundant channels where practical |
| **Diversity** | Use different sensor technologies for redundant inputs (e.g., one mechanical switch + one inductive sensor); use contactors from different manufacturers for redundant output paths; or justify same-type components with other high-scoring measures |
| **Design protection** | Apply surge protection, EMC filtering per IEC 61326, proper cable shielding and grounding; select components rated for the environment; follow manufacturer installation instructions |
| **Environmental** | Install in appropriate enclosure (IP rating), maintain temperature within component ratings, protect from vibration and shock, prevent contamination ingress |

### 5.7 Perform PL Calculation (ISO 13849-1 Pathway)

The PL calculation combines Category, MTTFd, DC, and CCF:

```
For each safety function:

1. Decompose into subsystems (Input, Logic, Output)

2. For each subsystem:
   a. Determine Category
   b. Calculate MTTFd (from B10d and nop, or from manufacturer data)
   c. Estimate DC (per Annex E)
   d. Score CCF (per Annex F) — must be ≥ 65

3. For the overall safety function:
   a. Combine subsystem PFHd values:
      PFHd_total = PFHd_SB1 + PFHd_SB2 + PFHd_SB3

   b. Map PFHd_total to PL:
      PL a: 10⁻⁵ ≤ PFHd < 10⁻⁴
      PL b: 3×10⁻⁶ ≤ PFHd < 10⁻⁵
      PL c: 10⁻⁶ ≤ PFHd < 3×10⁻⁶
      PL d: 10⁻⁷ ≤ PFHd < 10⁻⁶
      PL e: 10⁻⁸ ≤ PFHd < 10⁻⁷

   c. Verify: Achieved PL ≥ Required PLr

4. If achieved PL < PLr:
   → Upgrade components (higher MTTFd)
   → Upgrade architecture (higher Category)
   → Increase diagnostics (higher DC)
   → Iterate until PLr is met
```

#### PL Achievability Matrix (ISO 13849-1 Figure 5)

| Category | MTTFd per Channel | DC | Achievable PL |
|----------|-------------------|-----|---------------|
| B | Low | None | a |
| B | Medium | None | b |
| 1 | High | None | c |
| 2 | Low–Medium | Low | a–b |
| 2 | Medium | Medium | b–c |
| 2 | High | Medium | c–d |
| 3 | Low | Low | c |
| 3 | Medium | Low | c–d |
| 3 | High | Low | d |
| 3 | High | Medium | d |
| 4 | High | High | e |

### 5.8 Perform SIL Verification (IEC 62061 / IEC 61511 Pathway)

```
For each safety function:

1. Decompose into subsystems (Input, Logic, Output)

2. For each subsystem:
   a. Determine architecture (1oo1, 1oo1D, 1oo2, 1oo2D)
   b. Determine component failure rates (λd) or PFHd from manufacturer
   c. Determine DC
   d. Verify architectural constraints (HFT vs SFF per IEC 61508 tables)
   e. Calculate subsystem PFHd

3. For the overall safety function:
   a. Sum subsystem PFHd values:
      PFHd_total = PFHd_SB1 + PFHd_SB2 + PFHd_SB3

   b. Verify: PFHd_total meets SIL target:
      SIL 1: 10⁻⁶ ≤ PFHd < 10⁻⁵
      SIL 2: 10⁻⁷ ≤ PFHd < 10⁻⁶
      SIL 3: 10⁻⁸ ≤ PFHd < 10⁻⁷

   c. Verify: Architectural constraints are satisfied for each subsystem
   d. Verify: Systematic capability (SC) ≥ SIL target for complex subsystems

4. For IEC 61511 (process safety):
   a. Also calculate PFDavg (Probability of Failure on Demand — average)
      for low-demand mode applications:
      SIL 1: 10⁻² ≤ PFDavg < 10⁻¹
      SIL 2: 10⁻³ ≤ PFDavg < 10⁻²
      SIL 3: 10⁻⁴ ≤ PFDavg < 10⁻³
      SIL 4: 10⁻⁵ ≤ PFDavg < 10⁻⁴

   b. Proof test interval directly affects PFDavg —
      longer intervals = higher PFDavg = harder to meet SIL target
```

### 5.9 Verify Response Time Budget

The architecture must meet the response time requirement defined for each safety function in Stage 3. The total response time is the sum of all subsystem response times:

```
t_total = t_sensor + t_logic + t_actuator + t_mechanical

Where:
  t_sensor      = sensor response time (from manufacturer data)
  t_logic       = logic solver response/scan time (from manufacturer data or configuration)
  t_actuator    = actuator response time (from manufacturer data)
  t_mechanical  = mechanical stopping/braking time (from measurement or calculation)
```

**The total response time feeds directly into the safety distance calculation (ISO 13855):**

```
S = (K × T) + C

Where:
  S = minimum safety distance
  K = approach speed (1600mm/s for hand/arm, 2000mm/s for walking per ISO 13855)
  T = total response time of the safety system (t_total)
  C = supplementary distance (intrusion distance, depth penetration factor)
```

**If the total response time exceeds what is allowable for the available mounting distance, either:**
- Select faster components (lower t_sensor, t_logic, t_actuator)
- Move the safety device further from the hazard zone (if space permits)
- Reduce the mechanical stopping time (faster brakes, lower inertia)
- Redesign the safety function approach

### 5.10 Address Systematic Failures

Architectural measures address **random hardware failures**. Systematic failures (design errors, specification errors, manufacturing defects, software bugs) must be addressed separately:

| Systematic Failure Source | Measures |
|--------------------------|---------|
| **Specification errors** | Traceability from risk assessment → SRS → architecture → design → test (the lifecycle itself is the measure) |
| **Hardware design errors** | Use of well-tried components and well-tried safety principles per ISO 13849-2; use of proven-in-use components per IEC 62061; design reviews |
| **Software errors** | Addressed in Stage 4.5 (Safety Software) — limited variability language (LVL), software safety requirements, independent verification |
| **Installation errors** | Addressed in Stage 5 (wiring practices), Stage 7 (build), and Stage 8 (installation) — color coding, labeling, termination standards |
| **Maintenance errors** | Addressed in Stage 11 — clear maintenance instructions, proof test procedures, competency requirements |
| **Modification errors** | Addressed in Stage 12 (MOC) — structured change management prevents ad hoc modifications |

### 5.11 Document Architecture Decisions for Each Safety Function

For each safety function, the architecture documentation must include:

| Element | Content |
|---------|---------|
| SF-ID and description | From safety function register |
| Required PLr / SIL | From Stage 3 |
| Subsystem decomposition | Block diagram showing Input → Logic → Output with component identification |
| Architecture category per subsystem | Category (ISO 13849-1) or architecture designation (IEC 62061) |
| Component list per subsystem | Part number, manufacturer, safety data reference |
| MTTFd or λd per subsystem | Value, source, calculation if derived from B10d |
| DC per subsystem | Value, diagnostic measure, justification per Annex E/C |
| CCF score | Score per Annex F with individual measure scores |
| PFHd per subsystem | Calculated value |
| PFHd total | Sum of all subsystem PFHd values |
| Achieved PL / SIL | Result of calculation |
| Verification: Achieved ≥ Required | Pass / Fail |
| Response time per subsystem | Value from manufacturer data |
| Total response time | Sum of all subsystem response times |
| Response time vs requirement | Pass / Fail |
| Architectural constraints check | HFT vs SFF (IEC 62061 path) — Pass / Fail |
| Systematic capability check | SC ≥ SIL (IEC 62061 path) — Pass / Fail |
| Fault exclusions applied | List of any fault exclusions with justification per ISO 13849-2 |

---

## 6. Fault Exclusion

Fault exclusion is the documented engineering judgment that a specific fault is so improbable that it need not be considered in the architecture design. It is permitted under specific conditions but must be rigorously justified.

### When Fault Exclusion Is Permitted

| Standard | Conditions |
|----------|-----------|
| **ISO 13849-1 §7.3** | Fault exclusion may be applied if the fault is technically improbable considering the component's construction, application, and experience |
| **ISO 13849-2** | Provides specific fault lists and fault exclusion tables for electrical, pneumatic, hydraulic, and mechanical technologies |
| **IEC 62061 §6.5** | Fault exclusion may be applied with documented justification |
| **IEC 61511** | Fault exclusion is generally not permitted for SIS — all credible failure modes must be considered |

### Common Fault Exclusions and Their Justification

| Fault Excluded | Justification Basis | Conditions |
|---------------|-------------------|-----------|
| Short circuit between conductors of a coded safety switch | ISO 14119 coding level — high-coded actuators have unique mechanical coding that prevents activation by other actuators or simple tools | Actuator is coded type per ISO 14119 §7; wiring follows manufacturer instructions |
| Mechanical failure of a guard interlock actuator | Well-tried mechanical construction per ISO 13849-2 Table D.6 | Metal actuator, positive-mode operation, within rated load |
| Short circuit between conductors of different channels | Physical separation of wiring per installation requirements | Redundant channels in separate conduits, separated by ≥ specified distance |
| Contactor contacts welding simultaneously in both channels | Redundant contactors from different manufacturers or different types; EDM detects single welding | Diversity of contactors; EDM implemented; proper utilization category rating |

**Every fault exclusion must be documented with:**
- The specific fault being excluded
- The technical basis for exclusion (reference to ISO 13849-2 fault tables, manufacturer data, or engineering analysis)
- The conditions that must remain true for the exclusion to be valid (installation requirements, maintenance requirements)
- Who approved the fault exclusion

**If a fault exclusion condition is violated (e.g., someone routes both channels in the same conduit), the architecture is invalid.**

---

## 7. Key Deliverables

| # | Deliverable | Description |
|---|------------|-------------|
| 1 | **Safety architecture document** | Complete record of architecture decisions, calculations, and verification results for every safety function |
| 2 | **Safety function register (finalized)** | Updated register from Stage 3 with architecture category, component identification, and achieved PL/SIL added per function |
| 3 | **Subsystem block diagrams** | For each safety function: visual diagram showing Input → Logic → Output with component identification, channel architecture, and diagnostic paths |
| 4 | **PL/SIL calculation reports** | SISTEMA project files, SILver calculation files, or manual calculation worksheets for each safety function |
| 5 | **Component safety data register** | Compilation of manufacturer safety data sheets for every safety-rated component, with MTTFd, B10d, PFHd, SFF, and failure mode data |
| 6 | **CCF scoring worksheets** | Completed Annex F (ISO 13849-1) or Annex F (IEC 62061) scoring for each safety function requiring CCF analysis |
| 7 | **DC justification record** | For each subsystem: the DC value claimed, the diagnostic measure providing it, and the justification per Annex E/C |
| 8 | **Fault exclusion register** | List of all fault exclusions applied, with technical basis, conditions, and approval |
| 9 | **Response time analysis** | For each safety function: subsystem response times, total response time, comparison to requirement, and safety distance calculation (if applicable) |
| 10 | **Architectural constraints verification** | For IEC 62061 path: HFT vs SFF check for each subsystem; systematic capability check for complex subsystems |
| 11 | **Verification summary matrix** | Single table showing every safety function with: required PLr/SIL, achieved PL/SIL, pass/fail, response time pass/fail, CCF pass/fail |
| 12 | **Updated assumptions register** | Any assumptions made during architecture design (e.g., assumed operating rates for B10d calculations, assumed environmental conditions) |

### Verification Summary Matrix Template

| SF-ID | Safety Function | Required PLr/SIL | Architecture Category | Achieved PL/SIL | PFHd Total | PLr/SIL Met? | Response Time Required | Response Time Achieved | Response Time Met? | CCF Score | CCF Met (≥65)? | Arch. Constraints Met? | Status |
|-------|----------------|------------------|----------------------|-----------------|-----------|-------------|----------------------|----------------------|-------------------|-----------|---------------|----------------------|--------|
| SF-01 | Guard interlock — operator door | PLd | Cat. 3 | PLd | 4.2 × 10⁻⁸ | ✓ PASS | ≤200ms | 145ms | ✓ PASS | 75 | ✓ PASS | N/A (PL path) | COMPLETE |
| SF-02 | E-stop — operator station | PLd | Cat. 3 | PLd | 3.8 × 10⁻⁸ | ✓ PASS | ≤500ms | 310ms | ✓ PASS | 80 | ✓ PASS | N/A (PL path) | COMPLETE |
| SF-03 | Light curtain — infeed | PLe | Cat. 4 | PLe | 8.1 × 10⁻⁹ | ✓ PASS | ≤150ms | 92ms | ✓ PASS | 85 | ✓ PASS | N/A (PL path) | COMPLETE |
| SF-05 | SIS — high pressure trip | SIL 2 | 1oo2 | SIL 2 | 2.3 × 10⁻⁷ | ✓ PASS | ≤2s | 1.2s | ✓ PASS | N/A | N/A | ✓ PASS (HFT, SFF, SC) | COMPLETE |

---

## 8. Exit Criteria — Gate Review

This stage is complete when **all** of the following are true:

| # | Criterion | Evidence |
|---|-----------|----------|
| 1 | Every safety function has a defined architecture (category or HFT) with subsystem decomposition | Subsystem block diagrams for all safety functions |
| 2 | Every safety-rated component has manufacturer safety data documented | Component safety data register complete |
| 3 | PL or SIL calculation is complete for every safety function | SISTEMA files, SILver files, or manual calculation worksheets |
| 4 | Achieved PL ≥ PLr (or achieved SIL ≥ target SIL) for every safety function | Verification summary matrix — all pass |
| 5 | CCF score ≥ 65 for all safety functions requiring CCF analysis | Completed CCF worksheets |
| 6 | DC values are justified per Annex E/C with specific diagnostic measures identified | DC justification record |
| 7 | Response time analysis is complete and all safety functions meet their response time requirements | Response time analysis — all pass |
| 8 | All fault exclusions are documented with technical basis and conditions | Fault exclusion register |
| 9 | For IEC 62061/61508 path: architectural constraints (HFT vs SFF) are verified for every subsystem | Architectural constraints verification |
| 10 | For IEC 62061/61508 path: systematic capability (SC) ≥ SIL for all complex subsystems | SC verification record |
| 11 | Safety architecture document is reviewed by at least one person who did not author it | Review record (signature, date, comments resolved) |
| 12 | Safety function register is updated with architecture, components, and achieved PL/SIL | Updated safety function register |
| 13 | All assumptions are documented with owners and resolution dates | Updated assumptions register |

**If any safety function does not achieve its required PLr/SIL, the design must iterate before proceeding to Stage 5 (Detailed Design). Do not proceed with a known shortfall expecting to "fix it later."**

---

## 9. Roles and Responsibilities at This Stage

| Role | Responsibility |
|------|---------------|
| **Safety / Controls Engineer** | Owns this stage — performs subsystem decomposition, selects architecture, selects components, performs PL/SIL calculations, scores CCF, documents all results |
| **Electrical / Controls Designer** | Supports component selection with practical knowledge of available products, installation constraints, and wiring practices; validates that the architecture can be physically implemented |
| **Mechanical / Process Engineer** | Provides mechanical stopping time data, inertia calculations, pneumatic/hydraulic response times for response time analysis; validates that mechanical safety measures (guards, barriers) are compatible with the architecture |
| **Project Manager** | Monitors architecture completion against schedule; understands that architecture iteration (if PLr/SIL is not met) may affect project timeline and BOM cost |
| **Procurement** | Begins sourcing safety-rated components identified in this stage; confirms lead times for specialized safety components |
| **Independent Reviewer** | Reviews calculation methodology, parameter selections, and fault exclusions — should not be the same person who performed the calculations |

---

## 10. Common Mistakes at This Stage

| Mistake | Consequence | How to Avoid |
|---------|-------------|-------------|
| Using generic component data instead of manufacturer safety data | Calculation may use incorrect MTTFd or B10d values; achieved PL/SIL may be wrong | Always request the manufacturer's safety data sheet (not the general data sheet) — contact the manufacturer if not published |
| Forgetting to include all subsystems in the PFHd sum | If the output subsystem (contactors) is not included in the calculation, PFHd is understated and PL/SIL may be overstated | Systematically decompose into Input + Logic + Output; verify all subsystems are in the SISTEMA project or SIL calculation |
| Claiming high DC without implementing the diagnostic measure | DC = 99% claimed for contactor monitoring but EDM wiring is not in the design — the claimed PL is not achieved | For every DC value claimed, identify the specific physical diagnostic measure and verify it appears in the circuit design in Stage 5 |
| CCF score below 65 with no corrective action | Redundant architecture does not provide the claimed fault tolerance; achieved PL is lower than calculated | Score CCF early in the architecture stage; if below 65, implement additional measures (separation, diversity, environmental protection) before finalizing |
| Not capping MTTFd at 2500 years per channel | ISO 13849-1 §C.2 limits MTTFd per channel to 2500 years; exceeding this does not improve the PL | Apply the cap in all calculations |
| Applying fault exclusion without justification | Auditor rejects the fault exclusion; architecture must be recalculated without it, potentially reducing the achieved PL/SIL | Document every fault exclusion with reference to ISO 13849-2 fault tables and the specific conditions that justify it |
| Ignoring the difference between Category 3 and Category 4 | Category 4 requires that accumulation of undetected faults does not cause loss of safety function — this requires high DC (≥99%) on all subsystems, not just the output | If targeting PLe, verify DC ≥ 99% on every subsystem, not just overall |
| Using a safety PLC without checking its PFHd contribution | Safety PLCs have non-zero PFHd that must be included in the total; some safety PLCs consume a significant portion of the PFHd budget | Include the safety PLC PFHd per safety function (from manufacturer data) in the total calculation |
| Not verifying response time | Architecture achieves PLd but total response time exceeds what the safety distance allows — the safety device must be moved or the architecture is functionally inadequate | Always perform response time analysis alongside PL/SIL calculation |
| Mixing PL and SIL within a single safety function | Not permitted — one function, one methodology | Use the pathway selected in Stage 2 consistently for each safety function |
| Not considering demand rate for B10d components | A contactor that cycles 100 times/day has a very different MTTFd than one that cycles 10,000 times/day | Calculate nop accurately for each application; document the assumptions |

---

## 11. Relationship to Adjacent Stages

```
┌──────────────────────────────────────┐
│  STAGE 3: RISK ASSESSMENT             │
│  ★ PL/SIL DECISION POINT ★           │
│                                      │
│  Provides:                           │
│  • Safety function register          │
│  • PLr/SIL targets per function      │
│  • Safe state, response time req.    │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  STAGE 3.5: SRS (if implemented)      │
│                                      │
│  Formalizes safety function specs    │
│  into verifiable requirements        │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  STAGE 4: SAFETY ARCHITECTURE         │  ◄── You are here
│  ★ CONFIRM PL / SIL ★               │
│                                      │
│  Produces:                           │
│  • Architecture document             │
│  • Subsystem block diagrams          │
│  • PL/SIL calculations              │
│  • Component selections              │
│  • CCF/DC analysis                   │
│  • Response time analysis            │
│  • Fault exclusion register          │
│  • Verification summary matrix       │
└──────────────────┬───────────────────┘
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
┌────────────────┐   ┌─────────────────┐
│ STAGE 4.5:     │   │ STAGE 5:        │
│ SAFETY SOFTWARE│   │ DETAILED DESIGN │
│                │   │                 │
│ Uses:          │   │ Uses:           │
│ • Architecture │   │ • Architecture  │
│   to define    │   │   to create     │
│   software     │   │   circuit       │
│   safety req.  │   │   diagrams, BOM │
│ • Logic solver │   │ • Component     │
│   selection    │   │   selections    │
│   determines   │   │   for BOM       │
│   programming  │   │ • DC measures   │
│   requirements │   │   (EDM) for     │
│                │   │   wiring design │
└────────────────┘   └─────────────────┘
        │                     │
        └──────────┬──────────┘
                   ▼
┌──────────────────────────────────────┐
│  STAGE 9/10: PRE-COMM / COMMISSIONING│
│                                      │
│  V&V verifies:                       │
│  • Architecture is built as designed │
│  • Diagnostics function as claimed   │
│  • Response times meet requirements  │
│  • Safety functions achieve safe     │
│    state as specified                │
│                                      │
│  ★ Traceability: Architecture doc   │
│    is the reference for test plans ★│
└──────────────────────────────────────┘
```

---

## 12. Templates and Tools

| Resource | Purpose |
|----------|---------|
| **SISTEMA** (free — IFA/DGUV) | ISO 13849-1 PL calculation software — models subsystems, categories, MTTFd, DC, CCF, and calculates achieved PL. Industry-standard tool. |
| **SISTEMA Libraries** | Pre-built component libraries from major safety component manufacturers (Pilz, Sick, Banner, Allen-Bradley, Siemens, Schmersal, etc.) — import directly into SISTEMA |
| **SILver** (exida) | IEC 62061 / IEC 61508 SIL verification software |
| **exSILentia** (exida) | IEC 61511 SIL verification and LOPA tool for process safety |
| Subsystem block diagram template | Visio/CAD template showing Input → Logic → Output with fields for component ID, architecture, MTTFd, DC |
| Verification summary matrix template | Spreadsheet per Section 7 matrix |
| CCF scoring worksheet template | Fillable form per ISO 13849-1 Annex F |
| DC justification worksheet template | Table per subsystem with diagnostic measure, DC value, and Annex E/C reference |
| Fault exclusion register template | Table with fault, basis, conditions, and approval fields |
| Response time analysis worksheet | Spreadsheet for summing subsystem response times and calculating safety distances |
| Component safety data request template | Standard letter/email to manufacturers requesting MTTFd, B10d, PFHd, SFF data for specific part numbers |

---

← [Safety Requirements Specification]({{ '/lifecycle/safety-requirements-spec/' | relative_url }}) | [Detailed Design]({{ '/lifecycle/detailed-design/' | relative_url }}) →
