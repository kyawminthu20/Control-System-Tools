---
layout: default
title: "Lifecycle Stage 11 — Maintenance and Lifecycle Support"
description: "Proof testing at defined intervals, preventive maintenance, bypass management, and MOC — sustaining safety integrity across the full operational life."
redirect_from:
  - /lifecycle/maintenance/
  - /lifecycle/maintenance/index.html
breadcrumb:
  - name: "Lifecycle"
    url: "/verification/lifecycle/"
  - name: "11. Maintenance"
related_standards:
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
---

<div class="page-header">
  <span class="page-header__label">Lifecycle Stage 11</span>
  <h1>Maintenance and Lifecycle Support</h1>
</div>

## 1. Purpose of This Stage

This stage ensures that the safety performance validated at Stage 10 is **maintained throughout the entire operational life of the machine** — which may be 20 years or more. Safety functions degrade over time. Components wear. Contacts corrode. Springs fatigue. Sensors drift. Seals deteriorate. Software configurations get changed. Maintenance personnel who were trained at commissioning leave and are replaced by people who were not.

The PL/SIL calculation performed in Stage 4 is based on assumptions about component reliability, diagnostic coverage, and — critically — **proof test intervals**. The calculated PFHd or PFDavg assumes that dangerous undetected failures are revealed and corrected at defined intervals. If proof testing does not happen, or happens less frequently than assumed, the actual safety integrity degrades below the calculated level, and the safety function no longer provides the risk reduction assigned in Stage 3.

This is the longest stage in the lifecycle — it spans from handover (end of Stage 10) to decommissioning (Stage 13). It is also the stage most commonly neglected. The engineering team that designed and commissioned the system has moved on to other projects. The customer's operations and maintenance teams inherit responsibility for a safety system they did not design. The safety manual and proof test procedures created in earlier stages are the primary tools that bridge this gap.

This stage has three parallel, ongoing tracks:

- **Proof testing:** Periodic testing of safety functions to reveal dangerous undetected failures
- **Preventive maintenance:** Scheduled maintenance activities that preserve safety function integrity — calibration, component replacement, inspection
- **Reactive maintenance:** Response to failures, diagnostic alerts, and degradation discovered during operation or proof testing

This stage does **not** cover modifications to the safety system — that is Stage 12 (Management of Change). This stage covers maintaining the system **as designed and validated**. Any change to the system — component substitution, software modification, process change — triggers Stage 12.

> **This stage answers: Are the safety functions maintained at their validated PL/SIL throughout the operational life of the machine, with documented evidence that an auditor can verify at any point in time?**

---

## 2. Entry Criteria

This stage begins when **Stage 10 (Commissioning and Validation) is complete** and the system has been formally handed over to the customer/end user.

### Required Inputs

| Input | Source (Stage) | Why It Matters |
|-------|---------------|----------------|
| Safety manual (final) | Stage 10 | Defines proof test procedures, maintenance requirements, spare parts, component replacement intervals, and operational safety information — this is the primary maintenance reference document |
| Maintenance manual (final) | Stage 10 | Detailed maintenance procedures, calibration procedures, and preventive maintenance schedules |
| V&V report | Stage 10 | Reference for what was validated and the acceptance criteria — proof tests must verify the same criteria |
| Safety function register (finalized) | Stage 3/4 | Master reference for all safety functions — proof tests must cover every function in this register |
| Response time measurements (baseline) | Stage 9/10 | Baseline values for comparison during proof testing — degradation is detected by comparing current measurements to baseline |
| Calibration records (baseline) | Stage 9/10 | As-left values from initial calibration — drift is detected by comparing current as-found values to previous as-left values |
| Baseline measurements | Stage 9 | All baseline measurements (valve stroke times, motor currents, vibration levels, contactor operation counts) |
| PL/SIL calculation reports | Stage 4 | Contains the proof test interval assumptions — maintenance must test at the intervals assumed in the calculation |
| Configuration backup (final) | Stage 10 | Reference for detecting unauthorized software or configuration changes |
| Software version records (final) | Stage 10 | CRC/signatures for all safety software — verified during proof testing |
| As-built documentation (final) | Stage 10 | Schematics, BOM, I/O table — reference for troubleshooting and component replacement |
| Spare parts list | Stage 10 (safety manual) | Safety-rated components with exact part numbers and substitution restrictions |
| Training records | Stage 10 | Baseline training — retraining schedule must be established |
| LOTO procedure | Stage 6/10 | Machine-specific lockout procedure for all maintenance activities |
| CCF scoring worksheets | Stage 4 | Reference for understanding which installation conditions must be maintained (separation, environmental protection) |
| Fault exclusion register | Stage 4 | Reference for understanding which conditions must remain true for fault exclusions to remain valid |

### Maintenance Program Establishment

Before routine maintenance begins, the following must be established:

| Element | Action | Responsible |
|---------|--------|-------------|
| Proof test schedule | Establish calendar-based schedule for proof testing each safety function at the intervals specified in the safety manual / PL/SIL calculation | Maintenance manager / safety engineer |
| Calibration schedule | Establish calendar-based schedule for calibrating each safety-rated instrument at the intervals specified | Maintenance manager / instrument technician |
| Component replacement schedule | Establish schedule for mandatory component replacement based on mission time (B10d life, T10d life, manufacturer-specified replacement intervals) | Maintenance manager / safety engineer |
| Maintenance personnel assignment | Assign qualified personnel to safety-related maintenance activities; verify competency | Maintenance manager |
| Spare parts inventory | Stock critical safety-rated spare parts per the spare parts list — availability of correct spare parts is essential for timely repair | Maintenance manager / procurement |
| Maintenance documentation system | Establish a system for recording all maintenance activities, proof test results, calibration records, and component replacements — must be auditable | Maintenance manager / quality |
| Retraining schedule | Establish schedule for periodic retraining of operators and maintenance personnel on safety functions, proof testing, and emergency procedures | Training coordinator / safety manager |
| Management of change procedure | Establish (or confirm existing) MOC procedure per Stage 12 — maintenance personnel must understand when a maintenance activity crosses the line into a modification requiring MOC | Safety manager |

---

## 3. Standards Influence

| Standard | Role at This Stage | Key Requirements |
|----------|-------------------|-----------------|
| **ISO 13849-1:2023 §10** | Information for use — requires the manufacturer to provide maintenance information including: safety function descriptions, required PL, conditions for maintaining PL, maintenance instructions, and proof test requirements | §10.1 (general), §10.2 (information for maintenance), §10.3 (conditions for maintaining PL) |
| **ISO 13849-1:2023 §7.1.4** | Mission time — default 20 years; if component life is shorter than mission time, mandatory replacement interval must be defined and communicated to the user | §7.1.4 (mission time and component replacement) |
| **IEC 62061:2021 §6.8** | Documentation requirements including maintenance information | §6.8 |
| **IEC 61511-1:2016 §16** | Proof testing and inspection requirements for SIS — defines proof test effectiveness, proof test intervals, and the relationship between proof test coverage and PFDavg | §16.2 (proof testing), §16.3 (inspection and maintenance) |
| **IEC 61511-1:2016 §17** | Management of change — any modification during operation triggers MOC (see Stage 12) | §17 |
| **IEC 61508-1:2010 §7.6** | Operation and maintenance phase requirements — periodic testing, maintenance procedures, documentation | §7.6 |
| **IEC 61508-1:2010 §7.7** | Modification — routes to Stage 12 (MOC) | §7.7 |
| **OSHA 29 CFR 1910.147** | Lockout/Tagout — all maintenance activities on the machine must follow LOTO procedures | All applicable sections |
| **OSHA 29 CFR 1910.119** | Process Safety Management — for process safety applications, requires mechanical integrity programs, pre-startup safety reviews for modifications, and management of change | §(j) mechanical integrity, §(i) pre-startup safety review, §(l) management of change |
| **OSHA 29 CFR 1910.212** | General machine guarding — guards and safety devices must be maintained in working order | §1910.212 |
| **NFPA 79:2024** | Maintenance of machine electrical equipment — requires that electrical equipment be maintained in a condition that preserves the safety features of the original design | General requirement |
| **IEC 60204-1:2016 §18** | Periodic verification — suggests periodic re-verification of PE continuity and insulation resistance | §18 (referenced for periodic testing) |
| **ISO 14119:2013 §10** | Maintenance of interlocking devices — specific requirements for inspection and testing of guard interlock devices | §10 |
| **Manufacturer maintenance instructions** | Every safety-rated component has manufacturer-specified maintenance requirements — inspection intervals, cleaning, lubrication, replacement intervals | Per component |

---

## 4. Proof Testing — The Core Maintenance Activity

### 4.1 What Is Proof Testing?

Proof testing is the **periodic functional testing of a safety function to reveal dangerous undetected failures** that have accumulated since the last test. Between proof tests, dangerous failures may occur that are not detected by the safety system's built-in diagnostics (because no diagnostic system has 100% coverage). These undetected failures reduce the actual safety integrity below the calculated level.

The proof test reveals these failures so they can be corrected, restoring the safety function to its full calculated integrity.

