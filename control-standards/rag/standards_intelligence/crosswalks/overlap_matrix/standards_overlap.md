<!--
CONTENT_CLASS: DERIVED_REFERENCE
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

**AI_READ_ACCESS: ALLOWED**

Create UL 508A ↔ NEC ↔ NFPA 79 overlap matrix

Below is a **UL 508A ↔ NEC ↔ NFPA 79 overlap matrix** you can drop into your **RAG-approved** library. It’s **topic-based** (safe + indexable) and uses **standard identifiers** (Article/Chapter/Supplement) without copying any copyrighted text.

Key “hard links” you’ll want for compliance tooling:

* **NEC 409 marking requires SCCR** and explicitly points to **UL 508A Supplement SB** as an approved method. ([Electrical License Renewal][1])
* **UL guidance emphasizes each panel needs SCCR** for machinery and multi-panel machines. ([UL Solutions][2])
* NFPA’s official publication page confirms NFPA 79 chapter structure (e.g., Ch.5 Disconnecting Means, Ch.8 Grounding/Bonding). ([NFPA Link][3])
* UL notes that UL 508A may not cover all machinery-panel requirements, and NFPA 79 may be needed. ([UL Solutions][4])

---

## 1) Overlap matrix (Markdown)

```md
# UL 508A ↔ NEC (NFPA 70) ↔ NFPA 79 Overlap Matrix (Topic-Based)

Legend:
- NEC = National Electrical Code (NFPA 70), Article-based
- NFPA 79 = Electrical Standard for Industrial Machinery, Chapter-based
- UL 508A = Industrial Control Panels, construction/testing + SCCR method (Supplement SB)

| Topic Area | NEC (NFPA 70) Anchor | NFPA 79 Anchor | UL 508A Anchor | Primary “Owner” (Typical) | Notes / Use in Tools |
|---|---|---|---|---|---|
| Scope boundary (panel vs machine vs facility wiring) | Art. 409 (panels), Art. 670 (machinery), general installation rules | Scope/Admin chapters (NFPA 79 applies starting at machine supply connection) | Scope & panel definition | NFPA 79 for machine, UL 508A for panel, NEC for installation | Use to decide: “Which standard drives this decision?” |
| Component listing/labeling + install per manufacturer instructions | Art. 110 (listing/labeling, installation suitability) | General requirements chapters | General construction requirements | NEC + UL | Build “evidence pack” rule: manuals, listings, markings |
| Disconnecting means / isolation for servicing | Disconnect rules depending on installation | Ch. 5 Disconnecting Means | Panel disconnect integration requirements | NFPA 79 for machine behavior, NEC for installation | Checklist generator: location, accessibility, labeling, LOTO readiness |
| Overcurrent protection (branch circuits / protection coordination) | Art. 240 (OCP), Art. 430 (motors), others as applicable | Ch. 6 Overcurrent Protection | Overcurrent protection requirements | NEC + UL 508A | Use for fuse/breaker selection rules; tie to SCCR strategy |
| Grounding and bonding | Art. 250 Grounding & Bonding | Ch. 8 Grounding & Bonding | Grounding/bonding requirements | NEC baseline; NFPA 79 machine specifics | Design guide: bonding jumpers, door bonding, PE routing |
| Wiring methods (routing, protection, separation) | Art. 300 (wiring methods), Art. 310 (conductors) | Ch. 16 Wiring Methods; Ch. 17 Cables/Flexible Cords | Wiring methods & conductors | NEC baseline + UL 508A inside panel; NFPA 79 inside machine | Separation rules: power vs control vs comms; mechanical protection |
| Control circuits & control functions (start/stop behavior) | Control circuit articles as applicable | Ch. 9 Control Circuits & Control Functions | Control circuit construction; device suitability | NFPA 79 for functional behavior | Put “behavioral rules” in NFPA 79 layer; hardware build rules in UL 508A |
| Emergency stop (concept + implementation expectations) | (Referenced indirectly via installation + equipment requirements) | Ch. 9 includes stop functions / e-stop concepts | Safety-related device integration (panel construction side) | NFPA 79 (behavior) | Keep e-stop “what it must do” in NFPA 79; “how it’s built in panel” cross-links to UL |
| Control equipment / panel construction (enclosures, layout, workmanship) | Art. 409 panel marking + installation rules | Ch. 11 Control Equipment (machine panels) | Core domain: panel construction/testing | UL 508A | UL is your “panel build bible”; NFPA 79 adds machinery-specific gaps :contentReference[oaicite:4]{index=4} |
| SCCR (short-circuit current rating) determination + labeling | Art. 409 marking requires SCCR; references UL 508A SB as approved method :contentReference[oaicite:5]{index=5} | Machinery SCCR concept used in machinery context (varies by edition) | Supplement SB = SCCR method | NEC requires marking; UL gives method | Standards Intelligence Tool should: (1) require SCCR label (NEC), (2) compute via SB (UL) |
| Marking & documentation (nameplates, wire labels, drawings) | Art. 409 marking + general rules | Ch. 19 Marking & Documentation | Marking & documentation requirements | All three overlap | Your “handover pack” generator lives here |
| Motors / motor controllers / drives | Art. 430 (motors) | Motors + associated equipment chapters | Motor controllers/drives suitability for panel | NEC for motor circuits; UL for panel construction | Drive integration rules cross-link to NFPA 79 machine protection concepts |
| Control power (transformers, PSUs, secondary protection) | General conductor/OCP + control circuit rules | Transformers & power supplies chapters | Power supply/transformer construction rules | NFPA 79 + UL 508A | Use for 24VDC architecture and secondary protection checklists |
| Multi-panel machines / overall machinery SCCR aggregation | Panel SCCR marking still required | Machine-level considerations | UL guidance: each panel SCCR matters for machine SCCR :contentReference[oaicite:6]{index=6} | System-level engineering | Retainer engine: require SCCR records per panel; compute machine SCCR basis |
```

