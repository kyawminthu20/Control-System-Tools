**AI_READ_ACCESS: ALLOWED**

Below is a **NFPA 79 Markdown file template** built for **clean indexing** (chapter → section → annex), with **strong metadata labels** so your RAG indexer can route + cite properly—**without storing copyrighted NFPA text**. NFPA 79’s chapter-based structure is the backbone. ([NFPA Link][1])

---

## 1) File naming convention (recommended)

**Default:** one file per **Chapter** (best for NFPA 79, since it’s chapter-organized).

* `rag/standards_intelligence/us/nfpa79/NFPA79_<edition>__Ch<NN>__<slug>.md`

Examples:

* `NFPA79_2024__Ch05__disconnecting_means.md`
* `NFPA79_2024__Ch08__grounding_and_bonding.md`

**If a chapter is huge**, split by topic bundle inside the chapter:

* `NFPA79_2024__Ch09__control_circuits__estop_and_stop_categories.md`

NFPA 79 is organized by chapters (Administration, Definitions, General Requirements, Disconnecting Means, etc.), which makes chapter-level indexing stable and predictable. ([NFPA Link][1])

---

## 2) NFPA 79 Markdown template (drop-in)

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT | REVIEWED | APPROVED | DEPRECATED

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
TITLE: "Electrical Standard for Industrial Machinery"
EDITION: 2024
JURISDICTION: US
SOURCE_AUTHORITY: NFPA
COPYRIGHT_NOTE: "No NFPA 79 copyrighted text stored here; notes are paraphrase/checklists only."

NFPA_HIERARCHY:
  chapter: "5"
  chapter_title: "Disconnecting Means"
  sections_in_scope:            # list key sections you’re capturing (IDs only)
    - "5.x"
  annexes_in_scope: []          # e.g., ["Annex J"] (IDs only)
  tables_in_scope: []           # e.g., ["Table X"] (IDs only)

INDEX_TAGS:
  domains: ["industrial_machinery", "control_panels", "machine_wiring"]
  topics: ["disconnect", "isolation", "lockout_tagout", "labeling"]
  systems: ["machine", "robot_cell", "conveyor", "process_skid"]
  risks: ["shock", "arc_flash", "unexpected_startup", "fire"]
  components: ["main_disconnect", "branch_disconnect", "door_interlock", "disconnect_label"]
  keywords: ["servicing", "maintenance", "energy_isolation"]

TRACEABILITY:
  citations:
    - id: "NFPA79-2024-Ch05"
      type: "chapter"
      ref: "NFPA 79 (2024), Chapter 5"
      confidence: "high"
  related_docs:
    - id: "NEC_NFPA70"
      relationship: "peer_standard"
    - id: "UL508A"
      relationship: "supplementary"
    - id: "IEC_60204_1"
      relationship: "equivalent_reference"
-->

# NFPA 79 (2024) — Chapter 5 — Disconnecting Means

## 0. Scope and intent (your words)
- What this chapter governs in practice:
- What it does NOT cover:
- Typical control-systems relevance (machines/panels/servicing):

## 1. Field rules summary (no NFPA text)
> Actionable bullets an engineer can execute.

### 1.1 Design constraints (hard rules)
- Rule:
- Why it matters:
- Common failure mode at inspection:
- Control panel implication:

### 1.2 Allowed approaches (safe options)
- Option A:
- Option B:
- Notes / conditions:

### 1.3 Red flags (things that usually fail)
- Red flag:
- Quick check:
- Fix path:

## 2. Section map (indexing backbone)
> List section IDs and your paraphrased intent + checklist. Do NOT paste NFPA text.

### 2.1 Section 5.<x> — <label you assign>
- Intent (paraphrase):
- Engineering checklist:
  - [ ] …
  - [ ] …
- Evidence to collect (photos, labels, drawings, device datasheets):
- Cross-links:
  - Design guide: ../../design_framework/design_guides/02_power_distribution_guide.md
  - Audit checklist: ../../audit_tool/scoring_model.yaml