```
                     Proof Test         Proof Test         Proof Test
                        │                   │                   │
Safety                  │                   │                   │
Integrity  ─────────────┤                   │                   │
(PFDavg)                │\                  │\                  │\
                        │ \                 │ \                 │ \
                        │  \ Degradation    │  \ Degradation    │  \
                        │   \ (undetected   │   \ (undetected   │   \
                        │    \ failures)    │    \ failures)    │    \
                        │     \             │     \             │     \
                        │      │            │      │            │      │
                        │  Restored by      │  Restored by      │  Restored
                        │  proof test       │  proof test       │  by proof
                        │                   │                   │  test
                        ▼                   ▼                   ▼
```

**If proof tests are not performed at the assumed interval, the degradation between tests is greater than calculated, and the actual PFDavg (or PFHd) exceeds the SIL (or PL) limit.**

### 4.2 Proof Test Interval Determination

The proof test interval is determined during design (Stage 4) and is a critical input to the PL/SIL calculation:

| Framework | How Proof Test Interval Affects the Calculation |
|-----------|----------------------------------------------|
| **ISO 13849-1 (PL pathway)** | Mission time is the primary factor (default 20 years); proof testing within the mission time is addressed through component replacement intervals and diagnostic test intervals. The standard assumes that Category 2 test frequency is "reasonably practicable" (typically at machine startup or at defined intervals). |
| **IEC 62061 (SIL pathway for machinery)** | Proof test interval (T1) directly affects PFHd calculation for subsystems with less than 100% diagnostic coverage. Longer intervals → higher PFHd → harder to achieve SIL target. |
| **IEC 61511 (SIL pathway for process safety)** | Proof test interval directly affects PFDavg calculation. This is the most explicit and quantitative relationship: PFDavg = λDU × T1/2 (simplified for 1oo1 architecture). Doubling the proof test interval approximately doubles the PFDavg. |

**The proof test interval specified in the safety manual is not a suggestion — it is a design assumption. If the interval is not maintained, the calculated PL/SIL is not valid.**

### 4.3 Proof Test Coverage

Not all proof tests are equal. The **proof test coverage** is the fraction of dangerous undetected failures that the proof test can actually reveal:

| Proof Test Coverage | Description | Example |
|--------------------|-------------|---------|
| 100% (complete proof test) | The proof test reveals all possible dangerous undetected failures | Full functional test of safety function from sensor through logic to final element, including fault simulation |
| < 100% (partial proof test) | The proof test reveals some but not all possible dangerous undetected failures | Testing only the logic response without verifying mechanical valve operation; or testing valve closure without verifying valve seating integrity |

**For IEC 61511 applications, partial proof test coverage directly affects the PFDavg calculation. If the proof test only achieves 60% coverage, 40% of dangerous undetected failures remain undetected even after the proof test — and the effective proof test interval for those failures is the time until a complete overhaul or replacement.**

### 4.4 Proof Test Procedures — General Requirements

Every safety function must have a documented proof test procedure. The procedure must be:

| Requirement | Detail |
|------------|--------|
| **Specific** | Step-by-step instructions that a qualified technician can follow without ambiguity — not "test the safety function" but "open guard door GD-01; verify press ram stops within 200ms; verify HMI displays 'Guard Door 1 Open' alarm; verify restart is prevented until door is closed and reset button PB-01 is pressed" |
| **Complete** | Tests the safety function end-to-end — from the input device through the logic solver to the output device and the actual mechanical/process safe state |
| **Measurable** | Has quantitative acceptance criteria derived from the safety function specification — response time, trip point, safe state achieved (yes/no), diagnostic detection (yes/no) |
| **Safe** | Can be performed without creating a hazardous condition — or if the machine must be running for the test, compensating measures are defined (restricted access, reduced speed, dedicated observer) |
| **Documented** | Produces a record that can be retained and audited — date, tester, results, pass/fail, any deviations |
| **Repeatable** | The same test performed by different qualified technicians produces the same result |

### 4.5 Proof Test Procedures — By Safety Function Type

#### 4.5.1 Guard Interlock (Mechanical Guard with Safety Switch)

| Step | Action | Acceptance Criteria | Record |
|------|--------|--------------------| --------|
| 1 | Verify machine is running in automatic mode (or capable of running) | Machine in production-ready state | Mode confirmed |
| 2 | Open guard door | — | — |
| 3 | Verify machine stops | All hazardous motion ceases; output contactors de-energize (verify by contactor position or by monitoring safety controller output status) | Machine stopped: Y/N; Time to stop (if measured): ___ms |
| 4 | Verify HMI alarm | HMI displays correct alarm for this guard interlock | Alarm displayed: Y/N; Correct alarm text: Y/N |
| 5 | Attempt to restart machine with guard open | Machine must NOT restart | Restart prevented: Y/N |
| 6 | Close guard door | — | — |
| 7 | Attempt to restart machine without pressing reset | Machine must NOT restart (manual reset required) | Auto-restart prevented: Y/N |
| 8 | Press reset button; start machine | Machine restarts normally | Normal restart: Y/N |
| 9 | Verify safety controller diagnostics | No diagnostic errors related to this safety function in the safety controller log | Diagnostics clear: Y/N |
| 10 | Verify switch condition | Visual inspection of guard switch — no physical damage, mounting secure, actuator alignment correct, no signs of corrosion or contamination | Switch condition: Good / Degraded / Failed |
| 11 | Test EDM function (if time for detailed test) | With guard closed and machine ready: disconnect one contactor feedback wire; verify safety controller detects fault and prevents restart | EDM fault detected: Y/N |

#### 4.5.2 Emergency Stop

| Step | Action | Acceptance Criteria | Record |
|------|--------|--------------------| --------|
| 1 | Verify machine is running in automatic mode | Machine in production-ready state | Mode confirmed |
| 2 | Press e-stop at Station [X] | — | Station ID: ___ |
| 3 | Verify all hazardous motion stops | All motors stop; all actuators reach safe state; all safety outputs de-energize | All motion stopped: Y/N |
| 4 | Verify HMI alarm | Correct e-stop alarm displayed | Alarm displayed: Y/N |
| 5 | Attempt to restart with e-stop latched | Machine must NOT restart | Restart prevented: Y/N |
| 6 | Release (unlatch) e-stop | E-stop device releases mechanically; verify by feel and visual | Released: Y/N |
| 7 | Attempt to restart without pressing reset | Machine must NOT restart (manual reset required after e-stop) | Auto-restart prevented: Y/N |
| 8 | Press reset; start machine | Machine restarts normally | Normal restart: Y/N |
| 9 | Repeat steps 1-8 for EVERY e-stop station | Each station tested individually | Station 1: P/F; Station 2: P/F; Station 3: P/F; etc. |
| 10 | Verify e-stop device condition | Red mushroom-head on yellow background; no damage; latching mechanism functional; positive-opening contacts (verify by feel — distinct snap) | Device condition: Good / Degraded / Failed |

#### 4.5.3 Light Curtain / AOPD

| Step | Action | Acceptance Criteria | Record |
|------|--------|--------------------| --------|
| 1 | Verify machine is running in automatic mode | Machine in production-ready state | Mode confirmed |
| 2 | Interrupt light curtain beam with test piece (diameter = minimum object detection size per device specification) | — | Test piece diameter: ___mm |
| 3 | Verify machine stops | All hazardous motion in the protected zone ceases within required response time | Machine stopped: Y/N |
| 4 | Measure response time (if this is a response time proof test) | Use calibrated timer or manufacturer test equipment | Response time: ___ms; Requirement: ≤___ms; PASS/FAIL |
| 5 | Verify HMI alarm | Correct light curtain alarm displayed | Alarm displayed: Y/N |
| 6 | Remove test piece from beam | Beam restores | Beam restored: Y/N |
| 7 | Verify reset/restart behavior | Per design — manual reset or automatic restart as specified | Correct restart behavior: Y/N |
| 8 | Check alignment | Verify alignment indicators on light curtain are within acceptable range | Alignment: Good / Marginal / Failed |
| 9 | Clean lenses | Clean emitter and receiver lenses per manufacturer instructions | Lenses cleaned: Y/N |
| 10 | Verify detection zone coverage | Walk through all access paths; verify light curtain detects entry on every path; verify no reach-around, reach-over, or reach-under is possible | Coverage adequate: Y/N |
| 11 | Test muting function (if applicable) | Run product through muting sequence; verify muting engages and disengages correctly; verify muting does not engage for person-sized objects | Muting correct: Y/N |
| 12 | Verify manufacturer self-test | Check light curtain diagnostic indicators; verify self-test passes | Self-test: PASS / FAIL |

#### 4.5.4 Safety-Rated Drive Function (STO, SS1, SLS)

| Step | Action | Acceptance Criteria | Record |
|------|--------|--------------------| --------|
| 1 | Verify machine is running at production speed | Drive operating normally | Speed: ___RPM |
| 2 | Trigger the safety function that activates the drive safety function (e.g., guard open triggers STO) | — | Triggering event: ___ |
| 3 | Verify drive enters correct safe state | STO: motor torque removed immediately; SS1: controlled deceleration followed by STO; SLS: speed limited to safe value | Correct safe state: Y/N |
| 4 | Verify drive safety function diagnostic status | Check drive safety function status via drive diagnostic display or safety controller | Diagnostics: No faults |
| 5 | Verify recovery | Clear triggering condition; reset; restart | Normal recovery: Y/N |
| 6 | For SLS: verify speed limit | Command speed above SLS limit; verify drive limits speed to the safe value or trips | Speed limited correctly: Y/N |

