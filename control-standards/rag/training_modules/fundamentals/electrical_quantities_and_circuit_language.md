<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: FUNDAMENTALS
MODULE_ID: electrical_quantities_and_circuit_language
LEARNING_LEVEL: foundational

INDEX_TAGS:
  topics: ["voltage", "current", "resistance", "power", "nodes", "branches", "loops"]
  systems: ["electrical_circuits", "control_panels", "machines"]
-->

# Electrical Quantities and Circuit Language

## 0. Purpose

This module establishes the core vocabulary used in electrical analysis and practical control-panel reasoning.

## 1. Voltage, current, and resistance

- **Voltage** is the electrical potential difference that pushes charge through a circuit.
- **Current** is the rate of charge flow through a path.
- **Resistance** is the property that opposes current flow.

These three are tied together by Ohm's law:

- `V = I x R`

## 2. Power

Power describes the rate at which electrical energy is used or converted.

The most common relationship is:

- `P = V x I`

In real work, power checks matter because heat, not just current, often determines whether a component survives.

## 3. Circuit topology language

- **Node**: a connection point shared by two or more elements
- **Branch**: a single element or defined path between two nodes
- **Loop**: a closed path that returns to its starting point

These terms are the basis for KCL, KVL, nodal analysis, and loop analysis.

## 4. Sources and passive elements

Common idealized circuit elements are:

- voltage sources
- current sources
- resistors
- capacitors
- inductors

Most introductory practical analysis starts with ideal sources and resistors because they are the easiest path to understanding topology and current flow.

## 5. Why this matters in practice

This language is not just textbook vocabulary.

It helps with:

- reading schematics
- explaining troubleshooting steps clearly
- checking whether a circuit is series, parallel, or mixed
- deciding whether a quick Ohm's law estimate is reasonable

## 6. Working takeaway

Before solving a circuit, identify:

1. what quantities are known
2. what quantity is unknown
3. the circuit's basic topology

That step prevents many avoidable calculation mistakes.