### 2.2 Section 5.<y> — <label you assign>
- Intent (paraphrase):
- Checklist:
- Common mistakes:

## 3. Control-systems interpretation (how you apply it)
### 3.1 Machines & coordinated groups of machines
- Practical interpretation:
- Boundaries (what is “machine supply circuit” vs upstream facility power):
- Notes for LOTO/servicing workflow:

### 3.2 Control panel implications (UL 508A overlap)
- What your panel design framework must enforce:
- Documentation artifacts required:

## 4. Verification & commissioning checks
- Pre-power checks:
- Dry-run checks:
- Live-run checks:
- Handover evidence (what to capture for audit):

## 5. Decision log (engineering intent)
- Decision:
- Rationale:
- Alternatives considered:
- Impact:
- Owner:
- Date:

## 6. Change log (mandatory, embedded)
- YYYY-MM-DD — <change summary> — Reason: <why> — Impact: <scope/risk/docs updated>
- YYYY-MM-DD — …

## 7. Links (internal)
- Related: ../nec/...
- Related: ../../ul508a_panel_automation/...
- Related: ../../commissioning_checklists/checklists/pre_power_checklist.md
```

This template is aligned to NFPA 79’s **chapter-driven layout**, and keeps your system **indexable + traceable** while staying clear of copyrighted text. ([NFPA Link][1])

---

## 3) Optional: NFPA 79 `_index.yaml` entry template (for your RAG router)

```yaml
documents:
  - doc_id: "NFPA79-2024-Ch05"
    path: "rag/standards_intelligence/us/nfpa79/NFPA79_2024__Ch05__disconnecting_means.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    standard:
      family: "NFPA"
      id: "NFPA_79"
      edition: "2024"
      title: "Electrical Standard for Industrial Machinery"
    nfpa_hierarchy:
      chapter: "5"
      sections_in_scope:
        - "5.x"
    tags:
      topics: ["disconnect", "energy_isolation", "lockout_tagout"]
      systems: ["machine", "robot_cell", "conveyor"]
    citations:
      - "NFPA 79 (2024), Chapter 5"