#### 4.5.5 Safety Instrumented Function — SIS (IEC 61511)

| Step | Action | Acceptance Criteria | Record |
|------|--------|--------------------| --------|
| 1 | Notify operations that SIF proof test is in progress | Operations acknowledges; compensating measures in place (manual monitoring, temporary bypass with indication if necessary) | Operations notified: Y/N; Bypass authorized: Y/N |
| 2 | Record as-found values | Before making any adjustments: record current sensor readings, trip point settings, valve position, valve stroke time | As-found sensor reading: ___; As-found trip point: ___; As-found valve stroke time: ___s |
| 3 | Test sensor(s) | Inject known signal (calibrator) or apply actual process condition; verify sensor output is correct | Sensor 1 output: ___mA at ___[units]; Error: __%; Within tolerance: Y/N |
| 4 | Test logic solver | Verify logic solver responds correctly to sensor signal at the trip point; verify correct output command is generated | Trip point activation: Y/N at ___[value]; Output commanded: Y/N |
| 5 | Test final element(s) | Verify valve/actuator responds to logic solver command; verify full stroke to safe position; measure stroke time | Valve stroke: Full / Partial / Failed; Stroke time: ___s; Within specification: Y/N |
| 6 | Verify complete SIF end-to-end | From sensor input through logic to final element safe state | End-to-end function: Y/N |
| 7 | Calibrate sensor (if required) | If as-found values are outside tolerance: calibrate to correct values; record as-left values | As-left sensor reading: ___; Calibration adjustment: Yes / No |
| 8 | Record as-left values | After any adjustments: record all values | As-left values recorded: Y/N |
| 9 | Return system to normal operation | Remove bypass (if used); verify bypass indication clears; verify SIF is back in service; notify operations | SIF returned to service: Y/N; Bypass removed: Y/N; Operations notified: Y/N |
| 10 | Analyze as-found vs as-left | Compare as-found values to previous as-left values (from last proof test or from Stage 9 baseline) to detect drift or degradation | Drift within acceptable range: Y/N; Degradation detected: Y/N |

### 4.6 Proof Test Schedule Management

| Requirement | Detail |
|------------|--------|
| **Calendar-based scheduling** | Proof tests scheduled on a calendar — not "when we get around to it." Use the facility's CMMS (Computerized Maintenance Management System) or equivalent scheduling tool. |
| **Overdue management** | If a proof test becomes overdue: the safety function is operating beyond its calculated integrity basis. Escalate immediately to safety engineer/safety manager. Assess the risk of continued operation without proof test. Perform the proof test as soon as practicable. Document the overdue period and the risk assessment. |
| **Test interval tracking** | Record the actual date of each proof test; calculate the actual interval between tests; verify the actual interval does not exceed the specified interval. |
| **Staggered scheduling** | For systems with many safety functions: stagger proof tests so they do not all fall on the same date, minimizing production disruption. Ensure staggering does not cause any individual function to exceed its specified interval. |
| **Outage coordination** | Coordinate proof tests with planned maintenance outages or production shutdowns — many proof tests require the machine to be stopped or placed in a specific state. |

### 4.7 Proof Test Documentation

#### Proof Test Record Template

| Field | Content |
|-------|---------|
| SF-ID / SIF-ID | Safety function identifier |
| Safety function description | Brief description |
| Proof test procedure reference | Document number and revision of the procedure used |
| Proof test date | Date test was performed |
| Previous proof test date | Date of last proof test (or Stage 10 commissioning date if first proof test) |
| Actual interval since last test | Calendar days or months |
| Specified interval | From safety manual / PL/SIL calculation |
| Interval within specification? | Yes / No (if No — document overdue justification) |
| Tested by | Name and qualification of person performing the test |
| Test results | Step-by-step results per proof test procedure — each step pass/fail |
| As-found values (if applicable) | Sensor readings, trip points, valve stroke times, response times before any adjustment |
| As-left values (if applicable) | Values after any adjustment |
| Drift / degradation analysis | Comparison of as-found to previous as-left — trend identification |
| Overall result | PASS / FAIL |
| If FAIL: corrective action | Description of failure, root cause, corrective action taken, re-test result |
| Follow-up required? | Yes / No — if yes, describe (e.g., component replacement scheduled, engineering review required, MOC triggered) |
| Supervisor / safety engineer review | Signature and date |

### 4.8 Proof Test Failure Response

```
Proof test result = FAIL
        │
        ▼
┌─────────────────────────────────┐
│ Is the safety function currently │
│ protecting against a hazard?     │
└─────────────┬───────────────────┘
              │
        ┌─────┴──────┐
        ▼            ▼
       YES           NO (machine is shut down
        │             or hazard is not present)
        ▼                    │
┌────────────────┐           │
│ IMMEDIATE       │           │
│ ACTION:         │           │
│                 │           │
│ • Assess risk   │           │
│   of continued  │           │
│   operation     │           │
│ • If risk is    │           │
│   intolerable:  │           │
│   STOP machine  │           │
│ • If risk can   │           │
│   be managed:   │           │
│   implement     │           │
│   compensating  │           │
│   measures      │           │
│   (manual       │           │
│   monitoring,   │           │
│   restricted    │           │
│   operation,    │           │
│   increased     │           │
│   supervision)  │           │
│ • Time-limit    │           │
│   compensating  │           │
│   measures      │           │
└────────┬───────┘           │
         │                   │
         └─────────┬─────────┘
                   ▼
┌──────────────────────────────────┐
│ CORRECTIVE ACTION                 │
│                                  │
│ • Diagnose root cause            │
│ • Repair or replace failed       │
│   component                      │
│ • If repair is like-for-like     │
│   replacement: no MOC required   │
│ • If repair requires different   │
│   component or design change:    │
│   → Stage 12 (MOC)              │
│ • Re-test safety function after  │
│   repair (proof test procedure)  │
│ • Document failure, root cause,  │
│   corrective action, and re-test │
│   result                         │
└──────────────────────────────────┘
```

### 4.9 Proof Test Trend Analysis

Over time, proof test records reveal trends that inform maintenance strategy:

| Trend Observed | Interpretation | Action |
|---------------|---------------|--------|
| Instrument drift increasing over successive proof tests | Sensor degradation — approaching end of useful life | Reduce calibration interval; plan sensor replacement |
| Valve stroke time increasing | Valve wear, buildup, or actuator degradation | Plan valve maintenance or replacement; consider partial stroke testing between full proof tests |
| Response time increasing | Component degradation (contactor slowing, brake wear, drive response degradation) | Investigate root cause; repair or replace affected component; verify response time is still within requirement |
| Contactor operation count approaching B10d limit | Contactor is approaching its rated dangerous failure life | Plan contactor replacement before reaching B10d limit |
| Repeated failure of the same component | Systematic issue — wrong component for the application, environmental stress, installation deficiency | Engineering review — may require design change (→ Stage 12 MOC) |
| All proof tests consistently pass with no drift | System is healthy; current maintenance program is adequate | Continue current program; document positive trend |
| As-found values significantly different from as-left values | Indicates either rapid degradation, environmental stress, or possible tampering/unauthorized modification | Investigate root cause; check for unauthorized changes; review environmental conditions; increase monitoring frequency |

---

## 5. Preventive Maintenance

### 5.1 Safety-Specific Preventive Maintenance Activities

| Activity | Frequency Basis | What to Do |
|----------|----------------|------------|
| **Visual inspection of safety devices** | Monthly or per manufacturer recommendation | Check for physical damage, corrosion, contamination, loose mounting, misalignment, damaged cables, damaged lenses (optical devices), damaged actuators |
| **Light curtain / laser scanner lens cleaning** | Monthly or more frequently in dusty/dirty environments | Clean lenses per manufacturer instructions; verify alignment indicators after cleaning |
| **Guard interlock switch inspection** | Quarterly or per manufacturer recommendation | Check actuator alignment, mounting bolt tightness, cable condition, switch body condition, coding integrity (coded switches) |
| **E-stop device inspection** | Quarterly | Check mushroom-head for damage, color fading, or sticking; verify latching and release mechanism; check yellow background plate visibility |
| **Contactor inspection** | Per manufacturer recommendation or at proof test intervals | Check for signs of arc erosion on contacts (if accessible); verify contactor operation (listen for clean pull-in and drop-out); check coil resistance (if applicable); verify auxiliary contact operation |
| **Safety relay / safety controller inspection** | Annually | Check LED status indicators; review diagnostic log for any accumulated errors; verify firmware version unchanged; verify configuration CRC unchanged |
| **Cable and wiring inspection** | Annually | Check for cable damage (especially at flex points and cable entries); check for insulation degradation; check for rodent damage; check terminal tightness (re-torque if required) |
| **Enclosure inspection** | Annually | Check door gaskets for damage; check glands and seals for integrity; check for moisture ingress or contamination; check cooling system (fans, filters, heat exchangers) |
| **PE continuity re-verification** | Annually or per facility standard | Re-measure PE continuity from exposed conductive parts to PE terminal — ≤ 0.1Ω; compare to baseline; investigate any increase |
| **Insulation resistance re-verification** | Every 2-5 years or per facility standard | Megger test on power circuits — ≥ 1 MΩ; compare to baseline; investigate any decrease |
| **Safety PLC program verification** | At every proof test or annually (whichever is more frequent) | Read CRC/signature from safety controller; compare to approved CRC/signature on file; if mismatch → investigate immediately (possible unauthorized change) |
| **Drive safety parameter verification** | Annually | Verify safety-related drive parameters match approved values; if mismatch → investigate |
| **Guard integrity inspection** | Monthly | Check fixed guards for secure mounting, no missing fasteners, no gaps; check interlocked guards for correct operation; check guard condition (no bending, cracking, or holes) |
| **Safety distance re-verification** | After any mechanical change to the machine or guard positioning | Re-measure safety distances; compare to requirements |
| **Pneumatic/hydraulic safety system inspection** | Per manufacturer recommendation | Check safety valves for leakage; verify dump valve operation; check pressure switch calibration; check accumulator pre-charge (if applicable) |

