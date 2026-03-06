<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "409"
  article_title: "Industrial Control Panels"

INDEX_TAGS:
  topics: ["industrial_control_panel", "sccr", "labeling"]
  systems: ["control_panel"]
-->



# NEC 2023 — Article 409 — Industrial Control Panels

## 0. Why this article matters

Article 409 provides the specific safety requirements for industrial control panels (ICPs) operating at 1000 volts or less. While other articles (like 250 or 310) provide general rules, Article 409 is the primary authority that inspectors use to verify if a panel is safe to be energized. It ensures that the panel can safely withstand a short-circuit event and is properly marked for the technicians who will maintain it.

## 1. Panel definition and scope

* **Definition (409.2):** An assembly of two or more components from the following list:
1. **Power circuit components** (e.g., motor controllers, overload relays, fused disconnect switches, circuit breakers).
2. **Control circuit components** (e.g., pushbuttons, selector switches, control relays, PLCs, timers).


* **Scope:** Includes the enclosure and all associated wiring and terminals. It does *not* include the controlled equipment (e.g., the actual motor or the machine frame).

## 2. Short-circuit current rating (SCCR)

* **Mandatory Marking (409.110(4)):** Every ICP must be marked with its SCCR.
* **Determination (409.60):** The SCCR must be determined by one of the following:
1. **Tested Combination:** Testing the entire assembly in a lab.
2. **Approved Method:** Using the "weakest link" method described in **UL 508A, Supplement SB**.


* **Compliance:** The panel's SCCR **must** be equal to or greater than the available fault current (AFC) at the installation site. If the panel is rated for 5kA but the building can deliver 22kA, the installation is a violation and a major fire/explosion risk.

## 3. Labeling requirements

The nameplate must be permanent and include (409.110):

* **Manufacturer’s name** or trademark.
* **Supply voltage**, number of phases, frequency, and full-load current.
* **Short-Circuit Current Rating (SCCR).**
* **Enclosure Type Number** (e.g., Type 1, 4, 12).
* **Grounding:** Identification of the grounding terminal.

## 4. Relationship to UL 508A

The NEC and UL 508A are two sides of the same coin:

* **NEC Article 409:** The law (in most jurisdictions) governing the **installation** and minimum safety features.
* **UL 508A:** The technical **construction standard**.
* **Listing:** A panel "Listed" to UL 508A is automatically deemed to meet the requirements of Article 409. Most inspectors will look for a UL 508A sticker; without it, they may require a "Field Evaluation" which is significantly more expensive.

## 5. Inspector expectations

When an AHJ (Authority Having Jurisdiction) walks up to a panel, they typically follow this mental checklist:

1. **Is it listed?** (Check for UL, Intertek, or CSA labels).
2. **Does the SCCR match the facility?** (Checking the nameplate vs. the building's fault current study).
3. **Are the conductors sized correctly?** (Checking internal wiring against Article 310).
4. **Is the grounding correct?** (Looking for the door bonding jumper and the main EGC).

## 6. Change log

* 2026-01-15 — Initial draft created; established link between SCCR and UL 508A Supplement SB.

