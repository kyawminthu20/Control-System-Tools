---
layout: default
title: "Electrical Equations Reference"
description: "A compact reference card for the most-used relationships from the fundamentals training set."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Fundamentals"
    url: "/training/fundamentals/"
repo_path: "control-standards/rag/training_modules/fundamentals/electrical_equations_reference.md"
---

<div class="page-header">
  <span class="page-header__label">Training — Fundamentals</span>
  <h1>Electrical Equations Reference</h1>
</div>

## Purpose

This page is a compact reference card for the most-used relationships from the fundamentals training set.

## Ohm's law

- `V = I × R`
- `I = V / R`
- `R = V / I`

## Power

- `P = V × I`
- `P = I² × R`
- `P = V² / R`

## Series resistance

- `R_eq = R1 + R2 + R3 + ...`

## Parallel resistance

- `1 / R_eq = 1 / R1 + 1 / R2 + 1 / R3 + ...`

For two resistors:

- `R_eq = (R1 × R2) / (R1 + R2)`

## Voltage divider

- `V_out = V_s × (R_x / R_total)`

## Current divider

- `I_x = I_s × (R_other / (R_x + R_other))`

## Kirchhoff's laws

- Sum of currents at a node = 0
- Sum of voltages around a closed loop = 0

## Branch current in nodal form

- `I = (V_a - V_b) / R`

## Source transformation

- `V_s = I_s × R`
- `I_s = V_s / R`

## Thevenin and Norton relationship

- `V_th = I_n × R_th`
- `I_n = V_th / R_th`

## Capacitor energy

- `E = ½ × C × V²`

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/training/fundamentals/equivalent-circuit-methods/' | relative_url }}">&larr; Equivalent Circuit Methods</a>
  <a href="{{ '/training/fundamentals/' | relative_url }}">↑ Fundamentals</a>
  <a href="{{ '/training/fundamentals/passive-components/' | relative_url }}">Passive Components &rarr;</a>
</div>
