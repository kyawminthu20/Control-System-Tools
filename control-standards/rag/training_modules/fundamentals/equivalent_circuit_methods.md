<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: FUNDAMENTALS
MODULE_ID: equivalent_circuit_methods
LEARNING_LEVEL: intermediate

INDEX_TAGS:
  topics: ["source_transformation", "thevenin", "norton", "superposition"]
  systems: ["electrical_circuits", "load_models"]
-->

# Equivalent Circuit Methods

## 0. Purpose

This module explains how to replace a complicated section of a circuit with a simpler equivalent form that behaves the same way at the terminals of interest.

## 1. Source transformation

Two common source forms can be equivalent:

- voltage source in series with a resistor
- current source in parallel with a resistor

Core relationships:

- `V_s = I_s x R`
- `I_s = V_s / R`

The resistor value stays the same during the conversion.

## 2. Thevenin equivalent

Thevenin form replaces a network with:

- one equivalent voltage source
- one equivalent series resistance

Typical steps:

1. remove the load
2. find the open-circuit terminal voltage `V_th`
3. deactivate independent sources and find the terminal resistance `R_th`
4. reconnect the load to the simplified model

## 3. Norton equivalent

Norton form replaces a network with:

- one equivalent current source
- one equivalent parallel resistance

Thevenin and Norton are directly related:

- `I_n = V_th / R_th`
- `V_th = I_n x R_th`

## 4. Superposition

Superposition solves a linear circuit by considering one independent source at a time.

General rule:

1. keep one independent source active
2. deactivate the others
3. solve the partial response
4. repeat for each source
5. sum the results

This method applies only to linear circuits.

## 5. Practical use

Equivalent methods are useful when:

- the load is connected to a complicated upstream network
- the same network must be checked for multiple loads
- a source form is awkward for the surrounding analysis

## 6. Working takeaway

These methods do not change the terminal behavior you care about.

They change the form of the problem so it becomes easier to solve.
