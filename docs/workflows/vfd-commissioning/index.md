---
layout: default
title: VFD Commissioning Workflow
description: Structured first energization and functional check sequence for VFD-driven motor systems.
---

<div class="page-header">
  <div class="breadcrumb"><a href="{{ '/workflows/' | relative_url }}">Workflows</a> › Drive Systems</div>
  <h1>VFD Commissioning Workflow</h1>
  <p class="page-subtitle">Structure first energization and early functional checks for a VFD-driven motor system. Complements, but does not replace, the specific OEM startup procedure.</p>
  <div class="workflow-meta" style="margin-top:0.75rem;">
    <span class="workflow-badge drive">Drive Systems</span>
    <span class="wf-tag">Commissioning</span>
    <span class="wf-tag">VFD</span>
  </div>
</div>

<div class="content-note">
  This workflow sets a consistent first-energization baseline. Always follow the OEM startup guide alongside this structure. Retain evidence from each step.
</div>

## Step 1 — Electrical verification (before applying power)

Confirm before power is applied:

| Check | What to verify |
|---|---|
| Incoming supply rating | Voltage and phase match the drive nameplate |
| Protective earth and bonding | PE conductor terminated; bonding to enclosure confirmed |
| Branch protection and isolation | OCPD size and type match design; disconnect identified |
| Motor cable terminations | Phasing correct; terminations tight; no bare conductors exposed |
| Pre-power insulation | No obvious phase-to-phase or phase-to-ground resistance issues |

Do not power the drive until this step is confirmed clean.

## Step 2 — Capture and enter motor data

Enter motor nameplate data into the drive before first motion. Record:

| Parameter | Source |
|---|---|
| Rated voltage | Motor nameplate |
| Rated current (FLA) | Motor nameplate |
| Rated frequency | Motor nameplate (50 or 60 Hz) |
| Rated speed (RPM) | Motor nameplate |
| Rated power (HP or kW) | Motor nameplate |

Do not guess through this step. Wrong motor data produces poor control behavior or immediate protection trips.

## Step 3 — Safe first power-up

Power the drive under controlled conditions:

- Verify the drive powers up normally (no immediate fault)
- Understand operator/HMI indications before clearing any fault
- Confirm the machine is in a **safe non-motion state**
- Review any pre-existing faults and clear only after understanding their basis

## Step 4 — First motion check

Run the motor only under conditions approved as safe for the machine state:

| Verify | Expected result |
|---|---|
| Rotation direction | Matches design intent; correct for the load |
| Smooth acceleration | No hesitation, judder, or overshoot on ramp |
| Current behavior | Consistent with no-load or light-load expectation |
| Sound and vibration | No abnormal noise; vibration within normal range |
| Temperature trend | No immediate heating during short run |

Rotation direction must be confirmed before coupling the motor to the load.

## Step 5 — Functional run and load review

After basic motion is confirmed correct:

| Area | Review |
|---|---|
| Normal speed range | All commanded speeds stable and accurate |
| Acceleration and deceleration | Ramp times acceptable for the load |
| Braking behavior | Dynamic brake or regenerative behavior as designed |
| Drive and motor temperature | Trend acceptable over a representative run |
| EMC side effects | Nearby controls, encoders, and sensors not affected by switching noise |

## Step 6 — Evidence to retain

Document and retain:

- Motor nameplate data (photo or transcribed)
- Key drive parameter snapshot (printed or stored)
- Protection basis (OCPD size, overload setting, FLA used)
- Rotation verification result and direction
- Any commissioning notes or parameter deviations from design

---

## Related training

| Module | Topic |
|---|---|
| [VFD Fundamentals]({{ '/training/electrical-machines/vfd-fundamentals/' | relative_url }}) | Drive topology, control modes, and protection |
| [Motor Nameplates, Slip, and Torque]({{ '/training/electrical-machines/motor-nameplates-slip-torque/' | relative_url }}) | Reading and using nameplate data |
| [Motor Control Methods]({{ '/training/electrical-machines/motor-control-methods/' | relative_url }}) | V/Hz vs. vector vs. closed-loop control |
| [Grounding and Bonding for Control Panels]({{ '/training/nec-application/grounding-bonding-control-panels/' | relative_url }}) | Panel-level grounding and bonding checks |

## Related workflows

| Workflow | When to use |
|---|---|
| [Motor Selection Workflow]({{ '/workflows/motor-selection/' | relative_url }}) | Review design basis before commissioning begins |
| [Motor Troubleshooting Decision Tree]({{ '/workflows/motor-troubleshooting/' | relative_url }}) | If faults appear during commissioning |
| [Servo Commissioning Workflow]({{ '/workflows/servo-commissioning/' | relative_url }}) | For servo axes on the same machine |

## Related standards

| Standard | Relevance |
|---|---|
| [NEC Art. 430](/standards/us-electrical/nec/) | Motor branch circuits, protection, disconnecting means |
| [IEC 60204-1](/standards/machinery/iec-60204-1/) | Machine electrical commissioning and verification |

{% include trust-boundary.html %}

## Related Checklists

- [Capacitor Discharge Awareness Check]({{ '/commissioning-templates/capacitor-discharge/' | relative_url }})
- [Drive Commissioning]({{ '/commissioning-templates/drive-commissioning/' | relative_url }})
