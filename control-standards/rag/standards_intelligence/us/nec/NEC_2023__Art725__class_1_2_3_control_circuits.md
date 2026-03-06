<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "725"
  article_title: "Class 1, Class 2, and Class 3 Remote-Control Circuits"

INDEX_TAGS:
  topics: ["control_circuits", "class_2", "power_limited"]
-->


# NEC 2023 — Article 725 — Class 1, Class 2, and Class 3 Circuits

## 0. Scope for control panels

Article 725 covers remote-control, signaling, and power-limited circuits that are not an integral part of a device or appliance. In industrial control panels, this article is the primary authority for wiring **PLCs, 24VDC sensors, and pilot devices**. The goal is to differentiate between high-energy circuits (Class 1) and low-energy circuits (Class 2) that pose a lower risk of fire and shock.

## 1. Power-limited circuit rules (Class 2)

* **Class 2 Definition:** A circuit that has its power limited by a listed power supply (typically a Class 2 transformer or DC power supply). The voltage is generally **30V or less** with a power limit of **100VA**.
* **Safety Advantage:** Because Class 2 circuits are power-limited, they have relaxed requirements for wire insulation and mechanical protection compared to power circuits.
* **Class 1 Definition:** These are not power-limited. They can operate up to 600V and are treated essentially the same as power circuits regarding wiring methods.

## 2. Separation from power circuits (725.136)

The most critical rule for panel designers is the physical separation of Class 2/3 circuits from power and Class 1 circuits.

* **General Rule:** Class 2 and Class 3 circuit conductors **shall not** be placed in any enclosure, raceway, or cable with conductors of electric light, power, or Class 1 circuits.
* **Exceptions for Panels:** 1.  **Barrier:** Separation is permitted if a permanent, grounded barrier (like a metal partition or a separate wire duct) is installed.
2.  **600V Insulation:** If all conductors have insulation rated for at least 600V (the highest voltage in the enclosure), they can be mixed *only* where they are connected to the same equipment (e.g., at a motor starter with a 480V coil and 24V auxiliary contact).
* **Common Practice:** Use distinct colors (e.g., **Blue** for DC, **Red** for AC) and separate wire ducts for Class 2 and Power circuits.

## 3. Field wiring implications

* **Cable Types:** Class 2 circuits can often use specialized cables (like CL2, CL3, or PLTC) that are smaller and more flexible than standard THHN power wire.
* **Wet Locations:** If sensors are located in wet areas, the Class 2 cabling must be rated for wet environments (e.g., PLTC-ER).
* **Grounding:** While the DC common of a Class 2 supply is often grounded to the panel's backplane, it must be done in a way that does not introduce "noise" into the PLC system (referencing **Article 250**).

## 4. Change log

* 2026-01-15 — Initial draft created; emphasized Class 2 separation rules (725.136).

