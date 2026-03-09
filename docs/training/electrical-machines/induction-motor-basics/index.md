---
layout: default
title: "Induction Motor Basics"
description: "This module explains the basic operating chain of a three-phase induction motor in plain engineering language."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Electrical Machines"
    url: "/training/electrical-machines/"
repo_path: "control-standards/rag/training_modules/electrical_machines/induction_motor_basics.md"
---

<div class="page-header">
  <span class="page-header__label">Training — Electrical Machines</span>
  <h1>Induction Motor Basics</h1>
</div>

## Purpose

This module explains the basic operating chain of a three-phase induction motor in plain engineering language.

## Simple explanation

An induction motor works because the stator creates a rotating magnetic field and the rotor responds to that field without being wired directly to the line supply.

That is the key difference:

- stator receives the electrical supply directly
- rotor develops current by induction

## Main physical parts

- **Frame and end shields** support the machine mechanically.
- **Bearings and shaft** let torque reach the driven load.
- **Cooling system** removes heat so winding insulation is not damaged.
- **Stator** contains the stationary windings that create the rotating field.
- **Rotor** is commonly a squirrel-cage assembly of bars and end rings.

## How rotation is created

Balanced three-phase current in the stator creates a magnetic field that rotates around the air gap.

That moving field cuts the rotor conductors and induces rotor current.

The induced rotor current creates its own magnetic field, and the interaction between the rotor field and the stator field produces torque.

## Why slip is necessary

The rotor does not fully catch the rotating field during normal torque-producing operation.

That speed difference is called **slip**.

Slip matters because without relative motion between the field and the rotor, rotor current would collapse and useful torque would disappear.

## Practical ideas to remember

- More load usually means more current and more slip.
- Heat matters as much as electrical connection.
- Rotor bars are often skewed to reduce magnetic locking and smooth operation.
- Induction motors are simple mechanically, but protection and application still depend on nameplate data and system context.

## When this helps in real work

Use this mental model when you need to reason about:

- why a motor slows slightly under load
- why overload protection matters
- why a stalled or jammed load causes high current and heat
- why VFDs and starting methods affect motor behavior

## Related standards

- NEC 2023, Article 430 — Motors, Motor Circuits, and Controllers
- NFPA 79 2024, Chapter 12 — Motors and Associated Equipment
- IEC 60204-1 2018, Clause 12 — Motors and Drives
- UL 508A 2022 — Motor Controllers and Drives

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <span></span>
  <a href="{{ '/training/electrical-machines/' | relative_url }}">↑ Electrical Machines</a>
  <a href="{{ '/training/electrical-machines/dc-motor-basics/' | relative_url }}">DC Motor Basics &rarr;</a>
</div>
