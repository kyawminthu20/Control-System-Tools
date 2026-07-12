<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "17"
  chapter_title: "Cables and Flexible Cords"

INDEX_TAGS:
  topics: ["flexible_cables", "drag_chain", "robot_cabling"]
-->


## 0. Scope

The scope of Chapter 17 includes the selection and application of **flexible cords and cables** used for the external connection of machine parts. It addresses how these conductors must handle mechanical environmental factors—such as tension, sharp bends, and continuous flexing—while maintaining electrical insulation and grounding continuity.

## 1. Dynamic Motion Applications

In industrial machinery, cables are often required to move repeatedly. NFPA 79 distinguishes between "flexible" use and "continuous flex" use:

* **Continuous Flex (Drag Chains):** Cables used in power tracks or cable carriers must be specifically rated for that purpose. Standard THHN wire will fail quickly under these conditions. These cables must have fine-stranded conductors and specialized jackets (like PUR or TPE) to prevent "corkscrewing" or internal wire breakage.
* **Bend Radius:** The standard mandates that the inner bend radius of a flexible cable must not be less than a specific multiple of the cable's diameter (typically  to  depending on the cable type). Exceeding this limit leads to insulation fatigue.
* **Torsional Stress:** For robotic applications where the cable twists (6-axis movement), cables must be rated for "Torsion" to ensure the shielding and conductors can rotate without binding.

## 2. Strain Relief and Protection

A cable is only as safe as its connection points. Chapter 17 outlines how to prevent physical damage at the entry and exit points:

* **Strain Relief:** Every flexible cord or cable must be equipped with a strain-relief fitting (cord grip). The goal is to ensure that a pull on the cable is absorbed by the fitting and not transmitted to the electrical terminals inside the box.
* **Protection from Sharp Edges:** Cables passing through holes in the machine frame must be protected by bushings or grommets.
* **Liquid-Tight Integrity:** If the machine uses coolants or is subject to wash-downs, the cable entry must be liquid-tight (IP67 or NEMA 4/12) to prevent fluids from "wicking" into the electrical enclosure.
* **Support:** Cables must be supported (via trays, conduits, or hangers) to prevent them from becoming a trip hazard or being crushed by passing forklifts.

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Updated to include specific requirements for continuous-flex (drag chain) rating and torsion limits for robotic applications.
