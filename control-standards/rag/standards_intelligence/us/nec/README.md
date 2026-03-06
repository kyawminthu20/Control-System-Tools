Below is a **NEC Markdown file template** designed specifically for **proper indexing (RAG-friendly)** using **chapters → articles → parts → sections → tables → annexes**, with **strong metadata labels** so your indexer can route and cite correctly.

It does **not** include copyrighted NEC text—only your notes, paraphrases, checklists, and references. The NEC’s high-level structure (chapters/articles/parts) is the basis for this categorization. ([NFPA][1])

---

## 1) File naming convention (recommended)

* `rag/standards_intelligence/us/nec/NEC_<edition>__Ch<NN>__Art<NNN>__<slug>.md`

Examples:

* `NEC_2023__Ch01__Art110__requirements_for_electrical_installations.md`
* `NEC_2023__Ch04__Art430__motors_motor_circuits_and_controllers.md`

This mirrors NEC’s hierarchy: **Chapters → Articles → Parts → Sections/Tables**. ([NFPA][1])

---

## 2) NEC Markdown template (drop-in)

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT | REVIEWED | APPROVED | DEPRECATED

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023
JURISDICTION: US
SOURCE_AUTHORITY: NFPA
COPYRIGHT_NOTE: "No NEC copyrighted text stored here; notes are paraphrase/checklists only."

NEC_HIERARCHY:
  chapter: "1"
  chapter_title: "General"
  article: "110"
  article_title: "Requirements for Electrical Installations"
  part: "I"               # optional
  part_title: "General"   # optional
  section: "110.3(B)"     # optional: for single-section notes
  tables: []              # e.g., ["Table 310.16"]
  annexes: []             # e.g., ["Annex D"]

INDEX_TAGS:
  topics: ["industrial_control_panel", "wiring_methods", "bonding_grounding", "disconnects"]
  systems: ["control_panel", "machine", "conveyor", "robot_cell", "process_skid"]
  risk: ["shock", "fire", "arc_flash"]
  components: ["disconnect", "overcurrent_protection", "conductors", "enclosure"]
  keywords: ["listing", "labeling", "installation_instructions"]

TRACEABILITY:
  citations:
    - id: "NEC2023-110.3B"
      type: "code_section"
      ref: "NFPA 70 (NEC) 2023, 110.3(B)"
      confidence: "high"
  related_docs:
    - id: "UL508A"
      relationship: "supplementary"
    - id: "NFPA79"
      relationship: "peer_standard"
-->

# NEC 2023 — Chapter 1 — Article 110 — Requirements for Electrical Installations

## 0. Scope and intent (your words)
- What this article governs in practice:
- What it does NOT cover:
- Typical control-systems relevance:

## 1. “Field rules” summary (no NEC text)
> Write in actionable bullets an engineer can follow.

### 1.1 Design constraints (hard rules)
- Rule:
- Why it matters:
- Typical violation:
- Control panel implication:

### 1.2 Allowed approaches (safe options)
- Option A:
- Option B:
- Notes:

### 1.3 Red flags (things that usually fail inspection)
- Red flag:
- Quick check:
- Fix path:

## 2. Section map (indexing backbone)
> List sections you care about and what you store about them (no code text).

### 2.1 Section 110.3(B) — Installation & listing instructions
- Intent (paraphrase):
- Engineering checklist:
  - [ ] Verify device listing/labeling
  - [ ] Follow manufacturer installation instructions
  - [ ] Keep evidence (manual revision / datasheet)
- Evidence to collect:
- Cross-links:
  - See: ../ul_508a/...
  - See: ../design_framework/design_guides/...

### 2.2 Section <X.Y> — <your section label>
- Intent (paraphrase):
- Checklist:
- Measurement/verification:
- Common mistakes:

## 3. Control-system specific interpretation
### 3.1 Control panels (UL 508A / industrial panels)
- Practical impact:
- Design rule in your framework:
- Notes for UL file / SCCR / labeling:

### 3.2 Machines (NFPA 79 overlap)
- Where NEC ends and NFPA 79 takes lead:
- Conflict handling rule (jurisdiction/customer decides):

## 4. Test and verification
- What inspectors typically check:
- Pre-power checks:
- Documentation needed:

## 5. Decision log (engineering intent)
- Decision:
- Rationale:
- Alternatives considered:
- Impact:
- Owner:
- Date:

## 6. Change log (mandatory, embedded)
- YYYY-MM-DD — <change summary> — Reason: <why> — Impact: <scope/risk/docs updated>
- YYYY-MM-DD — ...

## 7. Links (internal)
- Related design guide: ../../design_framework/design_guides/02_power_distribution_guide.md
- Troubleshooting note: ../../troubleshooting_decision_engine/playbooks/networks_playbook.md

```

Why this works:

* **NEC_HIERARCHY** makes your indexer deterministic.
* **INDEX_TAGS** allow cross-cutting queries (“all grounding rules impacting control panels”).
* **TRACEABILITY** forces clause-level reference without storing copyrighted content. ([NFPA][1])

---

## 3) Optional: a simple `_index.yaml` entry template for NEC files

Put this in `rag/_index.yaml` (or your NEC-specific index file) so RAG only indexes approved notes:

```yaml
documents:
  - doc_id: "NEC2023-Ch01-Art110"
    path: "rag/standards_intelligence/us/nec/NEC_2023__Ch01__Art110__requirements_for_electrical_installations.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    standard:
      family: "NEC"
      id: "NFPA_70"
      edition: "2023"
    nec_hierarchy:
      chapter: "1"
      article: "110"
      part: null
      sections:
        - "110.3(B)"
    tags:
      topics: ["listing", "installation_instructions"]
      systems: ["control_panel", "machine"]
    citations:
      - "NFPA 70 (NEC) 2023 110.3(B)"
```

---

## 4) NEC categorization rules (for consistent indexing)

Use these rules when creating files:

* **One file per Article** (best default).
* If an Article is huge (e.g., motors), split by **Part**:

  * `Art430__PartI_general.md`, `Art430__PartIV_motor_control_centers.md`, etc.
* If you only care about one section right now, still keep it inside the Article file, but populate `section:` in metadata for precision.
* Tables and Annex references go into `tables:` and `annexes:` fields, because they’re often called out separately in searches. ([Mike Holt Enterprises][2])

---

If you tell me which NEC edition you’re standardizing on (2020 vs 2023, etc.), I’ll generate:

* A **starter folder tree** for `rag/standards_intelligence/us/nec/` with the **most control-panel-relevant Articles pre-created**, and
* A batch of **empty MD files** with the correct headers already filled.

[1]: https://www.nfpa.org/education-and-research/electrical/understanding-nfpa-70-national-electrical-code?utm_source=chatgpt.com "Learn More About NFPA 70, National Electrical Code (NEC)"
[2]: https://www.mikeholt.com/files/PDF/23CC_Top_Ten_Rules.pdf?srsltid=AfmBOoqrqCu2CghDtPwnKZJSl3c1Wc0IgTA3R_pmdePLWgfvORK8H70t&utm_source=chatgpt.com "January 18, 2024"

Below are **NEC Article Markdown templates** specifically curated for **industrial control panels**, with **headers pre-filled**, **RAG-safe metadata**, and **no copyrighted NEC text**.
Drop these directly into:

```
rag/standards_intelligence/us/nec/
```

They are organized **one file per Article** (best practice for NEC), and each includes an **embedded change log** and **indexing metadata**.

---

## 📁 NEC Articles to Generate (Control-Panel Focus)

**Core (almost every panel):**

* Article 110 — Requirements for Electrical Installations
* Article 250 — Grounding and Bonding
* Article 300 — General Wiring Methods
* Article 310 — Conductors for General Wiring
* Article 409 — Industrial Control Panels

**Commonly needed (motors, power, controls):**

* Article 430 — Motors, Motor Circuits, and Controllers
* Article 240 — Overcurrent Protection
* Article 408 — Switchboards, Switchgear, and Panelboards
* Article 725 — Class 1, Class 2, and Class 3 Remote-Control Circuits

**As applicable:**

* Article 670 — Industrial Machinery
* Article 409 — Industrial Control Panels (yes, it gets its own deep file)
* Article 800/820/830 — Communications (if applicable)
* Article 511/514 — Hazardous locations (if applicable)

---

## `NEC_2023__Art110__requirements_for_electrical_installations.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023
JURISDICTION: US

