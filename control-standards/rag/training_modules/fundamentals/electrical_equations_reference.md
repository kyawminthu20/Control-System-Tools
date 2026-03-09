<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: FUNDAMENTALS
MODULE_ID: electrical_equations_reference
LEARNING_LEVEL: reference

INDEX_TAGS:
  topics: ["equations", "ohms_law", "power", "dividers", "kcl", "kvl", "thevenin", "norton"]
  systems: ["electrical_circuits"]
-->

# Electrical Equations Reference

## 0. Purpose

This note is a compact reference card for the most-used relationships from the fundamentals training set.

## 1. Ohm's law

- `V = I x R`
- `I = V / R`
- `R = V / I`

## 2. Power

- `P = V x I`
- `P = I^2 x R`
- `P = V^2 / R`

## 3. Series resistance

- `R_eq = R1 + R2 + R3 + ...`

## 4. Parallel resistance

- `1 / R_eq = 1 / R1 + 1 / R2 + 1 / R3 + ...`

For two resistors:

- `R_eq = (R1 x R2) / (R1 + R2)`

## 5. Voltage divider

- `V_out = V_s x (R_x / R_total)`

## 6. Current divider

- `I_x = I_s x (R_other / (R_x + R_other))`

## 7. Kirchhoff laws

- `sum of currents at a node = 0`
- `sum of voltages around a closed loop = 0`

## 8. Branch current in nodal form

- `I = (V_a - V_b) / R`

## 9. Source transformation

- `V_s = I_s x R`
- `I_s = V_s / R`

## 10. Thevenin and Norton relationship

- `V_th = I_n x R_th`
- `I_n = V_th / R_th`

## 11. Capacitor energy

- `E = 1/2 x C x V^2`