**Why this matrix is “tool-grade”:**

* You can route every user question into a **Topic Area** → then pull the right “owner” standard.
* You can implement **conflict handling**: NFPA 79 may add requirements not fully covered by UL 508A for machinery panels. ([UL Solutions][4])

---

## 2) Same overlap matrix as YAML (for your rule engine / RAG index)

Save as:

```
rag/standards_intelligence/crosswalks/overlap_matrix/ul508a_nec_nfpa79_overlap.yaml
```

```yaml
overlap_matrix:
  id: "UL508A_NEC_NFPA79_OVERLAP"
  version: "0.1"
  status: "DRAFT"
  standards:
    nec:
      family: "NEC"
      id: "NFPA_70"
      edition: "2023"
    nfpa79:
      family: "NFPA"
      id: "NFPA_79"
      edition: "2024"
    ul508a:
      family: "UL"
      id: "UL_508A"
      edition: "2022"

  topics:
    - topic_id: "scope_boundary"
      name: "Scope boundary (panel vs machine vs facility wiring)"
      nec_anchors: ["Article 409", "Article 670", "Article 110 (general suitability)"]
      nfpa79_anchors: ["Scope/Admin chapters"]
      ul508a_anchors: ["Scope & panel definition"]
      typical_owner: ["NFPA 79 (machine)", "UL 508A (panel)", "NEC (installation)"]
      tool_notes:
        - "Use to decide which standard drives each design decision."
        - "Implement a router: question -> topic_id -> authoritative docs."

    - topic_id: "listing_labeling_instructions"
      name: "Listing/labeling + install per manufacturer instructions"
      nec_anchors: ["Article 110"]
      nfpa79_anchors: ["General requirements chapters"]
      ul508a_anchors: ["General construction requirements"]
      typical_owner: ["NEC + UL 508A"]
      tool_notes:
        - "Evidence pack: datasheets, listing marks, installation instructions."

    - topic_id: "disconnecting_means"
      name: "Disconnecting means / energy isolation for servicing"
      nec_anchors: ["Installation-dependent disconnect requirements"]
      nfpa79_anchors: ["Chapter 5 Disconnecting Means"]
      ul508a_anchors: ["Panel disconnect integration"]
      typical_owner: ["NFPA 79 (behavior) + NEC (installation)"]
      tool_notes:
        - "Commissioning checklist: accessibility, labeling, LOTO readiness."

    - topic_id: "overcurrent_protection"
      name: "Overcurrent protection"
      nec_anchors: ["Article 240", "Article 430 (motors)"]
      nfpa79_anchors: ["Chapter 6 Overcurrent Protection"]
      ul508a_anchors: ["Overcurrent protection requirements"]
      typical_owner: ["NEC + UL 508A"]
      tool_notes:
        - "Tie OCP selection to SCCR strategy."

    - topic_id: "grounding_bonding"
      name: "Grounding and bonding"
      nec_anchors: ["Article 250"]
      nfpa79_anchors: ["Chapter 8 Grounding and Bonding"]
      ul508a_anchors: ["Grounding and bonding requirements"]
      typical_owner: ["NEC baseline + NFPA 79 machine specifics"]
      tool_notes:
        - "Separate 'noise grounding' guidance from safety bonding rules."

    - topic_id: "wiring_methods_conductors"
      name: "Wiring methods / conductors (routing, protection, separation)"
      nec_anchors: ["Article 300", "Article 310"]
      nfpa79_anchors: ["Chapter 16 Wiring Methods", "Chapter 17 Cables/Flexible Cords"]
      ul508a_anchors: ["Wiring methods and conductors"]
      typical_owner: ["NEC baseline + UL 508A inside panel + NFPA 79 inside machine"]
      tool_notes:
        - "Enforce segregation rules: power vs control vs comms."

    - topic_id: "control_functions"
      name: "Control circuits & control functions (start/stop behavior)"
      nec_anchors: ["As applicable to control circuit classes"]
      nfpa79_anchors: ["Chapter 9 Control Circuits and Control Functions"]
      ul508a_anchors: ["Control circuit construction/device suitability"]
      typical_owner: ["NFPA 79 for behavior"]
      tool_notes:
        - "Behavioral requirements live in NFPA 79; hardware build rules in UL."

    - topic_id: "emergency_stop"
      name: "Emergency stop (concept + implementation expectations)"
      nec_anchors: ["Indirect via installation/equipment rules"]
      nfpa79_anchors: ["Chapter 9 (stop functions / e-stop concepts)"]
      ul508a_anchors: ["Panel integration aspects"]
      typical_owner: ["NFPA 79 (behavior)"]
      tool_notes:
        - "Keep 'what it must do' in NFPA 79; 'how built' cross-link to UL."

    - topic_id: "panel_construction"
      name: "Control equipment / panel construction"
      nec_anchors: ["Article 409 (marking/installation implications)"]
      nfpa79_anchors: ["Chapter 11 Control Equipment"]
      ul508a_anchors: ["Core construction/testing requirements"]
      typical_owner: ["UL 508A"]
      tool_notes:
        - "UL guidance notes NFPA 79 may be needed for machinery-specific gaps."

    - topic_id: "sccr"
      name: "SCCR determination + labeling"
      nec_anchors: ["Article 409 (SCCR marking)"]
      nfpa79_anchors: ["Machinery short-circuit considerations (edition dependent)"]
      ul508a_anchors: ["Supplement SB (SCCR method)"]
      typical_owner: ["NEC requires marking; UL provides method"]
      tool_notes:
        - "Workflow: require SCCR label -> compute via SB -> store evidence."
      citations:
        - "NEC 409 SCCR marking references UL 508A SB (approved method)"
        - "UL: each panel SCCR needed for machine SCCR"

    - topic_id: "marking_documentation"
      name: "Marking & documentation"
      nec_anchors: ["Article 409 marking", "General labeling practices (as applicable)"]
      nfpa79_anchors: ["Chapter 19 Marking and Documentation"]
      ul508a_anchors: ["Marking/documentation requirements"]
      typical_owner: ["All three overlap"]
      tool_notes:
        - "Handover pack generator: labels, drawings, SCCR label, revisions."

    - topic_id: "motors_drives"
      name: "Motors / motor controllers / drives"
      nec_anchors: ["Article 430"]
      nfpa79_anchors: ["Motors and associated equipment chapter"]
      ul508a_anchors: ["Motor controller/drive construction suitability (panel side)"]
      typical_owner: ["NEC motor circuits + UL panel construction"]
      tool_notes:
        - "Cross-link drive protection and fault handling to commissioning tests."

    - topic_id: "control_power"
      name: "Control power (transformers, PSUs, secondary protection)"
      nec_anchors: ["General OCP/conductor rules + control circuit rules as applicable"]
      nfpa79_anchors: ["Transformers and power supplies chapter"]
      ul508a_anchors: ["Transformer/PSU construction rules"]
      typical_owner: ["NFPA 79 + UL 508A"]
      tool_notes:
        - "Add checklist: secondary protection, 24VDC architecture, grounding."

    - topic_id: "multi_panel_machines"
      name: "Multi-panel machines / SCCR aggregation basis"
      nec_anchors: ["Panel SCCR marking remains required"]
      nfpa79_anchors: ["System-level machine considerations"]
      ul508a_anchors: ["UL guidance: each panel SCCR required for machine SCCR basis"]
      typical_owner: ["System-level engineering"]
      tool_notes:
        - "Retainer workflow: keep SCCR record per panel; compute machine basis."
      citations:
        - "UL SCCR guidance for multiple panels"
```

