---
layout: default
title: "Lifecycle Stage 3 — Risk Assessment"
description: "Systematic hazard identification and risk estimation — the critical gate where PLr or SIL targets are assigned to each safety function."
breadcrumb:
  - name: "Lifecycle"
    url: "/lifecycle/"
  - name: "3. Risk Assessment"
related_standards:
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
---

<div class="page-header">
  <span class="page-header__label">Lifecycle Stage 03</span>
  <h1>Risk Assessment</h1>
  <strong>PL/SIL Decision Point</strong>
</div>

## 1. Purpose of This Stage

This is the most consequential stage in the safety engineering lifecycle. Every design decision, component selection, architecture choice, and verification test downstream traces back to what is determined here. This stage answers three questions:

- **What can hurt someone?** (Hazard identification)
- **How bad can it get, and how likely is it?** (Risk estimation and evaluation)
- **How much risk reduction does each safety function need to provide?** (PLr or SIL assignment)

If hazards are missed here, they will not be designed against. If risk is underestimated, the safety architecture will be inadequate. If risk is overestimated, the project will carry unnecessary cost and complexity. There is no later stage that compensates for errors made here — Stage 10 (Commissioning) verifies what was designed, it does not discover what should have been designed.

This is the **PL/SIL decision point**. The required Performance Level (PLr) or Safety Integrity Level (SIL) for each safety function is assigned here, based on the risk assessment outcome and the pathway selected in Stage 2. This assignment drives everything in Stages 4 through 10.

> **This stage answers: What are the hazards, how much risk reduction is required, and what safety functions must exist to provide it?**

---

## 2. Entry Criteria

This stage begins when **Stage 2 (Standards Selection) exit criteria are met**.

### Required Inputs

| Input | Source (Stage) | Why It Matters |
|-------|---------------|----------------|
| System description | Stage 1 | Defines what the machine does — without this, hazard identification has no context |
| Machine / system boundary definition | Stage 1 | Defines what is inside scope — hazards outside the boundary are not assessed (or are assessed separately) |
| Intended use and foreseeable misuse statement | Stage 1 | Directly drives hazard identification — misuse scenarios are a primary source of hazards |
| Operating mode definitions | Stage 1 | Hazards differ by mode — a machine may be safe in automatic but hazardous during setup or maintenance |
| Preliminary hazard category scan | Stage 1 | Starting checklist to ensure no hazard category is overlooked |
| Standards register | Stage 2 | Determines which risk assessment methodology applies and which type-C standards impose specific hazard requirements |
| PL vs SIL pathway selection | Stage 2 | Determines whether PLr (ISO 13849-1 risk graph) or SIL (IEC 62061 / IEC 61511 method) is used to assign targets |
| Type-C standard applicability determination | Stage 2 | Type-C standards may define specific hazards, pre-defined safety measures, or modified risk assessment requirements for the machine type |
| Risk assessment team identification | Stage 1 | The right people must be in the room |

**If the boundary definition or intended use statement is incomplete, the risk assessment will have gaps. Do not proceed until Stage 1 deliverables are confirmed.**

---

## 3. Standards Influence

| Standard | Role at This Stage |
|----------|-------------------|
| **ISO 12100:2010 §5, §6, Annex A, Annex B** | Defines the complete risk assessment methodology: determination of limits, hazard identification, risk estimation, risk evaluation, and risk reduction strategy (three-step method). This is the foundational standard for this stage. |
| **ISO 13849-1:2023 §4, Annex A** | Provides the risk graph method for assigning required Performance Level (PLr) to each safety function — parameters S, F, P |
| **IEC 62061:2021 §5, Annex A** | Provides the SIL assignment method (SILCL determination) for machinery applications — parameters Se, Fr, Pr, Av |
| **IEC 61511-1:2016 §8, §9** | Provides HAZOP methodology for hazard identification and LOPA (Layer of Protection Analysis) for SIL assignment in process safety applications |
| **IEC 61508-5:2010** | Provides alternative SIL determination methods (risk graph, hazardous event severity matrix, quantitative method) — used when IEC 62061 or IEC 61511 are not applicable |
| **Applicable type-C standards** | May define specific hazards that must be assessed, pre-defined risk levels, or mandatory safety measures that bypass the risk graph (e.g., ISO 10218-2 defines specific hazards for robotic cells; ISO 16092 defines specific hazards for presses) |
| **ANSI B11.0** | US machinery risk assessment methodology — largely harmonized with ISO 12100 but with some differences in risk scoring approach. Required if ANSI B11 series is in the standards register. |
| **ISO/TR 14121-2:2012** | Technical report providing practical guidance and examples for the ISO 12100 risk assessment process — not normative but highly useful as a reference |

---

## 4. The Three-Step Risk Reduction Strategy (ISO 12100 §6)

