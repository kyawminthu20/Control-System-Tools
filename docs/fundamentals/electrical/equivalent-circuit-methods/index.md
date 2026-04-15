---
layout: training-module
title: "Equivalent Circuit Methods"
description: "This module explains how to replace a complicated section of a circuit with a simpler equivalent form that behaves the same way at the terminals of interest."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Electrical Fundamentals"
    url: "/fundamentals/electrical/"
repo_path: "control-standards/rag/training_modules/fundamentals/equivalent_circuit_methods.md"
redirect_from:
  - /training/fundamentals/equivalent-circuit-methods/
  - /training/fundamentals/equivalent-circuit-methods/index.html

---

## Purpose

This module explains how to replace a complicated section of a circuit with a simpler equivalent form that behaves the same way at the terminals of interest.

## Source transformation

Two common source forms can be equivalent:

- a voltage source in series with a resistor
- a current source in parallel with a resistor

Core relationships:

- `V_s = I_s × R`
- `I_s = V_s / R`

The resistor value stays the same during the conversion.

## Thevenin equivalent

Thevenin form replaces a network with one equivalent voltage source and one equivalent series resistance.

Typical steps:

1. remove the load
2. find the open-circuit terminal voltage (`V_th`)
3. deactivate independent sources and find the terminal resistance (`R_th`)
4. reconnect the load to the simplified model

## Norton equivalent

Norton form replaces a network with one equivalent current source and one equivalent parallel resistance.

Thevenin and Norton are directly related:

- `I_n = V_th / R_th`
- `V_th = I_n × R_th`

## Superposition

Superposition solves a linear circuit by considering one independent source at a time.

General procedure:

1. keep one independent source active
2. deactivate the others (replace voltage sources with short circuits, current sources with open circuits)
3. solve the partial response
4. repeat for each source
5. sum all partial results

This method applies only to linear circuits.

## Practical use

Equivalent methods are useful when:

- the load is connected to a complicated upstream network
- the same network must be checked for multiple loads
- a source form is awkward for the surrounding analysis

## Working takeaway

These methods do not change the terminal behavior you care about. They change the form of the problem so it becomes easier to solve.

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/electrical/kirchhoff-laws/' | relative_url }}">&larr; Kirchhoff's Laws and Systematic Analysis</a>
  <a href="{{ '/fundamentals/electrical/' | relative_url }}">↑ Electrical Fundamentals</a>
  <a href="{{ '/fundamentals/electrical/electrical-equations-reference/' | relative_url }}">Electrical Equations Reference &rarr;</a>
</div>
