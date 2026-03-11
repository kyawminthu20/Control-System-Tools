---
layout: training-module
title: "Series, Parallel, and Divider Methods"
description: "This module covers the first simplification patterns most engineers and technicians should recognize before moving to more formal analysis methods."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Electrical Fundamentals"
    url: "/training/fundamentals/"
repo_path: "control-standards/rag/training_modules/fundamentals/series_parallel_and_divider_methods.md"
---

## Purpose

This module covers the first simplification patterns most engineers and technicians should recognize before moving to more formal analysis methods.

## Series resistance

Resistors are in series when the same current must pass through each one in a single path.

Equivalent resistance:

- `R_eq = R1 + R2 + R3 + ...`

Main idea:

- current is the same through all series elements
- voltage is shared across them

## Parallel resistance

Resistors are in parallel when they share the same two connection nodes.

Equivalent resistance:

- `1 / R_eq = 1 / R1 + 1 / R2 + 1 / R3 + ...`

For two resistors:

- `R_eq = (R1 × R2) / (R1 + R2)`

Main idea:

- voltage is the same across all parallel branches
- current splits between branches based on resistance

## Voltage divider

A voltage divider uses series resistors to create a fraction of the source voltage.

For a two-resistor divider:

- `V_out = V_s × (R2 / (R1 + R2))`

Important caution: this result is only exact for the no-load case, or when the load is light enough not to disturb the divider materially.

## Current divider

A current divider is the parallel counterpart of the voltage divider.

For a two-branch case:

- `I_x = I_s × (R_other / (R_x + R_other))`

Main idea:

- lower resistance draws more current
- higher resistance draws less current

## Topology recognition

Before calculating anything, ask:

- do the elements truly share one current path?
- do they truly share the same two nodes?
- is there an attached load that changes the simple divider assumption?

Many circuits become easy once the topology is recognized correctly.

## Working takeaway

Start with the simplest pattern first:

1. series
2. parallel
3. divider

Only move to KCL, KVL, or equivalent-circuit methods when the topology cannot be reduced cleanly.

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/training/fundamentals/electrical-quantities/' | relative_url }}">&larr; Electrical Quantities and Circuit Language</a>
  <a href="{{ '/training/fundamentals/' | relative_url }}">↑ Electrical Fundamentals</a>
  <a href="{{ '/training/fundamentals/kirchhoff-laws/' | relative_url }}">Kirchhoff's Laws and Systematic Analysis &rarr;</a>
</div>
