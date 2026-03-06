<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_60204_1
EDITION: 2018

IEC_HIERARCHY:
  clause: "2"
  clause_title: "Normative References"

INDEX_TAGS:
  topics: ["references", "dependencies"]
-->

Clause 2 of **IEC 60204-1** is foundational because it establishes the legal and technical "links" to other standards. In the IEC framework, a normative reference is indispensable for the application of the document; if you don't comply with the referenced standard, you aren't fully compliant with IEC 60204-1.

---

## 0. Purpose

The purpose of Clause 2 is to list the external documents that contain provisions which, through reference in this text, constitute provisions of IEC 60204-1. This ensures that:

* **The "Wheel" isn't reinvented:** Instead of defining grounding in every standard, it points to the definitive grounding standard.
* **Global Consistency:** It ensures that machine safety (60204) aligns with general electrical safety (60364) and functional safety (13849).
* **Technical Rigor:** It forces manufacturers to use components and methods that meet secondary testing standards for reliability and fire safety.

## 1. Required Companion Standards

Compliance with IEC 60204-1 typically requires the machine builder to reference several key "B-Type" and "C-Type" standards:

* **IEC 60364-4-41 (Protection against electric shock):** This is the "parent" standard for shock protection and provides the math for disconnection times.
* **IEC 60529 (Degrees of protection provided by enclosures):** This defines the **IP (Ingress Protection)** ratings for the machine's control panels (e.g., IP54 or IP67).
* **ISO 13849-1 (Safety of machinery — Safety-related parts of control systems):** Used to determine the Performance Level (PL) of safety functions like light curtains or E-stops.
* **IEC 60947 series:** The standards for low-voltage switchgear (the actual breakers, contactors, and buttons inside the panel).

## 2. Control-Engineering Impact

Normative references directly dictate the hardware and software choices a control engineer makes:

* **Component Selection:** You cannot simply use any relay; Clause 2 implies that the relay must be manufactured and tested to **IEC 60947-5-1**.
* **Environmental Ratings:** Because of the reference to **IEC 60529**, an engineer must select an enclosure that matches the factory environment (e.g., ensuring protection against dust or water jets).
* **Safety Logic:** The reference to **ISO 13849** means that the control logic must be validated. It isn't enough to just wire a "Stop" button; the engineer must prove that the circuit remains safe even if a single component fails.

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Updated with specific impacts of ISO 13849 and IEC 60529 on control system design.