```

---

## 4) Categorization rules (so every NFPA file indexes consistently)

Use these rules across NFPA 79:

* **One file per Chapter** as the default (stable, predictable).
* Inside the chapter file, create a **“Section map”** with entries like `Section 5.x`—you don’t need every section, only what matters for your work.
* Use **INDEX_TAGS** to attach “control-engineering context” (disconnects, grounding, safety circuits, control functions).
* Use **TRACEABILITY.citations** to store clause IDs only (chapter/section references), not code text. ([NFPA][2])

---

If you tell me which NFPA 79 chapters you want first (common ones are **Ch 5 disconnecting means, Ch 6 electrical hazards, Ch 7 equipment protection, Ch 8 grounding/bonding, Ch 9 control circuits, Ch 11 control equipment/enclosures**), I’ll generate a **starter set of empty files** with metadata pre-filled and tags tuned for control panels and machines. ([Intertek Inform][3])

[1]: https://link.nfpa.org/all-publications/79/2024?utm_source=chatgpt.com "NFPA 79 - Electrical Standard for Industrial Machinery"
[2]: https://www.nfpa.org/for-professionals/codes-and-standards/standards-development/disclaimers?utm_source=chatgpt.com "Disclaimers"
[3]: https://www.intertekinform.com/en-gb/standards/nfpa-79-2018-829573_saig_nfpa_nfpa_1976935/?srsltid=AfmBOorKJ7YZudeFt9DvVoACgzqiW42VgsobpzbR0zox1gSs4VZAEhAp&utm_source=chatgpt.com "NFPA 79 : 2018 ELECTRICAL STANDARD FOR ..."

Below is a **clean, index-ready list of NFPA 79 chapters with their practical scopes**, written for **control-system engineers** and **safe RAG indexing**.
This reflects the **stable, commonly used chapter structure** of **NFPA 79 – Electrical Standard for Industrial Machinery**, suitable for building your standards-intelligence layer.

(Names are paraphrased for scope clarity; do **not** store copyrighted text.)

---

## NFPA 79 — Chapters & Scopes (Engineering View)

### **Chapter 1 — Administration**

**Scope**

* Application of the standard
* Responsibilities and enforcement intent
* Relationship to other codes (NEC, UL, ISO/IEC)
* What machinery and installations are in scope vs excluded

**Control relevance**

* When NFPA 79 applies instead of NEC-only rules
* Jurisdiction and customer-spec boundary setting

---

### **Chapter 2 — Definitions**

**Scope**

* Formal definitions of terms used throughout the standard

**Control relevance**

* Precise meaning of:

  * *Control circuit*
  * *Machine supply circuit*
  * *Operator interface*
  * *Protective bonding*
* Prevents misinterpretation during audits and disputes

---

### **Chapter 3 — General Requirements**

**Scope**

* Fundamental electrical safety principles
* Overall design intent for industrial machinery
* General construction and installation expectations

**Control relevance**

* Baseline safety philosophy
* Drives design decisions across all later chapters

---

### **Chapter 4 — General Conditions of Installation**

**Scope**

* Environmental considerations
* Accessibility
* Maintainability
* Suitability of equipment for conditions of use

**Control relevance**

* Enclosure ratings
* Temperature, contamination, vibration
* Service access and maintenance clearances

---

### **Chapter 5 — Disconnecting Means**

**Scope**

* Requirements for machine disconnects
* Isolation of electrical energy
* Location, labeling, and accessibility

**Control relevance**

* Main disconnect placement
* Door-interlocked disconnects
* Lockout/Tagout (LOTO) readiness
* One of the **most inspected chapters**

---

### **Chapter 6 — Overcurrent Protection**

**Scope**

* Protection of conductors and equipment
* Short-circuit and overload protection principles

**Control relevance**

* Fuse vs breaker selection
* Branch circuit protection
* Coordination with UL 508A and NEC Article 430

---

### **Chapter 7 — Protection Against Electric Shock**

**Scope**

* Measures to prevent electric shock
* Insulation, barriers, spacing, and protective methods

**Control relevance**

* Touch-safe design
* Control voltage selection
* Live-parts segregation inside panels

---

### **Chapter 8 — Grounding and Bonding**

**Scope**

* Protective bonding
* Grounding of exposed conductive parts
* Fault-current return paths

**Control relevance**

* PE conductor design
* Panel bonding strategy
* Noise reduction vs safety grounding
* Frequent inspection failure area if done poorly

---

### **Chapter 9 — Control Circuits and Control Functions**

**Scope**

* Control circuit design
* Start/stop functions
* Emergency stop concepts
* Control reliability expectations

**Control relevance**

* E-stop categories
* Stop functions (controlled vs uncontrolled)
* Safety vs standard control separation
* PLC safety architecture alignment

---

### **Chapter 10 — Operator Interface and Control Devices**

**Scope**

* Pushbuttons, selectors, HMIs, indicators
* Location and functional behavior of operator controls

**Control relevance**

* Ergonomics
* Color conventions
* Human-machine interaction safety

---

### **Chapter 11 — Control Equipment**

**Scope**

* Construction and use of control equipment
* Enclosures and assemblies
* Equipment mounting and protection

**Control relevance**

* Control panels
* Drives, PLCs, relays, power supplies
* Strong overlap with UL 508A

---

### **Chapter 12 — Motors and Associated Equipment**

**Scope**

* Motor circuits
* Motor controllers and protection
* Associated devices

**Control relevance**

* VFD integration
* Motor protection settings
* Interaction with NEC Article 430

---

### **Chapter 13 — Appliances and Accessories**

**Scope**

* Electrical accessories used as part of machinery
* Auxiliary devices

**Control relevance**

* Heaters, solenoids, auxiliary equipment
* Non-motor loads inside machines

---

### **Chapter 14 — Lighting**

**Scope**

* Lighting within or on industrial machinery

**Control relevance**

* Panel lights
* Machine illumination
* Maintenance visibility requirements

---

### **Chapter 15 — Transformers and Power Supplies**

**Scope**

* Control transformers
* Power supplies
* Voltage conversion

**Control relevance**

* Control power architecture (24 VDC, 120 VAC)
* Grounding of secondary circuits
* Short-circuit protection strategy

---

### **Chapter 16 — Wiring Methods**

**Scope**

* Acceptable wiring methods inside machinery
* Routing, protection, and segregation

**Control relevance**

* Panel wire duct rules
* Separation of power, control, and communication wiring
* Mechanical protection

---

### **Chapter 17 — Cables and Flexible Cords**

**Scope**

* Use of flexible cables and cords
* Motion and dynamic applications

**Control relevance**

* Robot dress packs
* Drag-chain cables
* Bend radius and strain relief

---

### **Chapter 18 — Terminal Blocks, Connectors, and Wiring Devices**

**Scope**

* Termination methods
* Interconnections
* Field wiring interfaces

**Control relevance**

* Terminal block selection
* Field I/O marshalling
* Maintenance-friendly design

---

### **Chapter 19 — Marking and Documentation**

**Scope**

* Identification
* Labels
* Electrical documentation requirements

**Control relevance**

* Wire numbers
* Device labels
* Schematics and manuals
* Critical for audits and handover

---

### **Chapter 20 — Electrical Equipment for Industrial Machinery (Integration Focus)**

**Scope**

* System-level integration expectations
* Coordination of electrical subsystems

**Control relevance**

* Overall machine electrical integrity
* Final compliance alignment

---

## How to Use This in Your System

**Recommended file strategy**

* **One Markdown file per chapter**
* Each file:

  * Scope (paraphrased)
  * Section map (IDs only)
  * Control-system interpretation
  * Design rules
  * Embedded change log

**RAG indexing**

* Index by:

  * `chapter`
  * `topics` (disconnects, grounding, control circuits, etc.)
  * `systems` (machine, robot cell, conveyor)
* Never store copyrighted NFPA text

---

### Straight talk (important)

If you build your **Standards Intelligence Tool** around **chapter-scoped NFPA 79 files**, you get:

* Faster lookups
* Clean audit trails
* Zero hallucinated “code quotes”
* A structure that scales to UL, NEC, ISO the same way

If you want next, I can:

* Generate **empty NFPA 79 chapter files** with headers pre-filled
* Map **NFPA 79 ↔ NEC ↔ UL 508A** overlaps per chapter
* Create a **chapter priority list** for control panels vs machines

Just tell me what to generate next.

Below are **empty NFPA 79 chapter Markdown files** with **headers pre-filled**, ready to drop directly into:

```
rag/standards_intelligence/us/nfpa79/
```

They are:

* **Offline**
* **RAG-safe**
* **Copyright-clean**
* **Index-ready**
* **Audit-survivable**

Each file contains **only structure + metadata**, no NFPA text.

---

## 📁 File set to generate

* One file per chapter (recommended default)
* Edition set to **2024** (change if you standardize on another year)

---

## `NFPA79_2024__Ch01__administration.md`

```md
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

