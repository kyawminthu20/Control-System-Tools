---
layout: training-module
title: "DC Motor Basics"
description: "This module explains the main construction and current path of a classical industrial DC motor."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Motors, Drives, and Motion"
    url: "/fundamentals/motors/"
repo_path: "control-standards/rag/training_modules/electrical_machines/dc_motor_basics.md"
redirect_from:
  - /training/electrical-machines/dc-motor-basics/
  - /training/electrical-machines/dc-motor-basics/index.html

---

## Purpose

This module explains the main construction and current path of a classical industrial DC motor.

## Simple explanation

A DC motor produces torque by energizing a rotating armature inside a stationary magnetic field.

Unlike a squirrel-cage induction motor, the rotor current path is supplied intentionally through brushes and a commutator.

## Main magnetic structure

- **Yoke and poles** provide the main magnetic path.
- **Field windings** create the stationary magnetic field.
- **Interpoles and compensating windings** help control commutation and magnetic distortion under load.

## Main rotating structure

- **Armature core** is laminated to reduce losses.
- **Armature windings** are placed in rotor slots.
- **Active conductor sections** inside the magnetic field develop torque.
- **Overhang sections** connect the windings but do not contribute directly to torque.

## Commutator and brush function

The commutator solves the problem of getting power into a rotating winding system.

- **Brushes** stay stationary.
- **Commutator segments** rotate with the armature.
- The brush/commutator interface switches the current path so the developed torque stays in the same rotational direction.

## Practical field ideas

- Commutation quality depends on brush condition, spring pressure, and commutator surface condition.
- Maintenance quality matters more on DC motors than on many induction motors.
- Brush wear, sparking, and contamination are practical failure clues.

## Why this still matters

Even though many modern systems use AC motors and VFDs, DC motors still appear in legacy lines, cranes, mills, and retrofit environments.

Engineers and technicians still need to recognize:

- what the commutator is doing
- why brush problems cause operational trouble
- why armature and field issues are not the same failure mode

## Related standards

- NFPA 79 2024, Chapter 12 — Motors and Associated Equipment
- IEC 60204-1 2018, Clause 12 — Motors and Drives

These standards govern application, protection, and integration, not the full internal motor-construction theory.

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/motors/induction-motor-basics/' | relative_url }}">&larr; Induction Motor Basics</a>
  <a href="{{ '/fundamentals/motors/' | relative_url }}">↑ Motors, Drives, and Motion</a>
  <a href="{{ '/fundamentals/motors/motor-nameplates-slip-torque/' | relative_url }}">Motor Nameplates, Slip, and Torque &rarr;</a>
</div>
