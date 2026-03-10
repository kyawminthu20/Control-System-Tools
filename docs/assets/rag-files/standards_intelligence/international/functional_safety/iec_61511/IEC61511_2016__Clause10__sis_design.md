<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_61511
EDITION: 2016

HIERARCHY:
  clause: "10"
  clause_title: "Design and Engineering of the SIS"

INDEX_TAGS:
  topics: ["sis_design", "pfdavg", "proof_test", "redundancy", "logic_solver", "final_element", "sensor", "architectural_constraints", "hft"]
  systems: ["process_industry", "sis", "safety_plc", "control_valve"]
-->

# IEC 61511:2016 — Clause 10 — SIS Design and PFDavg Calculation

## 0. Why this matters

The SIS design must demonstrate that each SIF achieves the required PFDavg established by the SIL determination. This clause drives the hardware selection, redundancy architecture, and proof test interval decisions. Getting these calculations right is the primary technical deliverable of SIS engineering.

Unlike machinery safety (IEC 62061), where PFHd targets are met largely through selecting certified subsystems and summing PFHd values, process SIS design requires explicit calculation of PFDavg for each SIF, including the effect of proof test interval and dangerous undetected failure rate (λDU).

## 1. The PFDavg equation

For a simple 1oo1 (single channel) subsystem, proof-test-limited:

**PFDavg = λDU × TI / 2**

Where:
- **λDU** = dangerous undetected failure rate of the subsystem (from vendor data or generic databases)
- **TI** = proof test interval (time between functional tests that detect DU failures)

**Key insight:** PFDavg scales linearly with the proof test interval. Halving the proof test interval (more frequent testing) approximately halves the PFDavg. This is the primary lever for achieving the required SIL when a single-channel architecture is used.

For a SIF with sensors, logic solver, and final elements in series:

**PFDavg (total SIF) = PFDavg (sensors) + PFDavg (logic solver) + PFDavg (final elements)**

Each subsystem contributes to the total PFDavg. Final elements (valves) typically dominate because they have the highest dangerous failure rates and are most difficult to test without interrupting the process.

## 2. Redundancy architectures

Redundancy reduces PFDavg by requiring multiple channels to fail simultaneously before the SIF is defeated.

### Voting architectures

| Architecture | Description | PFDavg effect | Spurious trip effect |
|-------------|-------------|----------------|----------------------|
| **1oo1** | Single channel; one failure = trip OR loss of SIF | Highest PFDavg | Lowest spurious trip rate |
| **1oo2** | Dual channel; either channel trips; one failure = trip | Lowest PFDavg (best safety) | Highest spurious trip rate |
| **2oo2** | Dual channel; both must trip; one failure = loss of SIF | Higher than 1oo1 (worse) | Lower spurious rate than 1oo2 |
| **2oo3** | Triple channel; any two trip; single failure tolerated | Moderate PFDavg | Moderate spurious rate |
| **1oo2D** | Dual channel with diagnostics; discrepancy detected | Similar to 1oo2 (better diagnostics) | Similar to 2oo2 (diagnostics reduce spurious) |

**Practical choice:**
- SIL 1: 1oo1 with annual proof test often sufficient
- SIL 2: 1oo2 or 2oo3 typical; annual or biennial proof test
- SIL 3: 2oo3 with 1oo2 inputs; frequent proof testing or high-diagnostic sensors

### PFDavg for 1oo2 architecture

**PFDavg (1oo2) ≈ (λDU × TI)² / 3**

The squared relationship means redundancy provides dramatic improvement: if a 1oo1 sensor has PFDavg = 0.05, a 1oo2 arrangement gives approximately 0.0017 — a factor of about 30 improvement.

### PFDavg for 2oo3 architecture

**PFDavg (2oo3) ≈ (λDU × TI)² / 1**

2oo3 provides slightly worse PFDavg than 1oo2 but much better spurious trip rate and is preferred for high-availability processes where spurious shutdowns have large economic consequences.

## 3. Sensor selection and design

Sensors are typically the element most directly exposed to process conditions. Selection criteria:

| Criterion | Guidance |
|-----------|----------|
| Failure mode data | Use OREDA, vendor data, or SINTEF database λDU values |
| Diagnostic coverage | Higher DC reduces λDU that contributes to PFDavg |
| Process fluid compatibility | Plugging, corrosion, and fouling increase real-world failure rates |
| Redundancy | 1oo2 or 2oo3 for SIL 2+; single sensor for SIL 1 if λDU is low enough |
| Common cause failure | Diverse sensor technologies or diverse installation points reduce CCF |
| Proof test capability | Can the sensor be tested in-situ without process shutdown? |