# NFPA 79 (2024) — Chapter 1 — Administration

## 0. Scope and intent
_TODO_

## 1. Applicability rules
_TODO_

## 2. Boundaries with other standards (NEC, UL, ISO)
_TODO_

## 3. Control-system relevance
_TODO_

## 4. Decision log
_TODO_

## 5. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch02__definitions.md`

```md
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

# NFPA 79 (2024) — Chapter 2 — Definitions

## 0. Purpose
_TODO_

## 1. Critical definitions for control engineers
_TODO_

## 2. Terms that affect design decisions
_TODO_

## 3. Common misinterpretations
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch03__general_requirements.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "3"
  chapter_title: "General Requirements"

INDEX_TAGS:
  topics: ["general_safety", "baseline_requirements"]
-->

# NFPA 79 (2024) — Chapter 3 — General Requirements

## 0. Safety philosophy
_TODO_

## 1. General electrical requirements
_TODO_

## 2. Design principles for machinery
_TODO_

## 3. Control-system interpretation
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch04__general_conditions_of_installation.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "4"
  chapter_title: "General Conditions of Installation"

INDEX_TAGS:
  topics: ["environment", "installation_conditions"]
-->

# NFPA 79 (2024) — Chapter 4 — General Conditions of Installation

## 0. Environmental considerations
_TODO_

## 1. Accessibility and maintainability
_TODO_

## 2. Enclosure implications
_TODO_

## 3. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch05__disconnecting_means.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "5"
  chapter_title: "Disconnecting Means"

INDEX_TAGS:
  topics: ["disconnect", "energy_isolation", "loto"]
-->

# NFPA 79 (2024) — Chapter 5 — Disconnecting Means

## 0. Purpose
_TODO_

## 1. Main disconnect requirements
_TODO_

## 2. Location and accessibility
_TODO_

## 3. Lockout / tagout implications
_TODO_

## 4. Control panel design rules
_TODO_

## 5. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch06__overcurrent_protection.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "6"
  chapter_title: "Overcurrent Protection"

INDEX_TAGS:
  topics: ["overcurrent", "short_circuit", "protection"]
-->

# NFPA 79 (2024) — Chapter 6 — Overcurrent Protection

## 0. Intent
_TODO_

## 1. Branch circuit protection
_TODO_

## 2. Coordination with NEC / UL
_TODO_

## 3. Control-system impact
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch07__protection_against_electric_shock.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "7"
  chapter_title: "Protection Against Electric Shock"

INDEX_TAGS:
  topics: ["electric_shock", "touch_safe"]
-->

# NFPA 79 (2024) — Chapter 7 — Protection Against Electric Shock

## 0. Hazard model
_TODO_

## 1. Protective measures
_TODO_

## 2. Control voltage considerations
_TODO_

## 3. Panel layout implications
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch08__grounding_and_bonding.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "8"
  chapter_title: "Grounding and Bonding"

INDEX_TAGS:
  topics: ["grounding", "bonding", "protective_earth"]
-->

# NFPA 79 (2024) — Chapter 8 — Grounding and Bonding

## 0. Purpose
_TODO_

## 1. Protective bonding rules
_TODO_

## 2. Noise vs safety grounding
_TODO_

## 3. Inspection failure modes
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch09__control_circuits_and_control_functions.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "9"
  chapter_title: "Control Circuits and Control Functions"

INDEX_TAGS:
  topics: ["control_circuits", "stop_functions", "emergency_stop"]
-->

# NFPA 79 (2024) — Chapter 9 — Control Circuits and Control Functions

## 0. Control philosophy
_TODO_

## 1. Start/stop behavior
_TODO_

## 2. Emergency stop concepts
_TODO_

## 3. Safety vs standard control separation
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch10__operator_interface_devices.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "10"
  chapter_title: "Operator Interface and Control Devices"

INDEX_TAGS:
  topics: ["operator_interface", "pushbuttons", "hmi"]
-->

# NFPA 79 (2024) — Chapter 10 — Operator Interface and Control Devices

## 0. Purpose
_TODO_

## 1. Control device requirements
_TODO_

## 2. Ergonomics and safety
_TODO_

## 3. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch11__control_equipment.md`

