<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "16"
  chapter_title: "Wiring Methods"

INDEX_TAGS:
  topics: ["wiring", "routing", "segregation"]
-->

Chapter 16 of **NFPA 79** defines the physical "craftsmanship" of the electrical system. While earlier chapters discuss what the circuits do, this chapter dictates how the wires are actually routed, bundled, and protected to ensure they don't rub through, overheat, or interfere with one another.

---

## 0. Scope

This chapter covers the requirements for **internal and external wiring methods** for industrial machinery. It sets the standard for how conductors must be supported, the use of raceways and cable trays, and the physical protection of wiring from mechanical abuse, liquids, and heat. The goal is to ensure the "physical integrity" of the electrical system over the machine's life cycle.

## 1. Internal Machine Wiring

Inside the control panel and across the machine frame, wiring must follow strict organizational rules:

* **Support and Securing:** Conductors must be supported so they do not put mechanical strain on terminal connections. This is typically achieved through the use of plastic wiring duct (slotted duct) inside panels and conduit or cable trays on the machine.
* **Flexing Applications:** Wiring that crosses a hinge (like a cabinet door) or moves with a machine axis (like a robot arm) must use **extra-flexible stranding** and be anchored at both ends of the flex point to prevent fatigue failure.
* **Terminal Identification:** Every wire must be identified at each termination point with a label (wire marker) that matches the electrical schematics.
* **Clearance from Moving Parts:** Wiring must be routed to maintain a minimum clearance from moving mechanical parts to prevent pinching or abrasion.

## 2. Segregation Rules

One of the most critical aspects of Chapter 16 is the physical separation of different types of circuits to prevent safety hazards and signal noise.

* **Voltage Segregation:** Conductors of different voltages can occupy the same enclosure or raceway **only if** all conductors are insulated for the maximum voltage present in the group.
* **Signal Interference:** Low-level signal wires (like thermocouple or 4-20mA analog wires) should be separated from high-power motor leads. NFPA 79 suggests a minimum distance or the use of grounded metallic barriers/conduit to prevent "crosstalk."
* **Color Coding (The "Uniform" Language):**
* **Black:** AC Power (Line voltage).
* **Red:** AC Control Circuits.
* **Blue:** DC Control Circuits.
* **Orange:** Interlock circuits fed from an external power source (remains "hot" when main disconnect is off).
* **Green (or Green/Yellow):** Equipment grounding conductor.



## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Added 2024 updates regarding the use of "listed" cable ties and expanded requirements for EMI segregation between power and safety-signal cabling.
