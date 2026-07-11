---
layout: training-module
title: "Motor and VFD Equations Reference"
description: "This module collects the most useful motor and VFD equations into one reference note for training and first-pass engineering review."
breadcrumb:
  - name: "Training"
    url: "/fundamentals/"
  - name: "Motors, Drives, and Motion"
    url: "/fundamentals/motors/"
repo_path: "control-standards/rag/training_modules/electrical_machines/motor_and_vfd_equations_reference.md"
redirect_from:
  - /fundamentals/electrical-machines/motor-vfd-equations/
  - /fundamentals/electrical-machines/motor-vfd-equations/index.html

---

## Purpose

This module collects the most useful motor and VFD equations into one reference note for training and first-pass engineering review.

Use these as working relationships, not as a substitute for detailed manufacturer data or standards-based design methods.

## Mechanical power and torque

Core relationship:

`P = T x omega`

Where:

- `P` = mechanical power
- `T` = torque
- `omega` = angular velocity

Common engineering form:

`P(kW) = T(Nm) x rpm / 9550`

Horsepower form:

`HP = T(lb-ft) x rpm / 5252`

## Synchronous speed

For AC machines:

`N_s = 120 x f / poles`

Where:

- `N_s` = synchronous speed in rpm
- `f` = electrical frequency
- `poles` = number of poles

This is why changing VFD output frequency changes motor speed.

## Slip

For induction motors:

`s = (N_s - N_r) / N_s`

Where:

- `N_s` = synchronous speed
- `N_r` = rotor speed

Slip is required for induction-motor torque production.

## Efficiency

`eta = P_out / P_in`

Efficiency is a ratio between useful mechanical output and electrical input.

## Power factor

`PF = Real Power / Apparent Power`

In simple terms, power factor indicates how effectively current is being converted into useful power.

## Three-phase power reminder

For quick review:

`P = sqrt(3) x V_LL x I_L x PF`

This is a useful relationship when estimating the electrical side of a motor system.

## VFD speed relationship

A VFD changes motor speed mainly by changing output frequency.

First-pass rule:

- lower output frequency → lower synchronous speed
- higher output frequency → higher synchronous speed until voltage and control limits are reached

## Practical cautions

- Equations alone do not select a motor or drive correctly.
- Real design still depends on nameplate data, load profile, duty cycle, and manufacturer ratings.
- Do not use simplified equations as a substitute for conductor, protection, or thermal review.

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/motors/motor-efficiency-losses/' | relative_url }}">&larr; Motor Efficiency, Power Factor, and Losses</a>
  <a href="{{ '/fundamentals/motors/' | relative_url }}">↑ Motors, Drives, and Motion</a>
  <a href="{{ '/fundamentals/motors/servo-feedback-inertia/' | relative_url }}">Servo Feedback and Inertia Matching &rarr;</a>
</div>
