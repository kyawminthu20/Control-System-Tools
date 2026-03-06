<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "11"
  chapter_title: "Control Equipment"

INDEX_TAGS:
  topics: ["control_panels", "enclosures", "control_equipment"]
-->


## 0. Scope

Chapter 11 specifically addresses the **physical location, mounting, and construction** of control equipment. This includes the internal arrangement of the control panel, the environmental protection provided by enclosures, and the physical accessibility of the components inside. Its goal is to prevent overheating, electrical interference, and physical damage to sensitive control hardware (like PLCs, VFDs, and relays).

## 1. Panel Construction Implications

The way a panel is built directly impacts its safety and longevity. Key requirements include:

* **Subpanel Rigidity:** All control equipment must be mounted on a rigid subpanel or frame that can withstand the vibrations of the machine.
* **Spacing and Heat Dissipation:** Components must be spaced to allow for adequate airflow. Manufacturers must account for the **heat rise** inside the cabinet to ensure components don't exceed their rated operating temperatures.
* **Separation of Voltages:** High-voltage power components (e.g., motor starters) should be grouped separately from low-voltage sensitive electronics (e.g., I/O modules) to prevent electromagnetic interference (EMI).
* **Terminal Strip Organization:** All internal wiring must terminate at terminal blocks rather than being "spliced" in mid-air. Terminals must be clearly numbered to match the electrical schematics.

## 2. UL 508A Overlap

For many engineers, the line between **NFPA 79** and **UL 508A** (the Standard for Industrial Control Panels) is blurry. Here is how they interact:

* **Complementary Standards:** While NFPA 79 governs the *entire machine system*, UL 508A is specifically for the *construction of the panel*. If a panel is "UL 508A Listed," it generally meets or exceeds the requirements of NFPA 79 Chapter 11.
* **Component Recognition:** UL 508A requires the use of UL-listed or recognized components. NFPA 79 references these requirements to ensure that the panel won't become a fire hazard.
* **The "Field Evaluation" Gap:** If a machine is built without a UL 508A shop certification, an inspector will use NFPA 79 Chapter 11 as the primary checklist to determine if the panel is safe for the facility.

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Updated with specific references to heat dissipation and UL 508A alignment.

