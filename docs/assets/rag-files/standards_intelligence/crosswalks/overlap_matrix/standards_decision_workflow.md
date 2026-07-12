Below is a **US ↔ EU machine compliance wizard** (offline-first) that **consumes your overlap notes** and outputs **“what changes”** per market.

You’ll get:

1. A **wizard spec** (`.md`) for humans + AI
2. A **YAML decision engine schema** your future tool can execute
3. A **generated output template** (`delta report`) your tool will produce
4. Exact **links to the overlap notes** you already created (NFPA79 ↔ IEC60204)

---

# 1) Wizard spec (Markdown)

Save as:

```
rag/design_framework/us_eu_compliance_wizard/US_EU_Machine_Compliance_Wizard.md
```

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

WIZARD_ID: US_EU_MACHINE_COMPLIANCE
INPUTS: project_profile.yaml
OUTPUTS: us_eu_delta_report.md
-->

# US ↔ EU Machine Compliance Wizard (NFPA 79 ↔ IEC 60204-1)

## Purpose
Given a machine profile, output:
- What standards apply (US vs EU baseline)
- What changes in design, documentation, verification
- Evidence/checklist deltas required for the target market

## Wizard Inputs (minimum)
- Market target: US_ONLY | EU_ONLY | BOTH
- Machine type: conveyor | robot_cell | packaging | process_skid | custom
- Supply: voltage, phases, frequency, short-circuit assumptions
- Control system: PLC type, safety PLC yes/no, e-stops count, safety functions list
- Environment: indoor/outdoor, washdown, hazardous (yes/no)
- Interfaces: field wiring method, network types, remote I/O, drives count
- Documentation maturity: concept | design | build | commission | ops

## Decision Engine (high level)
For each Topic ID:
1) Load the overlap note file for the topic
2) Determine “Owner” standard based on Market target
3) Produce: (a) required changes (b) evidence (c) checklist items (d) file cross-links

## Topics Covered (consumes overlap notes)
- scope_boundary
- definitions
- general_requirements
- incoming_supply_disconnect
- electric_shock_protection
- equipment_protection
- grounding_bonding
- control_functions
- operator_interface
- control_equipment
- motors_drives
- accessories_lighting
- marking_documentation
- verification

## Output Rules
- Never quote standards text
- Always produce:
  - Delta summary (US → EU and/or EU → US)
  - Required evidence pack
  - Commissioning/verification delta checklist
  - Cross-links to relevant chapter/clause templates and overlap notes
```

---

# 2) YAML decision engine (consumes overlap notes)

Save as:

```
rag/design_framework/us_eu_compliance_wizard/us_eu_wizard_rules.yaml
```

```yaml
wizard:
  id: US_EU_MACHINE_COMPLIANCE
  version: "0.1"
  status: DRAFT

  inputs_schema:
    market_target: ["US_ONLY", "EU_ONLY", "BOTH"]
    machine_type: ["conveyor", "robot_cell", "packaging", "process_skid", "custom"]
    supply:
      voltage_v: "number"
      phases: ["1", "3"]
      frequency_hz: "number"
      available_fault_current_ka: "number|null"
    environment:
      location: ["indoor", "outdoor", "washdown"]
      hazardous_area: ["no", "yes_unknown", "yes_confirmed"]
    control_system:
      plc: "string"
      safety_plc: ["no", "yes"]
      safety_functions: ["list<string>"]
      estop_count: "number"
      drives_count: "number"
      networks: ["list<string>"]
    doc_stage: ["concept", "design", "build", "commission", "ops"]

  overlap_notes:
    base_path: "rag/standards_intelligence/crosswalks/overlap_notes/"
    topics:
      - topic_id: scope_boundary
        note_file: "overlap_nfpa79_iec60204__scope_boundary.md"
        anchors:
          us: ["NFPA79_2024__Ch01__administration.md"]
          eu: ["IEC60204_1_2016A1__Clause01__scope.md"]

      - topic_id: definitions
        note_file: "overlap_nfpa79_iec60204__definitions.md"
        anchors:
          us: ["NFPA79_2024__Ch02__definitions.md"]
          eu: ["IEC60204_1_2016A1__Clause03__terms_and_definitions.md"]

      - topic_id: general_requirements
        note_file: "overlap_nfpa79_iec60204__general_requirements.md"
        anchors:
          us: ["NFPA79_2024__Ch03__general_requirements.md"]
          eu: ["IEC60204_1_2016A1__Clause04__general_requirements.md"]

      - topic_id: incoming_supply_disconnect
        note_file: "overlap_nfpa79_iec60204__incoming_supply_disconnect.md"
        anchors:
          us: ["NFPA79_2024__Ch05__disconnecting_means.md"]
          eu: ["IEC60204_1_2016A1__Clause05__incoming_supply.md"]

      - topic_id: electric_shock_protection
        note_file: "overlap_nfpa79_iec60204__electric_shock_protection.md"
        anchors:
          us: ["NFPA79_2024__Ch07__protection_against_electric_shock.md"]
          eu: ["IEC60204_1_2016A1__Clause06__protection_against_electric_shock.md"]

      - topic_id: equipment_protection
        note_file: "overlap_nfpa79_iec60204__equipment_protection.md"
        anchors:
          us: ["NFPA79_2024__Ch06__overcurrent_protection.md"]
          eu: ["IEC60204_1_2016A1__Clause07__protection_of_equipment.md"]

      - topic_id: grounding_bonding
        note_file: "overlap_nfpa79_iec60204__grounding_bonding.md"
        anchors:
          us: ["NFPA79_2024__Ch08__grounding_and_bonding.md"]
          eu: ["IEC60204_1_2016A1__Clause08__equipotential_bonding.md"]

      - topic_id: control_functions
        note_file: "overlap_nfpa79_iec60204__control_functions.md"
        anchors:
          us: ["NFPA79_2024__Ch09__control_circuits_and_control_functions.md"]
          eu: ["IEC60204_1_2016A1__Clause09__control_circuits_and_functions.md"]

      - topic_id: operator_interface
        note_file: "overlap_nfpa79_iec60204__operator_interface.md"
        anchors:
          us: ["NFPA79_2024__Ch10__operator_interface_devices.md"]
          eu: ["IEC60204_1_2016A1__Clause10__operator_interface.md"]

      - topic_id: control_equipment
        note_file: "overlap_nfpa79_iec60204__control_equipment.md"
        anchors:
          us: ["NFPA79_2024__Ch11__control_equipment.md"]
          eu: ["IEC60204_1_2016A1__Clause11__controlgear.md"]

      - topic_id: motors_drives
        note_file: "overlap_nfpa79_iec60204__motors_drives.md"
        anchors:
          us: ["NFPA79_2024__Ch12__motors_and_associated_equipment.md"]
          eu: ["IEC60204_1_2016A1__Clause14__electric_motors.md"]

      - topic_id: accessories_lighting
        note_file: "overlap_nfpa79_iec60204__accessories_lighting.md"
        anchors:
          us: ["NFPA79_2024__Ch13__appliances_and_accessories.md", "NFPA79_2024__Ch14__lighting.md"]
          eu: ["IEC60204_1_2016A1__Clause15__socket_outlets_and_lighting.md"]

      - topic_id: marking_documentation
        note_file: "overlap_nfpa79_iec60204__marking_documentation.md"
        anchors:
          us: ["NFPA79_2024__Ch19__marking_and_documentation.md"]
          eu: ["IEC60204_1_2016A1__Clause16__marking_and_warning_signs.md"]

      - topic_id: verification
        note_file: "overlap_nfpa79_iec60204__verification.md"
        anchors:
          us: ["NFPA79_2024__Ch20__system_integration.md"]
          eu: ["IEC60204_1_2016A1__Clause18__verification.md"]

  routing_logic:
    market_owner_rules:
      US_ONLY:
        default_owner: "NFPA79"
      EU_ONLY:
        default_owner: "IEC60204_1"
      BOTH:
        default_owner: "MOST_STRINGENT"
        tie_breaker: "DOCUMENT_DECISION"

  outputs:
    delta_report_template: "rag/design_framework/us_eu_compliance_wizard/us_eu_delta_report_template.md"
