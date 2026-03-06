<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "408"
  article_title: "Switchboards, Switchgear, and Panelboards"

INDEX_TAGS:
  topics: ["switchboards", "panelboards", "power_distribution"]
  systems: ["industrial_control_panel"]
-->


# NEC 2023 — Article 408 — Switchboards, Switchgear, and Panelboards

## 0. Scope and applicability to control panels

Article 408 covers the requirements for switchboards, switchgear, and panelboards. In industrial facilities, these are the primary distribution points that feed Industrial Control Panels (ICPs). Understanding Article 408 is essential for the "Upstream" design—ensuring the supply to the control panel is properly rated and that the ICP itself is not accidentally classified as a panelboard, which would trigger more restrictive busbar and space requirements.

## 1. When Article 408 vs Article 409 applies

The distinction is based on **intended use**:

* **Article 408 (Panelboards):** If the enclosure is primarily used to house overcurrent devices (breakers/fuses) that distribute power to lighting, appliance, or general-purpose branch circuits, it is a **Panelboard**.
* **Article 409 (Industrial Control Panels):** If the enclosure contains a systematic arrangement of control devices (relays, PLCs, motor starters) and their associated circuits, it is an **Industrial Control Panel**.
* **The "Hybrid" Rule:** Many control panels contain a small distribution section. If the control components are the "predominant" feature, Article 409 usually takes precedence for internal construction, but Article 408 rules apply to the main busbar and supply terminations.

## 2. Panel construction requirements

* **408.3 Support and Arrangement of Busbars:** Busbars must be rigidly mounted and physically protected. In a panelboard, the phase arrangement on 3-phase buses must be **A, B, C** from front to back, top to bottom, or left to right (as viewed from the front).
* **408.4 Field Identification:** Every circuit and circuit modification must be legibly identified as to its clear, evident, and specific purpose. Labels like "Miscellaneous" or "Lights" are insufficient; they must be specific (e.g., "Conveyor 1 Control Power").
* **408.18 Large Equipment:** Switchgear and switchboards require specific rear and side clearances (referencing **110.26**) to allow for safe maintenance of bus connections.
* **408.41 Grounded Conductor Terminations:** Each grounded conductor (neutral) must terminate within the panelboard in an individual terminal that is not also used for another conductor.

## 3. Change log

* 2026-01-15 — Initial draft created; defined boundary between Article 408 and 409.