**Prior use clause:** IEC 61511 Clause 11.5.3 permits use of field devices (sensors and final elements) that have a documented history of successful operation in similar service. This allows use of conventional process instruments without IEC 61508 certification — provided the prior use record is adequate. This is a major practical relief.

## 4. Logic solver selection

The logic solver (safety PLC) is typically a pre-certified IEC 61508-certified device. Selection considerations:

| Criterion | Guidance |
|-----------|----------|
| SILCL (SIL capability level) | Must be ≥ SIL target of the highest SIL SIF implemented |
| Certified PFD contribution | Vendor provides PFD data per IEC 61508 certification; often very low |
| Redundancy | Most SIL 2–3 logic solvers are 1oo2D or 2oo3 internally; verify with vendor |
| I/O capacity | Sufficient channels for all SIF inputs and outputs |
| Application programming restrictions | Understand what programming restrictions the SIL certification places on the user |
| Proof test | Logic solver internal diagnostics reduce need for functional proof test; verify coverage |

The logic solver contribution to overall SIF PFDavg is usually very small relative to sensors and final elements because certified logic solvers have very low λDU values and high diagnostic coverage. **Do not over-specify the logic solver** to compensate for poor sensor or final element selection.

## 5. Final element design

Final elements (control valves, shut-off valves, disconnects) are the highest-risk subsystem in most SIFs. They:
- Have the highest λDU of any SIF subsystem
- Are most difficult to proof test without process disruption
- Suffer from mechanical degradation (stiction, corrosion, packing wear) that increases real-world failure rates

Final element design guidance:

| Design choice | Impact |
|--------------|--------|
| Fail-safe position | De-energize-to-safe is preferred (loss of power → safe state); must be defined in SRS |
| Solenoid valve | SIL-rated solenoid valves have much lower λDU than generic valves |
| Partial stroke testing (PST) | Tests valve stroke during operation without full closure; improves diagnostic coverage and reduces effective λDU |
| Full stroke testing | Required at each proof test interval; confirms full travel to safe position |
| Proof test interval | Shorter TI reduces PFDavg; align with process turnaround schedule |
| Redundancy | 1oo2 solenoids on a single valve or parallel valve arrangements for SIL 2+ |

**Partial stroke testing (PST):** PST uses a positioner or solenoid to move the valve 10–30% of its travel during operation. It detects valve-stuck-open failures without full closure. PST can increase the effective λDD (detected dangerous) and reduce the contribution of final elements to PFDavg, allowing longer proof test intervals or achievement of higher SIL from the same architecture.

## 6. Architectural constraints

IEC 61511 Clause 11 specifies minimum architectural requirements that must be met regardless of PFDavg calculations. These ensure a minimum level of integrity through design.

| SIL | Minimum HFT (hardware fault tolerance) for field devices |
|-----|----------------------------------------------------------|
| SIL 1 | 0 (single channel acceptable if PFDavg is achieved) |
| SIL 2 | 0 (single channel with sufficient diagnostic coverage); 1 preferred |
| SIL 3 | 1 (dual channel minimum) |

IEC 61511 is less prescriptive on architectural constraints than IEC 61508 for field devices — the standard focuses primarily on achieving the required PFDavg through the combination of reliability data and proof test interval. Logic solvers used must have appropriate IEC 61508 certification for the SIL being implemented.

## 7. Safety requirements specification (SRS)

Before detailed design, the SRS must document each SIF:

| SRS element | Content |
|-------------|---------|
| SIF description | What the safety function does; initiating cause; safe state |
| SIL requirement | From LOPA or risk graph |
| Required PFDavg | From SIL table |
| Inputs | Which sensors, locations, voting logic |
| Outputs | Which final elements; voting logic; safe state |
| Response time | Maximum time from input demand to output action |
| Proof test interval | Maximum TI to achieve required PFDavg |
| Manual actions required | Any operator actions that are part of the SIF |
| Environmental conditions | Temperature, vibration, hazardous area classification |
| Interface to BPCS | What information is shared; independence requirements |

The SRS is the design basis. All subsequent SIS design decisions, calculations, and testing must trace back to the SRS.

## 8. Change log

- 2026-03-07 — Phase 3 corpus creation; Clause 10 SIS design document established.