Before identifying hazards and assigning safety functions, the team must understand the hierarchy of risk reduction that governs all decisions:

```
┌──────────────────────────────────────────────────────────┐
│  STEP 1: Inherently Safe Design (§6.2)                    │
│                                                          │
│  Eliminate the hazard or reduce risk by design choices:  │
│  • Eliminate pinch points by geometry change             │
│  • Reduce force/speed/energy to non-hazardous levels    │
│  • Substitute hazardous materials                        │
│  • Apply ergonomic principles                            │
│                                                          │
│  ★ This step is ALWAYS considered first ★               │
│  ★ Before any guard or safety function is applied ★     │
└──────────────────────────┬───────────────────────────────┘
                           │ If residual risk remains
                           ▼
┌──────────────────────────────────────────────────────────┐
│  STEP 2: Safeguarding and Protective Measures (§6.3)      │
│                                                          │
│  Apply guards and safety functions:                      │
│  • Fixed guards (ISO 14120)                              │
│  • Interlocked guards (ISO 14119)                        │
│  • Safety devices (light curtains, mats, two-hand)      │
│  • Safety-related control functions (e-stop, STO, etc.) │
│                                                          │
│  ★ Safety functions assigned here get PLr/SIL targets ★ │
└──────────────────────────┬───────────────────────────────┘
                           │ If residual risk remains
                           ▼
┌──────────────────────────────────────────────────────────┐
│  STEP 3: Information for Use (§6.4)                       │
│                                                          │
│  Warnings, signs, training, PPE instructions:            │
│  • Warning labels and signs                              │
│  • Operating manuals and safety instructions             │
│  • Training requirements                                 │
│  • PPE specifications                                    │
│                                                          │
│  ★ This step alone is NEVER sufficient for high risk ★  │
│  ★ It supplements Steps 1 and 2 — does not replace ★   │
└──────────────────────────────────────────────────────────┘
```

**Every hazard identified in this stage must be evaluated against all three steps in order.** The risk assessment must document what inherently safe design measures were considered (Step 1) before assigning safety functions (Step 2). Auditors specifically look for evidence that Step 1 was not skipped.

---

## 5. Engineering Activities

### 5.1 Assemble the Risk Assessment Team

The risk assessment is a **team activity**, not a solo exercise. Per ISO 12100 and good practice, the team should include:

| Role | Contribution |
|------|-------------|
| Safety / controls engineer | Facilitates the process, understands standards methodology, documents results |
| Mechanical / process engineer | Knows the physical hazards — forces, energies, materials, failure modes |
| Machine operator or operator representative | Knows actual use patterns, workarounds, and misuse scenarios that engineers may not anticipate |
| Maintenance technician or representative | Knows access requirements, common interventions, and what goes wrong in the field |
| Customer safety representative (if available) | Knows site-specific risks, local requirements, and organizational risk tolerance |
| Project manager (observer) | Understands scope and schedule implications of risk assessment findings |

**Minimum team size: 3 people with different perspectives. A risk assessment performed by one person is inherently limited and may not satisfy audit requirements.**

### 5.2 Determine Machine Limits (Confirm Stage 1)

Before identifying hazards, confirm that the machine limits defined in Stage 1 are still accurate and complete:

| Limit Category | Confirm |
|---------------|---------|
| Use limits | Intended use, foreseeable misuse, operator populations, skill levels |
| Space limits | Physical boundary, operator access positions, reach zones, adjacent equipment interfaces |
| Time limits | Machine life, component life, duty cycle |
| Other limits | Environmental conditions, materials processed, energy sources |

**If limits have changed since Stage 1, update the Stage 1 deliverables before proceeding.**

### 5.3 Identify Hazards — Systematic Process

This is the most critical activity. Missing a hazard here means it will not be assessed, not be designed against, and not be verified.

#### Method Selection

| Method | When to Use | Standard Reference |
|--------|------------|-------------------|
| **Checklist against ISO 12100 Annex B** | Always — baseline for every machine | ISO 12100 Annex B |
| **Task-based analysis** | When operator interaction is significant — walk through every task an operator or maintainer performs | ISO 12100 §5.4 |
| **Zone-based analysis** | When the machine has distinct physical zones with different hazard profiles | ISO 12100 §5.4, ISO 11161 (for integrated systems) |
| **Mode-based analysis** | When hazards differ significantly between operating modes (automatic, setup, maintenance) | ISO 12100 §5.2 |
| **HAZOP** | For process safety applications — systematic deviation analysis of process parameters | IEC 61511-1 §8 |
| **What-if analysis** | Supplementary method — brainstorming "what if" scenarios | General practice |
| **Failure mode analysis** | When control system failures can create hazards | ISO 13849-1, IEC 62061 |
| **Energy-based analysis** | Identify all energy sources (electrical, pneumatic, hydraulic, gravitational, kinetic, thermal, chemical) and trace their hazardous release paths | OSHA LOTO (29 CFR 1910.147), ISO 12100 Annex B |

