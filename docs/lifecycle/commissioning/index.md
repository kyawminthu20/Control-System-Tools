---
layout: default
title: "Lifecycle Stage 10 — Commissioning and Validation"
description: "FAT, SAT, safety function validation, and final PL/SIL verification — the stage where design intent is formally demonstrated on the physical system."
breadcrumb:
  - name: "Lifecycle"
    url: "/lifecycle/"
  - name: "10. Commissioning"
related_standards:
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
redirect_from:
  - /implementation/lifecycle-commissioning/
---

<div class="page-header">
  <span class="page-header__label">Lifecycle Stage 10</span>
  <h1>Commissioning and Validation</h1>
  <strong>Final PL/SIL Verification</strong>
</div>

## Commissioning Sequence

```mermaid
flowchart LR
    A[Pre-comm passed] --> B[Energize process]
    B --> C[Loop checks under load]
    C --> D[Safety function dynamic test]
    D --> E[Sequence / interlock test]
    E --> F[PL / SIL verification]
    F --> G[SAT with customer]
    G --> H[Handover · as-built docs]
```

## 1. Purpose of This Stage

This stage is the **final proof** that the safety system works as designed under actual or representative operating conditions. Everything in Stages 1–9 has been specification, design, construction, and preliminary verification. This stage answers the ultimate question: **does the installed, configured, real-world system actually achieve the required safety performance?**

The distinction between this stage and Stage 9 (Pre-Commissioning) is fundamental:

- **Pre-commissioning (Stage 9):** Verified that the system was correctly built, wired, configured, and calibrated — tested under controlled conditions without the process running, without material in the machine, without production dynamics
- **Commissioning and validation (this stage):** Verifies that the system **performs correctly under actual or representative production conditions** — with actual machine dynamics, actual stopping times, actual sensor response to real-world conditions, actual interaction between safety functions and the process

This stage produces the **Verification and Validation (V&V) Report** — the single most important document in the safety lifecycle from an audit and compliance perspective. The V&V report provides the evidence chain from safety function specification (Stage 3) through architecture design (Stage 4) to physical proof that the installed system achieves its required PLr or SIL. Without this report, the safety lifecycle is incomplete regardless of how rigorous the earlier stages were.

This is also the stage where the **Declaration of Conformity is signed** (for CE-marked machines), the **technical file is finalized**, and the system is formally **handed over** to the customer/end user for operation.

> **This stage answers: Does the installed, real-world system achieve the required PL/SIL for every safety function, under actual operating conditions, with documented evidence that an auditor can verify?**

---

## 2. Entry Criteria

This stage begins when **Stage 9 (Pre-Commissioning) exit criteria are met**.

### Required Inputs

| Input | Source (Stage) | Why It Matters |
|-------|---------------|----------------|
| Pre-commissioning checklist (completed, signed) | Stage 9 | Confirms system is correctly wired, configured, calibrated, and safety functions passed dry-run testing — pre-commissioning results are the foundation this stage builds upon |
| Safety function dry-run test records | Stage 9 | Baseline — commissioning repeats these tests under production conditions |
| Baseline measurements | Stage 9 | Reference values for comparison during commissioning measurements |
| Safety function verification plan | Stage 5 / Stage 6 | Defines test procedures and acceptance criteria for each safety function — the commissioning team executes this plan |
| Safety function register (finalized) | Stage 3 / Stage 4 | Master reference for all safety functions with PLr/SIL targets, safe states, response times, reset behavior |
| Safety architecture document | Stage 4 | Reference for understanding what the architecture should achieve — particularly response time budgets and diagnostic requirements |
| PL/SIL calculation reports | Stage 4 | Reference for confirming that the as-built system matches the calculated architecture |
| Response time analysis | Stage 4 | Calculated response time requirements — commissioning measures actual response times and compares |
| Cause and effect matrix | Stage 6 | Reference for verifying that every input produces the correct output under all conditions |
| FAT procedure | Stage 6 | Formal test procedure for factory acceptance (if contractually required) |
| SAT procedure | Stage 6 | Formal test procedure for site acceptance (if contractually required) |
| As-built schematics and documentation | Stage 7 / Stage 8 | Current revision reflecting all build and field changes |
| Calibration records | Stage 9 | Confirmed instrument calibration — instruments must be within calibration during commissioning |
| Safety manual (draft) | Stage 6 | Reference for operator training content; updated based on commissioning findings |
| Operating instructions (draft) | Stage 6 | Reference for operator training content |
| Maintenance manual (draft) | Stage 6 | Reference for maintenance training content |
| Customer specification | Sales / contract | Defines customer-specific commissioning requirements, witness points, and acceptance criteria |
| Customer site safety requirements | Customer | Permit requirements, LOTO procedures, site-specific PPE, access restrictions during commissioning |

### Commissioning Readiness Verification

Before commissioning activities begin:

| Check | Action | Responsible |
|-------|--------|-------------|
| Pre-commissioning complete and signed | All Stage 9 exit criteria met; all open items from Stage 9 resolved or formally deferred with risk acceptance | Commissioning engineer / safety engineer |
| Pre-commissioning open items resolved | Items classified as "must close before Stage 10" are closed | Project engineer |
| Machine mechanically ready | All mechanical systems installed, aligned, lubricated; guards installed; tooling installed (if applicable) | Mechanical engineer |
| Process materials available (if needed for testing) | If commissioning requires actual production material or process media | Customer / operations |
| Utilities available | All utilities (power, compressed air, hydraulics, cooling water, process fluids) at required parameters | Customer / site engineer |
| Test equipment available and calibrated | Response time measurement equipment (high-speed timer, oscilloscope, or calibrated safety device test instruments), calibrated multimeters, force gauges (if applicable) | Commissioning engineer |
| Customer witness schedule confirmed | If FAT/SAT witness is contractually required — customer representatives scheduled and available | Project manager |
| Training prerequisites identified | Operators and maintenance personnel who need training before handover are identified and scheduled | Project manager / customer |
| Emergency procedures in place | Emergency response procedures for the commissioning area are established; first aid available; emergency contacts identified | Customer safety / site supervisor |
| Commissioning risk assessment completed | If commissioning activities introduce hazards not present during normal operation (e.g., running machine with guards open under controlled conditions, first-time process operation), a commissioning-specific risk assessment is performed | Safety engineer / commissioning engineer |

---

## 3. Standards Influence

| Standard | Role at This Stage | Key Requirements |
|----------|-------------------|-----------------|
| **ISO 13849-1:2023 §8** | Validation of safety-related parts of control systems — defines validation methods (analysis, testing) and requires documentation of validation results | §8.1 (general validation principles), §8.2 (validation by analysis and testing), §8.3 (validation documentation) |
| **ISO 13849-2:2012** | Validation methods — fault lists and fault simulation methods for specific technologies; provides the technical basis for fault injection testing | All tables (fault lists by technology) |
| **IEC 62061:2021 §6.9** | Validation of SRECS — requires validation that the safety requirements specification is met, including functional testing and documentation | §6.9 (validation) |
| **IEC 61508-2:2010 §7.7, §7.9** | Hardware validation and integration testing requirements | §7.7 (overall validation), §7.9 (hardware integration testing) |
| **IEC 61508-3:2010 §7.7, §7.9** | Software validation and integration testing requirements | §7.7 (software validation), §7.9 (software integration testing) |
| **IEC 61511-1:2016 §15, §16** | SIS commissioning (§15) and safety validation (§16) — defines specific requirements for SIS validation including logic solver testing, final element testing, and SIF validation | §15 (commissioning), §16 (safety validation) |
| **IEC 60204-1:2016 §18** | Verification and testing of machine electrical equipment — functional tests under normal operating conditions | §18.6 (functional tests) |
| **NFPA 79:2024 §19** | Testing requirements — functional testing of machine electrical equipment | §19.4 (testing) |
| **ISO 13855:2010** | Safety distance verification — commissioning confirms that actual response times, combined with installed safety distances, provide adequate protection | All clauses |
| **IEC 62046:2018** | Validation of protective equipment application — muting, blanking, and bypass functions must be validated under actual operating conditions | All applicable clauses |
| **ISO 12100:2010 §6.4** | Information for use — validation that operating instructions, safety manual, and training are adequate for safe operation | §6.4 |
| **EU Machinery Directive 2006/42/EC / Machinery Regulation (EU) 2023/1230** | Technical file must be complete and Declaration of Conformity signed after all testing is complete | Annex VII (technical file), Annex II (Declaration of Conformity) |
| **Customer specification** | May impose additional commissioning requirements, specific test procedures, witness points, and acceptance criteria beyond what standards require | Per contract |

---

## 4. Verification vs Validation — Definitions

Understanding the distinction is essential for this stage:

| Term | Definition | Question It Answers | Example |
|------|-----------|--------------------| --------|
| **Verification** | Confirmation by examination and provision of objective evidence that specified requirements have been fulfilled (ISO 13849-1 §3.58) | "Did we build the system correctly?" | The circuit diagram shows dual-channel wiring; the P2P check confirms both channels are wired correctly; the safety PLC program CRC matches the approved version |
| **Validation** | Confirmation by examination and provision of objective evidence that the requirements for a specific intended use or application have been fulfilled (ISO 13849-1 §3.59) | "Did we build the correct system?" | When the guard door opens during automatic operation, the machine actually stops within 200ms, the operator cannot restart without resetting, and the safety distance provides adequate protection at the actual approach speed |

**Verification is largely completed in Stages 7–9 (build, installation, pre-commissioning). Validation is the primary purpose of this stage.**

