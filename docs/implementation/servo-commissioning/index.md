---
layout: default
title: Servo Commissioning Workflow
description: Staged commissioning sequence for a servo axis from readiness through tuning and functional motion review.
redirect_from:
  - /workflows/servo-commissioning/
  - /workflows/servo-commissioning/index.html
---

<div class="page-header">
  <div class="breadcrumb"><a href="{{ '/design/workflows/' | relative_url }}">Workflows</a> › Drive Systems</div>
  <h1>Servo Commissioning Workflow</h1>
  <p class="page-subtitle">Staged commissioning for a servo axis. Servo systems require tighter control over mechanical risk, feedback correctness, and tuning than a basic induction-motor drive.</p>
  <div class="workflow-meta" style="margin-top:0.75rem;">
    <span class="workflow-badge drive">Drive Systems</span>
    <span class="wf-tag">Commissioning</span>
    <span class="wf-tag">Servo</span>
  </div>
</div>

<div class="content-note">
  Do not skip the feedback verification step before enabling the axis. Commutation errors and feedback direction faults can cause immediate runaway — these must be resolved as blocking issues, not treated as tuning problems.
</div>

## Step 1 — Confirm axis readiness

Before enabling the axis, confirm:

| Item | Check |
|---|---|
| Correct motor/drive pairing | Motor model matches drive configuration |
| Axis mechanically safe to move | Travel limits understood; no mechanical interference |
| Hard limits and stops confirmed | Limit switches or software limits configured and tested |
| Safety-related functions understood | E-stop, door interlock, and enable chain reviewed |
| Feedback device terminations complete | Encoder or resolver cable seated and secured |
| Motor power cable complete | Correct phasing; PE confirmed |

## Step 2 — Enter motor and feedback data

Confirm the drive is configured with:

| Parameter | Source |
|---|---|
| Motor model or rated data | Motor nameplate or OEM motor file |
| Encoder or resolver type | Feedback device documentation |
| Feedback resolution | Counts per revolution or line count |
| Commutation or alignment method | OEM startup guide |

Configuration mismatch must be treated as a **blocking issue**. Do not proceed to enable with a configuration mismatch — do not attempt to tune through it.

## Step 3 — Verify feedback before motion

With the drive powered and axis not enabled:

| Check | Expected result |
|---|---|
| Signal health | Clean feedback; no error or noise indication |
| Direction sense | Manual shaft rotation shows correct count direction |
| Reference or homing assumptions | Home position method understood |
| Feedback loss warnings | No persistent feedback loss alarms |

Correct feedback direction before any motion. Incorrect direction causes immediate instability on enable.

## Step 4 — Controlled enable and commutation check

Enable the axis only in a controlled state:

- The motor should hold position or respond smoothly
- No unexpected jump, oscillation, or runaway on enable
- If the OEM commutation alignment process is required, complete it before motion
- Disable and investigate immediately if behavior is not as expected

## Step 5 — Stage the tuning work

Tune in this order. Do not skip levels:

```
1. Current / torque loop  →  stable and responsive
2. Velocity loop          →  smooth speed response
3. Position loop          →  accurate following
```

Jumping to aggressive position tuning before lower-level behavior is confirmed usually produces worse results and obscures the root issue.

## Step 6 — Functional motion review

After basic tuning is complete:

| Verify | Expected result |
|---|---|
| Direction matches command | Positive command produces positive motion |
| Overshoot and oscillation | Within acceptable limits for the application |
| Following error | Stays within expected limits at operating speed |
| Mechanical system | No resonance or backlash revealed by tuned response |

If mechanical issues appear (resonance, backlash, compliance), resolve them mechanically — do not attempt to compensate through tuning alone.

---

## Related training

| Module | Topic |
|---|---|
| [Servo Drive Fundamentals]({{ '/fundamentals/motors/servo-drive-fundamentals/' | relative_url }}) | Servo architecture, feedback, and control loops |
| [Motor Control Methods]({{ '/fundamentals/motors/motor-control-methods/' | relative_url }}) | Control loop structure (current, velocity, position) |
| [Motor Family Comparison]({{ '/fundamentals/motors/motor-family-comparison/' | relative_url }}) | Servo vs. induction vs. stepper selection |

## Related workflows

| Workflow | When to use |
|---|---|
| [Motor Troubleshooting Decision Tree]({{ '/troubleshooting/motors/' | relative_url }}) | If servo instability or faults appear |
| [VFD Commissioning Workflow]({{ '/implementation/vfd-commissioning/' | relative_url }}) | For VFD-driven induction motors on the same machine |
| [Motor Selection Workflow]({{ '/design/workflows/motor-selection/' | relative_url }}) | Review original selection basis |

{% include trust-boundary.html %}

## Related Checklists

- [Drive Commissioning]({{ '/implementation/commissioning-templates/drive-commissioning/' | relative_url }})
