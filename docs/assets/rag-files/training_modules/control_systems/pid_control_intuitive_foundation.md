<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: CONTROL_SYSTEMS
MODULE_ID: pid_control_overview
LEARNING_LEVEL: foundational

INDEX_TAGS:
  topics: ["pid", "feedback_control", "overview", "reading_path", "pi_vs_pid", "heater_control", "industrial_pid"]
  systems: ["control_loop", "process_control", "motion_axis", "machine", "plc", "vfd", "servo_drive", "heater"]
-->

# PID Control Overview

## 0. Purpose

This note is the entry point for the PID content in `training_modules/control_systems/`.

Use it to understand:

- what PID means at a high level
- where each deeper note fits
- which file to read for intuition, PLC implementation, loop architecture, or heater control

## 1. Quick reference

PID combines three types of correction:

| Term | Primary role | Typical effect |
| --- | --- | --- |
| `P` | reacts to present error | makes response faster |
| `I` | accumulates past error | removes steady-state offset |
| `D` | reacts to error trend | reduces overshoot and improves damping |

A useful shorthand is:

- `P` = present error
- `I` = accumulated past error
- `D` = future trend inferred from current rate of change

## 2. Recommended reading path

Use the PID notes in this order:

| File | Focus | Use it when you need |
| --- | --- | --- |
| [pid_control_intuition.md](./pid_control_intuition.md) | feedback basics and PID intuition | the mental model first |
| [industrial_pid_implementation.md](./industrial_pid_implementation.md) | PLC-style signals, bias, limits, sample time, Rockwell, Siemens | the controller as it appears in real platforms |
| [industrial_control_loop_architectures.md](./industrial_control_loop_architectures.md) | PI vs PID, VFD speed loops, servo loops, process loops | context for how loops are arranged in machines |
| [pid_heater_control_with_contactor.md](./pid_heater_control_with_contactor.md) | PI plus time-proportioning, minimum on/off time, safety logic, state machine | a real heater-control design with binary output hardware |

## 3. How the PID content is organized

The PID material used to sit in one long note. It is now split into smaller handbook-style modules so it is easier to:

- scan quickly
- retrieve specific topics in RAG workflows
- reuse on the website without one oversized page
- separate general theory from actuator-specific design details

## 4. Engineering takeaways

- Most industrial loops are effectively **PI**, not full PID.
- Derivative is most useful when transient behavior matters and feedback quality is good.
- PLC PID blocks always live inside a larger practical structure that includes limits, filters, sample time, and permissives.
- Heater control through a contactor is not a normal analog-output PID problem.
- A contactor-based heater loop should be treated as **PI plus output scheduling**, not as a fast continuous loop.

## 5. Typical application areas

PID-style thinking appears across:

- temperature control
- pressure control
- flow control
- level control
- speed control
- tension control
- motion and servo functions

The core logic stays recognizable, but the loop architecture and tuning constraints change significantly between those applications.

## 6. Engineering takeaway

Start with the intuition file if the question is "what is PID doing?".

Jump to the implementation file if the question is "what do SP, PV, CV, bias, limits, and sample time mean in a PLC?".

Jump to the architecture file if the question is "why is this drive loop PI instead of PID?".

Jump to the heater-control file if the question is "how do I control temperature with a contactor and minimum switching time?".

## Related files

- [PID Control Intuition](./pid_control_intuition.md)
- [Industrial PID Implementation](./industrial_pid_implementation.md)
- [Industrial Control Loop Architectures](./industrial_control_loop_architectures.md)
- [PID Heater Control With Contactor](./pid_heater_control_with_contactor.md)
- [Servo Drive Fundamentals](../../training_modules/electrical_machines/servo_drive_fundamentals.md)
- [Motor Control Methods and Operating Regions](../../training_modules/electrical_machines/motor_control_methods_and_operating_regions.md)
- [Servo Commissioning Workflow](../../design_framework/motor_systems/servo_commissioning_workflow.md)

## Related standards

Use these when the PID loop is part of machine control implementation rather than pure theory:

- [NFPA79_2024__Ch09__control_circuits_and_control_functions.md](../../standards_intelligence/us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md)
- [IEC60204_1_2018__Clause09__control_circuits_and_functions.md](../../standards_intelligence/international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md)