**Recommended approach for most machinery projects:**

Use a **combined task-based and zone-based approach** with the **ISO 12100 Annex B checklist** as a verification layer:

1. Divide the machine into physical zones per the boundary definition
2. For each zone, walk through every task performed by every user group in every operating mode
3. For each task-zone-mode combination, identify hazards using the Annex B categories
4. Cross-check the complete hazard list against Annex B to confirm no category was missed

#### Hazard Identification Checklist (ISO 12100 Annex B — Expanded)

| # | Hazard Category | Specific Hazards to Consider | Typical Sources |
|---|----------------|------------------------------|-----------------|
| 1 | **Mechanical** | Crushing, shearing, cutting/severing, entanglement, drawing-in/trapping, impact, stabbing/puncture, friction/abrasion, high-pressure fluid injection/ejection | Moving parts, closing dies, rotating shafts, conveyors, robots, hydraulic lines |
| 2 | **Electrical** | Direct contact with live parts, indirect contact (fault to ground), electrostatic phenomena, thermal radiation/short circuit, arc flash | Control panels, motor terminals, bus bars, high-voltage supplies, capacitor banks |
| 3 | **Thermal** | Burns from hot surfaces, scalds from steam/fluid, frostbite from cryogenics, heat stress from environment | Ovens, heaters, molten material, cryogenic systems, steam lines |
| 4 | **Noise** | Hearing damage from continuous exposure, startle response from impulse noise | Pneumatic exhausts, impacts, motors, gearboxes, material handling |
| 5 | **Vibration** | Whole-body vibration, hand-arm vibration | Vibrating feeders, impact tools, mobile equipment |
| 6 | **Radiation** | Ionizing (X-ray), non-ionizing (UV, IR, RF), laser | Welding, inspection systems, RF heaters, laser processing |
| 7 | **Material / substance** | Contact with or inhalation of chemicals, biological agents, dust, fume | Chemicals processed, welding fume, wood dust, oil mist |
| 8 | **Ergonomic** | Awkward posture, repetitive motion, excessive force, poor visibility, mental overload | Manual loading/unloading, control placement, display design |
| 9 | **Environmental** | Slip/trip/fall, oxygen deficiency/enrichment, fire, explosion | Floor conditions, confined spaces, flammable materials, dust accumulation |
| 10 | **Combination / associated** | Unexpected startup, failure to stop, overspeed, loss of stability (tip-over), ejection of parts/fluid, gravity fall of suspended load, loss of vacuum/pressure holding a load | Control system failure, energy storage release, pneumatic/hydraulic failure |
| 11 | **Hazards during specific life phases** | Transport, assembly/installation, commissioning, setting/teaching, process changeover, cleaning, fault-finding, maintenance, dismantling/disposal | All phases per ISO 12100 §5.4 |

### 5.4 Estimate Risk — For Each Identified Hazard

For each hazard, estimate risk using the parameters defined by the applicable standard:

#### ISO 12100 Risk Estimation (General)

| Parameter | Definition | Considerations |
|-----------|-----------|----------------|
| **Severity of harm (S)** | How bad is the worst credible outcome? | Reversible injury, irreversible injury, death |
| **Probability of occurrence of harm** | Composite of the following three factors: | |
| — Frequency and duration of exposure (F) | How often and how long is a person exposed? | Continuous, periodic, rare |
| — Probability of hazardous event (O) | How likely is the hazardous event given exposure? | Mechanical reliability, human error likelihood, environmental factors |
| — Possibility of avoiding or limiting harm (P) | Can the person detect and escape the hazard? | Speed of hazard onset, visibility, escape routes, awareness |

**Note:** The exact parameter names and scales vary between ISO 12100 (general risk estimation), ISO 13849-1 Annex A (PLr risk graph), and IEC 62061 Annex A (SIL assignment). Use the parameters from the methodology you selected in Stage 2.

#### ISO 13849-1 Risk Graph Parameters (for PLr Assignment)

```
                      Starting point
                          │
                 ┌────────┴────────┐
                 S1                S2
           (slight/reversible)  (serious/death)
                 │                 │
            ┌────┴────┐       ┌────┴────┐
            F1        F2      F1        F2
         (rare)    (frequent) (rare)  (frequent)
            │         │        │         │
          ┌─┴─┐    ┌─┴─┐   ┌─┴─┐    ┌─┴─┐
          P1  P2   P1  P2  P1  P2   P1  P2
          │   │    │   │   │   │    │   │
          a   b    b   c   b   c    c   d ← PLr
                                    d   e
```

