---
layout: training-module
title: "Vibration and Resonance in Control Systems"
description: "Physical causes of vibration and resonance in controlled mechanical systems, and the control and mechanical strategies used to mitigate them."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Control Systems"
    url: "/training/control-systems/"
related_standards: []
---

## Purpose

Every real mechanical system has natural frequencies — frequencies at which the structure will oscillate if excited. When control system outputs (motor commands, valve strokes, actuator movements) excite these frequencies, the result is resonance: sustained oscillation that degrades accuracy, accelerates wear, produces noise, and in severe cases causes structural failure.

Understanding the causes of resonance and the strategies for mitigating it is essential for commissioning servo systems, diagnosing unexpected machine behavior, and selecting the right combination of mechanical and control-layer solutions.

---

## Resonance vs Vibration

**Vibration** is periodic mechanical oscillation. It has a frequency, amplitude, and cause. Not all vibration is resonance.

**Resonance** is vibration that occurs at a system's natural frequency — the frequency at which the structure oscillates with maximum amplitude for minimum input energy. At resonance, a small control input produces a large mechanical response.

The natural frequency of a mechanical system depends on:
- **Stiffness** — stiffer systems have higher natural frequencies
- **Mass / inertia** — heavier loads have lower natural frequencies

```
Natural frequency ∝ √(stiffness / mass)
```

---

## Common Causes

| Cause | Mechanism | Typical symptom |
|---|---|---|
| **Flexible structure** | Low structural stiffness allows deflection under load; stored energy releases as oscillation | Oscillation only under load; stable in free motion |
| **Long shaft or lead screw** | Shaft torsional compliance — shaft twists, then unwinds | Position error that oscillates after motion stops |
| **Loose coupling** | Backlash or wear in coupling introduces lost motion and impact loading | Audible knock or jump on direction reversal |
| **Ball screw compliance** | Axial compliance of the screw transmits oscillation to the nut | Vibration increasing with screw length or load |
| **Gear mesh frequency** | Periodic force from gear tooth engagement | Tonal noise at speed-dependent frequency |
| **Control loop gain too high** | Controller is fast enough to excite a mechanical natural frequency | Instability that worsens as gains increase |
| **Jerk discontinuity** | Abrupt acceleration changes excite structural modes | Vibration at start and end of motion profile |

---

## Detection Methods

**Visual / tactile:** Oscillation visible on the axis or structure; vibration felt at the mounting surface.

**Position or velocity trace:** Plot commanded vs actual position or velocity over time. Oscillation in the actual signal after the command has settled indicates resonance or poor damping.

**Drive FFT tool:** Most servo drives (Elmo, Siemens SINAMICS, Yaskawa, Beckhoff) include a built-in frequency response analysis tool. Apply a chirp or step excitation; look for peaks in the bode plot or power spectrum. Each peak is a resonant mode.

**External vibration sensor:** Accelerometer mounted to the structure during motion. Useful for identifying structural modes that don't show up in the encoder signal.

---

## Mitigation Strategies

### Mechanical solutions (preferred)

Fix the underlying mechanical cause whenever possible. Control-layer solutions suppress resonance without eliminating it; they add tuning complexity and reduce robustness.

- Increase structural stiffness (stiffer frame, shorter spans, additional bracing)
- Improve coupling (zero-backlash coupling, higher-stiffness coupling type)
- Reduce inertia ratio (larger motor, gearbox, or load redistribution)
- Fix alignment to reduce periodic forcing

---

### Control solutions

**Notch filter:** Attenuates a specific frequency band in the control output. Used when the resonant frequency is identified and mechanical correction is not practical.
- Center frequency = resonant frequency identified by FFT
- Depth = attenuation required (typically 20–40 dB)
- Width = narrow enough to avoid affecting control bandwidth; wide enough to cover frequency variation

**Reduce loop bandwidth:** Lowering gains reduces the frequency content of the control output, avoiding excitation of high-frequency structural modes. Accepted cost: slower response and larger following error.

**Low-pass filter on the velocity or position signal:** Smooths measurement noise and high-frequency disturbances. Must be designed carefully — too much filtering introduces phase lag that destabilizes the loop.

**Motion profile shaping:** S-curve or jerk-limited motion profiles reduce the high-frequency content of the command signal, avoiding the abrupt transitions that excite structural resonance. This is a first-line mitigation for end-of-travel oscillation.

---

## Diagnostic Rule

| Symptom | Start investigating |
|---|---|
| Oscillation only under load | Mechanical stiffness; resonance excited by load force |
| Oscillation stable at low speed, worse at high speed | Speed-dependent resonance (gear mesh, shaft) |
| Oscillation at all speeds and loads | Gain too high; reduce loop bandwidth |
| High-frequency squeal or whine | Resonance; use FFT to identify frequency, apply notch |
| Oscillation only after motion stops | Insufficient damping; adjust velocity gain or add filter |
| Random noise, no clear frequency | Electrical noise; check encoder shielding and grounding |

---

## Engineering Takeaways

- Resonance is a property of the mechanical system — control tuning can suppress it but cannot eliminate the underlying cause.
- The first response to resonance should be mechanical investigation, not gain adjustment.
- FFT analysis converts a "mystery vibration" into a specific frequency that can be targeted with a notch filter.
- Motion profile shaping (jerk limiting, S-curve) is often the simplest and most robust way to prevent resonance from being excited in the first place.
- Resonance frequency changes with load, temperature, and mechanical wear — notch filter settings may need adjustment over machine lifetime.

---

## Related Modules

- [Servo Tuning Strategy]({{ '/training/control-systems/servo-tuning/' | relative_url }}) — loop tuning, notch filter application, and resonance in commissioning context
- [Control Loop Architectures]({{ '/training/control-systems/control-loop-architectures/' | relative_url }}) — how filters integrate into the control loop