Citations backing the most important overlap claims:

* NEC 409 SCCR marking + UL 508A SB called out as approved method. ([Electrical License Renewal][1])
* UL: each panel used to control a machine should have SCCR; needed for machine SCCR basis. ([UL Solutions][2])
* NFPA 79 chapter anchors (e.g., Disconnecting Means, Grounding and Bonding) confirmed on NFPA publication page. ([NFPA Link][3])
* UL: NFPA 79 may be needed because UL 508A may not cover all machinery-panel requirements. ([UL Solutions][4])

---

If you want the matrix to become **even more indexable**, the next step is:
**generate per-topic “overlap notes” MD files** (one per `topic_id`) that include:

* decision rules (which standard wins)
* evidence required
* checklist items
* cross-links into your NEC/NFPA79/UL508A template files

[1]: https://www.electricallicenserenewal.com/Electrical-Continuing-Education-Courses/NEC-Content.php?sectionID=442&utm_source=chatgpt.com "409.110 Industrial Control Panels. Marking."
[2]: https://www.ul.com/resources/determining-short-circuit-current-rating-sccr-machinery?utm_source=chatgpt.com "Determining Short-Circuit Current Rating (SCCR) for ..."
[3]: https://link.nfpa.org/all-publications/79/2021?utm_source=chatgpt.com "NFPA 79 - Electrical Standard for Industrial Machinery"
[4]: https://www.ul.com/resources/machine-supply-circuit-and-disconnecting-means?utm_source=chatgpt.com "Machine Supply Circuit and Disconnecting Means"

Below are **per-topic “overlap notes” Markdown files**—**one file per `topic_id`**—designed to live in:

```
rag/standards_intelligence/crosswalks/overlap_notes/
```

Each file includes:

* **Decision rules** (which standard wins, and when)
* **Evidence required** (what to collect/store)
* **Checklist items** (actionable)
* **Cross-links** into your **NEC / NFPA 79 / UL 508A** templates

All content is **copyright-clean**, **RAG-approved**, and **audit-ready**.

---

## 1) `overlap__scope_boundary.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: scope_boundary
-->

# Overlap Note — Scope Boundary (Panel vs Machine vs Facility)

## Decision rules (who wins)
- **Machine behavior & safety intent** → NFPA 79
- **Panel construction & testing** → UL 508A
- **Installation, inspection, enforcement** → NEC
- If a requirement conflicts: follow **jurisdiction/AHJ** and **customer spec**; document the choice.

## Evidence required
- Project scope statement
- One-line diagram showing machine supply boundary
- Panel definition statement (what is/isn’t the panel)
- Jurisdiction/AHJ notes

## Checklist
- [ ] Identify machine supply connection point
- [ ] Declare panel boundary explicitly
- [ ] Record governing standard per decision area
- [ ] Capture AHJ/customer overrides