### 5.2 Preventive Maintenance Schedule Template

| PM Task | Safety Function(s) Affected | Frequency | Last Performed | Next Due | Performed By | Record Reference |
|---------|---------------------------|-----------|---------------|----------|-------------|-----------------|
| Guard interlock switch inspection — GS-01 | SF-01 | Quarterly | 2024-01-15 | 2024-04-15 | | |
| E-stop device inspection — all stations | SF-02 | Quarterly | 2024-01-15 | 2024-04-15 | | |
| Light curtain lens cleaning — LC-01 | SF-03 | Monthly | 2024-02-15 | 2024-03-15 | | |
| Safety PLC program CRC verification | All SFs | Annually | 2024-01-15 | 2025-01-15 | | |
| PE continuity re-verification | All | Annually | 2024-01-15 | 2025-01-15 | | |
| Contactor inspection — K1, K2, K3, K4 | SF-01, SF-02, SF-03 | Annually | 2024-01-15 | 2025-01-15 | | |

### 5.3 Component Replacement Based on Mission Time

ISO 13849-1 §7.1.4 defines a default mission time of 20 years. If any safety-rated component has a useful life shorter than the mission time, it must be replaced at the specified interval:

| Component Type | Typical Replacement Driver | How to Determine Replacement Interval |
|---------------|--------------------------|--------------------------------------|
| **Electromechanical contactors** | B10d life — based on number of dangerous-failure operations | MTTFd = B10d / (0.1 × nop); replace when accumulated operations approach B10d; or replace at fixed calendar interval based on estimated annual operations |
| **Safety interlock switches** | B10d life — based on number of actuations | Track actuations (if counter available) or estimate from cycle rate; replace when approaching B10d |
| **E-stop devices** | Mechanical wear, contact degradation | Manufacturer-specified replacement interval or per proof test findings |
| **Light curtains** | Optical degradation, electronic aging | Manufacturer-specified service life; typically 10-20 years; replace if self-test failures increase |
| **Safety relays** | Electronic component aging | Manufacturer-specified service life; typically 10-20 years |
| **Batteries (safety controller backup)** | Battery life | Manufacturer-specified interval; typically 3-5 years |
| **Pressure transmitters (SIS)** | Sensor drift, diaphragm degradation | Based on proof test drift analysis and manufacturer recommendation |
| **Safety valves (SIS)** | Valve seat wear, actuator spring degradation | Based on proof test stroke time analysis, partial stroke test results, and manufacturer recommendation |
| **Cables in flex applications** | Flex fatigue | Manufacturer-specified flex life; or based on visual inspection and continuity testing |

**When replacing a safety-rated component:**

| Step | Requirement |
|------|------------|
| 1 | Use the exact part number specified in the BOM / spare parts list |
| 2 | If the exact part number is not available, **do not substitute without engineering review** — route through Stage 12 (MOC) |
| 3 | After replacement: perform proof test on the affected safety function(s) |
| 4 | Document: date, component replaced (old part number, new part number), reason for replacement, proof test result |
| 5 | Reset the component life counter (if tracked) |
| 6 | Update maintenance records |

---

## 6. Instrument Calibration

### 6.1 Calibration Program Requirements

| Requirement | Detail |
|------------|--------|
| **Calibration interval** | Defined in the safety manual / maintenance manual; based on manufacturer recommendation, regulatory requirements, and proof test drift analysis |
| **Traceable reference standards** | Calibration must be performed against reference standards with traceable calibration certificates |
| **As-found and as-left values** | Always record as-found values before adjustment and as-left values after adjustment — this is essential for drift analysis and proof test coverage assessment |
| **Calibration tolerance** | Defined per instrument specification and safety function requirements — the calibration tolerance must be tighter than the safety function trip point tolerance to ensure the safety function activates at the correct process value |
| **Calibration procedure** | Documented procedure — same procedure used every time for repeatability |
| **Calibration records** | Retained for the life of the instrument; auditable; include instrument tag, serial number, range, applied inputs, measured outputs, error, tolerance, pass/fail, calibrator identification, technician identification, date |

### 6.2 Safety-Rated Instrument Calibration — Additional Requirements

| Additional Requirement | Detail |
|----------------------|--------|
| **Proof test coverage** | Calibration is a component of the proof test — but calibration alone may not constitute a complete proof test (it verifies the sensor but may not verify the logic or final element) |
| **Drift analysis** | Track as-found values over multiple calibration cycles; calculate drift rate; use drift data to validate or adjust the calibration interval |
| **Calibration interval adjustment** | If drift analysis shows excessive drift: shorten the calibration interval. If drift is consistently minimal: interval may be extended (with engineering justification and documentation). |
| **Out-of-tolerance response** | If as-found value is out of tolerance: assess the impact — was the safety function capable of performing its function during the period since the last calibration? If not, this is a **revealed dangerous failure** — report it, assess the risk exposure, and document. |

### 6.3 Calibration Record Template

| Field | Content |
|-------|---------|
| Instrument tag | Field device identifier |
| Instrument description | Type, manufacturer, model |
| Serial number | Unique serial number |
| Location | Physical location on the machine |
| Safety function reference | SF-ID / SIF-ID |
| Calibration date | Date performed |
| Previous calibration date | Date of last calibration |
| Calibration interval | Specified interval |
| Interval within specification? | Yes / No |
| Calibrator used | Calibrator model, serial number, calibration due date |
| Range | Instrument range (0-100 PSI, 4-20mA, etc.) |
| As-found values | Readings at 0%, 25%, 50%, 75%, 100% of range — before adjustment |
| As-found within tolerance? | Yes / No (for each point) |
| Adjustments made | Description of any adjustments |
| As-left values | Readings at 0%, 25%, 50%, 75%, 100% of range — after adjustment |
| As-left within tolerance? | Yes / No (for each point) — must be Yes for all points |
| Drift from previous as-left | Difference between current as-found and previous as-left at each point |
| Drift within acceptable limits? | Yes / No |
| Overall result | PASS / FAIL |
| If FAIL: corrective action | Replace instrument, re-calibrate, engineering review |
| Performed by | Technician name and qualification |
| Reviewed by | Supervisor / safety engineer |

---

## 7. Reactive Maintenance — Responding to Failures and Diagnostics

### 7.1 Safety System Diagnostic Alerts

Modern safety controllers continuously monitor their own operation and generate diagnostic alerts for detected faults. The maintenance response to these alerts is critical:

| Diagnostic Alert Type | Typical Cause | Required Response | Urgency |
|----------------------|--------------|------------------|---------|
| **Channel discrepancy** | One channel of a dual-channel input differs from the other | Safety controller typically enters safe state or fault state; investigate cause (wiring fault, sensor failure, mechanical misalignment); repair and verify both channels before returning to service | Immediate — machine is in safe/fault state |
| **EDM fault (contactor feedback)** | Contactor did not open (welded) or feedback wiring is faulty | Safety controller prevents restart; investigate contactor (welded contacts? mechanical jam?); replace contactor if welded; verify feedback wiring; proof test after repair | Immediate — machine cannot restart |
| **Communication loss** | Safety network cable failure, node failure, or EMI | Safety controller enters safe state; investigate cable integrity, connector condition, network node status; repair and verify communication before returning to service | Immediate — machine is in safe state |
| **Ground fault detected** | Insulation breakdown on safety circuit wiring | Investigate location of ground fault (megger testing with circuits isolated); repair insulation or replace cable; verify ground fault is cleared | High — safety circuit integrity is compromised |
| **Safety device self-test failure** | Light curtain, laser scanner, or safety sensor internal fault | Device typically locks out; replace or repair per manufacturer instructions; proof test after repair | High — safety function is unavailable |
| **Watchdog timeout** | Safety controller internal fault | Safety controller enters safe state; cycle power; if fault persists, replace safety controller; verify configuration after replacement | Immediate — safety controller failure |
| **Over-temperature** | Enclosure cooling failure, ambient temperature exceedance | Investigate cooling system (fan failure, filter clogged, heat exchanger failure); repair cooling; verify temperatures return to normal; check component ratings | High — component reliability is affected |

### 7.2 Reactive Maintenance Documentation

Every reactive maintenance event on a safety system must be documented:

| Field | Content |
|-------|---------|
| Date and time of event | When the fault was detected or reported |
| Safety function(s) affected | SF-ID(s) |
| Description of fault | What was observed — diagnostic alert, machine behavior, operator report |
| Machine status during fault | Running, stopped, safe state, fault state |
| Immediate action taken | Machine stopped, compensating measures implemented, etc. |
| Root cause investigation | What caused the fault |
| Corrective action | What was done to fix it — component replaced, wiring repaired, configuration corrected |
| Component replaced (if any) | Old part number, new part number, serial number (if applicable) |
| Substitution verification | If component was replaced: was the exact part number used? If not, was MOC performed? |
| Proof test after repair | Results of proof test on affected safety function(s) after repair |
| Return to service | Date and time safety function was returned to full service |
| Downtime | Total time safety function was unavailable |
| Follow-up required? | Any additional actions needed — engineering review, MOC, design change |
| Documented by | Maintenance technician |
| Reviewed by | Maintenance supervisor / safety engineer |

### 7.3 Failure Reporting and Analysis

For significant or recurring safety system failures, perform a more detailed failure analysis:

| Analysis Element | Content |
|-----------------|---------|
| Failure mode | How the component failed (stuck closed, open circuit, drift, mechanical breakage, etc.) |
| Failure cause | Why it failed (wear, environmental stress, overvoltage, vibration, contamination, manufacturing defect, installation error) |
| Was the failure detected by diagnostics? | Yes (diagnostic detected it) / No (found during proof test or by operator observation) |
| If detected by diagnostics: was the diagnostic response correct? | Did the safety controller enter the correct state? Did the correct alarm appear? |
| If NOT detected by diagnostics: was this failure within the scope of the diagnostic coverage? | If yes — the diagnostic failed and must be investigated. If no — this is a dangerous undetected failure that would only be found by proof testing (which is expected behavior). |
| Impact on safety function | Was the safety function degraded? For how long? Was the remaining redundancy (if any) sufficient to maintain safety? |
| Risk assessment of the failure | Was there a period where the safety function was unable to perform? If so, what was the risk exposure? |
| Corrective action to prevent recurrence | Component upgrade, environmental protection, shortened proof test interval, design change (→ MOC), training improvement |
| Trend analysis | Is this a recurring failure? If so, systemic corrective action is required. |

---

## 8. Bypass and Override Management During Maintenance

### 8.1 Principle

During maintenance, it may be necessary to bypass or override safety functions — for example, to perform proof testing, to access guarded areas for repair, or to troubleshoot a safety circuit. Bypasses during maintenance are permitted but must be **controlled, documented, time-limited, and compensated.**

### 8.2 Bypass Requirements

| Requirement | Detail |
|------------|--------|
| **Authorization** | Every bypass must be authorized by a designated person (maintenance supervisor, safety engineer, or per facility bypass management procedure) |
| **Documentation** | Bypass logged with: safety function ID, reason, authorizer, date/time applied, compensating measures, expected duration |
| **Compensating measures** | While the safety function is bypassed, alternative risk control measures must be in place: restricted access, manual monitoring, reduced speed, dedicated observer, temporary barriers |
| **Visible indication** | Bypass must be visible — warning sign on machine, HMI indication, physical tag on bypassed device, status lamp |
| **Time limitation** | Bypass has a defined maximum duration; if exceeded, escalate to management for re-authorization or machine shutdown |
| **Automatic alerting** | If the safety controller supports bypass timers or alarms: configure to alert if bypass exceeds the time limit |
| **Removal verification** | After maintenance is complete: bypass must be removed; safety function must be proof-tested to confirm full operation; bypass log entry must show "removed and verified" |
| **No permanent bypasses** | A bypass that becomes permanent is a modification — it must be routed through Stage 12 (MOC) and the risk assessment (Stage 3) must be updated |

### 8.3 Bypass Log Template

| Bypass # | SF-ID | Safety Function | Reason | Authorized By | Date/Time Applied | Compensating Measures | Maximum Duration | Date/Time Removed | Removal Verified By | Proof Test After Removal | Proof Test Result |
|---------|-------|----------------|--------|--------------|------------------|---------------------|-----------------|------------------|--------------------|-----------------------|------------------|
| | | | | | | | | | | | |

---

## 9. Competency Management

### 9.1 Requirement

Personnel performing safety-related maintenance must be competent to do so. Competency is not just training — it is training plus demonstrated ability plus ongoing verification.

| Standard | Competency Requirement |
|----------|----------------------|
| **IEC 61511-1 §5.2.6** | Competency requirements for persons carrying out safety lifecycle activities — including maintenance |
| **IEC 61508-1 §6** | Competency requirements for functional safety management |
| **ISO 13849-1 §10** | Information for use must include the competency level expected of maintenance personnel |
| **OSHA 29 CFR 1910.147** | LOTO training requirements for authorized employees |

### 9.2 Competency Requirements for Safety Maintenance Personnel

| Competency Area | What They Must Know | How to Verify |
|----------------|--------------------| --------------|
| **Safety function understanding** | What each safety function does, why it exists, what happens if it fails | Written or verbal assessment; observation during proof testing |
| **Proof test procedures** | How to execute each proof test procedure correctly, including acceptance criteria and failure response | Supervised execution of proof test; assessment of results |
| **LOTO procedures** | Machine-specific lockout procedure; all energy sources; verification methods | LOTO training record; observed LOTO execution |
| **Diagnostic interpretation** | How to read safety controller diagnostics; what each diagnostic alert means; what action to take | Assessment; observation during fault response |
| **Component replacement** | How to replace safety-rated components; substitution restrictions; post-replacement proof test requirement | Supervised component replacement |
| **Bypass management** | When bypass is permitted; how to apply and remove; documentation requirements; compensating measures | Assessment; review of bypass log entries |
| **When to escalate** | Recognition of situations requiring engineering review or MOC — not all maintenance actions are like-for-like repair | Assessment; review of maintenance decisions |
| **Documentation** | How to complete proof test records, calibration records, maintenance records | Review of completed records for accuracy and completeness |

### 9.3 Retraining

| Trigger | Retraining Required |
|---------|-------------------|
| New maintenance personnel assigned to safety systems | Full training before performing any safety-related maintenance |
| Significant time since last training (>2 years recommended) | Refresher training |
| Change to safety system (MOC completed) | Training on the changes and any new procedures |
| Proof test failure attributed to maintenance error | Targeted retraining on the specific procedure or competency gap |
| New standards or regulatory requirements | Training on new requirements affecting maintenance activities |
| Audit finding related to maintenance competency | Corrective training per audit finding |

---

## 10. Key Deliverables — Ongoing

Unlike previous stages, this stage produces **ongoing, recurring deliverables** throughout the life of the machine:

| # | Deliverable | Frequency | Description |
|---|------------|-----------|-------------|
| 1 | **Proof test records** | Per proof test interval for each safety function | Complete test record per Section 4.7 template — date, results, pass/fail, as-found/as-left values, trend analysis |
| 2 | **Calibration records** | Per calibration interval for each instrument | Complete calibration record per Section 6.3 template |
| 3 | **Preventive maintenance records** | Per PM schedule | Records of all scheduled PM activities — inspections, cleaning, component checks |
| 4 | **Component replacement records** | As needed | Records of all safety component replacements — old/new part numbers, reason, proof test after replacement |
| 5 | **Reactive maintenance records** | As needed | Records of all unplanned maintenance on safety systems — fault description, root cause, corrective action, proof test after repair |
| 6 | **Bypass log** | As needed | Records of all safety function bypasses during maintenance |
| 7 | **Failure analysis reports** | For significant or recurring failures | Detailed analysis per Section 7.3 |
| 8 | **Proof test trend analysis** | Annually (recommended) | Review of all proof test results for trends — drift rates, failure rates, component degradation |
| 9 | **Safety PLC program verification records** | Per verification interval | CRC/signature comparison records |
| 10 | **Maintenance personnel competency records** | Ongoing | Training records, assessment records, retraining records |
| 11 | **Safety system performance summary** | Annually (recommended) | Summary of all safety system activities for the year — proof tests, failures, repairs, bypasses, trends, recommendations |
| 12 | **Updated as-built documentation** | After any change (via MOC) | Schematics, BOM, software versions — updated to reflect current as-installed configuration |
| 13 | **Spare parts inventory records** | Ongoing | Tracking of safety spare parts inventory — consumption, reorder, availability |

---

## 11. Auditing and Compliance Verification

### 11.1 Internal Audit

| Audit Element | What to Verify | Frequency |
|--------------|---------------|-----------|
| Proof tests are being performed on schedule | Compare proof test records to scheduled dates; identify any overdue tests | Annually |
| Proof test results are documented and reviewed | All records complete; all failures investigated and corrected; trend analysis performed | Annually |
| Calibration is being performed on schedule | Compare calibration records to scheduled dates | Annually |
| Safety components are being replaced per life limits | Track component operation counts or calendar age against replacement criteria | Annually |
| Safety PLC program has not been modified without authorization | CRC/signature verification records show no unauthorized changes | Annually |
| Bypass management is being followed | Bypass log entries are complete; no permanent bypasses exist; all bypasses were removed and verified | Annually |
| Maintenance personnel are competent | Training records current; competency assessments performed | Annually |
| Spare parts inventory is adequate | Critical safety spare parts are in stock | Annually |
| Documentation is current | As-built documentation matches the actual installed system (especially important after any MOC) | Annually |
| No unauthorized modifications have been made | Physical inspection compared to as-built documentation; software CRC verification | Annually |