| Parameter | Level | Description |
|-----------|-------|-------------|
| **S — Severity** | S1 | Slight (normally reversible) injury |
| | S2 | Serious (normally irreversible) injury including death |
| **F — Frequency/Duration** | F1 | Seldom-to-less-often and/or short exposure time |
| | F2 | Frequent-to-continuous and/or long exposure time |
| **P — Possibility of avoidance** | P1 | Possible under specific conditions |
| | P2 | Scarcely possible |

#### IEC 62061 SIL Assignment Parameters

| Parameter | Levels | Description |
|-----------|--------|-------------|
| **Se — Severity** | 4 | Death, loss of eye/arm |
| | 3 | Permanent, loss of fingers |
| | 2 | Reversible, medical attention |
| | 1 | Reversible, first aid |
| **Fr — Frequency of exposure** | 5 | ≥ 1/hour |
| | 4 | ≥ 1/day to < 1/hour |
| | 3 | ≥ 1/2 weeks to < 1/day |
| | 2 | ≥ 1/year to < 1/2 weeks |
| | 1 | < 1/year |
| **Pr — Probability of hazardous event** | 5 | Very high |
| | 4 | Likely |
| | 3 | Possible |
| | 2 | Rarely |
| | 1 | Negligible |
| **Av — Possibility of avoidance** | 5 | Impossible |
| | 3 | Possible |
| | 1 | Likely |

**Class (Cl) = Fr + Pr + Av**

| | Cl = 3–4 | Cl = 5–7 | Cl = 8–10 | Cl = 11–13 | Cl = 14–15 |
|---|---------|---------|----------|-----------|-----------|
| **Se = 4** | SIL 2 | SIL 2 | SIL 2 | SIL 3 | SIL 3 |
| **Se = 3** | — | SIL 1 | SIL 2 | SIL 3 | SIL 3 |
| **Se = 2** | — | — | SIL 1 | SIL 2 | SIL 2 |
| **Se = 1** | — | — | — | SIL 1 | SIL 1 |

#### IEC 61511 LOPA Method (Process Safety)

| Element | Description |
|---------|-------------|
| **Consequence** | Severity of the hazardous event if all protection layers fail |
| **Initiating event frequency** | How often the initiating cause occurs (demands/year) |
| **Protection layers (IPLs)** | Independent layers that reduce risk (BPCS, alarms, relief valves, dikes, etc.) |
| **Target mitigated event likelihood** | Tolerable frequency of the consequence, per corporate or regulatory risk criteria |
| **Required SIL** | Determined by the gap between the unmitigated event likelihood and the tolerable target after crediting all non-SIS IPLs |

**LOPA is a semi-quantitative method. Each IPL must be independent, auditable, and have a defined PFD. Do not credit IPLs that are not truly independent of the initiating event and each other.**

### 5.5 Evaluate Risk — Is the Risk Tolerable?

For each hazard, after estimation, determine:

| Question | If Yes | If No |
|----------|--------|-------|
| Is the risk already tolerable with inherently safe design only (Step 1)? | Document the inherent safe design measure. No safety function needed. Move to Step 3 (information for use) if any residual risk remains. | Proceed to Step 2 — assign safeguarding measures and safety functions. |
| After applying guards (fixed guards, barriers), is the risk tolerable? | Document the guarding measure. No safety-related control function needed for this hazard. | A safety-related control function (safety function) is required — assign PLr or SIL. |
| After applying the safety function at the assigned PLr/SIL, is the residual risk tolerable? | Document the residual risk and any Step 3 measures (warnings, training, PPE). | Increase the PLr/SIL target, add additional safety functions, or revisit inherent safe design. Iterate until tolerable. |

**Residual risk is never zero.** The goal is to reduce risk to a tolerable level, not to eliminate it. Document what residual risk remains and what Step 3 measures address it.

### 5.6 Define Safety Functions

For each hazard where a safety-related control function is required (Step 2), define the safety function:

| Element | What to Define | Example |
|---------|---------------|---------|
| **Safety function name/ID** | Unique identifier | SF-01: Guard interlock — operator access door |
| **Description** | What the function does in plain language | "When the operator access door is opened, the safety function shall remove power to the press ram drive within 200ms and prevent restart until the door is closed and a deliberate reset action is performed." |
| **Hazard reference** | Which hazard(s) this function mitigates | H-03: Crushing by press ram |
| **Triggering event** | What initiates the safety function | Door opened, light curtain interrupted, e-stop pressed |
| **Safe state** | What the machine must do when the safety function activates | Motor stopped, energy isolated, ram at top dead center, etc. |
| **Response time requirement** | Maximum allowable time from demand to safe state | 200ms (derived from safety distance calculation per ISO 13855) |
| **Required integrity level** | PLr or SIL target from the risk graph/assignment | PLr = d, or SIL 2 |
| **Reset behavior** | How the machine returns to normal after the safety function has activated | Manual reset required (per ISO 13849-1 §5.2.2), or automatic restart permitted (with justification per ISO 12100 §6.3.3.2.5) |
| **Operating modes affected** | Which modes this safety function is active in | Automatic, manual — bypassed during maintenance with LOTO |
| **Bypass/muting conditions (if any)** | Under what conditions the safety function may be bypassed | "Light curtain is muted during part ejection cycle when robot arm breaks the beam — muting conditions per IEC 62046" |

