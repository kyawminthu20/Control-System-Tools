---
layout: training-module
title: "Multi-Axis Coordination"
description: "How coordinated motion controllers synchronize multiple axes — master-slave coupling, electronic gearing, interpolation, and the architecture decisions that determine accuracy and safety."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Control Systems"
    url: "/fundamentals/control/"
related_standards: []
redirect_from:
  - /fundamentals/control/multi-axis-coordination/
  - /fundamentals/control/multi-axis-coordination/index.html

---

## Purpose

Multi-axis coordination is the control architecture used when two or more axes must move in a defined spatial or temporal relationship — an X-Y gantry tracing a path, a servo press coordinating ram position with rotary cam timing, or a winding machine maintaining tension between a drive roll and a winder. Simply starting both axes simultaneously is not coordination; it is hoping they stay synchronized under varying loads, inertias, and disturbances.

Coordinated motion requires the motion controller to manage the relationship between axes explicitly, ensuring synchronization is maintained deterministically.

---

## Core Coordination Modes

### Master-Slave

One axis is designated the master; one or more follower axes track it with a defined relationship. The follower's command is derived from the master's actual or commanded position rather than from an independent time-based profile.

- **Rigid coupling:** follower = master × gear ratio (electronic gearbox)
- **Cam-based coupling:** follower position is a function of master position defined by a cam table — allows non-linear relationships
- **Phase offset:** follower tracks master but with a defined lag or lead in position or angle

Used in: registration systems, print/cut machines, flying shear, rotary indexers, winding and unwinding.

---

### Electronic Gearing

A specific form of master-slave where the follower maintains a fixed ratio to the master. The ratio may be adjusted on-the-fly for applications like gear-change simulation, tension control, or synchronization with a line encoder.

Key parameter: **gear ratio** = follower units per master unit

Electronic gearing requires that the position loop of the follower closes against the master's position feedback, not against a motion profile generator. This is an architecture decision in the motion controller — not just a parameter.

---

### Linear Interpolation

Two or more axes move simultaneously along a straight line in Cartesian space. The motion controller calculates individual axis velocities such that the endpoint is reached simultaneously, producing a straight-line toolpath.

Used in: CNC machining, robot linear moves, gantry systems, laser cutting.

The interpolator runs at the motion controller level and produces coordinated position commands to each axis at each update cycle. Accuracy depends on the update rate and the quality of each axis's position control.

---

### Circular Interpolation

A specific interpolation mode producing circular or arc toolpaths by continuously recalculating the direction of motion in the X-Y (or other) plane.

Used in: CNC arcs, robotic circular welds, coordinated scanning.

---

### Synchronous Motion (Timed)

All axes execute their profiles on a shared time base, launched simultaneously from the same trigger. Each axis has an independent profile but they are coordinated in time rather than in position.

Used in: pick-and-place, Cartesian robots with independent axis profiles, applications where axes don't interact spatially but must finish together.

---

## Synchronization Architecture

Effective multi-axis coordination requires:

**Shared time base:** All axes must operate on the same clock. EtherCAT, PROFINET IRT, and SERCOS distribute a synchronized cycle time to all nodes. Standard Ethernet does not — this is why fieldbus selection matters for coordinated motion.

**Coordinated update rate:** The motion controller must issue coordinated commands to all axes at every cycle. A cycle time mismatch between axes causes following error and path deviation.

**Follower position closure:** In master-slave and electronic gearing, the follower's position loop must close against the master encoder signal, not against a reconstructed estimate. Latency in the master signal introduces phase error.

**Defined behavior at fault:** If the master axis faults mid-move, what happens to the followers? This must be designed explicitly. Common approaches: followers continue to their last commanded position (safe if they are at rest), followers decelerate at a defined rate, or all axes fault simultaneously.

---

## Common Problems

| Problem | Likely cause |
|---|---|
| Path deviation in Cartesian moves | Axis following error mismatch; one axis lagging |
| Synchronization error grows at speed | Insufficient loop bandwidth on follower; fieldbus jitter |
| Follower overshoots on master stop | Follower inertia mismatch; insufficient velocity feedforward |
| Phase error in cam-based coordination | Latency in master feedback path; cam table resolution |
| Gantry racking (skew) | Asymmetric load or gain mismatch between paired axes |

---

## Gantry (Dual-Drive Single-Axis) Special Case

A gantry with two motors on a single axis is a common variant. The two drives must produce equal force at all times while moving the same carriage. If their outputs differ, the gantry racks (skews on its guides).

Implementation options:
- **Master-slave torque mode:** one axis controls position; the second follows in torque mode, slaved to produce equal force
- **Cross-coupling control:** position error of each axis is corrected using the error from both axes together
- Both require careful mechanical alignment and matched inertias

---

## Engineering Takeaways

- Starting two axes simultaneously is not coordination — it is hoping for synchronization without enforcing it.
- Master-slave and electronic gearing derive the follower command from the master's feedback, not from an independent profile.
- Coordinated motion requires a deterministic, synchronized fieldbus — standard Ethernet introduces jitter that accumulates as path error.
- Fault behavior for multi-axis systems must be designed explicitly at commissioning time.
- Gantry racking is a mechanical and control problem simultaneously — alignment, matched gains, and cross-coupling must all be addressed.

---

## Related Modules

- [Servo Tuning Strategy]({{ '/fundamentals/control/servo-tuning/' | relative_url }}) — tuning individual axes before coordinating them
- [Deterministic vs Non-Deterministic Control]({{ '/fundamentals/control/deterministic-nondeterministic-control/' | relative_url }}) — why fieldbus choice matters for synchronization
- [Control Loop Architectures]({{ '/fundamentals/control/control-loop-architectures/' | relative_url }}) — how master-slave fits into the broader control hierarchy