### 11.2 External Audit Readiness

An auditor (customer, regulatory authority, insurance inspector, third-party assessor) may review the safety maintenance program at any time. The following must be readily available:

| Document | Purpose |
|---------|---------|
| Safety manual | Reference for what the maintenance requirements are |
| Proof test schedule and records | Evidence that proof tests are being performed |
| Calibration schedule and records | Evidence that instruments are being calibrated |
| Component replacement records | Evidence that worn components are being replaced |
| Failure and corrective action records | Evidence that failures are being investigated and corrected |
| Bypass log | Evidence that bypasses are controlled |
| Training records | Evidence that personnel are competent |
| MOC records (from Stage 12) | Evidence that changes are controlled |
| V&V report (from Stage 10) | Reference for what was validated |
| PL/SIL calculations (from Stage 4) | Reference for proof test interval basis |

---

## 12. Exit Criteria — Stage Transition

This stage does not have exit criteria in the traditional sense — it continues for the life of the machine. However, there are **transition triggers** to other stages:

| Trigger | Transition |
|---------|-----------|
| Modification proposed (component substitution with different part, software change, process change, addition/removal of safety function) | → **Stage 12: Management of Change** |
| Proof test reveals systematic design deficiency requiring redesign | → **Stage 12: MOC** → re-enters lifecycle at appropriate stage (Stage 3, 4, or 5) |
| New standard published that affects the machine | → Engineering review; if changes required → **Stage 12: MOC** |
| Machine or system is to be decommissioned | → **Stage 13: Decommissioning** |
| Major overhaul or life extension | → Engineering review; may require re-validation → **Stage 10** (partial or full) |
| Change of ownership | → Review of maintenance program adequacy; training of new owner's personnel; handover of all records |

---

## 13. Roles and Responsibilities at This Stage

| Role | Responsibility |
|------|---------------|
| **Maintenance Technician** | Executes proof tests, calibrations, preventive maintenance, and reactive repairs per documented procedures; documents all activities; reports failures and anomalies |
| **Maintenance Supervisor / Manager** | Manages maintenance schedule; ensures proof tests and calibrations are performed on time; reviews maintenance records; authorizes bypasses; manages spare parts inventory; escalates issues requiring engineering review |
| **Safety Engineer / Safety Manager** | Reviews proof test results and trends; approves corrective actions for safety system failures; reviews bypass log; conducts or supports annual safety system performance review; determines when MOC is required; maintains competency requirements |
| **Operations Manager** | Ensures machine is available for scheduled proof tests and maintenance; ensures operators report safety system anomalies promptly; ensures bypass management procedures are followed by operations personnel |
| **Instrument Technician** | Performs instrument calibration per documented procedures; documents as-found and as-left values; reports out-of-tolerance conditions |
| **Controls Engineer** | Supports troubleshooting of complex safety system issues; verifies safety PLC program integrity; supports engineering review when maintenance findings indicate potential design issues |
| **Training Coordinator** | Manages retraining schedule; ensures new personnel receive safety system training before performing safety-related maintenance |
| **Quality / Compliance** | Conducts or supports internal audits of the safety maintenance program; ensures records are complete and auditable |
| **Management** | Provides resources (personnel, time, spare parts, training budget) for the safety maintenance program; ensures maintenance is not deferred due to production pressure |

---

## 14. Common Mistakes at This Stage

| Mistake | Consequence | How to Avoid |
|---------|-------------|-------------|
| Proof tests not performed on schedule | Actual PFDavg or PFHd exceeds the calculated value; safety function does not provide the required risk reduction; calculated PL/SIL is no longer valid | Schedule proof tests in CMMS; set up overdue alerts; escalate overdue tests immediately; management must not defer proof tests for production |
| Proof tests performed but not documented | No evidence that testing occurred; auditor finds non-compliance; failure trends cannot be analyzed | Mandatory documentation for every proof test — no record means it did not happen |
| As-found values not recorded before calibration adjustment | Cannot determine if the instrument drifted; cannot assess whether the safety function was operating correctly during the previous interval; proof test coverage is incomplete | Always record as-found values BEFORE making any adjustment |
| Safety component replaced with non-identical substitute | Different B10d, PFHd, or SFF values invalidate the PL/SIL calculation; safety function may not achieve the required integrity level | Use exact part numbers from the spare parts list; if exact part is unavailable, route through MOC (Stage 12) before substituting |
| "Minor" changes made without MOC | Any change to a safety function — even one that seems minor — can affect PL/SIL, CCF, DC, response time, or safety distance; uncontrolled changes accumulate and the system drifts from its validated state | Define clear criteria for what constitutes a change requiring MOC; train maintenance personnel to recognize when MOC is needed; when in doubt, initiate MOC |
| Bypasses become permanent | A "temporary" bypass during troubleshooting is never removed; the safety function is permanently disabled; risk is uncontrolled | Time-limit all bypasses; automatic alerting for overdue bypasses; periodic audit of bypass log; any permanent bypass requires MOC and risk assessment update |
| Proof test only tests part of the safety function | Testing the logic response but not the final element (e.g., verifying the PLC output changes but not verifying the contactor actually opens and the motor actually stops) | Proof test procedures must test end-to-end: from input device through logic to final element to actual safe state |
| Maintenance personnel not trained on safety systems | Incorrect proof test execution; incorrect fault response; incorrect component replacement; safety system integrity compromised | Mandatory training before performing any safety-related maintenance; competency assessment; retraining schedule |
| Safety PLC program modified without MOC | Unauthorized logic change may disable or alter safety function behavior; change is not reflected in documentation; PL/SIL may be affected | CRC/signature verification at every proof test; password-protect safety PLC programming access; access logging if available; any program change requires MOC |
| Proof test failures not investigated | Failed proof test is recorded but root cause is not determined; same failure recurs; systematic issue is not addressed | Every proof test failure must have a root cause investigation and corrective action; trend analysis identifies recurring issues |
| Spare parts not stocked | Safety component fails; exact replacement not available; production pressure leads to unauthorized substitution | Stock critical safety spare parts per the spare parts list; monitor inventory; reorder before stock is depleted |
| No trend analysis of proof test results | Gradual degradation goes unnoticed until a proof test failure occurs; preventive replacement opportunity is missed | Annual review of proof test trends — drift rates, failure rates, component degradation indicators |
| Maintenance records not retained | Historical evidence is lost; auditor cannot verify maintenance program effectiveness; failure trends cannot be analyzed | Retain all safety maintenance records for the life of the machine; use electronic document management system if possible |
| Production pressure overrides maintenance schedule | Proof tests deferred "until the next shutdown" which never comes; calibration intervals exceeded; component replacement deferred | Management commitment to safety maintenance schedule; safety maintenance is not optional; escalation procedure for deferred maintenance |

---

## 15. Relationship to Adjacent Stages

```
┌──────────────────────────────────────┐
│  STAGE 10: COMMISSIONING              │
│                                      │
│  Provides:                           │
│  • Safety manual (final)             │
│  • V&V report                        │
│  • Baseline measurements             │
│  • Configuration backup              │
│  • Training records                  │
│  • Formal handover                   │
│                                      │
│  Establishes:                        │
│  • The validated state that this     │
│    stage must maintain               │
└──────────────────┬───────────────────┘
                   │
                   │  System in operation
                   ▼
┌──────────────────────────────────────┐
│  STAGE 11: MAINTENANCE                │  ◄── You are here
│  (Ongoing for life of machine)       │
│                                      │
│  Maintains:                          │
│  • Safety functions at validated     │
│    PL/SIL through proof testing,     │
│    calibration, PM, and component    │
│    replacement                       │
│                                      │
│  Produces (ongoing):                 │
│  • Proof test records                │
│  • Calibration records               │
│  • PM records                        │
│  • Failure records                   │
│  • Bypass logs                       │
│  • Trend analysis                    │
│  • Competency records                │
│                                      │
│  Triggers (when needed):             │
│  • Stage 12 (MOC) — when any         │
│    change is required                │
│  • Stage 13 (Decommissioning) —      │
│    when machine reaches end of life  │
└──────────────┬──────────┬────────────┘
               │          │
               ▼          ▼
┌────────────────┐  ┌──────────────────┐
│ STAGE 12:      │  │ STAGE 13:        │
│ MANAGEMENT     │  │ DECOMMISSIONING  │
│ OF CHANGE      │  │                  │
│                │  │ When machine     │
│ Triggered by:  │  │ reaches end of   │
│ • Component    │  │ life or is       │
│   substitution │  │ removed from     │
│ • Software     │  │ service          │
│   change       │  │                  │
│ • Process      │  │                  │
│   change       │  │                  │
│ • Design       │  │                  │
│   modification │  │                  │
│                │  │                  │
│ Routes back to │  │                  │
│ the appropriate│  │                  │
│ lifecycle stage│  │                  │
│ and re-enters  │  │                  │
│ through to     │  │                  │
│ re-validation  │  │                  │
│ (Stage 10)     │  │                  │
│ for affected   │  │                  │
│ scope          │  │                  │
└────────────────┘  └──────────────────┘
```

---

## 16. Key Performance Indicators (KPIs) for Safety Maintenance

