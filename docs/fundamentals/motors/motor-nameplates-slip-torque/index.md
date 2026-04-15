---
layout: training-module
title: "Motor Nameplates, Slip, and Torque"
description: "This module turns common motor-training concepts into a practical review note for selection and troubleshooting."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Motors, Drives, and Motion"
    url: "/fundamentals/motors/"
repo_path: "control-standards/rag/training_modules/electrical_machines/motor_nameplates_slip_and_torque.md"
redirect_from:
  - /fundamentals/motors/motor-nameplates-slip-torque/
  - /fundamentals/motors/motor-nameplates-slip-torque/index.html

---

## Purpose

This module turns common motor-training concepts into a practical review note for selection and troubleshooting.

## Nameplate items that matter first

Read these before assuming anything about the motor:

- rated voltage
- full-load current
- frequency
- rated speed
- phase
- horsepower or power rating
- service factor
- insulation class
- frame size
- enclosure type

## Rated speed versus synchronous speed

For induction motors, synchronous speed is the speed of the rotating magnetic field.

The common relationship is:

`synchronous speed = 120 x frequency / pole count`

The nameplate usually shows **rated speed**, which is lower than synchronous speed under normal load.

## Slip in practical terms

Slip is the difference between synchronous speed and actual rotor speed.

It increases with load because the rotor must lag the field more to develop additional torque.

## Torque-curve regions to recognize

- **Starting torque**: torque available at standstill
- **Pull-up torque**: the lowest torque available while accelerating
- **Breakdown torque**: the maximum torque the motor can produce without stalling
- **Rated-torque region**: the normal continuous operating area

## NEMA design letters in simple terms

- **Design B** is the common general-purpose baseline.
- **Design C** is often used where higher starting torque is needed.
- **Design D** is a higher-slip option for very demanding starting duties.

Exact application still depends on the real load profile.

## Enclosure type is not a side note

Common examples:

- `ODP`
- `TENV`
- `TEFC`
- `TEBC`

The enclosure affects cooling method, contamination tolerance, and environmental suitability.

## Practical takeaway

The most common field mistake is treating horsepower as the whole story.

Real motor review must also consider:

- speed requirement
- load type
- starting method
- enclosure/environment
- protection settings

## Related standards

- NEC 2023, Article 430 — Motors, Motor Circuits, and Controllers
- NFPA 79 2024, Chapter 12 — Motors and Associated Equipment
- IEC 60204-1 2018, Clause 12 — Motors and Drives

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/motors/dc-motor-basics/' | relative_url }}">&larr; DC Motor Basics</a>
  <a href="{{ '/fundamentals/motors/' | relative_url }}">↑ Motors, Drives, and Motion</a>
  <a href="{{ '/fundamentals/motors/motor-family-comparison/' | relative_url }}">Motor Family Comparison &rarr;</a>
</div>
