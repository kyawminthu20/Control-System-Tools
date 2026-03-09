<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: ELECTRICAL_MACHINES
MODULE_ID: dc_motor_basics
LEARNING_LEVEL: foundational

INDEX_TAGS:
  topics: ["dc_motors", "armature", "commutator", "brushes"]
  systems: ["machine", "motor_drive"]
-->

# DC Motor Basics

## 0. Purpose

This module explains the main construction and current path of a classical industrial DC motor.

## 1. Simple explanation

A DC motor produces torque by energizing a rotating armature inside a stationary magnetic field.

Unlike a squirrel-cage induction motor, the rotor current path is supplied intentionally through brushes and a commutator.

## 2. Main magnetic structure

- **Yoke and poles** provide the main magnetic path.
- **Field windings** create the stationary magnetic field.
- **Interpoles and compensating windings** help control commutation and magnetic distortion under load.

## 3. Main rotating structure

- **Armature core** is laminated to reduce losses.
- **Armature windings** are placed in rotor slots.
- **Active conductor sections** inside the magnetic field develop torque.
- **Overhang sections** connect the windings but do not contribute directly to torque.

## 4. Commutator and brush function

The commutator solves the problem of getting power into a rotating winding system.

- **Brushes** stay stationary.
- **Commutator segments** rotate with the armature.
- The brush/commutator interface switches the current path so the developed torque stays in the same rotational direction.

## 5. Practical field ideas

- Commutation quality depends on brush condition, spring pressure, and commutator surface condition.
- Maintenance quality matters more on DC motors than on many induction motors.
- Brush wear, sparking, and contamination are practical failure clues.

## 6. Why this still matters

Even though many modern systems use AC motors and VFDs, DC motors still appear in legacy lines, cranes, mills, and retrofit environments.

Engineers and technicians still need to recognize:

- what the commutator is doing
- why brush problems cause operational trouble
- why armature and field issues are not the same failure mode

## Related standards

- [NFPA79_2024__Ch12__motors_and_associated_equipment.md](../../standards_intelligence/us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md)
- [IEC60204_1_2018__Clause12__motors_and_drives.md](../../standards_intelligence/international/machinery/iec_60204_1/IEC60204_1_2018__Clause12__motors_and_drives.md)

These standards govern application, protection, and integration, not the full internal motor-construction theory.
