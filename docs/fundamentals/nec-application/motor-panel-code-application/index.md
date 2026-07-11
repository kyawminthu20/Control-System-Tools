---
layout: training-module
title: "Motor and Panel Code Application"
description: "A routing guide for common industrial-control NEC questions spanning Article 430, 409, 725, and 250."
breadcrumb:
  - name: "Training"
    url: "/fundamentals/"
  - name: "NEC for Machines and Panels"
    url: "/fundamentals/nec-application/"
repo_path: "control-standards/rag/training_modules/nec_application/motor_and_panel_code_application.md"
related_standards:
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
redirect_from:
  - /training/nec-application/motor-panel-code-application/
---

## Purpose

This module gives a quick routing guide for common industrial-control questions that span more than one NEC article.

## Article routing map

Most industrial questions do not live in one article only. The usual pattern is to find the primary article for the equipment type, then check linked articles for grounding, conductors, and overcurrent protection.

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
  Q[Industrial NEC Question] --> M{Motor-specific?}
  M -- Yes --> A430[Article 430\nMotors and Controllers]
  M -- No --> P{Panel assembly?}
  P -- Yes --> A409[Article 409\nIndustrial Control Panels]
  P -- No --> C{Control wiring?}
  C -- Yes --> A725[Article 725\nClass 1/2/3 Circuits]
  C -- No --> G{Grounding?}
  G -- Yes --> A250[Article 250\nGrounding and Bonding]
  G -- No --> CD{Conductors?}
  CD -- Yes --> A240[Articles 240 + 310\nProtection and Ampacity]
</pre>
</div>

## Use Article 430 for motor-specific questions

Typical triggers:

- Motor branch-circuit conductor sizing
- Overload protection selection and setting
- Short-circuit and ground-fault protection
- VFD supply conductors and disconnecting means

Article 430 contains its own internal structure for each protection function. Read the applicable part (Part II for conductors, Part III for overload, Part IV for branch-circuit protection) rather than searching the full article.

## Use Article 409 for panel-as-assembly questions

Typical triggers:

- Industrial control panel marking requirements
- Short-circuit current rating (SCCR) marking
- Panel identification and assembly labeling

Article 409 treats the panel as a complete assembly. The SCCR must be marked on the panel enclosure and must equal or exceed the available fault current at the installation point.

## Use Article 725 for remote or limited-energy control wiring

Typical triggers:

- Class 1, 2, or 3 circuit classification
- Control-circuit conductor separation from power conductors
- Low-energy remote-control wiring routing

Class 2 and Class 3 circuits have relaxed wiring methods permitted because they limit energy. Class 1 circuits follow power-circuit wiring rules.

## Use Article 250 for grounding and bonding questions

Typical triggers:

- Equipment grounding conductor (EGC) sizing
- Bonding jumper requirements
- Effective fault-current path continuity

Table 250.122 sizes the EGC based on the rating of the upstream overcurrent device, not the load current. That is a frequent source of errors.

## Use Articles 240 and 310 together for conductor protection

Typical triggers:

- Conductor ampacity selection
- Overcurrent device coordination
- Ambient and bundling correction factors
- Small-conductor protection (240.4(D))

Article 310 provides ampacity values. Article 240 provides the overcurrent device sizing rules. Both are needed to confirm a conductor-protection design is complete.

## Practical takeaway

Most industrial questions require navigating two or three articles.

The discipline is:

1. Identify the primary equipment type to find the anchor article
2. Check Article 250 for any grounding question that appears
3. Check Articles 240 and 310 together for any conductor-sizing question
4. Check Article 725 whenever control wiring separation or classification appears

## Related standards

- NFPA 79 2024, Chapter 11 — Control Equipment
- NFPA 79 2024, Chapter 12 — Motors and Associated Equipment
- UL 508A — Industrial Control Panels

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/nec-application/working-space-table-navigation/' | relative_url }}">&larr; Working Space and Table Navigation</a>
  <a href="{{ '/fundamentals/nec-application/' | relative_url }}">↑ NEC for Machines and Panels</a>
  <a href="{{ '/fundamentals/nec-application/branch-circuits-vs-feeders/' | relative_url }}">Branch Circuits vs. Feeders &rarr;</a>
</div>