Validation requires testing the safety function **as a complete system** under **actual or representative conditions** — not just verifying that individual components and circuits are correct.

---

## 5. Engineering Activities

### 5.1 Commissioning Sequence

```
Phase 1: COMMISSIONING PLANNING
    │
    ├── Step 1: Review pre-commissioning results
    ├── Step 2: Finalize commissioning test procedures
    ├── Step 3: Commissioning risk assessment
    ├── Step 4: Schedule and resource confirmation
    │
    ▼
Phase 2: FACTORY ACCEPTANCE TEST (FAT) — if contractually required
    │
    ├── Step 5: FAT execution at manufacturer facility
    ├── Step 6: FAT documentation and punchlist
    │   ★ GATE: FAT complete (or FAT not required) ★
    │
    ▼
Phase 3: INITIAL MACHINE RUN (at installation site)
    │
    ├── Step 7: First production cycle under controlled conditions
    ├── Step 8: Sequence verification under actual conditions
    ├── Step 9: Process parameter tuning
    │   ★ GATE: Machine operates in basic production mode ★
    │
    ▼
Phase 4: SAFETY FUNCTION VALIDATION (under actual conditions)
    │
    ├── Step 10: Safety function validation testing (each SF)
    ├── Step 11: Response time measurement (calibrated instruments)
    ├── Step 12: Safety distance verification (actual dynamics)
    ├── Step 13: Muting validation (under actual conditions)
    ├── Step 14: Mode-dependent behavior validation
    ├── Step 15: Fault injection testing
    ├── Step 16: Combined / interaction testing
    ├── Step 17: Endurance / repeatability testing
    │   ★ GATE: All safety functions validated ★
    │
    ▼
Phase 5: SITE ACCEPTANCE TEST (SAT) — if contractually required
    │
    ├── Step 18: SAT execution with customer witness
    ├── Step 19: SAT documentation and punchlist
    │   ★ GATE: SAT complete (or SAT not required) ★
    │
    ▼
Phase 6: DOCUMENTATION FINALIZATION
    │
    ├── Step 20: V&V report compilation
    ├── Step 21: As-built documentation finalization
    ├── Step 22: Safety manual finalization
    ├── Step 23: Technical file completion
    ├── Step 24: Declaration of Conformity signing (if CE)
    │
    ▼
Phase 7: TRAINING AND HANDOVER
    │
    ├── Step 25: Operator training
    ├── Step 26: Maintenance training
    ├── Step 27: Documentation handover
    ├── Step 28: Formal acceptance and handover
    │   ★ GATE: System handed over to operations ★
```

### 5.2 Phase 1: Commissioning Planning

#### Step 1: Review Pre-Commissioning Results

| Activity | Detail |
|---------|--------|
| Review all Stage 9 records | Confirm all safety functions passed dry-run testing; identify any items that require re-testing under production conditions |
| Review open items from Stage 9 | Confirm all "must close before Stage 10" items are closed; identify "close during Stage 10" items and assign to specific commissioning activities |
| Review baseline measurements | Understand the baseline values recorded in Stage 9 — commissioning measurements will be compared to these |
| Identify any changes since pre-commissioning | If anything changed between Stage 9 and Stage 10 (software update, component replacement, configuration change), those items must be re-verified before commissioning proceeds |

#### Step 2: Finalize Commissioning Test Procedures

| Activity | Detail |
|---------|--------|
| Review verification plan from Stage 6 | Confirm test procedures are appropriate for actual site conditions; modify if necessary based on pre-commissioning findings |
| Define specific test conditions | For each safety function test: what operating mode, what process conditions, what material (if any), what machine speed, what personnel positions |
| Define acceptance criteria | For each test: quantitative pass/fail criteria derived from the safety function register (response time, safe state, reset behavior) |
| Define test instrumentation | For response time measurements: specify the instrument, measurement method, and measurement points |
| Coordinate with customer | Confirm test schedule, witness points, access requirements, and any customer-specific test requirements |

#### Step 3: Commissioning Risk Assessment

| Consideration | Assessment |
|--------------|-----------|
| First-time operation under production conditions | Machine behavior may differ from dry-run; unexpected interactions between process and control system |
| Testing safety functions with actual hazards present | Machine must be running to test safety functions under real conditions — personnel may be in proximity to operating machine |
| Fault injection testing | Deliberately introducing faults may create temporary hazardous conditions |
| Reduced safeguarding during specific tests | Some tests may require guards to be open or safety functions to be temporarily modified — requires compensating measures |
| Process material hazards | First-time introduction of process materials (chemicals, hot materials, pressurized fluids) introduces process-specific hazards |

**Commissioning risk assessment output:** Documented risk assessment specific to commissioning activities, with control measures for each identified risk. This is not the machine risk assessment (Stage 3) — it is a supplementary assessment of the risks introduced by the commissioning process itself.

### 5.3 Phase 2: Factory Acceptance Test (FAT)

#### When FAT Is Performed

| Condition | FAT Required? |
|-----------|--------------|
| Contractually required by customer | Yes — per contract terms |
| Customer specification mandates FAT | Yes |
| Complex system with long installation timeline | Recommended — catches problems before shipping |
| Simple panel with standard design | Typically not required — in-panel testing at Stage 7 is sufficient |
| Process safety SIS | Recommended — IEC 61511 §15 supports factory testing before site installation |

#### FAT Scope and Limitations

| What FAT Can Verify | What FAT Cannot Verify |
|---------------------|----------------------|
| Panel construction quality | Field wiring |
| Internal wiring correctness | Safety device mounting and alignment |
| PLC program logic and sequence | Actual machine dynamics (stopping time, inertia) |
| Safety PLC configuration and safety function logic | Actual sensor response in the field environment |
| Safety function response to simulated inputs | Actual response times including field devices and mechanical systems |
| HMI operation and alarm management | Integration with actual process |
| Drive configuration and parameter verification | Motor rotation and actual load behavior |
| Communication between panel-internal devices | Communication over field-length cables |
| EDM logic (using simulated contactor feedback) | EDM with actual contactor behavior under load |
| Cause and effect matrix verification (simulated) | Cause and effect under actual process conditions |

#### FAT Execution

| Activity | Method | Documentation |
|----------|--------|--------------|
| Document review | Customer reviews schematics, BOM, safety manual draft, verification plan — prior to or at start of FAT | Review comments recorded and resolved |
| Visual inspection | Walk-through of panel construction — component placement, labeling, wire routing, safety section, grounding | FAT checklist — visual items |
| Power-up and configuration verification | Controlled power-up; verify voltages, PLC boot, safety controller configuration, HMI | FAT checklist — power-up items |
| I/O simulation testing | Simulate each input (using I/O simulator or manual activation); verify correct PLC response and output activation | I/O verification record |
| Safety function testing (simulated) | For each safety function: simulate the triggering input; verify safety controller response, output state, reset behavior, cross-channel behavior, EDM | Safety function FAT test record (per safety function) |
| Sequence testing | Run through all machine sequences with simulated I/O; verify correct sequence progression, interlocks, and error handling | Sequence test record |
| Alarm testing | Simulate alarm conditions; verify correct alarm generation, priority, display, and acknowledgment | Alarm test record |
| Communication testing | Verify all internal communication links (PLC to HMI, PLC to drives, PLC to safety controller, safety network) | Communication test record |
| Cause and effect matrix verification | Systematically verify each row of the C&E matrix with simulated inputs | C&E matrix verification record — every cell checked |
| Punchlist generation | Any deficiencies found during FAT documented on the punchlist with severity classification | FAT punchlist |

#### FAT Documentation

| Document | Content |
|---------|---------|
| **FAT report** | Summary of all tests performed, results, deficiencies found, punchlist items, and overall FAT result (pass/conditional pass/fail) |
| **FAT test records** | Individual test records for each test category — I/O, safety functions, sequences, alarms, communications, C&E matrix |
| **FAT punchlist** | List of deficiencies with: item number, description, severity (A = must fix before ship, B = fix before SAT, C = minor/cosmetic), responsible party, target date, resolution status |
| **FAT attendance record** | Names, roles, and signatures of all FAT participants including customer witnesses |
| **FAT sign-off** | Customer signature accepting FAT results (with conditions, if applicable) |

### 5.4 Phase 3: Initial Machine Run

#### Step 7: First Production Cycle Under Controlled Conditions

| Activity | Detail | Precautions |
|----------|--------|-------------|
| Run machine at reduced speed (if possible) | First cycle at minimum speed or in jog mode; observe all machine motions; verify no unexpected behavior | All personnel at safe distance; emergency stop accessible; only essential personnel in commissioning area |
| Verify sequence progression | Each step of the production sequence executes correctly; interlocks function; transitions are smooth | Compare actual sequence to design specification |
| Verify process parameter behavior | Pressures, temperatures, speeds, forces, flow rates within expected ranges | Monitor all critical parameters; ready to stop if any parameter exceeds safe limits |
| Verify no interference between safety system and process | Safety functions do not spuriously trip during normal operation; process events do not affect safety system integrity | Monitor safety controller diagnostic status during operation |

#### Step 8: Sequence Verification Under Actual Conditions

| Activity | Detail |
|---------|--------|
| Run all operating modes | Automatic, manual/jog, setup, cleaning — verify correct behavior in each mode |
| Mode transitions | Verify correct behavior during every mode transition (auto → manual, manual → setup, etc.) |
| Fault recovery | Introduce common fault conditions (material jam, sensor failure, overload trip); verify machine responds correctly and can be recovered safely |
| Startup and shutdown sequences | Verify startup sequence from cold start, warm restart, and restart after safety function trip |
| Emergency stop recovery | Activate e-stop during operation; verify complete stop; verify recovery procedure works correctly |

