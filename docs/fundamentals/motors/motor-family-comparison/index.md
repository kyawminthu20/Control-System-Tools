---
layout: training-module
title: "Motor Family Comparison"
description: "This module introduces the major motor families used in industrial automation so the reader can distinguish the motor type before choosing a drive, control method, or protection strategy."
breadcrumb:
  - name: "Training"
    url: "/fundamentals/"
  - name: "Motors, Drives, and Motion"
    url: "/fundamentals/motors/"
repo_path: "control-standards/rag/training_modules/electrical_machines/motor_family_comparison.md"
redirect_from:
  - /fundamentals/electrical-machines/motor-family-comparison/
  - /fundamentals/electrical-machines/motor-family-comparison/index.html

review:
  standard: "Motor and drive engineering practice — vendor documentation governs application"
  edition: "n/a — practice module"
  status: "Review pending"
  coverage: "Training module: Motor Family Comparison — educational treatment; sizing and application decisions follow vendor data and the governing standards."
  last_reviewed: "July 2026"
---

## Purpose

This module introduces the major motor families used in industrial automation and adjacent motion systems so the reader can distinguish the motor type before choosing a drive, control method, or protection strategy.

## High-level motor family map

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
    A[Electric Motors] --> B[AC Motors]
    A --> C[DC Motors]
    A --> D[Electronically Commutated Motors]

    B --> B1[Induction Motor]
    B --> B2[Synchronous Motor]
    B --> B3[Single-Phase AC Motor]

    C --> C1[Brushed DC Motor]
    C --> C2[Series DC Motor]
    C --> C3[Shunt DC Motor]

    D --> D1[BLDC Motor]
    D --> D2[PMSM Servo Motor]
    D --> D3[Stepper Motor]
</pre>
</div>

## Core motor families

### AC motors

AC motors dominate industrial power applications.

Common examples:

- induction motors
- synchronous motors
- single-phase utility motors

Common uses:

- pumps
- fans
- conveyors
- compressors
- process equipment

### DC motors

Classical DC motors use brushes and a commutator.

Common examples:

- brushed DC motors
- series DC motors
- shunt DC motors

These motors still matter in legacy systems, but many modern adjustable-speed systems use electronically commutated platforms instead.

### Electronically commutated motors

These motors need an electronic controller to generate phase switching.

Common examples:

- BLDC motors
- PMSM servo motors
- stepper motors

These are common in:

- robotics
- CNC systems
- battery-powered systems
- high-performance automation

## Comparison table

| Motor family | Supply form | Typical commutation method | Main strength | Main limitation | Common use |
| --- | --- | --- | --- | --- | --- |
| AC induction | AC | electromagnetic induction | rugged, common, economical | less precise without advanced control | pumps, fans, conveyors |
| Synchronous AC | AC | synchronous magnetic field | efficient and controlled speed relation | more specialized control | precision drives, power systems |
| Brushed DC | DC | brushes and commutator | simple speed-control concept | brush wear and maintenance | legacy motion systems |
| BLDC | DC bus plus inverter | electronic commutation | compact, efficient, high power density | controller dependent | portable and compact systems |
| PMSM servo | DC bus plus servo drive | electronic commutation plus feedback | precise control, fast response | higher cost and tuning complexity | robotics, CNC, packaging |
| Stepper | DC bus plus driver | step sequence | simple position control | can lose steps, weaker at speed | light-duty positioning |

## Engineering implications

Motor family changes the rest of the system design, including:

- drive architecture
- control strategy
- cable and grounding method
- commissioning workflow
- troubleshooting approach

Examples:

- induction motor plus VFD fits industrial variable-speed process loads
- PMSM servo fits precise positioning and dynamic motion
- BLDC often fits compact battery-powered systems

## Common mistakes

### Treating all electronic motors as servo motors

Not every electronically commutated motor is a servo system. A servo system usually implies closed-loop feedback and tuned position, velocity, or torque control.

### Treating BLDC and PMSM as completely unrelated

These families are closely related in hardware terms. Engineers often distinguish them by back-EMF shape, control method, and application context.

### Treating EV or drone motors like ordinary industrial motors

Their thermal assumptions, packaging goals, and duty expectations are often very different from industrial continuous-duty systems.

## Selection guidance

- choose `induction motor + VFD` for industrial variable-speed process loads
- choose `PMSM servo` for precise positioning and dynamic motion
- choose `BLDC` for lightweight or compact battery-powered systems
- choose `stepper` for lower-cost discrete positioning when performance limits are acceptable
- choose `brushed DC` mainly for legacy or specialized simple DC applications

## See also

- [BLDC vs PMSM Comparison]({{ '/fundamentals/motors/bldc-vs-pmsm/' | relative_url }}) — head-to-head engineering comparison with 10 application scenarios
- [BLDC Motor Reference]({{ '/fundamentals/motors/bldc-reference/' | relative_url }}) — deep BLDC reference
- [PMSM Motor Reference]({{ '/fundamentals/motors/pmsm-reference/' | relative_url }}) — deep PMSM reference
- [BLDC and PMSM Implementation Guide]({{ '/fundamentals/motors/bldc-pmsm-implementation/' | relative_url }}) — production-grade implementation reference
- [Motor Selection Scenarios]({{ '/fundamentals/motors/motor-selection-scenarios/' | relative_url }}) — three engineering-grade archetypes with tuning and measurement detail

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/motors/motor-nameplates-slip-torque/' | relative_url }}">&larr; Motor Nameplates, Slip, and Torque</a>
  <a href="{{ '/fundamentals/motors/' | relative_url }}">↑ Motors, Drives, and Motion</a>
  <a href="{{ '/fundamentals/motors/ac-vs-dc-motors/' | relative_url }}">AC vs DC Motors &rarr;</a>
</div>
