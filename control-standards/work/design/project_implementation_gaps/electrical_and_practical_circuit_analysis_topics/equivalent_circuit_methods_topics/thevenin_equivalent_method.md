<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: TRANSCRIPT_SEGMENT_NORMALIZED
CATEGORY: EQUIVALENT_CIRCUIT_METHODS
-->

# Thevenin Equivalent Method

## What this file is

This is a cleaned work note derived from the Thevenin-theorem portion of [source_transformation_and_equivalent_methods.md](../source_transformation_and_equivalent_methods.md).

Approximate source range in the original lesson:

- `1:11:40` to `1:20:46`

## Topic focus

This segment explains how to replace a black-box resistive network with one equivalent voltage source and one equivalent series resistance.

## Main concepts captured

### 1. Thevenin is a terminal-view simplification

- The transcript treats the original circuit as a black box.
- The internal complexity matters less than the behavior seen at the output terminals.

### 2. Thevenin reduction has two main quantities

- `Rth`: the equivalent resistance seen looking into the output terminals
- `Vth`: the open-circuit voltage at those terminals

### 3. The transcript's resistance-finding procedure is explicit

- remove the load resistor
- set independent sources equal to zero
- short voltage sources
- open current sources
- find the equivalent resistance looking into the output terminals

### 4. The transcript's voltage-finding procedure keeps sources active

- remove the load resistor
- leave the actual sources active
- find the open-circuit voltage across the output terminals
- treat that open-circuit voltage as `Vth`

### 5. The reduced circuit makes load calculations easier

- Once `Vth` and `Rth` are known, reconnect the load to the equivalent source-and-series-resistor model.
- The transcript then uses a simple voltage-divider step to solve the final load voltage.

## Working takeaway

Thevenin is most useful when:

- the load sits at the edge of a more complex resistive network
- you want to know how different loads will behave without re-solving the whole circuit every time
- voltage across the load is the quantity of interest

## Important caution

This file is a transcript-derived work note. The procedure shown is for circuits built from ideal resistors and independent sources as presented in the lesson.