## Cross-links
- NEC: `NEC_2023__Art409__industrial_control_panels.md`
- NEC: `NEC_2023__Art670__industrial_machinery.md` (if applicable)
- NFPA 79: `NFPA79_2024__Ch01__administration.md`
- UL 508A: `UL508A_2022__scope_and_application.md`
```

---

## 2) `overlap__listing_labeling_instructions.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: listing_labeling_instructions
-->

# Overlap Note — Listing, Labeling, Installation Instructions

## Decision rules
- **Component suitability & installation per listing** → NEC + UL
- **Machine context implications** → NFPA 79
- If manufacturer instructions exist, **they are mandatory**; document compliance.

## Evidence required
- Datasheets/manuals with revision IDs
- Listing/marking photos
- Installation instruction excerpts (paraphrased references)
- Compliance sign-off

## Checklist
- [ ] Verify listing/label for each component
- [ ] Follow manufacturer instructions
- [ ] Retain evidence (manual rev)
- [ ] Note deviations with rationale (if any)

## Cross-links
- NEC: `NEC_2023__Art110__requirements_for_electrical_installations.md`
- NFPA 79: `NFPA79_2024__Ch03__general_requirements.md`
- UL 508A: `UL508A_2022__general_construction_requirements.md`
```

---

## 3) `overlap__disconnecting_means.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: disconnecting_means
-->

# Overlap Note — Disconnecting Means / Energy Isolation

## Decision rules
- **Functional behavior, LOTO intent** → NFPA 79
- **Physical installation & location** → NEC
- **Panel integration details** → UL 508A

## Evidence required
- Disconnect location photos
- Label text/photos
- LOTO procedure reference
- Schematic showing isolation

## Checklist
- [ ] Disconnect accessible and clearly labeled
- [ ] Door interlock behavior documented
- [ ] LOTO compatible
- [ ] Isolation covers all required energy

## Cross-links
- NFPA 79: `NFPA79_2024__Ch05__disconnecting_means.md`
- NEC: `NEC_2023__Art110__requirements_for_electrical_installations.md`
- UL 508A: `UL508A_2022__general_construction_requirements.md`
```

---

## 4) `overlap__overcurrent_protection.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: overcurrent_protection
-->

# Overlap Note — Overcurrent Protection

## Decision rules
- **Protection sizing & coordination** → NEC
- **Panel construction limits** → UL 508A
- **Machine-level intent** → NFPA 79

## Evidence required
- OCP device specs
- Coordination rationale
- Short-circuit data inputs

## Checklist
- [ ] Branch circuits protected correctly
- [ ] Coordination supports SCCR
- [ ] Motor circuits handled per motor rules

## Cross-links
- NEC: `NEC_2023__Art240__overcurrent_protection.md`
- NEC: `NEC_2023__Art430__motors_motor_circuits_and_controllers.md`
- NFPA 79: `NFPA79_2024__Ch06__overcurrent_protection.md`
- UL 508A: `UL508A_2022__overcurrent_protection.md`
```

---

## 5) `overlap__grounding_bonding.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: grounding_bonding
-->

# Overlap Note — Grounding and Bonding

## Decision rules
- **Safety grounding baseline** → NEC
- **Machine bonding details** → NFPA 79
- **Panel workmanship** → UL 508A

## Evidence required
- Grounding schematic
- Bonding jumpers photos
- Continuity test results

## Checklist
- [ ] PE conductors sized and routed
- [ ] Doors/subpanels bonded
- [ ] No misuse of “noise ground” as safety ground

## Cross-links
- NEC: `NEC_2023__Art250__grounding_and_bonding.md`
- NFPA 79: `NFPA79_2024__Ch08__grounding_and_bonding.md`
- UL 508A: `UL508A_2022__grounding_and_bonding.md`
```

---

## 6) `overlap__wiring_methods_conductors.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: wiring_methods_conductors
-->

# Overlap Note — Wiring Methods & Conductors

## Decision rules
- **General wiring rules** → NEC
- **Inside panel** → UL 508A
- **Inside machine / moving parts** → NFPA 79

## Evidence required
- Wire types/specs
- Routing photos
- Separation diagram

## Checklist
- [ ] Power/control/comms separated
- [ ] Mechanical protection provided
- [ ] Conductors sized and rated

## Cross-links
- NEC: `NEC_2023__Art300__general_wiring_methods.md`
- NEC: `NEC_2023__Art310__conductors_for_general_wiring.md`
- NFPA 79: `NFPA79_2024__Ch16__wiring_methods.md`
- UL 508A: `UL508A_2022__wiring_methods_and_conductors.md`
```

---

## 7) `overlap__control_functions.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: control_functions
-->

# Overlap Note — Control Circuits & Control Functions

## Decision rules
- **Behavior (start/stop, stop categories)** → NFPA 79
- **Hardware build** → UL 508A
- **Power-limited classes** → NEC (as applicable)

## Evidence required
- Control philosophy description
- State diagrams (if used)
- IO list mapping

## Checklist
- [ ] Start/stop behavior documented
- [ ] Safety vs standard control separated
- [ ] Control circuits properly classified

## Cross-links
- NFPA 79: `NFPA79_2024__Ch09__control_circuits_and_control_functions.md`
- UL 508A: `UL508A_2022__control_circuits_and_devices.md`
- NEC: `NEC_2023__Art725__class_1_2_3_control_circuits.md`
```

---

## 8) `overlap__emergency_stop.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: emergency_stop
-->

# Overlap Note — Emergency Stop

