---
layout: training-module
title: "Interlocks, Permissives & Safety Trips"
description: "Three distinct layers of protective logic — what each one is, how they differ, and how they must be separated in control system design."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Control Systems"
    url: "/fundamentals/control/"
related_standards:
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
redirect_from:
  - /training/control-systems/interlocks-permissives-safety-trips/
  - /training/control-systems/interlocks-permissives-safety-trips/index.html

---

## Purpose

Interlocks, permissives, and safety trips are three distinct categories of protective logic. They operate at different points in the machine lifecycle, respond to different conditions, and carry different consequences when they activate. Treating them as the same thing — or mixing them in the same logic layer — is one of the most common design failures in industrial control systems.

---

## Definitions

### Permissives — conditions required to start

Permissives are pre-start conditions. The machine will not start unless all permissives are satisfied.

Examples:
- Air pressure within range
- Guards confirmed closed
- Temperature within acceptable band
- Previous cycle complete

**If a permissive is not met → the machine will not start.** There is no interruption of a running machine; permissives are evaluated at the start transition only.

---

### Interlocks — conditions required to keep running

Interlocks are runtime conditions. The machine started, but must stop or slow if a condition is violated during operation.

Examples:
- Cooling flow maintained above minimum
- Motor thermal protection not tripped
- Process variable within operating range
- Communication with a downstream device confirmed

**If an interlock trips during operation → controlled stop.** The response is defined: it may be a ramp-down, a hold, or a stop-in-sequence rather than an immediate de-energize.

---

### Safety Trips — hard safety events that override everything

Safety trips respond to hazardous conditions and override normal control logic entirely.

Examples:
- Emergency stop (E-stop) activated
- Safety gate opened during operation
- Overpressure detected (SIL/PL-rated)
- Safe torque off command from safety controller

**If a safety trip fires → immediate safe state.** The response is de-energize-to-trip: outputs go to their safe (off) condition. This cannot be masked or overridden by the standard PLC program.

---

## Comparison

| | Permissives | Interlocks | Safety Trips |
|---|---|---|---|
| **When evaluated** | Before start | During operation | Any time |
| **Response** | Prevent start | Controlled stop | Immediate de-energize |
| **Implemented in** | Standard PLC | Standard PLC | Safety PLC / safety relay |
| **Can be masked?** | Sometimes (with bypass key) | Sometimes | Never |
| **SIL/PL required?** | No | No | Yes (if safety function) |

---

## Logic Separation

Standard control logic and safety logic must be kept separate:

- **Standard PLC:** permissives, interlocks, sequence logic
- **Safety PLC or safety relay:** safety trips, SIL/PL-rated functions

Safety trips must be implemented in certified safety hardware with the required SIL or PL rating. Putting a safety function in a standard PLC program — even if the logic is correct — does not constitute a valid safety function under IEC 62061 or ISO 13849-1.

Mixing safety logic into the standard program creates:
- Audit failures
- Unverifiable safety claims
- Potential masking of safety functions by standard logic

---

## Bypass Design

Where operational bypass of a permissive or interlock is required (e.g., for maintenance), the bypass must be:

1. Physically keyed or access-controlled
2. Visible to the operator (annunciated)
3. Time-limited or automatically cleared
4. Logged

Safety trips **cannot be bypassed** during normal operation. Maintenance-mode bypass of safety functions requires a formal bypass procedure with additional safeguards in place.

---

## Engineering Takeaways

- Permissives answer: "Is it safe to start?"
- Interlocks answer: "Is it still safe to run?"
- Safety trips answer: "Is there a hazard that requires an immediate stop regardless of anything else?"
- The separation between standard and safety logic is not just good practice — it is a certification requirement.
- Layered protective logic means failures in one layer do not propagate into another.

---

## Related Modules

- [Machine State Model]({{ '/fundamentals/control/machine-state-model/' | relative_url }}) — where interlocks and permissives fit in the state machine
- [Async Faults in Distributed Systems]({{ '/fundamentals/control/async-faults-distributed-systems/' | relative_url }}) — how faults propagate across networked devices
