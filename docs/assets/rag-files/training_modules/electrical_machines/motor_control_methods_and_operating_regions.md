<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: ELECTRICAL_MACHINES
MODULE_ID: motor_control_methods_and_operating_regions
LEARNING_LEVEL: intermediate

INDEX_TAGS:
  topics: ["v_hz", "vector_control", "foc", "field_weakening", "regeneration"]
  systems: ["motor_drive", "motion_axis"]
-->

# Motor Control Methods and Operating Regions

## 0. Purpose

This module explains the main motor-control methods discussed in industrial drives and servo systems, plus two operating ideas that matter in real work:

- field weakening
- regeneration

## 1. V/Hz control

V/Hz control maintains a basic voltage-to-frequency relationship so motor flux stays in an acceptable range.

Typical uses:

- pumps
- fans
- simple conveyors

If the V/Hz ratio is too low:

- flux decreases
- torque falls
- acceleration suffers

If the V/Hz ratio is too high:

- magnetic saturation can occur
- current and heating increase

## 2. Vector control

Vector control improves torque response and low-speed behavior compared with simple V/Hz control.

It is commonly used when the application needs:

- stronger low-speed torque
- tighter speed regulation
- better dynamic response

## 3. Field-oriented control

FOC controls motor torque by controlling magnetic-field orientation.

Current is often separated conceptually into:

- d-axis current for flux
- q-axis current for torque

FOC is common in:

- servo drives
- EV motor control
- robotics

## 4. Servo loop context

Servo systems usually apply these control ideas within a closed-loop structure that includes:

- current loop
- velocity loop
- position loop

## 5. Field weakening

Above base speed, voltage limit becomes a constraint.

Flux is reduced so the machine can run faster, but torque capability drops.

This concept appears in:

- servo systems
- EV motors
- high-performance motor drives

## 6. Regeneration

Regenerative behavior occurs when the motor acts as a generator and energy flows back toward the DC bus.

Common examples:

- rapid deceleration
- lowering loads
- stopping high inertia systems

Typical responses include:

- braking resistor
- regenerative unit
- drive strategy that can absorb or return the energy

## 7. Practical takeaway

The control method changes:

- torque behavior
- low-speed performance
- tuning burden
- braking behavior
- acceptable application range

## Related files

- [VFD Fundamentals](./vfd_fundamentals.md)
- [Servo Drive Fundamentals](./servo_drive_fundamentals.md)
- [VFD and Servo Architecture Diagrams](./vfd_and_servo_architecture_diagrams.md)
