---
layout: training-module
title: "Machine State Model"
description: "How to design structured control logic using finite state machines — states, transitions, entry conditions, and fault handling."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Control Systems"
    url: "/training/control-systems/"
related_standards:
  - name: "IEC 61131-3 (PLC Programming)"
    url: "/standards/"
---

## Purpose

A machine state model defines what states a machine can be in, what conditions allow transitions between them, and what actions execute in each state. It replaces scattered conditional logic with a structured, deterministic framework that is easier to debug, audit, and hand off.

The core idea: **a machine should always be in one clearly defined state, and transitions must be explicit and event-driven.**

---

## Standard State Sequence

Most industrial machines follow a predictable lifecycle:

```
INIT → IDLE → READY → RUN → PAUSE → STOPPING → STOPPED
                                ↓
                             FAULT → RECOVERY
```

Each state has:
- **Entry conditions** — what must be true to enter this state
- **Active actions** — what the machine does while in this state
- **Exit conditions** — what event or condition causes the transition

---

## Main State Model Types

| Type | Description | Used for |
|---|---|---|
| **Finite State Machine (FSM)** | Fixed set of states, event-driven transitions | PLC logic, robotics sequences, embedded systems |
| **Hierarchical State Machine (HSM)** | States nested inside parent states; child inherits parent behavior | Complex machines with shared fault handling |
| **Statechart** | HSM extended with parallel regions (concurrent states) | Multi-axis or multi-zone machines running simultaneously |
| **PackML** | ISA-88–derived standard state model for packaging/CPG machinery | Industry-standard interoperability between OEM equipment |
| **Sequential Function Chart (SFC)** | IEC 61131-3 graphical programming language for sequential processes | Batch processes, filling lines, assembly sequences |

For most PLC-based machinery, **FSM or HSM** is the right choice. PackML is required when integrating with line-management systems (OEE, SCADA, MES) that expect standardized state reporting.

---

## Design Principles

**Separate state logic from I/O logic.** The state manager decides what state the machine is in. Separate output logic then acts based on current state. This keeps the state machine readable and testable independently.

**Use a central state variable.** One location in the program owns the current state. All other logic reads it; no other logic writes to it. Multiple places writing state leads to race conditions.

**Fault overrides all states.** Any active fault transitions the machine to FAULT unconditionally — regardless of current state. This is not a normal transition; it is a pre-emption.

**Never rely on sequence order alone.** Logic that depends on "this ran before that" without an explicit state check is fragile. Always encode the precondition in the state model.

---

## Transition Example

```
READY → RUN only if:
  - all permissives TRUE
  - no active faults
  - operator start command received

Any fault → immediate FAULT state (from any state)

FAULT → RECOVERY only if:
  - fault condition cleared
  - operator reset acknowledged
```

---

## Fault State Design

The FAULT state should:
- De-energize outputs to a safe condition (de-energize-to-trip)
- Latch until explicitly reset
- Log the fault source and timestamp
- Require operator acknowledgment before recovery

Recovery may be automatic or manual depending on fault classification. Safety faults (SIL/PL) must always require manual reset.

---

## Engineering Takeaways

- A state machine reveals whether you think in systems, not just rungs.
- Debugging a state machine means checking one variable — the current state — and tracing which transition fired.
- Every real control problem eventually maps to a state model; making it explicit is always better than leaving it implicit in logic.
- For multi-machine lines, each machine has its own state model; line-level coordination is a separate state model above them.

---

## Related Modules

- [Interlocks, Permissives & Safety Trips]({{ '/training/control-systems/interlocks-permissives-safety-trips/' | relative_url }}) — the logic that governs transitions
- [Async Faults in Distributed Systems]({{ '/training/control-systems/async-faults-distributed-systems/' | relative_url }}) — fault handling across networked devices
