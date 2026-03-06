**AI_READ_ACCESS: ALLOWED**

Below are **UL 508A clause Markdown templates** purpose-built for **industrial control panels**, with **pre-filled headers**, **RAG-safe metadata**, **no copyrighted UL text**, and **audit-ready structure**.

These drop directly into:

```
rag/standards_intelligence/us/ul_508a/
```

They are organized **one file per major UL 508A section/subject**, which is the **correct granularity** for panel work (UL 508A is clause-heavy and table-driven).

---

## 📁 UL 508A — Recommended Clause File Set (Control Panel Focus)

**Core / Always used**

* Scope & application
* General construction requirements
* Enclosures & environmental ratings
* Spacing, creepage, and clearance
* Wiring methods & conductor sizing
* Overcurrent protection
* Short-Circuit Current Rating (SCCR)
* Marking & documentation

**Common / Conditional**

* Industrial control equipment
* Power distribution components
* Control circuits & control devices
* Motor controllers & drives
* Transformers & power supplies
* Grounding & bonding
* Supplement SB (SCCR – critical)

---

# 🔧 UL 508A CLAUSE TEMPLATES

---

## `UL508A_2022__scope_and_application.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: UL
STANDARD_ID: UL_508A
TITLE: Industrial Control Panels
EDITION: 2022
JURISDICTION: US

UL_HIERARCHY:
  section: "1"
  title: "Scope and Application"

INDEX_TAGS:
  topics: ["scope", "application", "panel_definition"]
  systems: ["industrial_control_panel"]
-->

# UL 508A — Scope and Application

## 0. Purpose
_TODO_

## 1. What qualifies as an industrial control panel
_TODO_

## 2. In-scope vs out-of-scope equipment
_TODO_

## 3. Relationship to NEC Article 409
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## `UL508A_2022__general_construction_requirements.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: UL
STANDARD_ID: UL_508A
EDITION: 2022

UL_HIERARCHY:
  section: "2"
  title: "General Construction Requirements"

INDEX_TAGS:
  topics: ["construction", "panel_layout", "mechanical_integrity"]
-->

# UL 508A — General Construction Requirements

## 0. Intent
_TODO_

## 1. Panel layout principles
_TODO_

## 2. Component mounting and support
_TODO_

## 3. Access, serviceability, workmanship
_TODO_

## 4. Common UL nonconformities
_TODO_

## 5. Change log
- YYYY-MM-DD — Initial draft
```

---

## `UL508A_2022__enclosures_and_environmental_ratings.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: UL
STANDARD_ID: UL_508A
EDITION: 2022

UL_HIERARCHY:
  section: "3"
  title: "Enclosures and Environmental Considerations"

INDEX_TAGS:
  topics: ["enclosures", "nema_ratings", "environment"]
-->

# UL 508A — Enclosures and Environmental Ratings

## 0. Scope
_TODO_

## 1. Enclosure type selection
_TODO_

## 2. Cooling and ventilation implications
_TODO_

## 3. Environmental misuse risks
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## `UL508A_2022__spacing_creepage_clearance.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: UL
STANDARD_ID: UL_508A
EDITION: 2022

UL_HIERARCHY:
  section: "4"
  title: "Spacing, Creepage, and Clearance"

INDEX_TAGS:
  topics: ["spacing", "creepage", "clearance"]
  risks: ["arc_flash", "short_circuit"]
-->

# UL 508A — Spacing, Creepage, and Clearance

## 0. Why spacing matters
_TODO_

## 1. Live parts separation rules
_TODO_

## 2. Voltage-based spacing logic
_TODO_

## 3. Field inspection failure patterns
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## `UL508A_2022__wiring_methods_and_conductors.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: UL
STANDARD_ID: UL_508A
EDITION: 2022

UL_HIERARCHY:
  section: "5"
  title: "Wiring Methods and Conductors"

INDEX_TAGS:
  topics: ["internal_wiring", "conductors", "ampacity"]
-->

# UL 508A — Wiring Methods and Conductors

## 0. Scope
_TODO_

## 1. Internal panel wiring rules
_TODO_

## 2. Conductor sizing logic
_TODO_

## 3. Temperature ratings
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## `UL508A_2022__overcurrent_protection.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: UL
STANDARD_ID: UL_508A
EDITION: 2022

UL_HIERARCHY:
  section: "6"
  title: "Overcurrent Protection"

INDEX_TAGS:
  topics: ["overcurrent", "branch_circuits", "coordination"]
-->

# UL 508A — Overcurrent Protection

## 0. Intent
_TODO_

## 1. Branch circuit protection rules
_TODO_

## 2. Coordination with NEC
_TODO_

## 3. Common misapplications
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## `UL508A_2022__grounding_and_bonding.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: UL
STANDARD_ID: UL_508A
EDITION: 2022

UL_HIERARCHY:
  section: "7"
  title: "Grounding and Bonding"

INDEX_TAGS:
  topics: ["grounding", "bonding", "protective_earth"]
-->

# UL 508A — Grounding and Bonding

## 0. Purpose
_TODO_

## 1. Panel grounding strategy
_TODO_

## 2. Door and subpanel bonding
_TODO_

## 3. Noise vs safety grounding
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## 🚨 **CRITICAL**

## `UL508A_2022__sccr_short_circuit_current_rating.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: UL
STANDARD_ID: UL_508A
EDITION: 2022

UL_HIERARCHY:
  section: "SB"
  title: "Short-Circuit Current Rating (SCCR)"

INDEX_TAGS:
  topics: ["sccr", "short_circuit_rating"]
  risks: ["equipment_failure", "fire"]
-->

# UL 508A — Supplement SB — SCCR

## 0. Why SCCR exists
_TODO_

## 1. SCCR determination methods
_TODO_

## 2. Weakest-link logic
_TODO_

## 3. Typical SCCR pitfalls
_TODO_

## 4. Labeling requirements
_TODO_

## 5. Change log
- YYYY-MM-DD — Initial draft
```

---

## `UL508A_2022__marking_and_documentation.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: UL
STANDARD_ID: UL_508A
EDITION: 2022

UL_HIERARCHY:
  section: "8"
  title: "Marking and Documentation"

INDEX_TAGS:
  topics: ["labeling", "documentation", "nameplates"]
-->

# UL 508A — Marking and Documentation

## 0. Scope
_TODO_

## 1. Required panel markings
_TODO_

## 2. Documentation retention
_TODO_

## 3. Audit readiness
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## Optional / As Needed

* `UL508A_2022__control_circuits_and_devices.md`
* `UL508A_2022__motor_controllers_and_drives.md`
* `UL508A_2022__transformers_and_power_supplies.md`

---

## Why this structure works (engineering reality)

* Mirrors **how UL inspectors think**
* Separates **SCCR as a first-class risk**
* Aligns with:

  * NEC Article 409
  * NFPA 79 Chapter 11
* Enables:

  * Panel automation
  * Audit tooling
  * Future UL file compliance
  * Licensing/IP packaging

---

## My recommendation (next logical step)

If you want to make this **inspection-proof**:

1. Generate **SCCR calculation YAML schema**
2. Create **UL 508A ↔ NEC ↔ NFPA 79 overlap matrix**
3. Build **panel inspection checklist auto-generator**

Tell me which one you want next, and I’ll generate it cleanly.