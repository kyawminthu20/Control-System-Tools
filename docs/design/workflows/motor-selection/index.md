---
layout: default
title: Motor Selection Workflow
description: First-pass motor selection from load definition through protection and integration review.
redirect_from:
  - /workflows/motor-selection/
  - /workflows/motor-selection/index.html
review:
  standard: "Motor selection practice — application engineering"
  edition: "n/a — practice workflow"
  status: "Review pending"
  coverage: "Motor selection decision workflow; vendor data and project requirements govern."
  last_reviewed: "July 2026"
---

<div class="page-header">
  <div class="breadcrumb"><a href="{{ '/design/workflows/' | relative_url }}">Workflows</a> › Motor Systems</div>
  <h1>Motor Selection Workflow</h1>
  <p class="page-subtitle">Structure first-pass motor selection before detailed protective-device and drive coordination work begins.</p>
  <div class="workflow-meta" style="margin-top:0.75rem;">
    <span class="workflow-badge motor">Motor Systems</span>
    <span class="wf-tag">Selection</span>
    <span class="wf-tag">Design</span>
  </div>
</div>

<div class="content-note">
  Motor selection is unreliable if started from horsepower alone. Start with the load, then match the motor, supply, and protection to it.
</div>

## Step 1 — Define the load first

Collect before selecting any motor:

| Parameter | What to determine |
|---|---|
| Load type | Constant torque, variable torque, constant power, or impact load |
| Required running speed | Target RPM or speed range |
| Required starting torque | Load torque at zero speed; critical for breakaway loads |
| Duty cycle | Continuous, intermittent, short-time, or repetitive cycling |
| Stopping method | Coast, dynamic brake, regenerative braking, or mechanical brake |

Starting from horsepower alone produces unreliable results. Match motor behavior to load behavior first.

## Step 2 — Confirm supply and control architecture

| Item | Check |
|---|---|
| Available voltage and frequency | Match motor nameplate; confirm phase (1Ø or 3Ø) |
| Phase availability | 3Ø preferred for larger motors; 1Ø limits selection |
| Starting method | Direct-on-line, soft-start, or VFD — affects motor torque curve |
| Disconnecting means | Verify NEC Art. 430 or IEC 60204-1 isolation method |
| Service isolation expectations | Lockout/tagout-compatible disconnect |

## Step 3 — Review the environment

| Condition | Implication |
|---|---|
| Ambient temperature above 40°C | Derate the motor; check insulation class |
| Washdown, dust, or corrosive exposure | Minimum IP55 or NEMA 4/4X enclosure |
| Outdoor mounting | UV-rated terminal box; humidity sealing |
| Hazardous-location requirements | ATEX or NEC Art. 500/505 Ex rating required |

## Step 4 — Review nameplate and construction fit

Confirm all nameplate fields before finalizing:

- **Power rating** — HP or kW matched to load calculation
- **Full-load current (FLA)** — basis for branch-circuit and overload sizing
- **Speed** — synchronous RPM vs. rated slip
- **Enclosure type** — TEFC, ODP, TENV matched to environment
- **Service factor (SF)** — available thermal margin (1.0 or 1.15 typical)
- **Frame size** — NEMA or IEC frame; mounting and shaft dimensions
- **Insulation class** — Class F or H for most industrial motors

## Step 5 — Review protection and integration

Before finalizing the design, confirm the path for:

| Protection element | Basis |
|---|---|
| Branch-circuit protection | NEC Art. 430.52 or IEC 60204-1 §7 |
| Overload protection | FLA × service factor × derate factor |
| Grounding and bonding | NEC Art. 250 or IEC 60204-1 §8 |
| Drive compatibility | VFD-rated insulation, inverter-duty winding if VFD-driven |

---

## Related training

| Module | Topic |
|---|---|
| [Induction Motor Basics]({{ '/fundamentals/motors/induction-motor-basics/' | relative_url }}) | Motor operating principles |
| [Motor Nameplates, Slip, and Torque]({{ '/fundamentals/motors/motor-nameplates-slip-torque/' | relative_url }}) | Nameplate reading and torque curves |
| [Motor Family Comparison]({{ '/fundamentals/motors/motor-family-comparison/' | relative_url }}) | AC, DC, servo, stepper comparison |
| [VFD Fundamentals]({{ '/fundamentals/motors/vfd-fundamentals/' | relative_url }}) | Drive-driven motor selection considerations |
| [Branch Circuits vs. Feeders]({{ '/fundamentals/nec-application/branch-circuits-vs-feeders/' | relative_url }}) | NEC conductor and OCPD sizing |
| [Art. 430 Practical Workflow]({{ '/fundamentals/nec-application/article-430-workflow/' | relative_url }}) | NEC motor code application |

## Related workflows

| Workflow | When to use |
|---|---|
| [VFD Commissioning Workflow]({{ '/lifecycle/guides/vfd-commissioning/' | relative_url }}) | After selection, when a VFD is in the design |
| [Motor Troubleshooting Decision Tree]({{ '/tools/troubleshooting/motors/' | relative_url }}) | During field startup or fault investigation |

## Related standards

| Standard | Relevance |
|---|---|
| [NEC Art. 430](/standards/us-electrical/nec/) | Motor circuit conductors, protection, disconnecting means |
| [NFPA 79](/standards/us-electrical/nfpa-79/) | Machine motor requirements (Chapter 12) |
| [IEC 60204-1](/standards/machinery/iec-60204-1/) | International machine electrical equipment (§12) |

## Related Checklists

- [Motor Nameplate and Overload Setting]({{ '/lifecycle/guides/commissioning-templates/motor-nameplate-overload/' | relative_url }})

## Related References

- [Motor Selection Comparison Matrix]({{ '/design/motor-selection/motor-selection-matrix/' | relative_url }}) — decision flowchart and system-family comparison table