## Decision rules
- **What the E-stop must do** → NFPA 79
- **How it’s built into the panel** → UL 508A
- NEC applies indirectly via installation suitability.

## Evidence required
- E-stop behavior description
- Circuit diagram
- Functional test results

## Checklist
- [ ] E-stop category defined
- [ ] Reset behavior documented
- [ ] Test evidence recorded

## Cross-links
- NFPA 79: `NFPA79_2024__Ch09__control_circuits_and_control_functions.md`
- UL 508A: `UL508A_2022__control_circuits_and_devices.md`
```

---

## 9) `overlap__panel_construction.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: panel_construction
-->

# Overlap Note — Panel Construction

## Decision rules
- **Primary authority** → UL 508A
- NFPA 79 fills machinery gaps; NEC enforces installation.

## Evidence required
- Panel layout drawings
- Enclosure rating
- Workmanship photos

## Checklist
- [ ] Components mounted securely
- [ ] Spacing/clearance met
- [ ] Enclosure appropriate for environment

## Cross-links
- UL 508A: `UL508A_2022__general_construction_requirements.md`
- NFPA 79: `NFPA79_2024__Ch11__control_equipment.md`
- NEC: `NEC_2023__Art409__industrial_control_panels.md`
```

---

## 10) `overlap__sccr.md`  **(Critical)**

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: sccr
-->

# Overlap Note — SCCR (Short-Circuit Current Rating)

## Decision rules
- **SCCR marking required** → NEC
- **SCCR calculation method** → UL 508A Supplement SB
- NFPA 79 uses SCCR in machinery context.

## Evidence required
- Available fault current
- Component SCCR ratings
- Calculation worksheet
- Panel SCCR label

## Checklist
- [ ] Fault current known
- [ ] Weakest link identified
- [ ] SCCR label applied and documented

## Cross-links
- NEC: `NEC_2023__Art409__industrial_control_panels.md`
- UL 508A: `UL508A_2022__sccr_short_circuit_current_rating.md`
```

---

## 11) `overlap__marking_documentation.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: marking_documentation
-->

# Overlap Note — Marking & Documentation

## Decision rules
- All three standards overlap; **most stringent applies**.
- UL drives panel nameplates; NFPA drives machine docs; NEC enforces marking presence.

## Evidence required
- Nameplate photos
- Wire labels
- Schematics/manuals

## Checklist
- [ ] Panel nameplate complete
- [ ] Wire/device labels consistent
- [ ] Documentation retained for audit

## Cross-links
- NEC: `NEC_2023__Art409__industrial_control_panels.md`
- NFPA 79: `NFPA79_2024__Ch19__marking_and_documentation.md`
- UL 508A: `UL508A_2022__marking_and_documentation.md`
```

---

## 12) `overlap__motors_drives.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: motors_drives
-->

# Overlap Note — Motors, Controllers, Drives

## Decision rules
- **Motor circuit rules** → NEC
- **Machine protection intent** → NFPA 79
- **Panel suitability** → UL 508A

## Evidence required
- Motor FLA data
- Drive/controller specs
- Protection settings

## Checklist
- [ ] Motor protection correct
- [ ] Drive integration documented
- [ ] Coordination with SCCR verified

## Cross-links
- NEC: `NEC_2023__Art430__motors_motor_circuits_and_controllers.md`
- NFPA 79: `NFPA79_2024__Ch12__motors_and_associated_equipment.md`
- UL 508A: `UL508A_2022__motor_controllers_and_drives.md`
```

---

## 13) `overlap__control_power.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: control_power
-->

# Overlap Note — Control Power (Transformers / PSUs)

## Decision rules
- **Control power architecture** → NFPA 79
- **Construction & protection** → UL 508A
- **Conductor/OCP rules** → NEC

## Evidence required
- Transformer/PSU specs
- Secondary protection details
- Grounding scheme

## Checklist
- [ ] Secondary protected
- [ ] Voltage levels documented
- [ ] Grounding of secondary addressed

## Cross-links
- NFPA 79: `NFPA79_2024__Ch15__transformers_and_power_supplies.md`
- UL 508A: `UL508A_2022__transformers_and_power_supplies.md`
```

---

## 14) `overlap__multi_panel_machines.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: multi_panel_machines
-->

# Overlap Note — Multi-Panel Machines / SCCR Aggregation

## Decision rules
- **Each panel needs SCCR** → NEC + UL
- **Machine-level view** → NFPA 79 / system engineering

## Evidence required
- SCCR per panel
- Interconnection diagram
- Machine SCCR rationale

## Checklist
- [ ] SCCR recorded per panel
- [ ] Inter-panel connections documented
- [ ] Machine SCCR basis recorded

## Cross-links
- NEC: `NEC_2023__Art409__industrial_control_panels.md`
- UL 508A: `UL508A_2022__sccr_short_circuit_current_rating.md`
```

---

### What this gives you (strategically)

* A **decision router** your Standards Intelligence Tool can query
* Clear **“which standard wins” logic**
* Explicit **evidence requirements** (audit-proof)
* Drop-in links to your NEC / NFPA 79 / UL 508A templates
* Clean separation between **rules**, **proof**, and **execution**

If you want next, I can:

* Auto-generate the `_index.yaml` entries for these overlap notes
* Add **conflict-resolution rules** (what to do when standards disagree)
* Build a **wizard flow** that uses these notes to guide engineers step-by-step

Here’s a **NFPA 79 ↔ IEC 60204-1 clause overlap matrix** you can drop into your `rag/standards_intelligence/crosswalks/overlap_matrix/` folder.

It’s **topic-based** (best for routing), but also includes the **direct chapter↔clause anchors** so your indexer can jump straight to the right file.

Sources confirm the relevant NFPA 79 chapter anchors and IEC 60204-1 clause anchors used below. ([NFPA Link][1])

---

## NFPA 79 ↔ IEC 60204-1 Overlap Matrix (Markdown)

```md
# NFPA 79 ↔ IEC 60204-1 Overlap Matrix (Topic-Based)