**This definition becomes the Safety Function Specification, which is the primary input to the Safety Requirements Specification (SRS) in Stage 3.5.**

### 5.7 Apply Type-C Standard Requirements

If a type-C standard applies (identified in Stage 2), check it for:

| Type-C Requirement Type | Action |
|------------------------|--------|
| **Pre-defined hazard lists** | Verify your hazard identification covers all hazards listed in the type-C standard |
| **Mandatory safety measures** | Some type-C standards mandate specific safety measures regardless of risk assessment outcome (e.g., ISO 10218-2 requires specific safeguarding for collaborative workspaces) — add these to the safety function register even if your risk assessment alone would not have required them |
| **Pre-assigned PLr or SIL** | Some type-C standards assign PLr or SIL for specific safety functions — these override your risk graph result if they are more stringent |
| **Modified risk assessment parameters** | Some type-C standards modify or constrain the risk estimation parameters for specific hazards |
| **Specific test requirements** | Some type-C standards require specific validation tests that must be planned for in Stage 10 |

### 5.8 Consider All Life Phases

Hazards must be assessed for **every phase of the machine's life**, not just normal production operation:

| Life Phase | Hazards Often Missed |
|-----------|---------------------|
| **Transport and handling** | Tip-over, dropped load, shifting center of gravity |
| **Installation and assembly** | Electrical connection errors, first energization hazards, structural instability during assembly |
| **Commissioning and startup** | Unexpected motion during first power-up, unverified safety functions, software errors |
| **Setting, teaching, programming** | Operator in hazard zone during setup, reduced speed not verified, teach pendant failure |
| **Normal operation — automatic** | Primary production hazards (usually well-assessed) |
| **Normal operation — manual/jog** | Operator closer to hazards, reduced safeguarding, hold-to-run requirements |
| **Cleaning** | Access to normally guarded zones, chemical exposure, slip hazards |
| **Fault finding and troubleshooting** | Bypassed safety functions, energized troubleshooting, unexpected restart |
| **Maintenance and repair** | LOTO failures, stored energy release, gravity fall, working at height |
| **Process changeover / tooling change** | Manual handling of heavy tooling, pinch points during die/tool change |
| **Dismantling and disposal** | Stored energy, hazardous materials, structural collapse |

---

## 6. The PL/SIL Decision — Detailed

This is the formal decision point where each safety function receives its integrity target.

### Decision Process

```
For each safety function identified in 5.6:
    │
    ├─► Was the PL pathway selected in Stage 2?
    │     │
    │     └─ YES ──► Apply ISO 13849-1 Annex A risk graph
    │                 Assign PLr (a, b, c, d, or e)
    │                 Document S, F, P values and rationale
    │
    ├─► Was the SIL pathway selected in Stage 2?
    │     │
    │     └─ YES ──► Apply IEC 62061 Annex A SIL assignment
    │                 Assign SIL (1, 2, or 3)
    │                 Document Se, Fr, Pr, Av values and rationale
    │
    ├─► Is this a process safety SIF?
    │     │
    │     └─ YES ──► Apply IEC 61511 LOPA
    │                 Assign SIL (1, 2, 3, or 4)
    │                 Document initiating event, IPL credits, target
    │
    └─► Does the applicable type-C standard pre-assign a PLr/SIL?
          │
          └─ YES ──► Use the type-C assigned value if it is
                      MORE STRINGENT than your risk graph result.
                      If your risk graph gives a higher target
                      than the type-C standard, use the higher
                      value and document the rationale.
```

### Common PLr/SIL Assignment Errors

| Error | Consequence | How to Avoid |
|-------|-------------|-------------|
| Assigning PLr/SIL to the machine instead of to individual safety functions | Different safety functions on the same machine may require different integrity levels — a blanket assignment either over-designs or under-designs | Assign PLr/SIL per safety function, not per machine |
| Underestimating severity (S1 when S2 applies) | Integrity target is too low; safety function is under-designed | If the hazard can cause serious irreversible injury or death, it is S2 — do not downgrade because it "probably won't be that bad" |
| Claiming P1 (avoidance possible) without justification | Lowers the PLr by one level; if avoidance is not actually possible, the safety function is under-designed | P1 requires specific, documentable conditions: slow onset, high visibility, proven escape route, trained personnel. If in doubt, use P2. |
| Ignoring frequency of exposure for maintenance tasks | Maintenance may be infrequent (F1) but exposure during maintenance may be long and in close proximity — the combination still creates risk | Assess the actual exposure scenario, not just the calendar frequency |
| Crediting non-independent protection layers in LOPA | Overstates risk reduction; SIL target is too low | Each IPL must be independent of the initiating event and all other IPLs. BPCS cannot be credited as an IPL if BPCS failure is the initiating event. |
| Not iterating after applying risk reduction | Risk assessment shows high risk, safety function is assigned, but no one checks whether the residual risk is now tolerable | After assigning every safety function, re-evaluate the residual risk. Document that the residual risk is tolerable with the assigned measures in place. |

