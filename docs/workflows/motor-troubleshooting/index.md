---
layout: default
title: Motor Troubleshooting Decision Tree
description: First-pass routing for motor and drive faults before OEM diagnostics or component replacement.
---

<div class="page-header">
  <div class="breadcrumb"><a href="{{ '/workflows/' | relative_url }}">Workflows</a> › Motor Systems</div>
  <h1>Motor Troubleshooting Decision Tree</h1>
  <p class="page-subtitle">First-pass troubleshooting for motor and drive systems. Routes the review before deeper OEM diagnostics or component replacement.</p>
  <div class="workflow-meta" style="margin-top:0.75rem;">
    <span class="workflow-badge motor">Motor Systems</span>
    <span class="wf-tag">Troubleshooting</span>
    <span class="wf-tag">Field</span>
  </div>
</div>

<div class="content-note">
  This workflow is intentionally simple. It helps route the review, not replace the drive manual or fault-history tools. Always confirm the machine is safe to inspect and test before starting.
</div>

## Practical sequence — always start here

Use this order before diving into fault codes:

1. Confirm the machine is **safe to inspect and test**
2. Check **mechanical freedom and obvious damage** first
3. Check **supply, protection, and wiring** next
4. Review **configuration and parameter data** after hardware basics are known good
5. Use **OEM fault history and scoped measurements** only after the basic chain is verified

---

## Motor will not start

Work through this chain in order:

| Check | What to look for |
|---|---|
| Input power present? | Measure voltage at drive or starter input |
| Device healthy and powered? | No fault indication, ready state |
| Start command actually present? | Verify at the control input, not just at the HMI |
| Permissive or safety function blocking? | E-stop, door interlock, safety relay — confirm all are satisfied |
| Motor or cable open/shorted/disconnected? | Check motor resistance and cable continuity |
| Mechanical load jammed? | Try rotating the shaft by hand under zero-power conditions |

Do not assume software or parameter problems until the mechanical and electrical basics are confirmed clear.

## Overcurrent or immediate trip

Review in this order:

| Symptom / Cause | Check |
|---|---|
| Mechanical jam or high load | Shaft free to rotate? Load removed for test? |
| Acceleration time too aggressive | Increase ramp time in drive parameters |
| Incorrect motor data in drive | FLA, voltage, frequency entered correctly? |
| Motor cable fault | Phase-to-phase or phase-to-ground resistance |
| Wrong supply or connection | Delta vs. wye, supply voltage matches nameplate |
| Drive hardware fault | Exclude load causes first; then suspect hardware |

## Overheating or nuisance overload

Determine whether the problem is primarily **electrical** or **thermal**:

| Electrical causes | Thermal causes |
|---|---|
| Overload setting based on wrong FLA | Cooling reduced at low speed (VFD application) |
| Wrong voltage or connection arrangement | Ambient temperature or enclosure heat too high |
| Repetitive starts without sufficient cooling time | Motor running significantly above rated load |
| Long acceleration time heating the windings | High service factor consumed by process demand |

## Wrong speed, poor torque, or unstable running

| Symptom | Review |
|---|---|
| Wrong speed | Commanded frequency or speed reference value |
| Poor torque | Control mode selection (V/Hz vs. vector vs. closed-loop) |
| Drive not matching load | Nameplate data entered correctly? |
| Slip higher than expected | Is actual load near or above rated torque? |
| Low-speed torque insufficient | V/Hz drive may not deliver rated torque at low speed |

## Servo instability — axis oscillates or hunts

Work through in order:

1. **Motor and encoder model match** — confirm correct motor file or parameters
2. **Encoder polarity or direction** — wrong direction produces immediate instability
3. **Mechanical resonance** — check coupling, mount, and load rigidity
4. **Backlash or loose coupling** — mechanical compliance can appear as tuning instability
5. **Tuning values too aggressive** — reduce gains before increasing them
6. **Noise or intermittent feedback loss** — check cable routing and shielding

---

## Related training

| Module | Topic |
|---|---|
| [Induction Motor Basics]({{ '/training/electrical-machines/induction-motor-basics/' | relative_url }}) | Motor operating principles |
| [Motor Nameplates, Slip, and Torque]({{ '/training/electrical-machines/motor-nameplates-slip-torque/' | relative_url }}) | Slip, torque curves, and overload behavior |
| [VFD Fundamentals]({{ '/training/electrical-machines/vfd-fundamentals/' | relative_url }}) | Drive fault behavior and protection |
| [Servo Drive Fundamentals]({{ '/training/electrical-machines/servo-drive-fundamentals/' | relative_url }}) | Servo feedback and tuning concepts |
| [Motor Control Methods]({{ '/training/electrical-machines/motor-control-methods/' | relative_url }}) | Control mode comparison (V/Hz, vector, closed-loop) |

## Related workflows

| Workflow | When to use |
|---|---|
| [Motor Selection Workflow]({{ '/workflows/motor-selection/' | relative_url }}) | Review original design basis during fault investigation |
| [VFD Commissioning Workflow]({{ '/workflows/vfd-commissioning/' | relative_url }}) | Re-run commissioning steps if parameter changes are needed |
| [Servo Commissioning Workflow]({{ '/workflows/servo-commissioning/' | relative_url }}) | Re-run servo axis steps for instability faults |

{% include trust-boundary.html %}

## Related Checklists

- [Motor Rotation and Overload Verification]({{ '/field-engineering/motor-rotation-verification/' | relative_url }})
