---
layout: training-module
title: "Servo Tuning Strategy"
description: "Loop-by-loop servo tuning from mechanical validation through current, velocity, and position loop commissioning — including resonance detection and feedforward."
breadcrumb:
  - name: "Training"
    url: "/fundamentals/"
  - name: "Control Systems"
    url: "/fundamentals/control/"
related_standards: []
redirect_from:
  - /fundamentals/control-systems/servo-tuning/
  - /fundamentals/control-systems/servo-tuning/index.html

---

## Purpose

Servo tuning is the process of adjusting control loop gains so a servo axis tracks its commanded position, velocity, or torque accurately and stably under real operating conditions. Autotune provides a starting point, but it assumes ideal mechanical conditions and validates against no-load behavior. Most servo problems encountered in practice — oscillation under load, resonance, instability on direction change — are not solvable by adjusting gains alone; they require mechanical understanding and loop-level diagnostics.

---

## Control Architecture

A servo drive implements nested control loops:

```
Position loop (outer)
    ↓
Velocity loop (middle)
    ↓
Current / Torque loop (inner)
```

The critical rule: **inner loops must be stable and well-tuned before outer loops are commissioned.** A poorly tuned current loop makes the velocity loop unstable. A poorly tuned velocity loop makes the position loop unstable. You cannot compensate for inner loop problems by adjusting outer loop gains.

---

## Step 1 — Mechanical Validation

Tuning cannot fix mechanical problems. Validate the mechanical system before touching gains.

| Check | What to look for |
|---|---|
| **Backlash** | Free play before resistance when reversing by hand; spike in following error on direction change |
| **Coupling** | Loose set screws, worn flexible coupling, cracked spider insert |
| **Alignment** | Angular or parallel shaft misalignment — causes vibration and bearing wear |
| **Stiffness** | Behavior that is stable in free motion but oscillates under load — low structural stiffness |
| **Inertia ratio** | Load-to-motor inertia ratio; rule of thumb is ≤ 5:1 for standard tuning; higher ratios require feedforward |
| **Bearing friction** | Binding or stick-slip under low-speed moves |

A symptom that only appears under load (squeal, oscillation, instability) is a mechanical or resonance problem until proven otherwise — not a tuning problem.

---

## Step 2 — Current Loop

The current loop controls motor torque. It runs at the highest bandwidth (typically 1–5 kHz) and is usually pre-tuned by the drive manufacturer.

Validation (not tuning from scratch):
1. Disable velocity and position loops
2. Apply a step current command (10–20% rated)
3. Observe: fast rise, minimal overshoot, no oscillation

| Symptom | Likely cause |
|---|---|
| Slow rise | Kp too low |
| High-frequency oscillation | Kp too high or motor parameters wrong |
| Low-frequency drift | Ki too high |
| Noisy signal | Encoder grounding or shielding issue |

The current loop bandwidth must be significantly higher than the velocity loop bandwidth (10× or more). This separation is what allows the outer loops to function.

---

## Step 3 — Velocity Loop

The velocity loop controls speed and compensates for load inertia and friction.

Tuning procedure:
1. Disable position loop; keep current loop active
2. Command velocity steps at representative speeds
3. Increase **Kp** until response is fast with slight oscillation beginning
4. Back off ~20%
5. Add **Ki** to remove steady-state error — add slowly; too much Ki causes low-frequency hunting

Monitor both velocity response and the current signal simultaneously. If velocity oscillates while current spikes sharply, the cause is mechanical resonance, not gain instability.

| Symptom | Cause |
|---|---|
| Sluggish response | Kp too low |
| Overshoot then oscillation | Kp too high |
| Hunting around setpoint | Ki too high |
| Instability only on direction change | Backlash |
| Instability only under load | Stiffness / resonance |

---

## Step 4 — Position Loop

The position loop controls final position accuracy.

Tuning procedure:
1. Keep velocity loop stable first
2. Increase **Kp (position gain)** until following error is acceptable without oscillation
3. Add **velocity feedforward (Kvff)** to reduce following error during motion — this improves tracking without increasing instability risk
4. Add **acceleration feedforward (Kaff)** for demanding profiles (high acceleration, press applications)

Following error is the key metric: the difference between commanded and actual position during motion. High following error means the loop is lagging; oscillation around the target means gains are too aggressive.

---

## Step 5 — Validate Under Real Load

This is where most commissioning fails. Always validate:
- Under full operating load, not just unloaded
- At the full speed range (low speed, mid speed, max speed)
- Through direction changes
- Under the actual motion profile (not just step inputs)

Systems with variable loads (press applications, clamping, cutting) may require gain scheduling: different gain sets for different operating modes (travel vs. loaded contact).

---

## Resonance Detection and Notch Filters

Mechanical systems have natural frequencies. If control loop gains excite a natural frequency, the result is resonance: a high-frequency oscillation or squeal that cannot be resolved by reducing gains globally.

Detection:
- Use the drive's built-in FFT tool (Elmo, Siemens, Yaskawa, Beckhoff all provide this)
- Look for peaks in the frequency response — a peak indicates a resonant frequency
- Common sources: flexible couplings, long shafts, ball screw compliance, frame structures

Notch filter:
- Suppresses a specific frequency band without affecting the rest of the control bandwidth
- Parameters: center frequency (Hz), depth (attenuation dB), width (Q factor)
- Apply after identifying the resonant frequency via FFT; do not guess the frequency

---

## Key Tuning Metrics

| Metric | Definition |
|---|---|
| Rise time | Time from step command to first crossing of target |
| Settling time | Time until response stays within tolerance band |
| Overshoot % | How far above target the response goes |
| Following error | Command − actual position during motion |
| Gain margin | How much more gain the loop could take before instability |
| Phase margin | Stability reserve in degrees — target ≥ 45° |

---

## Engineering Takeaways

- Mechanical validation before tuning — always. You cannot tune a bad mechanical system.
- Tune inner → outer: current, then velocity, then position.
- Autotune is a starting point, not a commissioning method.
- Symptoms that appear only under load are mechanical until proven otherwise.
- FFT analysis and notch filters solve resonance problems that gain reduction cannot.
- Feedforward improves tracking without reducing stability margin — prefer it over pushing proportional gains.

---

## Related Modules

- [Control Loop Architectures]({{ '/fundamentals/control/control-loop-architectures/' | relative_url }}) — how servo loops fit into broader control architecture
- [Vibration and Resonance]({{ '/fundamentals/control/vibration-resonance/' | relative_url }}) — physical causes and mechanical mitigation
- [Multi-Axis Coordination]({{ '/fundamentals/control/multi-axis-coordination/' | relative_url }}) — applying tuned axes to coordinated motion
