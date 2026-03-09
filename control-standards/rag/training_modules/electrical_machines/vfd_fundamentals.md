<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: ELECTRICAL_MACHINES
MODULE_ID: vfd_fundamentals
LEARNING_LEVEL: intermediate

INDEX_TAGS:
  topics: ["vfd", "variable_frequency_drive", "pwm", "dc_bus", "vector_control"]
  systems: ["motor_drive", "machine"]
-->

# Variable Frequency Drive Fundamentals

## 0. Purpose

This module explains what a VFD does, how it is built internally, and what practical issues matter when connecting a drive to a real motor system.

## 1. Simple explanation

A variable frequency drive controls an AC motor by changing the frequency and voltage delivered to the motor.

In plain terms:

- line power comes in at fixed frequency
- the drive converts that power to DC
- the drive switches the DC back into a controlled AC output
- the motor responds to the commanded frequency and voltage

## 2. Main internal stages

The basic power path is:

`incoming AC -> rectifier -> DC bus -> inverter -> motor`

### Rectifier

The rectifier converts incoming AC to DC.

Common drive families use either:

- diode rectifiers for standard one-way power flow
- active front ends where regeneration or tighter line control is needed

### DC bus

The DC bus stores and smooths energy using capacitors.

For rough mental models only:

- `230 Vac` class drives often operate around `325 Vdc`
- `480 Vac` class drives often operate around `650 Vdc`

Actual values still depend on supply condition and drive design.

### Inverter

The inverter switches the DC bus rapidly, usually with IGBT or similar power devices, to create a controlled AC waveform for the motor.

That output is commonly created with PWM.

## 3. What PWM means

PWM stands for pulse width modulation.

The drive does not create a perfect analog sine wave directly. Instead, it switches the output devices rapidly and the motor responds to the average effect of those switching pulses.

This is why VFD systems raise practical questions about:

- insulation stress
- cable routing
- grounding and shielding
- motor heating at low speed

## 4. Common control methods

### V/Hz control

This is a simpler method that maintains a basic voltage-to-frequency relationship.

It is often acceptable for variable-torque loads such as:

- fans
- pumps
- simple conveyors

### Vector control

Vector control improves torque response and speed regulation.

Common forms are:

- sensorless vector control
- closed-loop vector control with feedback

This matters when the load requires stronger low-speed torque or tighter speed performance.

## 5. Practical integration issues

When a VFD is added, the motor system should be reviewed as a coordinated package rather than as isolated parts.

Key issues include:

- motor suitability for inverter duty
- reduced cooling if the motor runs slowly for long periods
- long motor leads and higher `dv/dt` stress
- cable noise coupling into control circuits
- bearing-current risk in some installations
- braking-energy handling for high-inertia loads

## 6. Typical protections and monitors

Most drives include protective or diagnostic functions such as:

- overcurrent
- overvoltage
- undervoltage
- motor overload model
- ground-fault detection
- overtemperature

These functions help, but they do not remove the need for correct branch protection, grounding, and motor setup.

## 7. Practical takeaway

The main engineering mistake is treating a VFD as only a speed-control box.

In practice, the drive changes:

- the power architecture
- the motor stress profile
- the wiring and EMC concerns
- the commissioning process

## Related files

- [VFD Motor Integration Review](../../design_framework/motor_systems/vfd_motor_integration_review.md)
- [Motor Selection Workflow](../../design_framework/motor_systems/motor_selection_workflow.md)
- [Drive Commissioning](../../commissioning_checklists/checklists/drive_commissioning.md)

## Related standards

- [NEC_2023__Art430__motors_motor_circuits_and_controllers.md](../../standards_intelligence/us/nec/NEC_2023__Art430__motors_motor_circuits_and_controllers.md)
- [NFPA79_2024__Ch12__motors_and_associated_equipment.md](../../standards_intelligence/us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md)
- [IEC60204_1_2018__Clause12__motors_and_drives.md](../../standards_intelligence/international/machinery/iec_60204_1/IEC60204_1_2018__Clause12__motors_and_drives.md)
- [UL508A_2022__motor_controllers_and_drives.md](../../standards_intelligence/us/ul_508a/UL508A_2022__motor_controllers_and_drives.md)
