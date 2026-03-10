<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: FUNDAMENTALS
MODULE_ID: kirchhoff_laws_and_systematic_analysis
LEARNING_LEVEL: intermediate

INDEX_TAGS:
  topics: ["kcl", "kvl", "nodal_analysis", "loop_analysis", "sign_convention"]
  systems: ["electrical_circuits", "control_circuits"]
-->

# Kirchhoff Laws and Systematic Analysis

## 0. Purpose

This module explains the two bookkeeping laws that make complex circuit solving systematic rather than guess-based.

## 1. Kirchhoff's Current Law

KCL states that the algebraic sum of currents at a node is zero.

Practical meaning:

- whatever current enters a node must leave it

This is the basis for nodal analysis.

## 2. Kirchhoff's Voltage Law

KVL states that the algebraic sum of voltage rises and drops around a closed loop is zero.

Practical meaning:

- total gain and total drop around a loop must balance

This is the basis for loop or mesh analysis.

## 3. Nodal analysis

Typical workflow:

1. choose a reference node
2. assign voltages to the remaining nodes
3. write KCL at each unknown node
4. express branch current as voltage difference divided by resistance
5. solve the resulting equations

Nodal analysis is often the better choice when the circuit has several connected nodes and current balance is easy to express.

## 4. Loop analysis

Typical workflow:

1. assign a loop current to each independent loop
2. write a KVL equation for each loop
3. account for shared elements using current difference
4. solve the resulting equations

Loop analysis is often easier when the circuit has a small number of clean, obvious loops.

## 5. Sign-convention discipline

Negative answers do not necessarily mean the setup failed.

They usually mean:

- the real current direction is opposite the assumed direction
- or the real polarity is opposite the assumed polarity

Consistency matters more than the first guess.

## 6. Working takeaway

Use systematic analysis when a circuit is no longer reducible by simple series/parallel recognition.

The method is less important than using one method consistently and carefully.