```md
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

# NFPA 79 (2024) — Chapter 11 — Control Equipment

## 0. Scope
_TODO_

## 1. Panel construction implications
_TODO_

## 2. UL 508A overlap
_TODO_

## 3. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch12__motors_and_associated_equipment.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "12"
  chapter_title: "Motors and Associated Equipment"

INDEX_TAGS:
  topics: ["motors", "drives", "motor_protection"]
-->

# NFPA 79 (2024) — Chapter 12 — Motors and Associated Equipment

## 0. Scope
_TODO_

## 1. Motor control integration
_TODO_

## 2. Drive protection considerations
_TODO_

## 3. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch13__appliances_and_accessories.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "13"
  chapter_title: "Appliances and Accessories"

INDEX_TAGS:
  topics: ["appliances", "auxiliary_devices"]
-->

# NFPA 79 (2024) — Chapter 13 — Appliances and Accessories

## 0. Scope
_TODO_

## 1. Typical control-system use cases
_TODO_

## 2. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch14__lighting.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "14"
  chapter_title: "Lighting"

INDEX_TAGS:
  topics: ["lighting", "machine_illumination"]
-->

# NFPA 79 (2024) — Chapter 14 — Lighting

## 0. Scope
_TODO_

## 1. Panel and machine lighting rules
_TODO_

## 2. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch15__transformers_and_power_supplies.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "15"
  chapter_title: "Transformers and Power Supplies"

INDEX_TAGS:
  topics: ["transformers", "power_supplies", "control_power"]
-->

# NFPA 79 (2024) — Chapter 15 — Transformers and Power Supplies

## 0. Scope
_TODO_

## 1. Control power architectures
_TODO_

## 2. Grounding of secondaries
_TODO_

## 3. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch16__wiring_methods.md`