Legend
- NFPA 79: Electrical Standard for Industrial Machinery (US)
- IEC 60204-1: Electrical Equipment of Machines (International)
- “Owner” = which standard usually leads the engineering decision when both apply

| Topic Area | NFPA 79 Anchor (Chapter) | IEC 60204-1 Anchor (Clause) | Typical Owner | Practical Notes (Tool Use) |
|---|---|---|---|---|
| Scope boundary (where machine electrical equipment begins) | Ch. 1 Administration / applicability | Clause 1 Scope + supply boundary concept | Tie | Use this to define “machine supply connection point” and what’s in-scope for machine electrical equipment. IEC explicitly frames machine electrical equipment starting at the point of supply connection. :contentReference[oaicite:1]{index=1} |
| Definitions / terminology | Ch. 2 Definitions | Clause 3 Terms and definitions | Tie | Build a shared glossary + alias map (same concept, different term). |
| General requirements / overall principles | Ch. 3 General requirements | Clause 4 General requirements | Tie | Route “baseline rules” questions here before diving into specifics. |
| Incoming supply / disconnecting means / isolation | Ch. 5 Disconnecting means | Clause 5 Incoming supply / disconnecting & switching off devices | Tie (jurisdiction decides) | This is your primary mapping: NFPA 79 Ch.5 ↔ IEC Clause 5. :contentReference[oaicite:2]{index=2} |
| Overcurrent protection / protection of equipment | Ch. 7 Protection of equipment (and Ch. 6 overcurrent in many editions) | Clause 7 Protection of equipment | Tie | Use for device protection strategy, coordination, and “what protection is required where.” |
| Protection against electric shock | Ch. 6 Electrical hazards (edition dependent naming) / shock protection concepts | Clause 6 Protection against electric shock | IEC lead internationally | Route “touch-safe, barriers, protective measures” here. |
| Grounding & bonding / equipotential bonding | Ch. 8 Grounding and bonding | Clause 8 Equipotential bonding | Tie | NFPA 79 Ch.8 ↔ IEC Clause 8 is the direct pair. :contentReference[oaicite:3]{index=3} |
| Control circuits & control functions (start/stop, stop categories, control behavior) | Ch. 9 Control circuits and control functions | Clause 9 Control circuits and control functions | Tie | Put behavior requirements here; keep panel-build details elsewhere. |
| Operator interface / control devices | Ch. 10 Operator interface and control devices | Clause 10 Operator interface | Tie | Route anything “HMI, pushbuttons, indicators, operator controls.” |
| Control equipment / enclosures / panel equipment used on machines | Ch. 11 Control equipment | Clause 11 Control equipment | Tie | Best place to capture “machine panel” requirements beyond a standalone industrial control panel standard. |
| Motors and drives | Ch. 12 Motors and associated equipment | Clause 12 Motors and drives | Tie | Route “VFDs, motor protection, motor control integration.” |
| Accessories and lighting | Ch. 13 Appliances/accessories + Ch. 14 Lighting | Clause 13 Accessories and lighting | IEC lead for combined topic | IEC combines these; NFPA splits into two chapters. Keep a cross-link note. |
| Marking & documentation | Ch. 19 Marking and documentation | Clause 14 Marking and documentation | Tie | Build your “handover pack” and labeling rules here. |
| Verification / tests | Commissioning/verification concepts (varies by edition; verification is explicit in later chapters/sections) | Clause 15 Verification | IEC lead | IEC has a dedicated Verification clause—great for test checklists and evidence requirements. :contentReference[oaicite:4]{index=4} |
```

---

## Recommended file cross-links (so your RAG can jump cleanly)

Use these as canonical cross-links between the chapter/clause templates you already generated:

* NFPA 79 Ch.5 ↔ IEC Clause 5
  `NFPA79_2024__Ch05__disconnecting_means.md` ↔ `IEC60204_1_2016A1__Clause05__incoming_supply.md` ([Gt-Engineering][2])

* NFPA 79 Ch.8 ↔ IEC Clause 8
  `NFPA79_2024__Ch08__grounding_and_bonding.md` ↔ `IEC60204_1_2016A1__Clause08__equipotential_bonding.md` ([NFPA Link][1])

* NFPA 79 Ch.9 ↔ IEC Clause 9
  `NFPA79_2024__Ch09__control_circuits_and_control_functions.md` ↔ `IEC60204_1_2016A1__Clause09__control_circuits_and_functions.md` ([NFPA Link][1])

* NFPA 79 Ch.19 ↔ IEC Clause 14
  `NFPA79_2024__Ch19__marking_and_documentation.md` ↔ `IEC60204_1_2016A1__Clause16__marking_and_warning_signs.md` ([NFPA Link][1])

* IEC Scope boundary note (important for your “scope router”)
  `IEC60204_1_2016A1__Clause01__scope.md` should explicitly include: “machine electrical equipment begins at the point of supply connection” as an **approved paraphrase note**. ([Certifico][3])

---

[1]: https://link.nfpa.org/all-publications/79/2021?utm_source=chatgpt.com "NFPA 79 - Electrical Standard for Industrial Machinery"
[2]: https://www.gt-engineering.it/en/technical-standards/ul-and-nfpa-standards/industrial-machinery/nfpa-79-2021-chapter-5-disconnecting-means/?utm_source=chatgpt.com "NFPA 79 - 2021, Chapter 5: Disconnecting Means"
[3]: https://www.certifico.com/component/attachments/download/3856?utm_source=chatgpt.com "IEC 60204-1"

Below are **per-topic overlap notes (Markdown files)** for **NFPA 79 ↔ IEC 60204-1**, formatted exactly like your earlier overlap notes and ready to drop into:

```
rag/standards_intelligence/crosswalks/overlap_notes/
```

Each file includes:

* **Decision rules** (which standard leads, and when)
* **Evidence required**
* **Checklist items**
* **Cross-links** to your existing **NFPA 79** and **IEC 60204-1** clause templates

All content is **paraphrased**, **copyright-clean**, and **RAG-approved**.

---

## 1) `overlap_nfpa79_iec60204__scope_boundary.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC_ID: scope_boundary
-->

