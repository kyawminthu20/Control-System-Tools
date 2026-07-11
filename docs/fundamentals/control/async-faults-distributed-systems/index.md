---
layout: training-module
title: "Async Faults in Distributed Systems"
description: "How to detect, classify, and respond to faults that arrive out of sequence across multi-device control architectures — PLCs, drives, sensors, and IPCs."
breadcrumb:
  - name: "Training"
    url: "/fundamentals/"
  - name: "Control Systems"
    url: "/fundamentals/control/"
related_standards:
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
redirect_from:
  - /fundamentals/control-systems/async-faults-distributed-systems/
  - /fundamentals/control-systems/async-faults-distributed-systems/index.html

---

## Purpose

In a single-device system, faults are synchronous: the PLC detects a fault on a scan cycle and responds in the same program execution context. In a distributed system — where a PLC coordinates drives, sensors, remote I/O, safety controllers, and IPCs over a network — faults arrive asynchronously. Network delays, device restarts, and partial failures mean the main controller cannot assume fault reports are timely, complete, or consistent.

Designing for asynchronous fault handling means building detection, classification, and response as explicit layers rather than assuming faults will always arrive cleanly.

---

## The Problem

Distributed systems introduce failure modes that don't exist in standalone controllers:

- **Network delays** — a fault condition exists at the device but the controller doesn't know yet
- **Race conditions** — two devices report conflicting status nearly simultaneously
- **Partial failures** — one subsystem fails while others continue operating, creating an inconsistent system state
- **Silent failures** — a device stops communicating without sending a fault message
- **Cascading faults** — a fault in one subsystem triggers secondary faults in dependent subsystems

A fault-handling design that works for a single PLC will fail in a distributed system if it assumes faults arrive before their consequences do.

---

## Four-Layer Fault Handling Model

### Layer 1 — Detection

The controller must actively probe device health rather than waiting for fault messages.

Detection mechanisms:
- **Heartbeats** — regular status messages between controller and each device; absence = failure
- **Watchdog timers** — each communication channel has a timeout; expiry triggers fault detection
- **Status word monitoring** — drive, safety, and I/O device status words polled every scan cycle
- **Timeout monitoring** — expected responses (motion complete, valve confirmed, etc.) that don't arrive within a defined window trigger a fault

Detection must be faster than the worst-case consequence of the failure. For safety functions, detection time is a component of the overall reaction time calculation.

---

### Layer 2 — Classification

Not all faults require the same response. Classifying faults before responding prevents unnecessary production stops and ensures the severity of the response matches the severity of the fault.

| Class | Definition | Response |
|---|---|---|
| **Critical** | Hazard or loss of safe state possible | Immediate transition to FAULT — full stop |
| **Major** | Production impact, no immediate hazard | Controlled stop, hold current state |
| **Minor / Warning** | Degraded operation but safe | Log, annunciate, continue with monitoring |
| **Communication fault** | Loss of link without confirmed device state | Treat as Critical until device state confirmed |

Classification must be defined at design time, not determined ad hoc during operation. Each device's failure modes should have a pre-assigned class.

---

### Layer 3 — Response

The system response to a classified fault must be deterministic and reproducible.

- **Critical fault:** transition machine to FAULT state, de-energize outputs to safe condition, latch fault until manually cleared
- **Major fault:** complete the current motion safely if possible, then hold; do not proceed to next step
- **Minor fault:** log with timestamp, source device, and fault code; annunciate to operator; continue

Fault response must not depend on the order in which fault messages arrive. If two faults arrive simultaneously, the higher-severity class determines the response.

---

### Layer 4 — Recovery

Recovery logic determines how the system returns to operation after a fault is cleared.

- **Manual reset:** operator acknowledges fault, confirms machine state, commands reset — required for all Critical faults and all safety trips
- **Automatic recovery:** system re-attempts connection or clears non-critical fault after a defined delay — acceptable for communication faults with no safety implication
- **State validation before recovery:** before exiting FAULT, the system must confirm that all subsystems are in a known, consistent state — not just that the fault condition has cleared

Recovery logic should include a **re-validation scan**: after a Critical fault clears, the system checks all permissives and subsystem status before allowing restart, as if starting from IDLE.

---

## Fault Log Requirements

Every fault must be recorded with:
- Timestamp (controller time, not device time)
- Source device
- Fault code or description
- System state at fault time
- Operator action (if any) and recovery time

This supports root-cause analysis and documents the fault history required by IEC 61511 and IEC 62061 for SIS and SRECS validation.

---

## Engineering Takeaways

- Assume faults will arrive late, out of order, or not at all — design detection to be active, not passive.
- A communication timeout with an unknown device state is a Critical fault until proven otherwise.
- Classification must be done at design time; doing it during operation creates inconsistent behavior.
- Recovery is not just clearing a fault bit — it requires re-validating system state.
- Timestamp faults at the controller, not the device, to maintain consistent ordering across a distributed system.

---

## Related Modules

- [Machine State Model]({{ '/fundamentals/control/machine-state-model/' | relative_url }}) — the FAULT state and recovery transitions
- [Interlocks, Permissives & Safety Trips]({{ '/fundamentals/control/interlocks-permissives-safety-trips/' | relative_url }}) — the protective layers that generate faults
- [Deterministic vs Non-Deterministic Control]({{ '/fundamentals/control/deterministic-nondeterministic-control/' | relative_url }}) — why timing matters in distributed fault detection
