---
layout: training-module
title: "Passive Components: Resistors and Capacitors"
description: "This module explains the basic practical behavior of two common passive components used throughout electrical and control work."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Electrical Fundamentals"
    url: "/fundamentals/electrical/"
repo_path: "control-standards/rag/training_modules/fundamentals/passive_components_resistors_capacitors.md"
redirect_from:
  - /training/fundamentals/passive-components/
  - /training/fundamentals/passive-components/index.html

---

## Purpose

This module explains the basic practical behavior of two common passive components used throughout electrical and control work.

## Resistors

Resistors are used to:

- limit current
- create intentional voltage drop
- bias signals
- form dividers and timing networks

Key practical checks:

- resistance value
- power rating
- tolerance
- heat generated in use

## Capacitors

Capacitors store charge between two conductors separated by an insulating dielectric.

Common uses:

- smoothing and filtering
- timing
- energy storage
- noise suppression

## Component families

Common resistor families:

- carbon or film types
- metal film
- wire-wound

Common capacitor families:

- ceramic
- film
- electrolytic

Different families trade size, stability, voltage capability, and failure mode differently.

## Practical cautions

- Electrolytic capacitors are polarity-sensitive.
- Capacitors can hold hazardous stored energy after power is removed.
- Resistors fail from heat as often as from wrong resistance value.
- Real components are not ideal; tolerance and temperature matter.

## Working takeaway

For both parts, value alone is not enough. Always check:

- the electrical job
- the physical part family
- the rating
- the failure consequence

## Related standards

- NFPA 79-2024, Chapter 7 — Protection against electric shock
- IEC 60204-1:2018, Clause 6 — Protection against electric shock

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/electrical/electrical-equations-reference/' | relative_url }}">&larr; Electrical Equations Reference</a>
  <a href="{{ '/fundamentals/electrical/' | relative_url }}">↑ Electrical Fundamentals</a>
  <a href="{{ '/fundamentals/electrical/diodes-transistors/' | relative_url }}">Diodes, Transistors, and Switching Basics &rarr;</a>
</div>
