<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "300"
  article_title: "General Wiring Methods"

INDEX_TAGS:
  topics: ["wiring_methods", "routing", "mechanical_protection"]
-->


# NEC 2023 — Article 300 — General Wiring Methods

## 0. Scope inside control panels

Article 300 covers the general requirements for all wiring methods. For industrial control panels, it dictates how wires are protected from abrasion, how they are grouped to prevent inductive heating, and how they must be secured when transitioning from the panel to the machine.

## 1. Routing and protection rules

* **300.3(B) Conductors of the Same Circuit:** All conductors of the same circuit (including the grounded conductor and all equipment grounding conductors) must be contained within the same raceway, cable tray, or trench.
* *Reason:* This minimizes inductive heating in metallic enclosures/conduits caused by electromagnetic fields.


* **300.4 Protection Against Physical Damage:** Conductors must be protected where they are subject to physical damage.
* **Bushings (300.4(G)):** Where ungrounded conductors 4 AWG or larger enter an enclosure, they must be protected by a substantial fitting providing a smoothly rounded insulating surface (e.g., an insulating bushing).


* **300.14 Length of Free Conductors:** At least **6 inches** (150 mm) of free conductor must be left at each outlet, junction, or switch point for terminations or splicing.

## 2. Separation of circuits

* **300.3(C) Conductors of Different Systems:** * Conductors of rated voltages **600V or less** are permitted to occupy the same enclosure or wireway, provided all conductors have an insulation rating equal to at least the maximum circuit voltage applied to any conductor within the enclosure.
* *Exception:* This does not override specific requirements in **Article 725** for Class 2 or Class 3 circuits, which often require physical separation from power circuits to prevent interference or high-voltage migration.



## 3. Common panel violations

1. **Inductive Heating (300.20):** Running individual phase conductors through separate "knockouts" or holes in a steel enclosure. This creates a "transformer effect" that heats the metal. All phases must pass through a single opening.
2. **Abrasion at Enclosure Entry:** Failing to use proper connectors or grommets where wires pass through sheet metal, leading to insulation failure over time due to vibration.
3. **Missing Firestopping (300.21):** Forgetting to seal openings in panels that penetrate fire-rated walls or floors.
4. **Improper Support:** Using wire duct (Panduit) as the *sole* means of support for heavy cables without additional mechanical strapping near the termination points.

## 4. Change log

* 2026-01-15 — Initial draft created; added requirements for conductor grouping and inductive heating prevention.