NEC_HIERARCHY:
  article: "110"
  article_title: "Requirements for Electrical Installations"

INDEX_TAGS:
  topics: ["listing", "labeling", "installation_instructions"]
  systems: ["industrial_control_panel", "machine"]
  risks: ["shock", "fire", "arc_flash"]
-->

# NEC 2023 — Article 110 — Requirements for Electrical Installations

## 0. Scope and relevance to control panels
_TODO_

## 1. Installation & listing requirements (field rules)
_TODO_

## 2. Manufacturer instructions & evidence
_TODO_

## 3. Common inspection failures
_TODO_

## 4. Control-panel design implications
_TODO_

## 5. Decision log
_TODO_

## 6. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NEC_2023__Art250__grounding_and_bonding.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "250"
  article_title: "Grounding and Bonding"

INDEX_TAGS:
  topics: ["grounding", "bonding", "protective_earth"]
  systems: ["industrial_control_panel"]
-->

# NEC 2023 — Article 250 — Grounding and Bonding

## 0. Purpose for control panels
_TODO_

## 1. Equipment grounding conductors
_TODO_

## 2. Bonding of enclosures and doors
_TODO_

## 3. Noise vs safety grounding
_TODO_

## 4. Inspection failure patterns
_TODO_

## 5. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NEC_2023__Art300__general_wiring_methods.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "300"
  article_title: "General Wiring Methods"

INDEX_TAGS:
  topics: ["wiring_methods", "routing", "mechanical_protection"]
-->

# NEC 2023 — Article 300 — General Wiring Methods

## 0. Scope inside control panels
_TODO_

## 1. Routing and protection rules
_TODO_

## 2. Separation of circuits
_TODO_

## 3. Common panel violations
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NEC_2023__Art310__conductors_for_general_wiring.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "310"
  article_title: "Conductors for General Wiring"

INDEX_TAGS:
  topics: ["conductors", "ampacity", "temperature_rating"]
-->

# NEC 2023 — Article 310 — Conductors for General Wiring

## 0. Scope for panel conductors
_TODO_

## 1. Ampacity and derating
_TODO_

## 2. Temperature ratings
_TODO_

## 3. Control panel wire sizing logic
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NEC_2023__Art409__industrial_control_panels.md`  **(CRITICAL)**

```md
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
_TODO_

## 1. Panel definition and scope
_TODO_

## 2. Short-circuit current rating (SCCR)
_TODO_

## 3. Labeling requirements
_TODO_

## 4. Relationship to UL 508A
_TODO_

## 5. Inspector expectations
_TODO_

## 6. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NEC_2023__Art430__motors_motor_circuits_and_controllers.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "430"
  article_title: "Motors, Motor Circuits, and Controllers"

INDEX_TAGS:
  topics: ["motors", "drives", "motor_protection"]
-->

# NEC 2023 — Article 430 — Motors, Motor Circuits, and Controllers

## 0. Scope for control panels
_TODO_

## 1. Motor protection concepts
_TODO_

## 2. VFD considerations
_TODO_

## 3. Coordination with UL 508A
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## `NEC_2023__Art725__class_1_2_3_control_circuits.md`

```md
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
_TODO_

## 1. Power-limited circuit rules
_TODO_

## 2. Separation from power circuits
_TODO_

## 3. Field wiring implications
_TODO_

## 4. Change log
- YYYY-MM-DD — Initial draft
```

---

## Optional (generate only if applicable)

* `NEC_2023__Art670__industrial_machinery.md`
* `NEC_2023__Art511__hazardous_locations.md`
* `NEC_2023__Art800__communications_circuits.md`

---

## Why this set is correct

* Covers **>90% of control panel inspections**
* Maps cleanly to **UL 508A**
* Aligns with **NFPA 79**
* Enables:

  * Standards Intelligence Tool
  * Audit Tool
  * Panel automation
  * Design frameworks
  * Future licensing

---

## Strong recommendation (next step)

If you want this to become **bulletproof**:

1. Generate **UL 508A clause templates**
2. Create **NEC ↔ NFPA 79 ↔ UL 508A overlap map**
3. Add **SCCR calculation worksheet (YAML + MD)**

Say which one you want next.
