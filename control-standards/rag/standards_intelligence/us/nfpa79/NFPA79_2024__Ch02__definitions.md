<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "2"
  chapter_title: "Definitions"

INDEX_TAGS:
  topics: ["definitions", "terminology"]
-->


## 0. Purpose

The purpose of Chapter 2 is to provide precise, standardized definitions for terms used throughout the document. These definitions ensure that design requirements—such as those for **Emergency Stops** or **Control Circuits**—are not left to subjective interpretation, which could lead to unsafe machine operation or failed inspections.

## 1. Critical Definitions for Control Engineers

Understanding these specific terms is essential for the electrical design of any industrial machine:

* **Industrial Machinery:** A power-driven machine (or group of machines) used to process material by various means. This definition is the trigger for whether NFPA 79 applies to your project versus just the NEC.
* **Control Circuit:** The circuit of a control apparatus (e.g., PLC I/O, relays) that carries the electric signals directing the performance of the controller but does not carry the main power current.
* **Interlock (for Safety):** An arrangement of control elements where the operation of one part of the machine depends on the state of another part (e.g., a guard being closed before a motor can start).
* **Emergency Stop:** A function that is intended to avert arising or reduce existing hazards to persons, damage to machinery, or damage to work in progress; initiated by a single human action.

## 2. Terms That Affect Design Decisions

The way a term is defined in Chapter 2 directly dictates how you wire the machine:

* **Grounded vs. Grounding:**
* **Grounded:** Connected to ground or to a conducting body that extends the ground connection (the state of the system).
* **Grounding Conductor (Equipment):** The conductor used to connect the non-current-carrying metal parts of equipment to the system grounded conductor (the physical wire you install).


* **Enclosure Types:** Definitions for NEMA or IP ratings are referenced here, which dictate the level of protection required for environmental factors like oil, dust, or water spray.
* **Stop Categories:** * **Category 0:** Uncontrolled stop by immediate removal of power.
* **Category 1:** Controlled stop with power available to achieve the stop, then power removal.
* **Category 2:** Controlled stop with power left available.



## 3. Common Misinterpretations

Misunderstanding these definitions often results in non-compliance during a field evaluation:

* **"Control Station" vs. "Operator Interface":** A control station is a physical assembly of devices (buttons, switches), whereas an operator interface may be a touchscreen (HMI). NFPA 79 has different requirements for the physical durability and accessibility of each.
* **"Safe State":** Engineers often assume "Safe State" always means "off." However, in some processes (like a cooling pump for a reactor), the safe state might actually be "on."
* **"Qualified Person":** This is not just anyone who can use a multimeter. It refers specifically to someone who has the skills and knowledge related to the construction and operation of the electrical equipment and has received **safety training** on the hazards involved.