# Overlap — Scope Boundary (Machine Electrical Equipment)

## Decision rules (who leads)
- **US / AHJ-driven machinery** → NFPA 79
- **EU / CE-marked machinery** → IEC 60204-1
- When both apply, define a **single machine supply connection point** and document which clauses govern upstream vs downstream.

## Evidence required
- Machine scope statement
- One-line diagram with machine supply boundary
- Jurisdiction/customer requirement record

## Checklist
- [ ] Machine supply connection point defined
- [ ] In-scope vs out-of-scope equipment listed
- [ ] Governing standard recorded per subsystem

## Cross-links
- NFPA 79: `NFPA79_2024__Ch01__administration.md`
- IEC 60204-1: `IEC60204_1_2016A1__Clause01__scope.md`
```

---

## 2) `overlap_nfpa79_iec60204__definitions.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC_ID: definitions
-->

# Overlap — Definitions & Terminology

## Decision rules
- Use the **active jurisdiction’s definitions** as authoritative.
- Maintain an **alias map** where terms differ but intent is equivalent.

## Evidence required
- Approved glossary
- Notes on equivalent terms (NFPA ↔ IEC)

## Checklist
- [ ] Critical terms mapped across standards
- [ ] Ambiguous terms clarified in project glossary

## Cross-links
- NFPA 79: `NFPA79_2024__Ch02__definitions.md`
- IEC 60204-1: `IEC60204_1_2016A1__Clause03__terms_and_definitions.md`
```

---

## 3) `overlap_nfpa79_iec60204__general_requirements.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC_ID: general_requirements
-->

# Overlap — General Requirements / Principles

## Decision rules
- Both standards are **functionally equivalent** at principle level.
- Follow the **more explicit requirement** where wording differs.

## Evidence required
- Design philosophy summary
- Risk assumptions

## Checklist
- [ ] General safety principles documented
- [ ] Deviations justified and recorded

## Cross-links
- NFPA 79: `NFPA79_2024__Ch03__general_requirements.md`
- IEC 60204-1: `IEC60204_1_2016A1__Clause04__general_requirements.md`
```

---

## 4) `overlap_nfpa79_iec60204__incoming_supply_disconnect.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC_ID: incoming_supply_disconnect
-->

# Overlap — Incoming Supply / Disconnecting Means

## Decision rules
- **Functional isolation intent** → both standards
- **Implementation details** follow jurisdiction (NFPA for US, IEC for EU)

## Evidence required
- Disconnect device specs
- Location photos
- Isolation description

## Checklist
- [ ] Supply disconnect provided
- [ ] Accessible and clearly identified
- [ ] Covers all required energy sources

## Cross-links
- NFPA 79: `NFPA79_2024__Ch05__disconnecting_means.md`
- IEC 60204-1: `IEC60204_1_2016A1__Clause05__incoming_supply.md`
```

---

## 5) `overlap_nfpa79_iec60204__electric_shock_protection.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC_ID: electric_shock_protection
-->

# Overlap — Protection Against Electric Shock

## Decision rules
- IEC is typically **more prescriptive** internationally.
- NFPA aligns conceptually; follow stricter requirement when combined.

## Evidence required
- Barrier/insulation descriptions
- Voltage level documentation

## Checklist
- [ ] Live parts protected
- [ ] Touch-safe design verified
- [ ] Control voltages justified

## Cross-links
- NFPA 79: `NFPA79_2024__Ch07__protection_against_electric_shock.md`
- IEC 60204-1: `IEC60204_1_2016A1__Clause06__protection_against_electric_shock.md`
```

---

## 6) `overlap_nfpa79_iec60204__equipment_protection.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC_ID: equipment_protection
-->

# Overlap — Protection of Equipment (Overcurrent / Environmental)

## Decision rules
- Overcurrent philosophy is aligned.
- Use local installation rules where referenced externally.

## Evidence required
- Protection device selection rationale
- Environmental assumptions

## Checklist
- [ ] Equipment protected against overload/short-circuit
- [ ] Environmental protection addressed

## Cross-links
- NFPA 79: `NFPA79_2024__Ch06__overcurrent_protection.md`
- IEC 60204-1: `IEC60204_1_2016A1__Clause07__protection_of_equipment.md`
```

---

## 7) `overlap_nfpa79_iec60204__grounding_bonding.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC_ID: grounding_bonding
-->

