<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: FUNDAMENTALS
MODULE_ID: series_parallel_and_divider_methods
LEARNING_LEVEL: foundational

INDEX_TAGS:
  topics: ["series_circuits", "parallel_circuits", "voltage_divider", "current_divider"]
  systems: ["electrical_circuits", "control_interfaces"]
-->

# Series, Parallel, and Divider Methods

## 0. Purpose

This module covers the first simplification patterns most engineers and technicians should recognize before moving to more formal analysis methods.

## 1. Series resistance

Resistors are in series when the same current must pass through each one in a single path.

Equivalent resistance:

- `R_eq = R1 + R2 + R3 + ...`

Main idea:

- current is the same through all series elements
- voltage is shared across them

## 2. Parallel resistance

Resistors are in parallel when they share the same two connection nodes.

Equivalent resistance:

- `1 / R_eq = 1 / R1 + 1 / R2 + 1 / R3 + ...`

For two resistors:

- `R_eq = (R1 x R2) / (R1 + R2)`

Main idea:

- voltage is the same across all parallel branches
- current splits between branches based on resistance

## 3. Voltage divider

A voltage divider uses series resistors to create a fraction of the source voltage.

For a two-resistor divider:

- `V_out = V_s x (R2 / (R1 + R2))`

Important caution:

- this result is only exact for the no-load case or when the load is light enough not to disturb the divider materially

## 4. Current divider

A current divider is the parallel counterpart of the voltage divider.

For a two-branch case:

- `I_x = I_s x (R_other / (R_x + R_other))`

Main idea:

- lower resistance draws more current
- higher resistance draws less current

## 5. Topology recognition

Before calculating anything, ask:

- do the elements truly share one current path
- do they truly share the same two nodes
- is there an attached load that changes the simple divider assumption

Many circuits become easy once the topology is recognized correctly.

## 6. Working takeaway

Start with the simplest pattern first:

- series
- parallel
- divider

Only move to KCL, KVL, or equivalent-circuit methods when the topology cannot be reduced cleanly.
