<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
TITLE: Electrical Standard for Industrial Machinery
EDITION: 2024
JURISDICTION: US

NFPA_HIERARCHY:
  chapter: "1"
  chapter_title: "Administration"

INDEX_TAGS:
  domains: ["industrial_machinery"]
  topics: ["applicability", "scope", "enforcement"]
  systems: ["machine", "robot_cell", "conveyor"]
-->


## 0. Scope and Intent

The primary scope of NFPA 79 covers the **electrical/electronic equipment**, apparatus, or systems of industrial machines operating from a nominal voltage of **1000 volts or less**.

* **Intent:** To provide detailed information for the application of electrical equipment to promote safety to persons and property.
* **Machine Definition:** It applies to the point of connection to the electrical supply (typically the output of the disconnecting means).

## 1. Applicability Rules

NFPA 79 applies to "industrial machinery," which is defined as a power-driven machine (or a group of machines working together) used to process material by cutting, forming, pressure, electrical, or other means.

* **Includes:** Machine tools, injection molding machines, wood machinery, assembly machines, and material handling equipment (conveyors).
* **Excludes:** Fixed offshore platforms, aircraft, automotive vehicles, and equipment used in hazardous (classified) locations (which fall under NFPA 70/NEC).

## 2. Boundaries with Other Standards

Navigating the "Standard Map" is often where engineers face the most confusion. Here is how NFPA 79 interacts with its peers:

| Standard | Relationship to NFPA 79 |
| --- | --- |
| **NFPA 70 (NEC)** | The NEC governs the **supply** to the machine (Art. 670); NFPA 79 governs the **internal** wiring of the machine. |
| **UL 508A** | Focuses on the **construction** of the industrial control panel itself. NFPA 79 covers the entire machine system. |
| **ISO 13849 / IEC 62061** | These cover **functional safety**. NFPA 79 provides the electrical framework to implement these safety circuits. |

## 3. Control-System Relevance

NFPA 79 is critical for control system design because it dictates specific requirements for:

* **Stop Functions:** Defines Category 0 (immediate power removal), Category 1 (controlled stop then power removal), and Category 2 (controlled stop with power left available).
* **Operating States:** Requirements for "Safe State" and protection against unintended startup after a power loss.
* **Operator Interface:** Color coding for pushbuttons and indicator lights (e.g., Red for Emergency Stop, Green for Start).