---

## 7. Key Deliverables

| # | Deliverable | Description |
|---|------------|-------------|
| 1 | **Risk assessment report** | Complete documented record of the risk assessment process, including all inputs, participants, methods, hazard identification, risk estimation, risk evaluation, risk reduction decisions, and residual risk |
| 2 | **Hazard identification register** | Systematic list of all identified hazards, organized by zone, task, mode, and life phase, with reference to ISO 12100 Annex B categories |
| 3 | **Risk estimation and evaluation records** | For each hazard: severity, frequency, probability, avoidance parameters with rationale; risk level before and after risk reduction measures |
| 4 | **Safety function register** | List of all safety functions with the specification elements defined in Section 5.6 — this is the primary input to the SRS (Stage 3.5) |
| 5 | **PLr/SIL assignment record** | For each safety function: the assigned PLr or SIL with the risk graph/assignment parameters and rationale documented |
| 6 | **Three-step method documentation** | For each hazard: evidence that inherently safe design (Step 1) was considered before safeguarding (Step 2) and information for use (Step 3) |
| 7 | **Residual risk register** | Documentation of residual risk remaining after all three steps, with assessment that it is tolerable |
| 8 | **Type-C standard cross-check record** | If a type-C standard applies: evidence that all type-C hazards were assessed and type-C mandatory measures were included |
| 9 | **Updated assumptions register** | Any new assumptions identified during risk assessment, with owner and resolution date |

### Safety Function Register — Template

This is the most important output of this stage. It bridges the risk assessment to the safety architecture.

| SF-ID | Safety Function Name | Description | Hazard Ref | Triggering Event | Safe State | Response Time | Required PLr / SIL | Risk Graph Parameters | Reset Behavior | Active Modes | Bypass/Muting Conditions | Type-C Mandate? | Notes |
|-------|---------------------|-------------|-----------|-----------------|-----------|--------------|--------------------|-----------------------|---------------|-------------|------------------------|----------------|-------|
| SF-01 | Guard interlock — operator door | Remove press ram drive power when door opens | H-03 | Door opened | Ram stopped, drive de-energized | ≤200ms | PLd | S2, F2, P2 | Manual reset | Auto, Manual | None | No | Response time from ISO 13855 calc |
| SF-02 | E-stop — operator station | Stop all hazardous motion on e-stop activation | H-01 through H-12 | E-stop pressed | Category 0 or 1 stop per IEC 60204-1 | ≤500ms | PLd | S2, F2, P1 | Manual reset | All modes | None | No | Per ISO 13850 |
| SF-03 | Light curtain — infeed | Prevent press cycling when operator is in detection zone | H-03, H-04 | Light curtain interrupted | Ram stopped, cycle inhibited | ≤150ms | PLe | S2, F2, P2 | Automatic restart permitted during auto cycle | Auto | Muted during robot load cycle — muting per IEC 62046 | No | Safety distance per ISO 13855 |
| SF-04 | Speed monitoring — setup mode | Limit ram speed to ≤10mm/s during setup mode | H-03 | Speed exceeds limit | Drive disabled | ≤100ms | PLd | S2, F1, P1 | Manual reset | Setup only | N/A | ISO 16092 requires speed limiting in setup | Type-C driven |
| SF-05 | SIS — high pressure trip | Close isolation valve on high-pressure detection | H-15 | Pressure > setpoint | Valve closed, process isolated | ≤2s | SIL 2 | LOPA: IE freq 0.1/yr, consequence severity 4, no credited IPLs | Manual reset after investigation | All | None | IEC 61511 applies | Process safety SIF |

### Risk Assessment Report — Recommended Structure