Consider tracking these KPIs to monitor the effectiveness of the safety maintenance program:

| KPI | Definition | Target |
|-----|-----------|--------|
| **Proof test completion rate** | Percentage of scheduled proof tests completed on time | 100% |
| **Proof test overdue count** | Number of proof tests currently overdue | 0 |
| **Proof test pass rate** | Percentage of proof tests that pass on first attempt | Track trend — decreasing rate indicates system degradation |
| **Calibration completion rate** | Percentage of scheduled calibrations completed on time | 100% |
| **Calibration out-of-tolerance rate** | Percentage of calibrations where as-found values are out of tolerance | Track trend — increasing rate indicates instrument degradation |
| **Safety system failure rate** | Number of safety system failures per year (by type: diagnostic-detected, proof-test-detected, demand-detected) | Track trend — increasing rate indicates system degradation |
| **Mean time to repair (MTTR) for safety systems** | Average time from safety system failure to return to service | Minimize — long MTTR means extended risk exposure |
| **Bypass duration** | Total hours of safety function bypass per year | Minimize — extended bypasses increase risk exposure |
| **Safety spare parts availability** | Percentage of critical safety spare parts in stock | 100% |
| **Training currency** | Percentage of maintenance personnel with current safety system training | 100% |
| **MOC compliance** | Percentage of safety system changes that followed the MOC process | 100% |

---

## 17. Templates and Tools

| Resource | Purpose |
|----------|---------|
| Proof test record template | Per Section 4.7 — individual test form per safety function |
| Proof test schedule template | Calendar-based schedule with all safety functions, intervals, and due dates |
| Calibration record template | Per Section 6.3 — instrument calibration form with as-found/as-left fields |
| Calibration schedule template | Calendar-based schedule with all instruments, intervals, and due dates |
| Preventive maintenance schedule template | Per Section 5.2 — all PM tasks with frequencies and due dates |
| Component replacement record template | Form for documenting safety component replacement |
| Reactive maintenance record template | Per Section 7.2 — fault documentation form |
| Failure analysis report template | Per Section 7.3 — detailed failure analysis form |
| Bypass log template | Per Section 8.3 — bypass tracking form |
| Proof test trend analysis worksheet | Spreadsheet for tracking as-found values, drift rates, and failure trends over time |
| Safety system annual performance summary template | Summary report template per Section 10 deliverable #11 |
| Maintenance personnel competency assessment form | Assessment checklist per Section 9.2 — competency areas, verification method, pass/fail, assessor signature |
| Maintenance training record template | Training attendance, topics covered, trainer, trainee acknowledgment, assessment results |
| Safety PLC CRC/signature verification form | Form for documenting periodic program integrity verification — expected CRC, actual CRC, match (yes/no), verified by, date |
| Drive safety parameter verification form | Parameter-by-parameter comparison form for periodic verification of safety-related drive parameters |
| Spare parts inventory tracking sheet | Inventory of all safety-rated spare parts — part number, description, quantity on hand, reorder point, supplier, lead time |
| Internal audit checklist — safety maintenance | Per Section 11.1 — structured audit checklist for annual self-assessment of the safety maintenance program |
| KPI tracking dashboard template | Per Section 16 — spreadsheet or dashboard for tracking safety maintenance KPIs over time |
| Bypass management procedure template | Documented procedure for authorizing, applying, monitoring, and removing safety function bypasses |
| Overdue proof test escalation procedure template | Procedure defining escalation path when a proof test becomes overdue — notification, risk assessment, corrective action |
| Component life tracking worksheet | Spreadsheet for tracking contactor operation counts, switch actuations, valve cycles, and calendar age against B10d/T10d limits and manufacturer replacement intervals |
| CMMS configuration guide for safety maintenance | Guide for configuring the facility's Computerized Maintenance Management System to schedule, track, and alert on safety-specific maintenance activities (proof tests, calibrations, component replacements) |

---

## 18. Lifecycle Degradation Scenarios — Decision Guide

Over the operational life of the machine, various degradation scenarios will occur. This guide helps maintenance and safety personnel determine the correct response:

### 18.1 Scenario Decision Matrix

| Scenario | Detection Method | Immediate Action | Engineering Assessment Required? | MOC Required? | Lifecycle Re-Entry Point |
|----------|-----------------|-----------------|-------------------------------|--------------|------------------------|
| **Contactor contacts show visible arc erosion during inspection** | Visual inspection during PM | Assess severity; if contacts are within manufacturer wear limits, document and continue monitoring; if approaching limits, schedule replacement | No (if like-for-like replacement) | No (if exact same part number) | None — routine maintenance |
| **Contactor welds during operation — detected by EDM** | Safety controller diagnostic (EDM fault) | Machine in safe state (EDM prevents restart); replace contactor with exact same part number; proof test SF after replacement | No (if like-for-like replacement) | No (if exact same part number) | None — reactive maintenance |
| **Contactor operation count reaches 80% of B10d** | Component life tracking | Schedule replacement during next planned outage; order exact replacement part | No | No | None — preventive replacement |
| **Proof test reveals response time has increased from 151ms to 190ms (requirement ≤200ms)** | Proof test measurement | Document; assess margin (only 10ms remaining); investigate cause (brake wear? actuator degradation?); plan corrective action | Yes — safety engineer should assess whether margin is adequate for continued operation until next planned maintenance | No (if corrective action is like-for-like repair/adjustment) | None if repaired; Stage 12 if design change needed |
| **Proof test reveals response time has increased to 215ms (requirement ≤200ms)** | Proof test measurement | **FAIL** — safety function does not meet requirement; machine must not operate with this safety function until corrected | Yes — root cause investigation; determine corrective action (brake replacement, actuator replacement, drive parameter adjustment) | Depends on corrective action — like-for-like repair: No; design change: Yes (Stage 12) | If design change: Stage 4/5 → through to Stage 10 re-validation |
| **Calibration reveals safety transmitter has drifted outside tolerance** | Calibration as-found value | Calibrate to correct values; assess whether the safety function was capable of performing during the period since last calibration; if not — document as revealed dangerous failure; report per facility procedures | Yes — if drift caused the safety function to be unable to perform, assess risk exposure for the elapsed period | No (if recalibration restores function) | None — recalibration is routine maintenance |
| **Safety transmitter repeatedly drifts outside tolerance at each calibration interval** | Calibration trend analysis | Shorten calibration interval; plan transmitter replacement; investigate cause (process conditions, vibration, temperature cycling) | Yes — assess whether shorter interval is adequate or replacement is required | If replacement with different model: Yes (Stage 12) | If different model: Stage 4 → recalculate → Stage 10 re-validate |
| **Light curtain alignment degrades repeatedly due to machine vibration** | Proof test / inspection | Investigate root cause (machine vibration, mounting rigidity); improve mounting; add vibration isolation; re-align | Yes — if mounting modification is needed | Yes — mounting modification is a physical change to the safety device installation | Stage 8 (installation change) → Stage 9/10 re-verify |
| **Safety PLC CRC/signature does not match approved version** | Periodic CRC verification | **STOP — potential unauthorized modification**; investigate immediately; determine what changed and who changed it; compare current program to approved backup; if unauthorized change is confirmed, restore from backup and proof test all safety functions | Yes — mandatory investigation; determine impact on safety functions | Yes — if the change was intentional and is to be retained; No — if the change was unauthorized and the backup is restored | If change is retained: Stage 4.5 → Stage 7 → Stage 10 re-validate |
| **Guard switch actuator becomes misaligned due to guard hinge wear** | Visual inspection or proof test failure (switch does not activate reliably) | Re-align actuator; repair or replace guard hinge; proof test after repair | No (if repair restores original alignment) | No (if repair restores original condition) | None — routine maintenance |
| **New safety standard published that affects the machine** | Industry monitoring, customer notification, or audit finding | Engineering review — determine if the new standard imposes additional requirements; assess gap between current design and new standard requirements | Yes — engineering assessment of the gap and the risk | Yes — if changes to the safety system are required to comply with the new standard | Stage 2 (standards review) → forward through affected stages |
| **Customer requests addition of a new safety function** | Customer request | This is a new safety function, not maintenance — it requires full lifecycle treatment from risk assessment through design, build, installation, and validation | Yes — full engineering scope | Yes — this is a modification to the safety system | Stage 3 (risk assessment for the new hazard/access point) → through all subsequent stages |
| **Machine is relocated to a different facility** | Customer decision | Re-verify installation: available fault current at new location, supply voltage, ambient conditions, grounding system; re-verify safety distances if machine layout changed; proof test all safety functions after relocation | Yes — installation conditions may have changed | Possibly — if installation conditions differ significantly from original design assumptions | Stage 8 (installation verification) → Stage 9 (pre-commissioning) → Stage 10 (re-validation if conditions changed significantly) |
| **Machine ownership transfers to new company** | Business transaction | Transfer all documentation (safety manual, V&V report, maintenance records, configuration backups); train new owner's maintenance personnel; verify maintenance program continuity | Yes — assessment of new owner's maintenance capability | No (if no changes to the machine) | None — but maintenance program must be re-established under new ownership |

### 18.2 The Boundary Between Maintenance and Modification

The single most important distinction at this stage is between **maintenance** (which stays in Stage 11) and **modification** (which triggers Stage 12 — MOC):