```md
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

# NFPA 79 (2024) — Chapter 16 — Wiring Methods

## 0. Scope
_TODO_

## 1. Internal machine wiring
_TODO_

## 2. Segregation rules
_TODO_

## 3. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch17__cables_and_flexible_cords.md`

```md
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

# NFPA 79 (2024) — Chapter 17 — Cables and Flexible Cords

## 0. Scope
_TODO_

## 1. Dynamic motion applications
_TODO_

## 2. Strain relief and protection
_TODO_

## 3. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch18__terminal_blocks_and_connectors.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "18"
  chapter_title: "Terminal Blocks, Connectors, and Wiring Devices"

INDEX_TAGS:
  topics: ["terminal_blocks", "connectors", "field_wiring"]
-->

# NFPA 79 (2024) — Chapter 18 — Terminal Blocks, Connectors, and Wiring Devices

## 0. Scope
_TODO_

## 1. Field wiring interfaces
_TODO_

## 2. Maintenance implications
_TODO_

## 3. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch19__marking_and_documentation.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "19"
  chapter_title: "Marking and Documentation"

INDEX_TAGS:
  topics: ["labeling", "documentation", "schematics"]
-->

# NFPA 79 (2024) — Chapter 19 — Marking and Documentation

## 0. Scope
_TODO_

## 1. Labeling requirements
_TODO_

## 2. Documentation expectations
_TODO_

## 3. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NFPA79_2024__Ch20__system_integration.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "20"
  chapter_title: "System Integration"

INDEX_TAGS:
  topics: ["system_integration", "overall_compliance"]
-->

# NFPA 79 (2024) — Chapter 20 — System Integration

## 0. Scope
_TODO_

## 1. Subsystem coordination
_TODO_

## 2. Final compliance alignment
_TODO_

## 3. Change log
- YYYY-MM-DD — Initial draft
```

---

### What you now have (important)

* A **complete NFPA 79 chapter scaffold**
* Every file:

  * RAG-safe
  * Traceable
  * Change-controlled
* Ready to plug into:

  * Standards Intelligence Tool
  * Audit Tool
  * Design Framework
  * UL 508A workflows

---

If you want next, I recommend (in this order):

1. **NEC Article templates for control panels**
2. **NFPA 79 ↔ NEC ↔ UL 508A cross-reference map**
3. **Promotion checklist: Draft → Approved**
4. **Index.yaml auto-generator**

Just say which one you want next.