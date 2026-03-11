---
layout: training-module
title: "Motor Efficiency, Power Factor, and Losses"
description: "This module explains three motor concepts that are often mentioned together but should not be confused: efficiency, power factor, and loss mechanisms."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Motors, Drives, and Motion"
    url: "/training/electrical-machines/"
repo_path: "control-standards/rag/training_modules/electrical_machines/motor_efficiency_power_factor_and_losses.md"
---

## Purpose

This module explains three motor concepts that are often mentioned together but should not be confused:

- efficiency
- power factor
- loss mechanisms

## Efficiency

Efficiency measures how much electrical input becomes useful mechanical output.

Relationship:

`eta = P_out / P_in`

Low efficiency means more input power is being lost as heat or other internal losses.

## Power factor

Power factor is the ratio of real power to apparent power.

`PF = P / S`

In practical terms:

- lower power factor means higher current is needed for the same real power
- higher current increases conductor and system burden

Induction motors commonly operate below unity power factor.

## Main motor loss types

Common loss categories:

- stator copper loss
- rotor copper loss
- core loss
- mechanical loss
- stray losses

### Stator copper loss

Caused by current flowing in stator windings.

### Rotor copper loss

Important in induction motors because rotor current exists due to slip.

### Core loss

Magnetic loss in the steel, often associated with hysteresis and eddy-current effects.

### Mechanical loss

Includes bearing friction, windage, and other rotational mechanical losses.

### Stray losses

Smaller losses not always grouped neatly into the main buckets.

## Why engineers should care

These concepts affect:

- heating
- current demand
- enclosure temperature
- operating cost
- motor selection quality

## Practical mistakes

### Confusing efficiency and power factor

They are not the same:

- efficiency compares output power to input power
- power factor compares real power to apparent power

### Ignoring losses when current seems acceptable

A motor can overheat because of cooling or mechanical issues even when measured current is not obviously excessive.

## Practical takeaway

If a motor is running hot, do not stop at current alone. Review:

- actual load
- cooling path
- ambient temperature
- friction or bearing problems
- electrical loss and operating condition

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/training/electrical-machines/motor-control-methods/' | relative_url }}">&larr; Motor Control Methods and Operating Regions</a>
  <a href="{{ '/training/electrical-machines/' | relative_url }}">↑ Motors, Drives, and Motion</a>
  <a href="{{ '/training/electrical-machines/motor-vfd-equations/' | relative_url }}">Motor and VFD Equations Reference &rarr;</a>
</div>