| Section | Content |
|---------|---------|
| 1. Scope and objectives | Machine/system identified, boundary reference, standards applied |
| 2. Risk assessment team | Names, roles, qualifications, date(s) of assessment |
| 3. Methodology | Which method(s) used (ISO 12100, HAZOP, LOPA, etc.), which risk graph (ISO 13849-1 or IEC 62061), justification |
| 4. Machine limits | Reference to Stage 1 system description, intended use, foreseeable misuse, operating modes |
| 5. Hazard identification | Complete hazard register with zone, task, mode, life phase, hazard category |
| 6. Risk estimation and evaluation | For each hazard: parameters, risk level before risk reduction, three-step method analysis |
| 7. Safety function register | Complete register per template above |
| 8. PLr/SIL assignments | Summary table of all safety functions with assigned integrity levels |
| 9. Residual risk assessment | For each hazard: residual risk after all three steps, tolerability determination |
| 10. Type-C cross-check | Evidence of compliance with type-C specific requirements |
| 11. Assumptions and limitations | What was assumed, what was not assessed, what requires follow-up |
| 12. Conclusions and recommendations | Summary of key findings, any items requiring design team action |
| 13. Signatures | Risk assessment team sign-off with date |
| Appendix A | Photographs, layout drawings, zone maps used during assessment |
| Appendix B | Completed checklists (ISO 12100 Annex B, type-C checklists) |
| Appendix C | LOPA worksheets (if applicable) |

---

## 8. Exit Criteria — Gate Review

This stage is complete when **all** of the following are true:

| # | Criterion | Evidence |
|---|-----------|----------|
| 1 | All hazards are identified systematically using at least one structured method and cross-checked against ISO 12100 Annex B | Completed hazard register |
| 2 | All life phases are covered, not just normal operation | Life phase column populated in hazard register |
| 3 | All operating modes are assessed | Mode column populated in hazard register |
| 4 | For each hazard, the three-step risk reduction method is documented (inherent safe design considered before safeguarding) | Three-step documentation for each hazard |
| 5 | Every safety function has a unique ID, description, safe state, response time, and assigned PLr or SIL | Completed safety function register |
| 6 | PLr/SIL risk graph parameters are documented with rationale for each safety function | PLr/SIL assignment record |
| 7 | Type-C standard requirements are cross-checked and any mandatory measures are included | Type-C cross-check record |
| 8 | Residual risk is assessed and documented as tolerable for every hazard | Residual risk register |
| 9 | Risk assessment team includes at least 3 people with relevant expertise | Team roster in report |
| 10 | Risk assessment report is reviewed and signed by all team members | Signed report |
| 11 | Safety function register is complete and ready to serve as input to SRS (Stage 3.5) | Register reviewed and approved |
| 12 | All assumptions are documented with owners and resolution dates | Updated assumptions register |

**If any safety function does not have an assigned PLr/SIL, Stage 4 (Safety Architecture) cannot proceed for that function.**

---

## 9. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **Safety / Controls Engineer** | Facilitates and documents the risk assessment; applies risk graph methodology; authors safety function register and PLr/SIL assignments; authors risk assessment report |
| **Mechanical / Process Engineer** | Identifies mechanical/process hazards, energy sources, failure modes; provides input on severity and frequency; validates inherently safe design considerations |
| **Operator / Operator Representative** | Provides real-world input on exposure frequency, misuse scenarios, avoidance possibility; validates operating mode descriptions |
| **Maintenance Technician / Representative** | Identifies maintenance-phase hazards, access requirements, LOTO scenarios, common failure modes |
| **Customer Safety Representative** | Confirms site-specific hazards, risk tolerance, and any mandatory measures from customer safety standards |
| **Project Manager** | Ensures the risk assessment is scheduled with adequate time and the right participants; understands schedule impact of findings |

---

## 10. Common Mistakes

| Mistake | Consequence | How to Avoid |
|---------|-------------|-------------|
| Risk assessment performed by one person at a desk | Misses hazards that are obvious to operators and maintainers; may not satisfy audit requirements for team-based assessment | Assemble a multidisciplinary team; conduct the assessment at the machine or with detailed drawings/models |
| Only assessing automatic mode | Misses hazards during setup, maintenance, cleaning, fault recovery — which is where most serious injuries occur | Use the life phase and operating mode tables in Sections 5.3 and 5.8 as mandatory checklists |
| Skipping Step 1 (inherently safe design) | Jumps straight to adding guards and safety functions; may result in unnecessary complexity when a design change could eliminate the hazard | For every hazard, ask "can we eliminate or reduce this by design?" before assigning a safety function |
| Treating risk assessment as a one-time event | Machine scope changes, new hazards are discovered during design, customer changes requirements — the risk assessment becomes outdated | Risk assessment is a living document. Re-enter this stage via MOC whenever scope or design changes affect hazards |
| Using the risk graph mechanically without engineering judgment | Parameters are selected by rote without considering the actual scenario; PLr/SIL may be inappropriate | Each parameter selection must have a documented rationale specific to the hazard and scenario |
| Not documenting residual risk | Auditors cannot verify that risk was reduced to a tolerable level; end users do not know what residual risks they must manage | Complete the residual risk register for every hazard |
| Confusing hazard with risk | Listing "robot" as a hazard instead of "crushing injury to upper body from robot arm motion during automatic cycle in zone A" | A hazard is a potential source of harm. A risk is the combination of severity and probability of that harm. Be specific. |
| Not considering stored energy | After machine is stopped and de-energized, stored energy (gravity, springs, pressurized fluid, capacitors, thermal mass) can still cause harm | For every energy source, assess the hazard from stored energy after the machine is commanded to stop |
| Not aligning safety functions with reset and restart requirements | Safety function stops the machine but restart conditions are undefined — operator may restart into a hazardous condition | Every safety function definition must include reset behavior and restart conditions |