# Overlap — Grounding & Bonding / Equipotential Bonding

## Decision rules
- Concepts are **direct equivalents**.
- Terminology differs; intent is the same.

## Evidence required
- Bonding diagram
- Continuity test results

## Checklist
- [ ] Exposed conductive parts bonded
- [ ] PE continuity verified
- [ ] No misuse of functional grounds

## Cross-links
- NFPA 79: `NFPA79_2024__Ch08__grounding_and_bonding.md`
- IEC 60204-1: `IEC60204_1_2016A1__Clause08__equipotential_bonding.md`
```

---

## 8) `overlap_nfpa79_iec60204__control_functions.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC_ID: control_functions
-->

# Overlap — Control Circuits & Control Functions

## Decision rules
- Behavioral expectations are **equivalent**.
- Align stop/start logic to the **most restrictive interpretation**.

## Evidence required
- Control philosophy narrative
- I/O mapping

## Checklist
- [ ] Start/stop behavior defined
- [ ] Emergency stop logic documented
- [ ] Safety vs standard control separated

## Cross-links
- NFPA 79: `NFPA79_2024__Ch09__control_circuits_and_control_functions.md`
- IEC 60204-1: `IEC60204_1_2016A1__Clause09__control_circuits_and_functions.md`
```

---

## 9) `overlap_nfpa79_iec60204__operator_interface.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC_ID: operator_interface
-->

# Overlap — Operator Interface & Control Devices

## Decision rules
- Both standards align; IEC often more explicit on ergonomics.
- Use customer/market expectation where stricter.

## Evidence required
- Control device list
- Ergonomic placement notes

## Checklist
- [ ] Controls clearly identified
- [ ] Indicators unambiguous
- [ ] Ergonomic access verified

## Cross-links
- NFPA 79: `NFPA79_2024__Ch10__operator_interface_devices.md`
- IEC 60204-1: `IEC60204_1_2016A1__Clause10__operator_interface.md`
```

---

## 10) `overlap_nfpa79_iec60204__control_equipment.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC_ID: control_equipment
-->

# Overlap — Control Equipment / Enclosures

## Decision rules
- Requirements are aligned in intent.
- Construction details may differ by market norms.

## Evidence required
- Enclosure rating
- Layout drawings

## Checklist
- [ ] Equipment suitable for environment
- [ ] Access and serviceability addressed

## Cross-links
- NFPA 79: `NFPA79_2024__Ch11__control_equipment.md`
- IEC 60204-1: `IEC60204_1_2016A1__Clause11__controlgear.md`
```

---

## 11) `overlap_nfpa79_iec60204__motors_drives.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC_ID: motors_drives
-->

# Overlap — Motors and Drives

## Decision rules
- Protection and integration philosophy aligned.
- Apply local motor rules where referenced externally.

## Evidence required
- Motor data
- Drive configuration notes

## Checklist
- [ ] Motor protection verified
- [ ] Drive behavior documented

## Cross-links
- NFPA 79: `NFPA79_2024__Ch12__motors_and_associated_equipment.md`
- IEC 60204-1: `IEC60204_1_2016A1__Clause14__electric_motors.md`
```

---

## 12) `overlap_nfpa79_iec60204__accessories_lighting.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC_ID: accessories_lighting
-->

# Overlap — Accessories & Lighting

## Decision rules
- IEC combines accessories and lighting; NFPA splits them.
- Ensure **both topics are covered** regardless of structure.

## Evidence required
- Accessory list
- Lighting design notes

## Checklist
- [ ] Machine lighting adequate
- [ ] Accessories safely integrated

## Cross-links
- NFPA 79: `NFPA79_2024__Ch13__appliances_and_accessories.md`
- NFPA 79: `NFPA79_2024__Ch14__lighting.md`
- IEC 60204-1: `IEC60204_1_2016A1__Clause15__socket_outlets_and_lighting.md`
```

---

## 13) `overlap_nfpa79_iec60204__marking_documentation.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC_ID: marking_documentation
-->

# Overlap — Marking & Documentation

## Decision rules
- Follow **most stringent labeling/documentation requirement**.
- Both standards strongly aligned.

## Evidence required
- Labels
- Schematics/manuals

## Checklist
- [ ] Equipment labeled
- [ ] Documentation complete and retained

## Cross-links
- NFPA 79: `NFPA79_2024__Ch19__marking_and_documentation.md`
- IEC 60204-1: `IEC60204_1_2016A1__Clause16__marking_and_warning_signs.md`
```

---

## 14) `overlap_nfpa79_iec60204__verification.md`

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC_ID: verification
-->

# Overlap — Verification & Testing

## Decision rules
- IEC has **explicit verification clause**.
- NFPA verification concepts exist but are less centralized.

## Evidence required
- Test records
- Inspection results

## Checklist
- [ ] Electrical tests performed
- [ ] Results recorded
- [ ] Nonconformities resolved

## Cross-links
- NFPA 79: `NFPA79_2024__Ch20__system_integration.md`
- IEC 60204-1: `IEC60204_1_2016A1__Clause18__verification.md`
```

---

### What you now have

* A **complete NFPA 79 ↔ IEC 60204-1 overlap note set**
* Clear **decision routing** for US vs EU builds
* Evidence + checklist hooks for audits
* Direct links into your clause templates

**Recommended next step:**
Generate a **US ↔ EU machine compliance wizard** that consumes these overlap notes and outputs “what changes” per market.

