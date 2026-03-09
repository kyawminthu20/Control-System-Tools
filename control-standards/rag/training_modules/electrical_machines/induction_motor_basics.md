<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: ELECTRICAL_MACHINES
MODULE_ID: induction_motor_basics
LEARNING_LEVEL: foundational

INDEX_TAGS:
  topics: ["induction_motors", "rotating_field", "squirrel_cage", "slip"]
  systems: ["machine", "motor_branch"]
-->

# Induction Motor Basics

## 0. Purpose

This module explains the basic operating chain of a three-phase induction motor in plain engineering language.

## 1. Simple explanation

An induction motor works because the stator creates a rotating magnetic field and the rotor responds to that field without being wired directly to the line supply.

That is the key difference:

- stator receives the electrical supply directly
- rotor develops current by induction

## 2. Main physical parts

- **Frame and end shields** support the machine mechanically.
- **Bearings and shaft** let torque reach the driven load.
- **Cooling system** removes heat so winding insulation is not damaged.
- **Stator** contains the stationary windings that create the rotating field.
- **Rotor** is commonly a squirrel-cage assembly of bars and end rings.

## 3. How rotation is created

Balanced three-phase current in the stator creates a magnetic field that rotates around the air gap.

That moving field cuts the rotor conductors and induces rotor current.

The induced rotor current creates its own magnetic field, and the interaction between the rotor field and the stator field produces torque.

## 4. Why slip is necessary

The rotor does not fully catch the rotating field during normal torque-producing operation.

That speed difference is called **slip**.

Slip matters because without relative motion between the field and the rotor, rotor current would collapse and useful torque would disappear.

## 5. Practical ideas to remember

- More load usually means more current and more slip.
- Heat matters as much as electrical connection.
- Rotor bars are often skewed to reduce magnetic locking and smooth operation.
- Induction motors are simple mechanically, but protection and application still depend on nameplate data and system context.

## 6. When this helps in real work

Use this mental model when you need to reason about:

- why a motor slows slightly under load
- why overload protection matters
- why a stalled or jammed load causes high current and heat
- why VFDs and starting methods affect motor behavior

## Related standards

- [NEC_2023__Art430__motors_motor_circuits_and_controllers.md](../../standards_intelligence/us/nec/NEC_2023__Art430__motors_motor_circuits_and_controllers.md)
- [NFPA79_2024__Ch12__motors_and_associated_equipment.md](../../standards_intelligence/us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md)
- [IEC60204_1_2018__Clause12__motors_and_drives.md](../../standards_intelligence/international/machinery/iec_60204_1/IEC60204_1_2018__Clause12__motors_and_drives.md)
- [UL508A_2022__motor_controllers_and_drives.md](../../standards_intelligence/us/ul_508a/UL508A_2022__motor_controllers_and_drives.md)