---

## 11. Relationship to Adjacent Stages

```
┌──────────────────────────────────┐
│  STAGE 2: STANDARDS SELECTION     │
│                                  │
│  Provides:                       │
│  • Standards register            │
│  • PL vs SIL pathway            │
│  • Type-C standard confirmation  │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│  STAGE 3: RISK ASSESSMENT         │  ◄── You are here
│  ★ PL/SIL DECISION POINT ★       │
│                                  │
│  Produces:                       │
│  • Risk assessment report        │
│  • Hazard register               │
│  • Safety function register      │
│  • PLr/SIL assignments           │
│  • Residual risk register        │
└──────────────┬───────────────────┘
               │
               │  All outputs feed directly into
               ▼
┌──────────────────────────────────┐
│  STAGE 3.5: SAFETY REQUIREMENTS   │
│  SPECIFICATION (SRS)              │
│                                  │
│  Formalizes each safety function │
│  into a verifiable specification │
│  with:                           │
│  • Inputs and outputs            │
│  • Required PLr/SIL             │
│  • Response time                 │
│  • Diagnostic requirements       │
│  • Test acceptance criteria      │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│  STAGE 4: SAFETY ARCHITECTURE     │
│                                  │
│  Uses PLr/SIL targets to        │
│  determine:                      │
│  • Architecture category         │
│  • Hardware fault tolerance      │
│  • Diagnostic coverage           │
│  • Component selection           │
└──────────────────────────────────┘

         ┌────────────────────────────────────┐
         │ TRACEABILITY CHAIN                  │
         │                                    │
         │ Hazard (Stage 3)                   │
         │   └─► Safety Function (Stage 3)    │
         │         └─► SRS Requirement (3.5)  │
         │               └─► Architecture (4) │
         │                     └─► Design (5) │
         │                        └─► Test(10)│
         │                                    │
         │ Every link must be documented.     │
         │ If any link is missing, the        │
         │ safety function is not traceable.  │
         └────────────────────────────────────┘
```

---

## 12. Templates and Tools

| Resource | Purpose |
|----------|---------|
| Risk assessment report template | Structured document per Section 7 report structure |
| Hazard identification checklist (ISO 12100 Annex B) | Printable checklist with all hazard categories and specific hazards |
| Safety function register template | Spreadsheet with all columns per Section 7 register template |
| ISO 13849-1 risk graph worksheet | Fillable form for documenting S, F, P parameters and PLr result per safety function |
| IEC 62061 SIL assignment worksheet | Fillable form for documenting Se, Fr, Pr, Av parameters and SIL result per safety function |
| LOPA worksheet template | Fillable form for initiating event, IPL credits, and SIL determination per IEC 61511 |
| Zone/task/mode matrix template | Grid for systematic hazard identification across zones, tasks, and operating modes |
| Residual risk register template | Table for documenting residual risk per hazard after all three risk reduction steps |
| SISTEMA software | Free tool from IFA (German DGUV) for ISO 13849-1 PL calculations — used in Stage 4 but useful to reference here for understanding PLr requirements |
| exSILentia / SILver | SIL verification tools — used in Stage 4 but useful to reference for LOPA and SIL target understanding |

---

## 13. Iterative Nature of Risk Assessment

Risk assessment is not a single event. It is revisited when:

| Trigger | Action |
|---------|--------|
| Design changes during Stage 4 or 5 alter the hazard profile | Re-enter Stage 3 for affected hazards; update risk assessment and safety function register |
| Commissioning (Stage 10) reveals hazards not identified during risk assessment | Re-enter Stage 3; assess new hazards; determine if additional safety functions are required |
| Management of Change (Stage 12) modifies the machine or process | Re-enter Stage 3 via MOC for the scope of the change |
| New information about severity, frequency, or avoidance becomes available | Update the risk estimation for affected hazards; verify PLr/SIL assignments are still valid |
| A type-C standard is revised and imposes new requirements | Review hazard register and safety function register against new requirements |

**The risk assessment report must have a revision history tracking all updates.**

---

[← Standards Selection]({{ '/lifecycle/standards-selection/' | relative_url }}) | [Safety Requirements Specification →]({{ '/lifecycle/safety-requirements-spec/' | relative_url }})