| Activity | Maintenance (Stage 11) | Modification (Stage 12 — MOC) |
|---------|----------------------|------------------------------|
| Replacing a contactor with the exact same part number | Yes | |
| Replacing a contactor with a different part number (even if "equivalent") | | Yes |
| Recalibrating an instrument to its original specification | Yes | |
| Changing an instrument's calibrated range or trip point | | Yes |
| Cleaning a light curtain lens | Yes | |
| Relocating a light curtain to a different position | | Yes |
| Re-aligning a guard switch actuator to its original position | Yes | |
| Changing the guard design or guard switch type | | Yes |
| Restoring safety PLC program from approved backup | Yes | |
| Modifying safety PLC program logic (any change) | | Yes |
| Replacing a safety relay with the exact same model | Yes | |
| Upgrading a safety relay to a newer model | | Yes |
| Tightening a loose terminal | Yes | |
| Rerouting a safety circuit cable | | Yes (may affect CCF) |
| Adding a new e-stop station | | Yes |
| Adjusting a drive speed parameter within the original specification range | Depends — if the parameter is not safety-related: Yes | If the parameter is safety-related (SLS limit, SS1 deceleration ramp): Yes (MOC) |
| Changing the proof test interval | | Yes (affects PL/SIL calculation assumptions) |
| Adding or removing a guard | | Yes |
| Changing the process (new material, higher speed, different product) that affects the hazard profile | | Yes |

**When in doubt, treat it as a modification and initiate MOC. It is always safer to over-classify than to under-classify.**

---

## 19. Record Retention

### 19.1 Retention Requirements

| Record Type | Minimum Retention Period | Basis |
|------------|------------------------|-------|
| Proof test records | Life of the machine | Demonstrates ongoing compliance; needed for trend analysis; needed for audit |
| Calibration records | Life of the machine | Same as above |
| Component replacement records | Life of the machine | Provides component history; supports B10d life tracking |
| Failure and corrective action records | Life of the machine | Provides failure history; supports trend analysis; needed for audit |
| Bypass log | Life of the machine | Demonstrates bypass management compliance |
| Training records | Life of the machine or per regulatory requirement (whichever is longer) | Demonstrates competency compliance |
| Safety manual and maintenance procedures | Current version plus all superseded versions | Audit trail of procedure changes |
| As-built documentation | Current version plus all superseded versions | Audit trail of system changes |
| Configuration backups | Current version plus previous version (minimum) | Ability to restore or compare; detect unauthorized changes |
| V&V report (from Stage 10) | Life of the machine | Reference document for the validated state |
| PL/SIL calculation reports (from Stage 4) | Life of the machine | Reference for proof test interval basis and component life assumptions |
| Risk assessment (from Stage 3) | Life of the machine | Reference for hazard identification and risk reduction basis |
| MOC records (from Stage 12) | Life of the machine | Audit trail of all modifications |
| Technical file (CE marking) | Minimum 10 years after last machine of the type was manufactured | Machinery Directive Art. 5 / Machinery Regulation Art. 10 |

### 19.2 Record Storage

| Requirement | Detail |
|------------|--------|
| **Accessible** | Records must be retrievable when needed — for proof test trend analysis, for audit, for troubleshooting, for MOC reference |
| **Secure** | Records must be protected from unauthorized modification, loss, or destruction |
| **Organized** | Records must be organized by safety function, by date, and by type — finding a specific proof test record for SF-01 from 3 years ago must be straightforward |
| **Backed up** | Electronic records must be backed up; paper records should be scanned or have duplicate storage |
| **Format** | Electronic preferred (CMMS, document management system, database); paper acceptable if properly organized and stored |

---

## 20. Special Considerations

### 20.1 Aging Machines

As machines age beyond their original design mission time (typically 20 years per ISO 13849-1):

| Consideration | Action |
|--------------|--------|
| Components are beyond their designed useful life | Engineering assessment of continued operation; may require comprehensive inspection, component replacement, or re-validation |
| Original spare parts may be discontinued | Identify alternative sources or equivalent replacements; any substitution requires MOC (Stage 12) |
| Standards have been updated since the machine was designed | Engineering assessment of gap between original design basis and current standards; customer/owner decision on whether to upgrade |
| Maintenance personnel who were originally trained may have left | Ensure current personnel are trained; ensure institutional knowledge is documented in procedures |
| Documentation may be incomplete or lost | Reconstruct documentation where possible; perform comprehensive inspection and testing to establish current baseline |

### 20.2 Mothballed Machines

When a machine is taken out of service temporarily (mothballed) but not decommissioned:

| Consideration | Action |
|--------------|--------|
| Safety functions are not being exercised | Components may degrade differently when not operated (corrosion, seal degradation, lubricant drying) |
| Proof tests are not being performed | The PL/SIL calculation assumes ongoing proof testing; if the machine is mothballed for longer than one proof test interval, the safety integrity at restart is uncertain |
| Before returning to service | Perform full proof test of all safety functions; perform calibration of all instruments; verify safety PLC program CRC; inspect all safety devices; verify environmental conditions have not degraded components; essentially re-execute Stage 9 (pre-commissioning) before restarting |

### 20.3 Multi-Site Fleets

When the same machine type is deployed across multiple sites:

| Consideration | Action |
|--------------|--------|
| Consistent maintenance standards | All sites should follow the same proof test procedures, calibration procedures, and PM schedules |
| Fleet-wide trend analysis | Aggregate proof test and failure data across all sites; identify fleet-wide trends (e.g., if the same component fails at multiple sites, it may indicate a design issue) |
| Standardized spare parts | All sites should stock the same spare parts; centralized spare parts management may be more efficient |
| Shared lessons learned | Failure at one site should trigger review at all sites with the same machine type |
| Consistent training | All maintenance personnel across all sites trained to the same standard |
| Configuration management | All sites should have the same software version and configuration (unless site-specific modifications were made through MOC) |

---

## 21. Relationship to Stage 12 (Management of Change) — Interface Definition

The interface between Stage 11 (Maintenance) and Stage 12 (Management of Change) is the most frequently crossed boundary in the operational lifecycle. Defining this interface clearly prevents both under-classification (modifications treated as maintenance, bypassing MOC) and over-classification (routine maintenance treated as modifications, creating unnecessary bureaucracy).

### 21.1 Decision Flowchart

```
Maintenance activity required
        │
        ▼
┌───────────────────────────────────┐
│ Is the activity a LIKE-FOR-LIKE    │
│ replacement or restoration to      │
│ original design condition?         │
│                                   │
│ • Same part number                │
│ • Same calibration specification  │
│ • Same configuration              │
│ • Same physical location          │
│ • Same wiring                     │
│ • No change to safety function    │
│   behavior or performance         │
└─────────────┬─────────────────────┘
              │
        ┌─────┴──────┐
        ▼            ▼
       YES           NO or UNSURE
        │             │
        ▼             ▼
┌────────────┐  ┌──────────────────────┐
│ STAGE 11   │  │ STAGE 12             │
│ Maintenance│  │ Management of Change │
│            │  │                      │
│ Proceed    │  │ Initiate MOC         │
│ with       │  │ process before       │
│ maintenance│  │ implementing the     │
│ per        │  │ change               │
│ documented │  │                      │
│ procedures │  │                      │
│            │  │                      │
│ Proof test │  │                      │
│ after      │  │                      │
│ completion │  │                      │
│            │  │                      │
│ Document   │  │                      │
│ the        │  │                      │
│ activity   │  │                      │
└────────────┘  └──────────────────────┘
```

### 21.2 Grey Areas — Guidance

| Situation | Guidance |
|-----------|---------|
| Manufacturer releases a "direct replacement" for a discontinued part | Even if the manufacturer claims it is a direct replacement, verify: same B10d/PFHd/SFF? Same form/fit/function? Same safety certification? If ANY parameter differs, it is a modification requiring MOC. |
| Firmware update available for safety controller | Firmware change can affect PFHd, diagnostic behavior, and safety certification. This is a modification requiring MOC — even if the manufacturer recommends the update. |
| Adjusting a non-safety drive parameter (e.g., acceleration ramp) | If the parameter does not affect any safety function behavior or response time, it may be treated as maintenance. If the parameter could affect stopping time, speed limiting, or any safety function, it requires MOC. When in doubt, MOC. |
| Cleaning or repainting a guard | If the guard dimensions, material, and mounting are unchanged, this is maintenance. If the guard is modified in any way (hole added, material changed, mounting changed), it is a modification requiring MOC. |
| Replacing a cable with the same specification but different manufacturer | If the cable specification (type, gauge, voltage rating, temperature rating, shielding) is identical, this is generally acceptable as like-for-like maintenance. If any specification differs, MOC. |
| Adding a temporary guard or barrier during maintenance | Temporary safeguarding during maintenance is part of the bypass management procedure (Section 8), not MOC. However, if the temporary measure becomes permanent, it requires MOC. |

---

<div class="nav-links">
  <a href="{{ '/implementation/lifecycle-commissioning/' | relative_url }}" class="card__link">&larr; Stage 10: Commissioning and Validation</a>
  <a href="{{ '/verification/management-of-change/' | relative_url }}" class="card__link">Stage 12: Management of Change &rarr;</a>
</div>