#### Step 9: Process Parameter Tuning

| Activity | Detail |
|---------|--------|
| Tune PID loops (if applicable) | Process control loops tuned to achieve stable operation |
| Adjust timing parameters | Cycle times, dwell times, delay times adjusted to achieve production requirements |
| Verify safety function behavior during tuning | Safety functions remain operational and correct during all parameter adjustments; no tuning parameter affects safety function behavior unless formally evaluated |
| Document final parameter values | All tuned parameters documented as the commissioning baseline |

**★ GATE: Machine Operates in Basic Production Mode ★**

### 5.5 Phase 4: Safety Function Validation (Under Actual Conditions)

**This is the core validation phase — the primary purpose of this stage.** Each safety function is tested under actual or representative operating conditions to validate that it achieves its specified behavior.

#### Step 10: Safety Function Validation Testing

For each safety function in the register, perform validation testing under actual conditions:

| Test Element | Pre-Commissioning (Stage 9) | Commissioning Validation (This Stage) |
|-------------|---------------------------|--------------------------------------|
| **Triggering** | Physically activated safety device — machine not running | Physically activated safety device — **machine running in production mode** |
| **Safe state** | Verified output devices de-energize | Verified **machine actually stops** — actual motion ceases, actual energy is removed, actual safe state is achieved |
| **Response time** | Preliminary measurement with stopwatch | **Calibrated measurement** with appropriate instrument — actual end-to-end response time including sensor, logic, actuator, and mechanical stopping |
| **Reset behavior** | Verified reset procedure works | Verified reset procedure works **under production conditions** — no unexpected restart behavior |
| **Interaction** | Individual safety function tested in isolation | **Multiple safety functions tested for interaction** — simultaneous demands, priority, no conflicts |
| **Endurance** | Single test | **Multiple repetitions** to verify consistent behavior |

#### Safety Function Validation Test Record Template

| SF-ID | Safety Function | PLr/SIL Target | Test Date | Test Conditions (Mode, Speed, Material) | Triggering Device Activated | Safe State Achieved? | Actual Response Time (Measured) | Response Time Requirement (From Stage 4) | Response Time PASS/FAIL | Correct Outputs De-Energized? | Machine Motion Actually Stopped? | Residual Energy Dissipated? | HMI Indication Correct? | Reset Procedure Correct? | Auto-Restart Prevented? (Unless Designed) | Cross-Channel Verified? | EDM Verified? | Muting Verified? (If Applicable) | Repetitions Performed | All Repetitions Consistent? | Overall Result | Tested By | Witnessed By | Notes |
|-------|----------------|----------------|-----------|----------------------------------------|---------------------------|---------------------|-------------------------------|----------------------------------------|------------------------|------------------------------|--------------------------------|---------------------------|------------------------|------------------------|------------------------------------------|----------------------|--------------|--------------------------------|----------------------|---------------------------|----------------|-----------|-------------|-------|
| SF-01 | Guard interlock — operator door | PLd | | Auto, full speed, with material | Door opened | Y/N | ___ms | ≤200ms | P/F | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N | N/A | 5 | Y/N | PASS/FAIL | | | |

#### Step 11: Response Time Measurement

**This is one of the most critical measurements in the entire safety lifecycle.** The actual response time determines whether the safety distance provides adequate protection.

##### What to Measure

```
t_total = t_sensor + t_logic + t_communication + t_actuator + t_mechanical

Where:
  t_sensor       = time from hazard detection to signal reaching the logic solver
  t_logic        = safety controller processing/scan time
  t_communication = safety network transmission time (if applicable)
  t_actuator     = time from output command to actuator action (contactor opening, valve closing)
  t_mechanical   = time from actuator action to cessation of hazardous condition
                   (mechanical stopping time, including deceleration)
```

##### Measurement Methods

| Method | Description | Accuracy | When to Use |
|--------|-------------|----------|-------------|
| **High-speed timer / data logger** | Trigger channel connected to safety device output; stop channel connected to machine motion sensor (proximity sensor at hazard point) or actuator position sensor | ±1ms typical | Preferred method for critical safety functions; provides objective, calibrated measurement |
| **Safety device manufacturer test equipment** | Some safety device manufacturers (Sick, Pilz, Banner) offer test instruments specifically designed to measure response time of their devices | Per instrument specification | When manufacturer test equipment is available and covers the full response chain |
| **Oscilloscope with current clamp** | Current clamp on motor circuit; trigger on safety device activation; measure time to current drop to zero | ±1ms typical | When motor stopping time is the primary component |
| **PLC timestamp method** | Safety PLC records timestamp of input change and timestamp of output change; difference is the logic processing time | Limited to logic time only — does not capture sensor, actuator, or mechanical time | Supplementary — use to verify logic time component, but not as the sole response time measurement |
| **High-speed video** | Camera recording at ≥120 fps with visible safety device activation and visible machine motion | ±8ms at 120fps | Supplementary evidence; useful for visualizing the stopping behavior |
| **Stopwatch** | Manual timing from safety device activation to observed stop | ±200-500ms (human reaction time) | **NOT acceptable** as the primary measurement method for safety function response time — only for very coarse initial screening |

##### Response Time Measurement Record Template

| SF-ID | Safety Function | Measurement Point (Start) | Measurement Point (Stop) | Instrument Used | Instrument Calibration Date | Trial 1 (ms) | Trial 2 (ms) | Trial 3 (ms) | Trial 4 (ms) | Trial 5 (ms) | Average (ms) | Maximum (ms) | Requirement (ms) | Maximum vs Requirement | PASS/FAIL | Measured By | Date |
|-------|----------------|--------------------------|-------------------------|----------------|---------------------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-----------------|----------------------|-----------|------------|------|
| SF-01 | Guard interlock — door | Door switch contact change | Motor current = 0 | High-speed timer Model X, S/N 12345 | 2024-01-10 | 142 | 148 | 145 | 151 | 144 | 146 | 151 | ≤200 | 151 < 200 | PASS | | |

**Use the MAXIMUM measured value (not the average) for comparison to the requirement. The safety distance must protect against the worst-case stopping time.**

##### Response Time vs Safety Distance Verification

After measuring actual response time, recalculate the safety distance and verify it is still met:

```
S_actual = (K × t_max_measured) + C

Where:
  K = approach speed (per ISO 13855)
  t_max_measured = maximum measured response time
  C = supplementary distance (per ISO 13855)

Verify: S_actual ≤ D_installed

Where:
  D_installed = actual installed distance from safety device to hazard point
                (measured during Stage 8 installation)
```

| SF-ID | t_max_measured (ms) | K (mm/s) | C (mm) | S_actual (mm) | D_installed (mm) | S_actual ≤ D_installed? | PASS/FAIL |
|-------|--------------------| ---------|--------|---------------|-----------------|------------------------|-----------|
| SF-01 | 151 | 1600 | 850 | 1092 | 1200 | Yes | PASS |
| SF-03 | 92 | 2000 | 850 | 1034 | 1100 | Yes | PASS |

**If S_actual > D_installed, the safety function FAILS validation.** Options:
- Reduce response time (faster components, faster braking)
- Increase D_installed (move safety device further from hazard — if space permits)
- Re-evaluate approach speed assumptions (if justified)
- Add additional safeguarding measures

#### Step 12: Safety Distance Verification (Actual Dynamics)

Beyond the response time calculation, verify safety distances with actual machine behavior:

| Test | Method | Acceptance Criteria |
|------|--------|--------------------|
| Reach-over test | Verify that a person cannot reach over the safety device (light curtain, guard) to the hazard point — per ISO 13857 Table 1 | Physical measurement of device height and distance; person cannot reach hazard point by reaching over |
| Reach-through test | Verify that a person cannot reach through openings in guards to the hazard point — per ISO 13857 Tables 2–4 | Opening size and distance to hazard comply with ISO 13857 tables |
| Reach-around test | Verify that a person cannot reach around the safety device (around the end of a light curtain) to the hazard point | No unprotected access path around the safety device |
| Under-reach test | Verify that a person cannot reach under the safety device (under a light curtain's lowest beam) to the hazard point | Lowest detection point provides adequate protection per ISO 13855 |
| Detection zone coverage | Walk through every possible access path to the hazard zone; verify the safety device detects access on every path | No undetected access path exists |

#### Step 13: Muting Validation (Under Actual Conditions)

If any safety function includes muting (per IEC 62046):

| Test | Conditions | Acceptance Criteria |
|------|-----------|--------------------|
| Muting activates with actual product | Run actual product through the muting sequence; verify muting enables and disables correctly | Muting engages when product enters; muting disengages when product clears; timing is correct |
| Muting does not activate for personnel | With muting configured: walk through the detection zone (not carrying product); verify muting does NOT engage | Safety function activates; muting does not engage for person-sized objects |
| Product variation | Test with different product sizes/shapes within the specified range | Muting functions correctly across the full product range |
| Muting timeout under actual conditions | Start muting sequence; simulate a product jam (product stops in the muting zone); verify muting times out | Muting disengages after timeout; safety device returns to active protection |
| Muting indicator visible | Muting lamp visible from operator position and from all access points | Lamp clearly visible during muting; lamp OFF when muting is not active |
| Concurrent muting and person entry | During active muting (product present): enter the detection zone from a non-muted direction | Safety function activates for person entry even during muting |

#### Step 14: Mode-Dependent Behavior Validation

| Test | Conditions | Acceptance Criteria |
|------|-----------|--------------------|
| Automatic mode — all safety functions active | Machine running in automatic at production speed | All safety functions respond correctly when triggered |
| Manual/jog mode — safety functions with modified behavior | Switch to manual mode; verify safety functions active with any mode-specific modifications (reduced speed, hold-to-run) | Correct behavior per safety function register; reduced speed verified by measurement; hold-to-run device must be held continuously |
| Setup/teach mode — safety functions with modified behavior | Switch to setup mode (if applicable); verify enabling device requirement, speed limiting, reduced force (if applicable) | Enabling device required and functional; speed limit verified by measurement; all other safety functions active as specified |
| Mode transition during operation | Switch modes while machine is running (if permitted by design); verify safety system re-evaluates and applies correct safety behavior for new mode | No loss of safety function during transition; machine achieves safe state if transition requires it |
| Unauthorized mode change attempt | Attempt to change mode without proper authorization (key, password) | Mode change prevented; machine remains in current mode |

#### Step 15: Fault Injection Testing

Fault injection testing validates that the safety system responds correctly to component failures — this is the validation counterpart to the diagnostic verification done in Stage 9.

| Fault to Inject | Method | Expected Response | Acceptance Criteria |
|----------------|--------|------------------|--------------------|
| Single-channel failure (input) | Disconnect one channel of a dual-channel safety input | Safety controller detects fault; enters safe state or fault state; prevents restart until fault is cleared | Correct detection within discrepancy time; correct response |
| Single-channel failure (output) | Prevent one output contactor from opening (simulate welding by disconnecting feedback, or by physically holding in if safe) | Safety controller detects fault via EDM; prevents restart on next cycle | Correct detection; restart prevented |
| Both channels simultaneous loss (input) | Disconnect both channels simultaneously (simulates wire break or connector failure) | Safety controller enters safe state immediately | Safe state achieved within response time requirement |
| Power supply failure to safety device | Disconnect 24VDC to a safety device | Safety controller detects loss of input signal; enters safe state | Safe state achieved |
| Safety network communication failure | Disconnect safety network cable between safety controller and remote I/O or between safety controllers | Safety controller detects communication loss; enters safe state within specified communication timeout | Safe state achieved within timeout |
| Ground fault on safety circuit | Introduce controlled ground fault on a safety circuit (if safe to do so and if ground fault detection is part of the design) | Safety controller detects ground fault | Correct detection and response |
| Safety controller power cycle | Remove and restore power to safety controller | Safety controller boots into correct state; does not auto-restart machine; requires manual reset and restart sequence | Correct boot behavior; no auto-restart |
| Process fault during safety function activation | Trigger safety function while process fault is occurring (e.g., material jam, overpressure, overtemperature) | Safety function achieves safe state despite process fault conditions | Safe state achieved; no additional hazardous condition created |

**Fault injection testing must be performed with appropriate safety precautions. Personnel must be at safe distance; the machine should be in a condition where the injected fault does not create an uncontrolled hazard. If fault injection cannot be performed safely with the machine running, perform with the machine in a controlled, reduced-risk state and document the limitation.**

#### Step 16: Combined / Interaction Testing

| Test | Conditions | Acceptance Criteria |
|------|-----------|--------------------|
| Simultaneous activation of multiple safety functions | Activate two or more safety functions simultaneously (e.g., e-stop + guard interlock; light curtain + overspeed) | All activated safety functions achieve their safe states; no conflict between safety functions; most restrictive safe state applies |
| Safety function during mode transition | Trigger safety function at the exact moment of mode transition | Safety function activates correctly regardless of mode transition timing |
| Safety function during startup sequence | Trigger safety function during machine startup (before full speed is reached) | Safety function activates and achieves safe state; startup sequence does not override safety function |
| Safety function during controlled stop | Trigger safety function while a controlled stop (Category 1) is in progress | Safety function takes priority if it requires immediate stop (Category 0); or integrates correctly with controlled stop |
| Safety function during fault recovery | Trigger safety function while operator is recovering from a previous fault | Safety function activates correctly; fault recovery does not bypass safety function |
| E-stop during muting | Activate e-stop while muting is active | E-stop overrides muting; all outputs de-energize; machine stops |
| Multiple e-stop stations | Activate e-stop at one station; while held, activate e-stop at another station; release first e-stop | Machine remains stopped until ALL e-stops are released and reset is performed |

#### Step 17: Endurance / Repeatability Testing

| Test | Method | Acceptance Criteria |
|------|--------|--------------------|
| Repeated safety function activation | Activate each safety function multiple times (minimum 5 repetitions recommended; more for critical functions) | Consistent response every time; no degradation of response time; no intermittent failures |
| Repeated e-stop cycling | Activate and reset e-stop 10+ times in succession | Consistent response; no contact bounce issues; no reset failures |
| Extended operation monitoring | Monitor safety system during extended production run (duration per customer specification or minimum 4–8 hours) | No spurious trips; no diagnostic errors; safety functions remain fully operational |
| Temperature stabilization | Monitor safety controller and safety device temperatures during extended operation | All temperatures within rated operating range after thermal equilibrium is reached |

**★ GATE: All Safety Functions Validated ★**

### 5.6 Phase 5: Site Acceptance Test (SAT)

#### When SAT Is Performed

| Condition | SAT Required? |
|-----------|--------------|
| Contractually required by customer | Yes |
| Machine was FAT-tested at factory and installed at site | Recommended — verifies field installation did not introduce issues |
| Process safety SIS | Required per IEC 61511 |
| Customer specification mandates SAT | Yes |

#### SAT Scope

SAT typically includes:

| SAT Activity | Scope |
|-------------|-------|
| Review of installation records | Confirm installation was performed per design |
| Review of pre-commissioning records | Confirm pre-commissioning was completed |
| Repeat of selected safety function tests under actual conditions | All safety functions or a subset per contract — under actual production conditions with customer witness |
| Response time measurements | Formal calibrated measurements (may have been done in Phase 4 and repeated for customer witness) |
| Integration testing | Verify integration with upstream/downstream equipment, facility utilities, and building management systems |
| Production trial run | Extended production run to demonstrate reliable operation |
| Documentation review | Customer reviews final documentation package — safety manual, operating instructions, as-built schematics |
| Training verification | Customer confirms operators and maintenance personnel have been trained |
| Punchlist closure | All FAT and commissioning punchlist items resolved |

#### SAT Documentation

| Document | Content |
|---------|---------|
| **SAT report** | Summary of all tests performed, results, deficiencies, and overall SAT result |
| **SAT test records** | Individual test records — same format as Phase 4 validation records |
| **SAT punchlist** | Deficiencies found during SAT with severity, responsible party, target date, and resolution status |
| **SAT attendance record** | Names, roles, signatures of all participants including customer witnesses |
| **SAT sign-off** | Customer signature accepting SAT results — this is typically the formal acceptance milestone |

**★ GATE: SAT Complete ★**

### 5.7 Phase 6: Documentation Finalization

#### Step 20: V&V Report Compilation

The V&V report is the **definitive record** of safety function verification and validation. It compiles evidence from multiple stages into a single, auditable document.

##### V&V Report Structure

| Section | Content | Source |
|---------|---------|--------|
| **1. Executive summary** | Summary of all safety functions, their PLr/SIL targets, and the validation result for each | This stage |
| **2. Scope and objectives** | Machine identification, boundary, standards applied, validation objectives | Stages 1, 2 |
| **3. Safety function register** | Complete register with all specification parameters | Stage 3/4 |
| **4. Verification evidence** | | |
| 4.1 Design verification | Architecture document, PL/SIL calculation reports, SISTEMA/SILver files | Stage 4 |
| 4.2 Build verification | Component verification checklist, P2P wiring check, build records, NCR log | Stage 7 |
| 4.3 Installation verification | Installation record, field wiring verification, grounding verification, safety distance measurements | Stage 8 |
| 4.4 Pre-commissioning verification | Pre-commissioning checklist, I/O verification, safety function dry-run tests, Annex K checklist, calibration records | Stage 9 |
| **5. Validation evidence** | | |
| 5.1 Safety function validation test records | Individual test record for each safety function — under actual conditions | This stage (Phase 4) |
| 5.2 Response time measurements | Calibrated measurements for each safety function with response time requirements | This stage (Step 11) |
| 5.3 Safety distance verification | Measured response time → recalculated safety distance → compared to installed distance | This stage (Step 12) |
| 5.4 Muting validation | Muting test records under actual conditions | This stage (Step 13) |
| 5.5 Mode-dependent behavior validation | Test records for each operating mode | This stage (Step 14) |
| 5.6 Fault injection test results | Results of each fault injection test | This stage (Step 15) |
| 5.7 Combined / interaction test results | Results of simultaneous and interaction testing | This stage (Step 16) |
| 5.8 Endurance / repeatability test results | Results of repeated testing and extended operation | This stage (Step 17) |
| **6. FAT report** (if applicable) | FAT results, punchlist, resolution | This stage (Phase 2) |
| **7. SAT report** (if applicable) | SAT results, punchlist, resolution | This stage (Phase 5) |
| **8. Final PL/SIL confirmation** | For each safety function: required PLr/SIL, achieved PL/SIL (from Stage 4 calculation confirmed by validation), validation result (PASS/FAIL) | Stages 4 + this stage |
| **9. As-built documentation reference** | Reference to final as-built schematics, BOM, software versions — the documentation that represents the validated system | Stages 7, 8, this stage |
| **10. Deviations and resolutions** | Any deviations from the design found during commissioning, how they were resolved, and impact on PL/SIL | This stage |
| **11. Open items (if any)** | Any items deferred to post-commissioning with justification, risk acceptance, and resolution plan | This stage |
| **12. Training records** | Evidence that operators and maintenance personnel have been trained | This stage (Phase 7) |
| **13. Conclusions** | Statement that all safety functions have been validated to meet their required PLr/SIL, or identification of any functions that did not meet requirements with the corrective action taken | This stage |
| **14. Signatures** | Commissioning engineer, safety engineer, project engineer, customer representative (if SAT) | This stage |
| **Appendices** | All supporting test records, calibration certificates, photographs, instrument data | All stages |

##### V&V Summary Matrix

This is the single most important page in the V&V report — it provides the complete status of every safety function at a glance:

| SF-ID | Safety Function | Required PLr/SIL | Architecture Category | Achieved PL/SIL (Calculated, Stage 4) | Response Time Required | Response Time Measured (Max) | Response Time PASS/FAIL | Safety Distance Required | Safety Distance Installed | Safety Distance PASS/FAIL | Dry-Run Test (Stage 9) | Validation Test (Stage 10) | Fault Injection | Mode Testing | Overall Validation Result |
|-------|----------------|------------------|----------------------|---------------------------------------|----------------------|----------------------------|------------------------|------------------------|--------------------------|--------------------------|----------------------|--------------------------|----------------|-------------|--------------------------|
| SF-01 | Guard interlock — door | PLd | Cat. 3 | PLd | ≤200ms | 151ms | PASS | 1092mm | 1200mm | PASS | PASS | PASS | PASS | PASS | **PASS** |
| SF-02 | E-stop — station 1 | PLd | Cat. 3 | PLd | ≤500ms | 310ms | PASS | N/A | N/A | N/A | PASS | PASS | PASS | PASS | **PASS** |
| SF-03 | Light curtain — infeed | PLe | Cat. 4 | PLe | ≤150ms | 92ms | PASS | 1034mm | 1100mm | PASS | PASS | PASS | PASS | PASS | **PASS** |
| SF-05 | SIS — high pressure | SIL 2 | 1oo2 | SIL 2 | ≤2s | 1.2s | PASS | N/A | N/A | N/A | PASS | PASS | PASS | PASS | **PASS** |

#### Step 21: As-Built Documentation Finalization

| Activity | Detail |
|---------|--------|
| Incorporate all commissioning changes | Any changes made during commissioning (parameter adjustments, wiring corrections, component replacements) incorporated into formal document revisions |
| Schematics updated to final as-built | "As-Built" revision stamp; all changes from build, installation, and commissioning reflected |
| BOM updated to final as-built | Any component changes reflected; safety component list accurate |
| Software version records finalized | Final CRC/signature of safety PLC program, standard PLC program, HMI application, and drive parameters — these are the approved versions for operation |
| Configuration backup updated | Final backup of all software and configuration — this is the definitive backup for the life of the machine |

#### Step 22: Safety Manual Finalization

| Activity | Detail |
|---------|--------|
| Update safety manual from draft to final | Incorporate any changes from commissioning — updated response times, updated operating procedures, any additional residual risk information discovered during commissioning |
| Add achieved PL/SIL values | Safety manual must state the achieved PL or SIL for each safety function (per ISO 13849-1 §10) |
| Add proof test procedures (finalized) | Based on commissioning experience — specific, step-by-step proof test procedures for each safety function that maintenance personnel can execute |
| Add proof test intervals | Based on Stage 4 architecture and IEC 61511 requirements (for SIS) — how often each safety function must be proof-tested |
| Add spare parts list (finalized) | Based on final as-built BOM — safety-rated components with part numbers, quantities, and replacement intervals |
| Customer review and acceptance | Customer reviews final safety manual; comments resolved; final version issued |

#### Step 23: Technical File Completion

| Activity | Detail |
|---------|--------|
| Add test reports | V&V report, FAT report, SAT report, response time measurements, calibration records — all added to the technical file |
| Add as-built documentation | Final as-built schematics, BOM, software version records |
| Add Declaration of Conformity (to be signed in Step 24) | Draft updated to final with serial number, date, and signatory |
| Verify completeness against Machinery Directive Annex VII | Every required element of the technical file is present |
| Technical file archived | Complete technical file stored per company document retention policy — must be available for 10 years after the last machine of the type was manufactured (per Machinery Directive) |

#### Step 24: Declaration of Conformity Signing (CE Marking)

| Prerequisite | Verification |
|-------------|-------------|
| Technical file is complete | All elements present per Annex VII checklist |
| All safety functions validated | V&V summary matrix shows all PASS |
| All applied harmonized standards confirmed | Standards register reflects actual standards applied (not just planned) |
| All punchlist items resolved | FAT and SAT punchlists closed |
| Safety manual is final | Final version issued |
| Authorized signatory available | Person authorized to sign on behalf of the manufacturer |

**The Declaration of Conformity is signed and dated. The CE marking is applied to the machine. This is the formal declaration that the machine complies with the applicable EU directives.**

**For non-CE machines (US market only):** No Declaration of Conformity, but the V&V report serves the same function as evidence of compliance with applicable standards.

### 5.8 Phase 7: Training and Handover

#### Step 25: Operator Training

| Training Topic | Content | Standard Reference |
|---------------|---------|-------------------|
| Machine operation — all modes | How to operate the machine in automatic, manual, setup, and maintenance modes | Operating instructions (Stage 6) |
| Safety function awareness | What each safety function does, where the safety devices are located, what happens when a safety function activates, how to reset | Safety manual |
| Emergency procedures | E-stop locations, emergency shutdown procedure, emergency egress routes, first aid | Safety manual, site emergency procedures |
| Residual risks | What hazards remain after all safeguarding; required PPE; prohibited actions | Safety manual — residual risk section |
| Startup and shutdown | Correct startup sequence; correct shutdown sequence; restart after safety function trip | Operating instructions, safety manual |
| Fault recognition and response | How to recognize common faults; how to respond safely; when to call maintenance | Operating instructions |
| What NOT to do | Prohibited actions — bypassing safety devices, reaching into guarded areas, operating without guards, defeating interlocks | Safety manual — intended use and foreseeable misuse |

#### Step 26: Maintenance Training

| Training Topic | Content | Standard Reference |
|---------------|---------|-------------------|
| LOTO procedures | Machine-specific lockout procedure; all energy sources; isolation points; verification | LOTO procedure (Stage 6), OSHA 29 CFR 1910.147 |
| Proof testing procedures | How to perform proof tests on each safety function; required frequency; pass/fail criteria; what to do if a proof test fails | Safety manual — proof test section |
| Safety component replacement | How to replace safety-rated components; substitution restrictions; what to verify after replacement; when to contact the manufacturer | Safety manual — spare parts and maintenance section |
| Safety PLC program management | How to verify program CRC/signature; how to detect unauthorized changes; how to restore from backup; who is authorized to modify | Safety manual — software section |
| Calibration procedures | How to calibrate safety-rated instruments; required frequency; calibration standards; documentation requirements | Maintenance manual, calibration procedures |
| Troubleshooting safety circuits | How to safely troubleshoot safety circuit issues; what NOT to do (no jumpers, no bypasses without MOC) | Safety manual, maintenance manual |
| Management of change | Understanding that any modification to safety functions requires MOC process; who to contact; what approvals are needed | Safety manual — modification restrictions section |

#### Step 27: Documentation Handover

| Document Package | Recipient | Content |
|-----------------|-----------|---------|
| End-user documentation package | Customer operations / maintenance | Safety manual (final), operating instructions (final), maintenance manual (final), LOTO procedure, as-built schematics, BOM, spare parts list |
| Configuration backup media | Customer controls/IT | PLC programs (safety and standard), HMI application, drive parameters, safety controller configuration — on secure media with verification instructions |
| V&V report | Customer engineering / safety | Complete V&V report with all test records |
| Calibration records | Customer maintenance / quality | All instrument calibration records with calibration intervals established |
| Training records | Customer HR / safety | Training attendance records, training content outline, trainee acknowledgment signatures |
| Warranty information | Customer | Warranty terms, contact information, support procedures |

#### Step 28: Formal Acceptance and Handover

| Activity | Detail |
|---------|--------|
| Final walk-through | Project engineer, safety engineer, and customer representative walk through the machine; review all safety device locations; review all documentation; address any final questions |
| Punchlist closure verification | Confirm all FAT and SAT punchlist items are closed; customer agrees all items are resolved |
| Formal acceptance signature | Customer signs acceptance document acknowledging: machine is installed, commissioned, tested, documented, and training has been provided |
| Handover of operational responsibility | From this point, the customer is responsible for operating the machine per the safety manual and maintaining the safety functions per the maintenance plan |
| Warranty period begins | Per contract terms |
| Support transition | Ongoing support arrangements (if any) documented — contact information, response time commitments, spare parts agreements |

**★ GATE: System Handed Over to Operations ★**

---

## 6. Key Deliverables

| # | Deliverable | Description |
|---|------------|-------------|
| 1 | **V&V report (complete)** | Comprehensive verification and validation report per Section 5.7 Step 20 — the definitive safety lifecycle evidence document |
| 2 | **V&V summary matrix** | Single-page summary of all safety functions with required PLr/SIL, achieved PL/SIL, response time results, and validation status |
| 3 | **Safety function validation test records** | Individual test record for each safety function — under actual conditions, with all test elements documented |
| 4 | **Response time measurement records** | Calibrated measurements for each safety function with response time requirements — instrument identification, calibration date, multiple trials, maximum value |
| 5 | **Safety distance verification records** | Recalculated safety distances using actual measured response times; compared to installed distances |
| 6 | **Fault injection test records** | Results of each fault injection test with expected and actual response |
| 7 | **Combined / interaction test records** | Results of simultaneous and interaction testing |
| 8 | **Muting validation records (if applicable)** | Muting tested under actual conditions per IEC 62046 |
| 9 | **Mode-dependent behavior validation records** | Safety behavior verified in each operating mode |
| 10 | **FAT report (if applicable)** | Complete FAT documentation with test records, punchlist, and sign-off |
| 11 | **SAT report (if applicable)** | Complete SAT documentation with test records, punchlist, and sign-off |
| 12 | **As-built documentation (final revision)** | Final schematics, BOM, I/O table, cable schedule, panel layout — "As-Built" revision incorporating all changes |
| 13 | **Safety manual (final)** | Final version incorporating commissioning findings, achieved PL/SIL values, proof test procedures, and maintenance requirements |
| 14 | **Operating instructions (final)** | Final version |
| 15 | **Maintenance manual (final)** | Final version with proof test procedures and calibration intervals |
| 16 | **Technical file (complete)** | All elements per Machinery Directive Annex VII (or equivalent for non-CE) |
| 17 | **Declaration of Conformity (signed)** | Signed, dated, with CE marking applied (if applicable) |
| 18 | **Software version records (final)** | Final CRC/signatures for safety PLC, standard PLC, HMI, drives |
| 19 | **Configuration backup (final)** | Complete backup of all software and configuration — definitive version for operation |
| 20 | **Training records** | Operator and maintenance training attendance, content, and acknowledgment signatures |
| 21 | **Formal acceptance record** | Customer signature accepting the system |
| 22 | **Commissioning punchlist (closed)** | All punchlist items resolved and closed |
| 23 | **Test equipment calibration records** | Calibration certificates for all instruments used during commissioning — particularly response time measurement instruments |

---

## 7. Exit Criteria — Gate Review

This stage is complete when **all** of the following are true:

| # | Criterion | Evidence |
|---|-----------|----------|
| 1 | Every safety function validated under actual or representative operating conditions | Safety function validation test records — all PASS |
| 2 | Response times measured with calibrated instruments for all safety functions with response time requirements | Response time measurement records — all PASS |
| 3 | Safety distances verified using actual measured response times | Safety distance verification records — all PASS |
| 4 | Fault injection testing completed for all testable fault conditions | Fault injection test records — all expected responses confirmed |
| 5 | Combined / interaction testing completed | Interaction test records — no conflicts, correct priority behavior |
| 6 | Muting validation completed under actual conditions (if applicable) | Muting validation records — all PASS |
| 7 | Mode-dependent behavior validated in all operating modes | Mode test records — all PASS |
| 8 | Endurance / repeatability testing completed | Endurance test records — consistent behavior confirmed |
| 9 | FAT completed and punchlist closed (if applicable) | FAT report and closed punchlist |
| 10 | SAT completed and punchlist closed (if applicable) | SAT report and closed punchlist |
| 11 | V&V report compiled with all evidence sections complete | Complete V&V report |
| 12 | V&V summary matrix shows all safety functions PASS | V&V summary matrix — all PASS |
| 13 | As-built documentation is at final revision reflecting all changes | Final as-built document set |
| 14 | Safety manual is final and issued | Final safety manual |
| 15 | Technical file is complete (if CE marking) | Technical file completeness checklist — all items present |
| 16 | Declaration of Conformity is signed (if CE marking) | Signed Declaration of Conformity |
| 17 | Software version records are final; configuration backup is created and stored | Final software records; backup confirmed |
| 18 | Operator training completed | Training records signed |
| 19 | Maintenance training completed | Training records signed |
| 20 | Documentation handed over to customer | Handover transmittal record |
| 21 | Formal acceptance signed by customer | Acceptance document signed |
| 22 | All commissioning punchlist items closed | Closed punchlist |
| 23 | Test equipment calibration records on file | Calibration certificates |
| 24 | V&V report reviewed and signed by commissioning engineer, safety engineer, and project engineer | Signed V&V report |

**If any safety function fails validation, it must be investigated and corrected. The correction may require returning to an earlier lifecycle stage (Stage 4 for architecture redesign, Stage 5 for circuit modification, Stage 7 for build change). After correction, the affected safety function must be re-validated. The V&V report must document the failure, the corrective action, and the successful re-validation.**

---

## 8. Handling Validation Failures

### 8.1 Failure Classification

| Failure Type | Example | Required Action |
|-------------|---------|----------------|
| **Response time exceeds requirement** | Measured 220ms; requirement is ≤200ms | Investigate root cause (slow brake, slow actuator, excessive logic scan time); reduce response time or increase safety distance; re-validate |
| **Safety function does not achieve safe state** | Machine does not fully stop; residual motion after safety function activates | Investigate root cause (brake failure, contactor not opening, drive not responding to STO); correct and re-validate |
| **Safety function does not detect fault** | EDM does not detect simulated contactor welding; cross-channel discrepancy not detected | Investigate wiring, configuration, and logic; correct and re-validate; if unresolvable, DC claim must be reduced and PL/SIL recalculated |
| **Safety distance insufficient** | Actual measured response time results in required safety distance > installed distance | Move safety device further from hazard (if space permits); reduce response time; add physical barrier; re-validate |
| **Spurious trips during normal operation** | Safety function activates without a genuine safety demand | Investigate root cause (EMI, vibration, misalignment, wiring issue, software logic error); correct without reducing safety integrity; re-validate |
| **Muting does not function correctly** | Muting engages when it should not; or does not engage when it should | Investigate muting sensor positioning, timing, and logic; correct per IEC 62046; re-validate |
| **Interaction between safety functions** | Activating one safety function prevents another from functioning correctly | Investigate logic and wiring; correct priority and independence; re-validate |

### 8.2 Failure Documentation

Every validation failure must be documented:

| Field | Content |
|-------|---------|
| SF-ID and safety function name | Which function failed |
| Test reference | Which test, date, conditions |
| Failure description | What happened vs what was expected |
| Root cause analysis | Why the failure occurred |
| Corrective action | What was done to correct the failure |
| Impact assessment | Does the corrective action affect PL/SIL calculation, CCF score, DC claim, response time, or safety distance? |
| Re-validation | Test record for the re-validation after corrective action — same test procedure, same acceptance criteria |
| Re-validation result | PASS/FAIL |
| Approved by | Safety engineer signature confirming corrective action and re-validation are adequate |

### 8.3 Returning to Earlier Stages

| Corrective Action Required | Stage to Return To |
|---------------------------|-------------------|
| Architecture redesign (different category, different components, different redundancy) | Stage 4 — re-design architecture, re-calculate PL/SIL, then forward through Stages 5–10 for affected scope |
| Circuit modification (additional wiring, different component, additional diagnostic) | Stage 5 — modify design, then forward through Stages 6–10 for affected scope |
| Build change (re-wire, replace component, add component) | Stage 7 — implement change with NCR process, then forward through Stages 8–10 for affected scope |
| Installation change (move safety device, reroute cable, change safety distance) | Stage 8 — implement change with field change process, then forward through Stages 9–10 for affected scope |
| Software change (modify safety program logic, change parameters) | Stage 4.5 — modify software, re-verify, then forward through Stages 7–10 for affected scope |
| Risk assessment revision (PLr/SIL target change) | Stage 3 — re-assess risk, assign new target, then forward through all subsequent stages for affected scope |

**Any return to an earlier stage must follow the same rigor as the original stage — including documentation, review, and verification.**

---

## 9. Roles and Responsibilities at This Stage

| Role | Responsibility |
|------|---------------|
| **Commissioning Engineer** | Owns this stage — executes commissioning test procedures, performs response time measurements, compiles test records, authors commissioning sections of V&V report |
| **Safety / Controls Engineer** | Reviews and approves all safety function validation results; performs or reviews fault injection testing; authors safety sections of V&V report; confirms achieved PL/SIL; signs V&V report; signs Declaration of Conformity (if authorized) |
| **PLC Programmer** | Supports commissioning with software adjustments (parameter tuning, timing adjustments); resolves any software issues found during commissioning; finalizes software versions and CRC/signatures |
| **Electrical / Controls Designer** | Updates as-built documentation for any commissioning changes; supports troubleshooting of wiring or circuit issues |
| **Mechanical / Process Engineer** | Supports initial machine run and process parameter tuning; provides mechanical stopping time data for response time analysis; resolves any mechanical issues found during commissioning |
| **Project Engineer** | Coordinates commissioning schedule; manages FAT/SAT logistics; manages punchlist resolution; coordinates with customer |
| **Project Manager** | Overall responsibility for project completion; manages handover process; ensures all deliverables are complete; manages customer relationship |
| **Customer Representative / Witness** | Witnesses FAT/SAT tests per contract; reviews documentation; provides acceptance signature |
| **Customer Operations** | Participates in operator training; begins operating the machine under supervision; provides feedback on operating procedures |
| **Customer Maintenance** | Participates in maintenance training; reviews maintenance manual and proof test procedures; begins maintenance program |
| **Independent Verifier** | For SIL 2+ (per IEC 61508/61511) or complex PL d/e systems: independent person reviews V&V report and confirms that validation evidence is adequate — should not be the same person who designed or commissioned the safety functions |
| **Quality / Compliance** | Verifies technical file completeness; verifies Declaration of Conformity content; verifies document revision control |
| **Technical Writer** | Finalizes end-user documentation (safety manual, operating instructions, maintenance manual) incorporating commissioning findings and customer feedback |

---

## 10. Common Mistakes at This Stage

| Mistake | Consequence | How to Avoid |
|---------|-------------|-------------|
| Measuring response time with a stopwatch | Human reaction time (200–500ms) makes stopwatch measurements unreliable for safety-critical response times; auditors will not accept stopwatch measurements for safety function validation | Use calibrated instruments (high-speed timer, oscilloscope, data logger, manufacturer test equipment) with documented calibration |
| Using the average response time instead of the maximum | Safety distance must protect against worst-case stopping time; using the average understates the risk | Always use the maximum measured value for safety distance calculation; perform multiple trials (minimum 5) |
| Testing safety functions only in automatic mode | Safety functions may behave differently in manual, setup, or maintenance modes — mode-specific issues are missed | Test every safety function in every operating mode specified in the safety function register |
| Not performing fault injection testing | Safety system's response to component failures is unvalidated; diagnostic functions (EDM, cross-monitoring) are not proven to work in the field | Perform fault injection testing for all testable fault conditions per Section 5.5 Step 15 |
| Not testing interaction between safety functions | Individual safety functions may work correctly in isolation but conflict when activated simultaneously | Perform combined/interaction testing per Section 5.5 Step 16 |
| Signing Declaration of Conformity before validation is complete | The machine is declared compliant before evidence of compliance exists; if a safety function subsequently fails validation, the Declaration is false | Declaration of Conformity is signed ONLY after all safety functions pass validation and the technical file is complete |
| Not training operators and maintenance personnel before handover | Operators do not understand safety functions, residual risks, or emergency procedures; maintenance personnel cannot perform proof tests or replace safety components | Training is a deliverable of this stage, not an afterthought; training must be completed before formal handover |
| Not finalizing the safety manual | End user does not have the information needed to maintain safety functions for the life of the machine; proof test procedures are missing; residual risks are not communicated | Safety manual must be finalized at this stage with achieved PL/SIL values, proof test procedures, and all operational safety information |
| V&V report is incomplete or poorly organized | Auditor cannot follow the evidence chain from risk assessment through design to validation; compliance cannot be demonstrated | Use the V&V report structure in Section 5.7 Step 20; include the V&V summary matrix; ensure every safety function has a complete evidence chain |
| Not creating a final configuration backup | If the PLC or safety controller is damaged, corrupted, or replaced, the program must be reloaded; without a verified final backup reflecting all commissioning changes, the program must be recreated from scratch or restored from a pre-commissioning version that may not include commissioning adjustments | Create final configuration backup after all commissioning changes are complete; verify backup by comparing CRC/signature to the loaded program; store backup securely in project records AND provide a copy to the customer |
| Not documenting commissioning changes | Changes made during commissioning (parameter adjustments, wiring corrections, software modifications) are not reflected in the as-built documentation; documentation delivered to customer does not match the actual installed system | Mandatory as-built update process — every commissioning change documented in a commissioning change log and incorporated into formal document revisions before handover |
| Accepting "close enough" on response time measurements | Measured response time is 195ms against a 200ms requirement — accepted without margin analysis; future component degradation (brake wear, contactor aging) may push actual response time over the limit | Apply a safety margin — if measured response time is within 10% of the limit, investigate whether degradation over the machine's life could cause exceedance; document the margin analysis; consider specifying a tighter in-service limit for proof testing |
| Not verifying safety function behavior during startup sequence | Safety function works during steady-state operation but does not activate correctly during the startup sequence (e.g., safety controller has not completed initialization when machine begins moving) | Test safety function triggering during every phase of startup — including the period between power-on and full operational state |
| Commissioning engineer is the same person who designed the safety system | Independence of validation is compromised; design errors may not be detected because the designer has the same blind spots during validation | For SIL 2+ (per IEC 61508/61511) and best practice for PLd/PLe: validation should involve at least one person who was not responsible for the design; document the independence assessment |
| Not performing endurance/repeatability testing | A safety function that works once may not work consistently over hundreds of activations — intermittent wiring faults, contact bounce, timing races may only appear under repeated operation | Perform minimum 5 repetitions of each safety function test; perform extended operation monitoring (4–8 hours minimum); document consistency |
| Punchlist items left open at handover | Customer accepts the machine with unresolved deficiencies; items are never completed; safety-related punchlist items create ongoing risk | Classify punchlist items by severity; safety-related items must be closed before handover (no exceptions); non-safety items may be deferred with customer agreement and documented resolution plan |
| Not verifying that FAT punchlist items were actually resolved | FAT identified deficiencies; punchlist was generated; but resolution was not verified during SAT or commissioning — deficiencies may still exist | SAT or commissioning must include verification that all FAT punchlist items were resolved; do not assume — verify |
| Calibration certificates for test equipment not retained | Response time measurements were made with a high-speed timer, but the calibration certificate is not on file; auditor cannot verify that the measurement instrument was accurate | Retain calibration certificates for every instrument used during commissioning; include instrument identification and calibration dates in every measurement record |
| Not testing e-stop from every station | E-stop at station 1 was tested during pre-commissioning; e-stop at stations 2 and 3 were assumed to be identical and not tested during commissioning under actual conditions | Test every e-stop device at every station during commissioning — under actual operating conditions; each station has unique wiring and may have unique failure modes |
| Muting validated with only one product size | Muting works correctly with the standard product but fails with the smallest or largest product in the range — or engages incorrectly with no product present | Test muting with the full range of product sizes/shapes; test with no product; test with person-sized objects; test with partial products |

---

## 11. Independence of Validation

### 11.1 Requirement

| Standard | Independence Requirement |
|----------|------------------------|
| **ISO 13849-1:2023 §8.1** | Validation shall be performed; standard does not explicitly require independence for PL a–c, but recommends it for PL d–e |
| **IEC 62061:2021 §6.9** | Validation shall be planned and performed; independence recommended but not mandated for SIL 1 |
| **IEC 61508-1:2010 Table 5** | Independence requirements scale with SIL: SIL 1 — independent person; SIL 2 — independent department; SIL 3/4 — independent organization |
| **IEC 61511-1:2016 §5.2.6** | SIL 1 — independent person; SIL 2 — independent department; SIL 3 — independent organization; SIL 4 — independent organization |

### 11.2 Practical Implementation

| Level | Description | When Required | Implementation |
|-------|-------------|--------------|----------------|
| **Independent person** | Validation performed or reviewed by a person who did not design or implement the safety function | SIL 1 (IEC 61508/61511); best practice for all PL/SIL levels | Commissioning engineer or reviewer is a different person than the design engineer |
| **Independent department** | Validation performed or reviewed by a person from a different organizational department than the design team | SIL 2 (IEC 61508/61511); recommended for PL d/e | Separate commissioning team or quality/safety department reviews validation results |
| **Independent organization** | Validation performed or reviewed by an external organization (third-party assessor, notified body, independent safety consultancy) | SIL 3/4 (IEC 61508/61511); may be required by customer specification or regulatory authority | External functional safety assessment (FSA) |

### 11.3 Documenting Independence

The V&V report must document the independence of the validation:

| Element | Documentation |
|---------|--------------|
| Design team members | Names and roles of persons who designed the safety functions |
| Validation team members | Names and roles of persons who performed and reviewed validation |
| Independence assessment | Statement confirming that validation personnel were independent from design personnel at the required level |
| If independence requirement cannot be met | Document the limitation, the reason, and the compensating measures (e.g., additional review, more rigorous testing, management sign-off) |

---

## 12. Process Safety Specific — SIS Commissioning and Validation (IEC 61511)

### 12.1 Additional Requirements for SIS

IEC 61511 imposes specific commissioning and validation requirements beyond those for machinery safety:

| Requirement | IEC 61511 Reference | Detail |
|------------|---------------------|--------|
| **SIF validation** | §16.2 | Each safety instrumented function (SIF) must be validated to confirm it meets the safety requirements specification — including logic, final elements, and sensors as a complete function |
| **Proof test procedure validation** | §16.3 | The proof test procedures that will be used during operation (Stage 11) must be validated during commissioning — confirm that the proof test actually reveals the failure modes it is intended to detect |
| **Partial stroke testing validation (if used)** | §16.3 | If partial stroke testing is part of the proof test strategy for valves, validate that partial stroke testing actually detects the relevant failure modes and provides the claimed diagnostic coverage |
| **Bypass management validation** | §16.2 | Validate that bypass/override procedures work correctly — bypass is indicated, time-limited, and automatically removed (or alarmed if not removed) |
| **Demand mode verification** | §16.2 | Confirm that the SIF is operating in the correct demand mode (low demand vs high demand/continuous) as assumed in the SIL calculation |
| **SIF response time validation** | §16.2 | Measure end-to-end SIF response time including sensor, logic solver, and final element — compare to the process safety time (the time available between the hazardous condition being detected and the hazardous event occurring) |
| **Process safety time verification** | §16.2 | Confirm that the process safety time assumed in the design is valid — the SIF response time must be significantly less than the process safety time |

### 12.2 SIF Validation Test Record Template

| SIF-ID | Safety Instrumented Function | SIL Target | Sensor(s) | Logic Solver | Final Element(s) | Test Conditions | Triggering Condition Applied | Safe State Achieved? | Response Time Measured | Process Safety Time | Response Time < Process Safety Time? | Proof Test Procedure Validated? | Bypass Management Validated? | Overall Result | Tested By | Witnessed By |
|--------|---------------------------|-----------|-----------|-------------|-----------------|----------------|---------------------------|---------------------|----------------------|--------------------|------------------------------------|-------------------------------|-----------------------------| --------------|-----------|-------------|
| SIF-01 | High pressure trip | SIL 2 | PT-101A/B (1oo2) | SIS Logic Solver | XV-101A/B (1oo2) | Process at normal operating conditions | Simulated high pressure signal injected at transmitter | Y/N | ___s | 10s | Y/N | Y/N | Y/N | PASS/FAIL | | |

### 12.3 Pre-Startup Acceptance Test (PSAT)

For SIS applications, the Pre-Startup Acceptance Test (PSAT) is the formal final test before the process is started with the SIS in service. It includes:

| PSAT Element | Content |
|-------------|---------|
| SIF end-to-end testing | Every SIF tested from sensor through logic to final element |
| Communication testing | SIS communication with BPCS, HMI, and historian verified |
| Bypass management testing | All bypass functions tested and verified |
| Manual shutdown testing | Manual SIS trip from all trip stations verified |
| Power failure testing | SIS response to power loss verified (UPS function, fail-safe state) |
| PSAT documentation | Complete test records with pass/fail for each SIF |
| PSAT sign-off | SIS engineer, process engineer, operations representative, and safety representative sign-off |

---

## 13. Relationship to Adjacent Stages

```
┌──────────────────────────────────────┐
│  STAGE 9: PRE-COMMISSIONING          │
│                                      │
│  Provides:                           │
│  • Pre-commissioning checklist       │
│    (completed)                       │
│  • Safety function dry-run test      │
│    records (all PASS)                │
│  • Calibration records               │
│  • Baseline measurements             │
│  • System verified as correctly      │
│    wired, configured, and basically  │
│    functional                        │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  STAGE 10: COMMISSIONING AND          │  ◄── You are here
│  VALIDATION                           │
│  ★ FINAL PL/SIL PROOF ★             │
│                                      │
│  Produces:                           │
│  • V&V report (complete)             │
│  • Validated safety functions        │
│  • Measured response times           │
│  • Verified safety distances         │
│  • FAT/SAT reports                   │
│  • Final as-built documentation      │
│  • Final safety manual               │
│  • Signed Declaration of Conformity  │
│  • Complete technical file           │
│  • Training records                  │
│  • Formal acceptance                 │
└──────────────────┬───────────────────┘
                   │
                   │  System handed over to operations
                   ▼
┌──────────────────────────────────────┐
│  STAGE 11: MAINTENANCE                │
│                                      │
│  Uses from this stage:               │
│  • Safety manual (final) — defines   │
│    proof test procedures, intervals, │
│    maintenance requirements          │
│  • V&V report — reference for what   │
│    was validated and the acceptance  │
│    criteria for each safety function │
│  • Response time measurements —      │
│    baseline for detecting            │
│    degradation during proof tests    │
│  • Calibration records — baseline    │
│    for detecting instrument drift    │
│  • Configuration backup — reference  │
│    for detecting unauthorized        │
│    program changes                   │
│  • Training records — basis for      │
│    retraining schedule               │
│                                      │
│  Maintains:                          │
│  • Safety functions at their         │
│    validated PL/SIL through          │
│    periodic proof testing,           │
│    calibration, and component        │
│    replacement                       │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  STAGE 12: MANAGEMENT OF CHANGE       │
│                                      │
│  Triggered when:                     │
│  • Any modification to the validated │
│    system is proposed                │
│  • Component substitution is needed  │
│  • Software change is requested      │
│  • Process change affects safety     │
│    functions                         │
│  • Proof test reveals degradation    │
│    requiring design change           │
│                                      │
│  MOC routes back to the appropriate  │
│  lifecycle stage for the scope of    │
│  the change — and re-validation      │
│  through this stage is required for  │
│  the affected safety functions       │
└──────────────────────────────────────┘
```

### Traceability Chain — Complete

The V&V report closes the traceability chain that runs through the entire lifecycle:

```
┌──────────────────────────────────────────────────────────────┐
│  COMPLETE TRACEABILITY CHAIN                                  │
│                                                              │
│  Hazard (Stage 3)                                            │
│    └─► Safety Function (Stage 3)                             │
│          └─► PLr/SIL Target (Stage 3)                        │
│                └─► Safety Requirements Specification (3.5)    │
│                      └─► Architecture Design (Stage 4)       │
│                            └─► PL/SIL Calculation (Stage 4)  │
│                                  └─► Detailed Design (Stage 5)│
│                                        └─► Build (Stage 7)   │
│                                              └─► Install (8) │
│                                                    └─► Pre-  │
│                                                       Comm(9)│
│                                                         └─►  │
│                                                     Validation│
│                                                      (Stage10)│
│                                                         └─►  │
│                                                    V&V Report │
│                                                              │
│  Every link in this chain must be documented.                │
│  The V&V report is the document that proves the              │
│  chain is complete and unbroken.                             │
│                                                              │
│  If any link is missing, the safety function is not          │
│  fully verified and validated.                               │
└──────────────────────────────────────────────────────────────┘
```

---

## 14. Post-Commissioning Obligations

### 14.1 Warranty Period Monitoring

| Activity | Detail |
|---------|--------|
| Monitor safety function performance during warranty | Track any safety function issues reported during the warranty period — spurious trips, diagnostic faults, component failures |
| Warranty claim assessment | For any safety-related warranty claim: assess whether the issue affects PL/SIL; determine if the issue existed at commissioning or developed in service; determine corrective action |
| Warranty-period modifications | Any modification during the warranty period must follow the MOC process (Stage 12) — even if performed by the manufacturer |

### 14.2 Post-Commissioning Support

| Activity | Detail |
|---------|--------|
| First proof test support | Manufacturer may support the customer's first proof test cycle — verify that the customer's maintenance team can execute proof tests per the safety manual procedures |
| Lessons learned | Conduct a lessons-learned review of the project — identify what worked well and what should be improved for future projects; feed improvements back into the lifecycle process |
| Customer feedback integration | Collect customer feedback on documentation quality, training effectiveness, and machine operation — incorporate into documentation updates if warranted |

### 14.3 Document Retention

| Document | Retention Period | Standard Reference |
|---------|-----------------|-------------------|
| Technical file (CE marking) | Minimum 10 years after the last machine of the type was manufactured | Machinery Directive Art. 5 / Machinery Regulation Art. 10 |
| V&V report | Life of the machine plus retention period per company policy | Good practice; IEC 61508/61511 recommend retention for the life of the safety system |
| Risk assessment | Life of the machine | ISO 12100; good practice |
| PL/SIL calculations | Life of the machine | ISO 13849-1; IEC 62061 |
| Training records | Per company policy and regulatory requirements | OSHA requires training documentation |
| Calibration records | Life of the machine or per quality management system | IEC 61511; quality management requirements |
| Configuration backups | Life of the machine — updated with every authorized change | Good practice; IEC 62443 |

---

## 15. Templates and Tools

| Resource | Purpose |
|----------|---------|
| V&V report template | Structured document per Section 5.7 Step 20 with all sections pre-formatted |
| V&V summary matrix template | Spreadsheet per Section 5.7 — single-page summary of all safety functions |
| Safety function validation test record template | Per Section 5.5 Step 10 — individual form per safety function |
| Response time measurement record template | Per Section 5.5 Step 11 — with instrument identification, multiple trials, and maximum value calculation |
| Safety distance verification worksheet | Spreadsheet for recalculating safety distance using actual measured response times |
| Fault injection test record template | Form per Section 5.5 Step 15 — fault description, expected response, actual response |
| Combined / interaction test record template | Form per Section 5.5 Step 16 |
| FAT procedure template | Structured test procedure with sign-off blocks and customer witness points |
| FAT report template | Summary report with test results, punchlist, and sign-off |
| SAT procedure template | Structured test procedure for site conditions |
| SAT report template | Summary report with test results, punchlist, and sign-off |
| Commissioning punchlist template | Deficiency tracking form with severity classification, responsible party, target date, and resolution status |
| Commissioning change log template | Log of all changes made during commissioning with safety impact assessment |
| Training record template | Attendance record with training topics, date, trainer, and trainee acknowledgment signature |
| Formal acceptance document template | Customer acceptance signature form with conditions (if any) |
| SIF validation test record template (process safety) | Per Section 12.2 — for IEC 61511 applications |
| PSAT checklist template (process safety) | Per Section 12.3 — for SIS pre-startup acceptance |
| Independence assessment record template | Per Section 11.3 — documenting validation independence |
| High-speed timer / data logger | For calibrated response time measurement — the single most important test instrument at this stage |
| Safety device manufacturer test equipment | Manufacturer-specific instruments for validating their safety devices (alignment tools, test instruments, diagnostic software) |
| Response time measurement setup guide | Step-by-step guide for connecting measurement instruments to safety circuits for response time measurement — trigger and stop channel definitions per safety function type |

---

## Navigation

← [Stage 9: Pre-Commissioning]({{ '/lifecycle/pre-commissioning/' | relative_url }}) | [Stage 11: Maintenance]({{ '/lifecycle/maintenance/' | relative_url }}) →