```

---

# 3) Delta report template (what your wizard outputs)

Save as:

```
rag/design_framework/us_eu_compliance_wizard/us_eu_delta_report_template.md
```

```md
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
REPORT_ID: US_EU_DELTA
-->

# US ↔ EU Machine Compliance Delta Report

## 0. Project Profile
- Market target:
- Machine type:
- Supply:
- Environment:
- Control system summary:
- Documentation stage:

## 1. Executive Delta Summary
### 1.1 US → EU changes (top deltas)
- [ ] TODO
### 1.2 EU → US changes (top deltas)
- [ ] TODO

## 2. Topic-by-Topic Deltas

### 2.1 scope_boundary
**Owner standard (this market):**  
**What changes:**  
- TODO  
**Evidence required:**  
- TODO  
**Checklist:**  
- [ ] TODO  
**Cross-links:**  
- Overlap note: `rag/standards_intelligence/crosswalks/overlap_notes/overlap_nfpa79_iec60204__scope_boundary.md`
- NFPA 79 anchor(s): `rag/standards_intelligence/us/nfpa79/NFPA79_2024__Ch01__administration.md`
- IEC anchor(s): `rag/standards_intelligence/international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause01__scope.md`

(Repeat sections for each topic_id…)

## 3. Evidence Pack (audit-ready)
- Wiring diagrams:
- One-line diagram:
- Label photos:
- Test results:
- Manuals/datasheets:
- Change log references:

## 4. Verification & Commissioning Delta Checklist
- [ ] Incoming supply/disconnect checks
- [ ] Shock protection checks
- [ ] Bonding continuity checks
- [ ] Control function tests (start/stop/e-stop behavior)
- [ ] Documentation completeness check

## 5. Decisions & Deviations Log
- Decision:
- Rationale:
- Market impact:
- Date/owner:
```

---

# 4) Project profile input template (so you can run it repeatedly)

Save as:

```
drafts/us_eu_wizard_runs/project_profile_template.yaml
```

```yaml
market_target: BOTH
machine_type: conveyor

supply:
  voltage_v: 480
  phases: "3"
  frequency_hz: 60
  available_fault_current_ka: null

environment:
  location: indoor
  hazardous_area: no

control_system:
  plc: "ControlLogix L85E"
  safety_plc: "yes"
  safety_functions:
    - "E-stop"
    - "Guard doors"
  estop_count: 6
  drives_count: 12
  networks: ["EtherNet/IP"]

doc_stage: design
```

---

## How you use it (practical workflow)

* Fill `project_profile.yaml`
* Your future script/agent:

  * Reads `us_eu_wizard_rules.yaml`
  * For each `topic_id`, pulls the overlap note + anchors
  * Writes `us_eu_delta_report.md` with **market-specific deltas**

If you want, I can generate the **actual first-pass delta report** for a typical Amazon-style conveyor/robot cell profile (using reasonable defaults), so you can see what the wizard output looks like in practice.
