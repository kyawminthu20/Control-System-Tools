# Project Change Log

**Last Updated:** 2026-03-13
**Status:** Active

## Purpose

This file tracks meaningful project-level changes for the current implementation effort.

Use it for:

- project direction changes
- documentation workflow changes
- tooling changes
- architecture and delivery changes

Keep entries concise and oriented to what future work needs to know.

## Change History

### 2026-03-13 — FE Study Tools: `.doc` File Support
- feat(fe_study): `.doc` file support — LibreOffice headless conversion, `howto_doc` family (P2 priority), cached under `_converted/`
- Conversion: LibreOffice headless (`soffice --headless --convert-to docx`), cached in `_converted/`
- Covers all `.doc` files under `planning/FE_Study/How to/`
- Filtered: `~$*.doc` temp/lock files excluded from scanning
- Full test suite: 15/15 PASS

### 2026-03-13 — Phase 18 Track B: Field Engineering Section

- Added `/field-engineering/` site section with 7 pages (landing + 6 commissioning checklists)
- New `field-checklist` layout with Liquid data lookup from `field_checklists.yml`, "When to use" box, cross-links block, and print-optimized view
- Created `docs/_data/field_checklists.yml` flat YAML catalog driving all checklist metadata
- CSS additions: `.checklist-body` (☐ pseudo-element), `.field-checklist__cross-links`, `.cross-links-group`, print hiding rules
- Reverse links: `related_checklists` key added to 11 training module entries in `training_catalog.yml`; `training-module.html` updated to render them
- Reverse links: "Related Checklists" sections appended to 5 workflow pages
- Sidebar: Field Engineering section with 7 links and active state logic
- Jekyll build: clean, 123 pages

### 2026-03-13 — Phase 19 engineering-workflow navigation refactor queued

- Added plan doc: `docs/plans/2026-03-13-phase19-engineering-workflow-navigation.md`
- Queued Phase 19 in `project_state/project_state.md` as the next navigation refactor after Phase 18 Track C
- Recorded that the first refactor pass will keep current URLs stable, add workflow/reference hub pages, and move the sidebar toward a data-driven model

### 2026-03-13 — Phase 18 Track A: Control Systems training surfaced (9 new pages)

- Added `/training/control-systems/` group landing page and 7 module pages: Control Theory Overview, PID Foundation, PID Intuition, Industrial PID Implementation, Control Loop Architectures, PID Heater Control, PID Drone Control
- Added `/training/fundamentals/earthing-systems-iec/` page covering IEC TN-C/TT/TN-C-S/TN-S/IT earthing systems with comparison table
- Updated `docs/_data/training_catalog.yml`: control-systems topic group (7 modules), Control Systems Engineering learning path, start-here audience entry, fundamentals count 8→9, earthing module entry
- Updated sidebar: Control Systems link added under Training section
- Fundamentals group index updated: description and module count 8→9
- Jekyll build: clean, 116 pages (up from 107)

### 2026-03-13 — Project-state backlog reconciled after Phase 17

- Updated `project_state/project_state.md` to reflect the actual post-Phase-17 site state: 107-page clean build, 45-term glossary, 9 scenarios, 6 crosswalk pages, 32 surfaced training modules, 5 workflow pages, and standards graph coverage that already includes IEC 60079, IEC 61511, and SEMI
- Clarified `Next Phase` as `Phase 18 QUEUED — Field Engineering, Reference Library, and Control Systems Training`
- Replaced the stale note that Control Systems training needs new RAG corpus; canonical `training_modules/control_systems/` content already exists, so the remaining work is site surfacing and navigation
- Marked the old GitHub Pages deployment notes as completed and converted the old Phase 3 backlog note into historical carryover status
- Added direct references in `project_state/project_state.md` to the Phase 18 control-systems plan and the field/reference pre-plan

### 2026-03-10 — Phase 16 complete: NEC training expansion — 11-module NEC track

- Expanded NEC application training track from 3 to 11 modules (8 new RAG files + 8 new site pages)
- New RAG files in `control-standards/rag/training_modules/nec_application/`: branch_circuits_vs_feeders_motor_loads.md, disconnecting_means_for_machinery.md, grounding_bonding_control_panels.md, sccr_workflow.md, conductor_ocpd_sizing_examples.md, class1_class2_remote_control_circuits.md, article_430_practical_workflow.md, article_409_practical_workflow.md
- All 8 RAG files mirrored to `docs/assets/rag-files/training_modules/nec_application/`
- `control-standards/rag/training_modules/nec_application/_index.yaml` updated to 11 files
- `docs/_data/training_catalog.yml`: 8 new module entries added; nec-application topic_group module_count updated to 11; panel-design-nec learning path expanded with 4 new URLs
- `docs/training/nec-application/index.md`: description updated to 11 modules; recommended entry modules expanded to 4; page header updated
- `docs/training/nec-application/motor-panel-code-application/index.md`: footer next-link updated to point to branch-circuits-vs-feeders
- `docs/_data/rag_tree.json` regenerated (249 .md files, 5 top-level entries)
- Jekyll build: clean (0.529 s)

### 2026-03-10 — Phase 16 partial: four additional NEC site pages (pages 5–8)

- Added `docs/training/nec-application/conductor-ocpd-sizing/index.md` — step-by-step Art 430 sizing: table FLC, 125% conductor, 115%/125% overload, Table 430.52 OCPD, Table 250.122 EGC; full worked examples for 10 HP and 25 HP motors; Art 430.24 feeder formula with three-motor example; quick-reference HP sizing table (1–50 HP at 460/480 V); common mistakes table; won't-start exception explained
- Added `docs/training/nec-application/class1-class2-circuits/index.md` — Art 725 circuit classification (Class 1/2/3), supply-listing rule, 24 VDC PLC I/O as Class 2, Mermaid classification flowchart, Art 725.136 separation rules (separate duct / barrier), NFPA 79 color coding (blue=24 VDC, red=120 VAC), common mistakes table
- Added `docs/training/nec-application/article-430-workflow/index.md` — Art 430 Parts routing table (Parts I–X), Art 430.6(A) table-not-nameplate rule, Mermaid motor-circuit question router, standard 5-step sizing sequence (table FLC → conductor → overload → OCPD → disconnect), full worked example for 25 HP 460 V through all 5 steps, won't-start exception procedure, NFPA 79 alignment notes
- Added `docs/training/nec-application/article-409-workflow/index.md` — Art 409 ICP scope (factory-built assembly), Art 409.20 supply conductor sizing formula (125% largest motor + 100% others + 125% resistance heating), worked example with 25 HP + 10 HP motors, Art 409.110 required markings table (SCCR, FLC, enclosure type), Art 409.22 OCPD sizing, Art 409 vs. UL 508A comparison table (code vs. product standard), ICP (Art 409) vs. MCC (Art 430 Part F) comparison table, pre-shipment inspection checklist
- All four pages use `layout: training-module`, correct breadcrumbs, prev/next navigation, and Mermaid diagrams where specified
- Prev/next chain now complete: sccr-workflow → conductor-ocpd-sizing → class1-class2-circuits → article-430-workflow → article-409-workflow (terminus)

### 2026-03-10 — Phase 16 partial: four new NEC site pages

- Added `docs/training/nec-application/branch-circuits-vs-feeders/index.md` — branch circuit vs. feeder boundary, Art 430.22 125% conductor rule, Art 430.24 multi-motor feeder formula, Mermaid circuit flow, nameplate vs. table FLC common mistake
- Added `docs/training/nec-application/disconnecting-means/index.md` — Art 430.102 in-sight rule (visible + ≤50 ft), permitted disconnect types (HP-rated switch, MCCB, molded-case switch), NFPA 79 §6.2 lockable main disconnect, group disconnect exception Art 430.112, VFD placement rule (input side only), Mermaid VFD flow
- Added `docs/training/nec-application/grounding-bonding-panels/index.md` — grounding vs. bonding distinction, EGC sizing from Table 250.122 (earth rod is not the fault-current path), EGC sizing reference table (15A–200A), neutral/ground separation at downstream panels, enclosure bonding, VFD grounding notes, Mermaid 4-wire feeder flow
- Added `docs/training/nec-application/sccr-workflow/index.md` — SCCR definition, NEC 409.110 marking requirement, available fault current concept, UL 508A Supplement SB 4-step component method, current-limiting device raise strategy, Mermaid SB workflow diagram, 5 kA contactor default trap
- All pages use `layout: training-module`, correct breadcrumb, prev/next navigation, and Mermaid diagrams
- `training_catalog.yml` entries for these 4 modules still pending

### 2026-03-10 — Phase 15 complete: Training Module UX

- Created `docs/_layouts/training-module.html` — dedicated layout that looks up module metadata from `training_catalog.yml` by `page.url` and renders level chip, time, type, focus, Core badge, outcome sentence, and prerequisites before page content
- Added CSS: `.module-meta-bar`, `.module-outcome`, `.module-prereqs` to `main.css`
- Batch-updated all 24 module pages: layout changed to `training-module`, hardcoded page-header div removed, breadcrumb labels updated to new display names (Electrical Fundamentals, Motors Drives and Motion, NEC for Machines and Panels)
- Jekyll build: clean, 0.535 s

### 2026-03-10 — Phase 14 complete: Training Curriculum Upgrade

- Created `docs/_data/training_catalog.yml` — shared data model for all 24 modules with level, time, type, focus, prerequisites, featured flag, learning paths, start-here entries, and related standards
- Added training-specific CSS section to `docs/assets/css/main.css` — verification note, start-here cards, learning-path cards, training chips/badges (beginner/intermediate/advanced/concept/reference/code/featured), module table wrapper, related-standards strip, mobile responsive rules
- Rewrote `docs/training/index.md` — now a curriculum hub with verification note, start-here audience cards, four learning paths, browse-by-topic cards, data-driven all-modules table with metadata, and a related-standards strip; trust-boundary include retained at bottom
- Upgraded `docs/training/fundamentals/index.md` — new display label "Electrical Fundamentals", group intro, recommended entry modules, metadata-rich table driven from catalog
- Upgraded `docs/training/electrical-machines/index.md` — renamed to "Motors, Drives, and Motion", group intro, recommended entry modules, metadata-rich table
- Upgraded `docs/training/nec-application/index.md` — renamed to "NEC for Machines and Panels", group intro, recommended entry modules, metadata-rich table, note about Phase 16 expansion
- Updated sidebar labels to match new display names (URLs unchanged)
- Jekyll build: clean, 0.391 s

### 2026-03-11 — Post-Phase 16 site planning expanded for control-systems and eVTOL content

- Updated `docs/plans/2026-03-10-training-system-integration-preplan.md` to reserve a future `docs/training/control-systems/` route for the new PID/control-loop material
- Added a candidate scenario/page for a paraphrased public-source Archer vs. Joby eVTOL motor architecture comparison
- Recorded page rules that future public-source application notes should be paraphrased engineering analysis rather than raw transcript dumps or authoritative standards guidance
- Updated `project_state/project_state.md` post-Phase 16 target themes without changing the queued Phase 14-16 sequence

### 2026-03-10 — Training system integration pre-plan added

- Added planning-prep note: `docs/plans/2026-03-10-training-system-integration-preplan.md`
- Captured the current architecture gap between training, standards, lifecycle, scenarios, workflows, field checklists, and reference material
- Documented a post-Phase 16 candidate breakdown for:
  - cross-layer knowledge routing
  - field engineering and reference-library surfacing
  - safety and machine-architecture training expansion
  - scenario-driven learning
- Updated `project_state/project_state.md` with a post-Phase 16 planning candidate reference without changing the current queued Phase 14-16 sequence

### 2026-03-10 — Phase 14 training curriculum planning docs added

- Added design doc: `docs/plans/2026-03-10-phase14-training-curriculum-design.md`
- Added implementation plan: `docs/plans/2026-03-10-phase14-training-curriculum-implementation.md`
- Updated `project_state/project_state.md` Phase 14 section to reference the new planning docs
- Planning direction keeps current URLs stable while redesigning `/training/` around Start Here, Learning Paths, metadata-backed tables, filters, standards links, and a top-of-page verification note

### 2026-03-10 — Training page review converted into queued Phase 14-16 work

- `project_state/project_state.md` — next planned work changed from generic maintenance to `Phase 14 QUEUED — Training Curriculum Upgrade`
- Recorded that the current `/training/` section is complete but still behaves more like a browsable module index than a guided learning system
- Added `Phase 14 Scope — Training Curriculum Upgrade` for Start Here entry points, learning paths, audience framing, stronger hierarchy, outcome-focused copy, and a top-of-page verification note
- Added `Phase 15 Scope — Training Metadata And Module UX` for module chips and metadata fields covering level, time, prerequisites, type, role focus, and optional filtering/sorting
- Added `Phase 16 Scope — NEC Training Expansion` to grow NEC training from 3 modules to at least 8-10 modules with practical Article 409/430, SCCR, bonding, OCPD, and control-circuit topics

### 2026-03-10 — Phase 13 COMPLETE — all secondary backlog items done

- `docs/crosswalks/iec61511-iec61508/index.md` — new crosswalk: process SIS (IEC 61511) vs. functional safety foundation (IEC 61508); lifecycle comparison, SIL framework, architecture constraints, prior use, clause cross-reference (~250 lines)
- `docs/crosswalks/iec60079-nec-500-505/index.md` — new crosswalk: Zone vs. Division hazardous area; classification tables, EPL, gas groups, equipment marking, protection types, Zone/Division selection flow (~260 lines)
- `docs/crosswalks/index.md` — 2 new rows added
- `docs/_includes/sidebar.html` — 2 new crosswalk sidebar links
- All remaining Phase 13 backlog items confirmed complete: industry pages (5), standards graph (IEC 60079/61511/SEMI nodes), glossary (45 terms)
- Build: clean

### 2026-03-09 — Training site pages complete (24 modules)

- `docs/training/index.md` — landing page, 24 modules in 3 groups
- `docs/training/fundamentals/` — 8 pages: circuit theory, components, equations, conductor sizing
- `docs/training/electrical-machines/` — 13 pages: motors, drives, servo systems
- `docs/training/nec-application/` — 3 pages: code reading, table navigation, motor/panel application
- Sidebar updated with Training section (Training → Fundamentals / Electrical Machines / NEC Application)
- Build: 85 pages, clean

---

### 2026-03-09 — Motor interview source note promoted into additional training and design files

- `control-standards/work/design/check_this.md` — used as a read-only source for motor interview-style fundamentals, VFD electrical design points, and troubleshooting patterns; source file left unchanged.
- `control-standards/rag/training_modules/electrical_machines/` — added `motor_and_vfd_equations_reference.md`, `motor_efficiency_power_factor_and_losses.md`, `motor_control_methods_and_operating_regions.md`, and `servo_feedback_and_inertia_matching.md`; updated the module README and `_index.yaml`.
- `control-standards/rag/design_framework/motor_systems/` — added `motor_cable_and_protection_review.md` and `motor_symptom_troubleshooting_patterns.md`; updated the module README and `_index.yaml`.

---

### 2026-03-09 — Phase 12 Complete: Offshore / Marine Industry Overlay

- `DNV_OS_D201__electrical_installations.md` — RAG module: marine grade, IT earthing, LSOH cable, DP class, ESD/F&G class requirements, class approval workflow
- `ABS_offshore_electrical_control.md` — RAG module: ABS class notations, type approval, IT earthing implications, emergency power requirements
- `docs/industries/offshore/index.md` — full reference page: standards matrix by phase, DNV/ABS selection flow, IT earthing, LSOH, 11-item compliance checklist
- `docs/industries/marine/index.md` — deepened with IMO regulatory framework, IEC 60092 series structure, marine vs. offshore comparison; IEC 60092 corpus gap documented
- `docs/scenarios/offshore-platform-control/index.md` — Scenario 09: 4-phase workflow, ESD level hierarchy, Mermaid power/ESD architecture diagram, IT earthing and FAT decisions
- Scenarios index and sidebar updated

---

### 2026-03-09 — Electrical Knowledge Integration complete

Promoted three transcript-derived electrical learning sources into the existing canonical RAG layers.
No new parallel layer created. All content routes into existing `training_modules/`, `design_framework/`,
`commissioning_checklists/checklists/`, and `standards_intelligence/crosswalks/overlap_notes/`.

Design doc: `docs/plans/2026-03-08-electrical-intelligence-integration-design.md`

#### training_modules/fundamentals/ (new)
- 7 files: `electrical_quantities_and_circuit_language`, `series_parallel_and_divider_methods`,
  `kirchhoff_laws_and_systematic_analysis`, `equivalent_circuit_methods`,
  `electrical_equations_reference`, `passive_components_resistors_capacitors`,
  `diodes_transistors_and_switching_basics`

#### training_modules/electrical_machines/ (expanded)
- 3 core motor files + 6 additional: `vfd_fundamentals`, `servo_drive_fundamentals`,
  `ac_vs_dc_motor_comparison`, `motor_family_comparison`,
  `brushless_dc_ev_and_drone_motor_comparison`, `vfd_and_servo_architecture_diagrams`

#### training_modules/nec_application/ (new)
- 3 files: `nec_code_reading_fundamentals`, `working_space_and_table_navigation`,
  `motor_and_panel_code_application`

#### design_framework/electrical_review/ (new)
- 4 files: `ohms_law_and_power_check_workflow`, `basic_resistive_network_review`,
  `component_selection_basics`, `simple_signal_and_interface_circuit_notes`

#### design_framework/motor_systems/ (expanded)
- 13 total files including: selection workflow, nameplate checklist, star-delta notes,
  VFD integration review, commissioning workflows, troubleshooting decision tree,
  comparison matrices, integrated-drive architecture notes

#### commissioning_checklists/checklists/ (expanded)
- 6 files: motor rotation/overload, nameplate/overload setting, circuit polarity,
  capacitor discharge, drive commissioning, pre-power panel check

#### standards_intelligence/crosswalks/overlap_notes/ (gap fill)
- `overlap__motors_drives.md`
- `overlap_nfpa79_iec60204__motors_drives.md`

---

### 2026-03-09 — Integrated motor-drive architecture notes extracted from work-note source

- `control-standards/work/design/check_this.md` — used as a read-only source for integrated drive-on-motor content; source file left unchanged during extraction.
- `control-standards/rag/design_framework/motor_systems/` — added `integrated_motor_drive_architecture_comparison.md`, `industrial_vs_ev_vs_drone_motor_drive_standards_matrix.md`, `motor_mounted_drive_thermal_and_emc_design_notes.md`, `integrated_drive_failure_modes_and_tradeoffs.md`, and `integrated_drive_serviceability_and_field_replacement_review.md`.
- `control-standards/rag/design_framework/motor_systems/README.md` and `_index.yaml` — updated to include the new integrated-drive architecture note set.

---

### 2026-03-09 — Motor comparison pages extracted from work-note source

- `control-standards/work/design/check_this.md` — used as a read-only source for new motor comparison and architecture content; source file left unchanged during the extraction pass.
- `control-standards/rag/training_modules/electrical_machines/` — added `motor_family_comparison.md`, `ac_vs_dc_motor_comparison.md`, `vfd_and_servo_architecture_diagrams.md`, and `brushless_dc_ev_and_drone_motor_comparison.md`; updated the module README and `_index.yaml`.
- `control-standards/rag/design_framework/motor_systems/motor_selection_comparison_matrix.md` — added a concept-stage motor-family selection matrix; updated the module README and `_index.yaml`.

---

### 2026-03-09 — Motor comparison/diagram source note normalized for RAG promotion prep

- `control-standards/work/design/check_this.md` — converted a raw generated draft on motor, VFD, servo, BLDC, EV, and drone comparison pages into a scoped promotion-prep note.
- The note now identifies which content should enrich existing motor fundamentals files, which new RAG files are high-value next additions, and which EV/drone topics should remain lower-priority unless the repository scope expands.

---

### 2026-03-09 — Motor/VFD/servo RAG modules expanded from updated work note

- `control-standards/work/design/check_this.md` — used as a source note for additional motor-drive training, workflow, and checklist content; source left in place as work material.
- `control-standards/rag/training_modules/electrical_machines/` — added `vfd_fundamentals.md` and `servo_drive_fundamentals.md`, and updated the module README and `_index.yaml`.
- `control-standards/rag/design_framework/motor_systems/` — added `motor_troubleshooting_decision_tree.md`, `vfd_commissioning_workflow.md`, and `servo_commissioning_workflow.md`, and updated the module README and `_index.yaml`.
- `control-standards/rag/commissioning_checklists/checklists/drive_commissioning.md` — added a field checklist for first drive power-up and early verification; checklist README and `_index.yaml` updated accordingly.

---

### 2026-03-09 — Templates folder refreshed to current project conventions

- `control-standards/templates/README.md` — rewritten to match the current repo structure and actual available templates.
- `control-standards/templates/md_headers/` — refreshed `rag_approved_header.md` and `draft_only_header.md`, and added `archived_header.md` in the current metadata style.
- `control-standards/templates/checklists/checklist_template.md` — added a real checklist starter.
- `control-standards/templates/design_guides/design_guide_template.md` — added a design-guide starter.
- `control-standards/templates/reports/report_template.md` — added a report starter.
- `control-standards/templates/work_notes/work_note_template.md` — added a work-note starter for transcript-derived and normalized source notes.

---

### 2026-03-09 — Pre-power commissioning checklist promoted from work note

- `control-standards/work/design/check_this.md` — normalized as a commissioning source note for pre-power panel and incoming-supply verification.
- `control-standards/rag/commissioning_checklists/checklists/pre_power_panel_and_incoming_supply_check.md` — added a new pre-power checklist covering incoming supply, upstream protection, panel inspection, grounding/bonding, staged energization, and stored-energy awareness.
- `control-standards/rag/commissioning_checklists/README.md` and `checklists/README.md` — updated to reflect the expanded checklist set.
- `control-standards/rag/commissioning_checklists/checklists/_index.yaml` — updated with the new pre-power checklist.

---

### 2026-03-09 — Fundamentals training modules expanded from circuit-analysis source set

- `control-standards/rag/training_modules/fundamentals/` — added seven missing fundamentals modules covering circuit language, series/parallel methods, Kirchhoff laws, equivalent-circuit methods, electrical equations, passive components, and diode/transistor switching basics.
- `control-standards/rag/training_modules/fundamentals/README.md` — updated to reflect the expanded fundamentals module set.
- `control-standards/rag/training_modules/fundamentals/_index.yaml` — updated with the new module list.

---

### 2026-03-09 — Electrical integration design and implementation docs rewritten

- `docs/plans/2026-03-08-electrical-intelligence-integration-design.md` — replaced the obsolete `electrical_intelligence/` parallel-layer design with the current canonical architecture using `training_modules`, `design_framework`, `commissioning_checklists/checklists`, and `standards_intelligence`.
- `docs/plans/2026-03-08-electrical-intelligence-integration-plan.md` — replaced the stale implementation plan with a current executable backlog focused on the remaining circuit-analysis promotions and current validation constraints.

---

### 2026-03-09 — Electrical integration requirements doc added

- `docs/plans/2026-03-08-electrical-intelligence-integration-requirements.md` — added a concrete requirement list covering architecture, source readiness, metadata, target files, engineering-rule constraints, validation, and acceptance criteria for rewriting the Phase 11 electrical integration docs.

---

### 2026-03-09 — Missing electrical-intelligence components promoted into current RAG architecture

- `control-standards/work/design/project_implementation_gaps/nec_exam_prep_topics/` — added a normalized source package from `electrical exam prep.md`, including README and integration guidance based on the source's real content.
- `control-standards/rag/training_modules/` — added root README/index plus new `electrical_machines/` and `nec_application/` submodules with induction-motor, DC-motor, nameplate/slip/torque, NEC code-reading, table-navigation, and article-routing modules.
- `control-standards/rag/design_framework/electrical_review/` — added quick electrical review workflows for Ohm's law, resistive networks, component selection, and simple interface circuits.
- `control-standards/rag/design_framework/motor_systems/` — added motor selection, nameplate review, star/delta supply matching, and VFD integration review notes.
- `control-standards/rag/commissioning_checklists/` — added root README/index plus starter field checklists for circuit polarity/power, capacitor discharge awareness, and motor startup verification.
- `control-standards/rag/standards_intelligence/crosswalks/overlap_notes/` — added the previously missing `motors_drives` overlap notes for UL 508A/NEC/NFPA 79 and NFPA 79/IEC 60204-1 routing.

---

### 2026-03-09 — Design framework minimum viable set created

- `control-standards/rag/design_framework/README.md` — added module purpose and scope note.
- `control-standards/rag/design_framework/_index.yaml` — added seeded-content index for the design framework.
- `control-standards/rag/design_framework/design_guides/02_power_distribution_guide.md` — added applied power-distribution workflow guide.
- `control-standards/rag/design_framework/constraints/grounding_bonding_rules.yaml` — added reusable grounding and bonding ruleset.
- `control-standards/rag/design_framework/us_eu_compliance_wizard/` — added wizard README, spec, rules, and delta-report template to satisfy existing internal references.

---

### 2026-03-09 — Google tag added sitewide

- `docs/_layouts/default.html` — added the Google tag (`gtag.js`) snippet in `<head>` with measurement ID `G-RPL3G47EFZ`, which applies to every page using the default Jekyll layout.
- `project_state/project_state.md` — updated current-state tracking to record sitewide analytics installation.
- `project_state/environment.md` — recorded the active measurement ID and layout location for site analytics.
- Corrected the documented live GitHub Pages URL to `https://kyawminthu20.github.io/Control-System-Tools/`.

---

### 2026-03-09 — Conductor ampacity topic promoted into standards and training

- `control-standards/rag/training_modules/fundamentals/conductor_ampacity_and_termination_temperature.md` — new fundamentals training module covering ampacity, bundling, ambient correction, terminal temperature limits, and protection logic.
- `control-standards/rag/training_modules/fundamentals/README.md` — new fundamentals training-module index note.
- `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art240__overcurrent_protection.md` — corrected the Article 240.4 conductor-protection reference and expanded the conductor/OCPD coordination workflow.
- `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art310__conductors_for_general_wiring.md` — replaced placeholder artifacts with cleaner ampacity, current-carrying-conductor, and termination-temperature guidance.

---

### 2026-03-08 — UL 508A website update: scenario and lifecycle pages

- `docs/scenarios/us-industrial-control-panel/index.md` — major rework: 4 thin engineering decisions expanded to 12 topic-aligned decisions covering listing basis, enclosures, layout, spacing/creepage, wiring, SCCR (weakest-link), grounding, control circuits, motor controllers, transformers, marking, and E-stop; added inspection readiness checklist table.
- `docs/lifecycle/detailed-design/index.md` — key activities updated: old UL section number references replaced with descriptive topic references; SCCR bullet expanded with weakest-link logic; spacing/creepage bullet improved; deliverables table updated to match current RAG module names.

---

### 2026-03-08 — UL 508A spacing/creepage/clearance module populated

- `UL508A_2022__spacing_creepage_clearance.md` — populated from project working note: clearance vs creepage definitions, voltage-based heuristics (0–150 V, 151–300 V, 301–600 V), live parts review logic, mitigation methods (barriers, finger-safe, routing, layout), field inspection failure patterns.
- `docs/standards/us-electrical/ul-508a/index.md` — topic table updated (removed "in progress" marker); spacing/creepage section added between Enclosures and Wiring Methods.
- All 11 UL 508A RAG modules now populated.

---

### 2026-03-08 — UL 508A RAG populated; website updated

- All 11 UL 508A RAG modules filled from `_TODO_` to substantive practical guidance (10 populated; `spacing_creepage_clearance` still TODO).
- `docs/standards/us-electrical/ul-508a/index.md` — major rework: RAG-aligned topic table, practical topic sections for all 10 populated modules, expanded SCCR weakest-link section, marking/documentation section.
- `docs/crosswalks/ul508a-nec-nfpa79/index.md` — minor: expanded grounding row with safety vs noise grounding distinction.
- `docs/lifecycle/build/index.md` — expanded panel build activity into detailed UL 508A build checklist (layout, wiring, grounding, enclosure integrity, SCCR, nameplate).

---

### 2026-03-08 — Phase 11 Complete: Industry Overlay Depth

- `docs/industries/petroleum/index.md` — full reference page: standards matrix by phase, selection flow, checklist; all gap badges removed
- `docs/industries/semiconductor/index.md` — full reference page: SEMI badges updated to complete, applicability matrix, SEMI S2 compliance flow
- `docs/scenarios/oil-gas-process-skid/index.md` — Scenario 07: onshore O&G ESD/F&G/HIPPS with IEC 61511 + IEC 60079 + NEC workflow, Mermaid SIS diagram, engineering decisions
- `docs/scenarios/semiconductor-fab-tool/index.md` — Scenario 08: etch/CVD fab tool with SEMI S2/S14 gas control system, Mermaid interlock diagram, engineering decisions
- Scenarios index and sidebar updated with new entries

---

### 2026-03-08 — Phase 10 Complete: IEC 60079 + SEMI Corpus Gap-Fill

#### IEC 60079 (Hazardous Area)
- 6 new RAG files: Parts 0, 1, 10-1, 11, 14, 17
- _index.yaml indexing all 6 parts
- 2 site pages: hazardous-area family landing + IEC 60079 standard page

#### SEMI S2/S8/S14 (Semiconductor Equipment Safety)
- 3 new RAG files: S2 (equipment safety), S8 (ergonomics), S14 (fire risk)
- _index.yaml indexing all 3 standards
- 2 site pages: semiconductor family landing + SEMI S2/S8/S14 detail page

#### Site updates
- docs/standards/index.md: added Hazardous Area + Semiconductor sections
- docs/scenarios/semiconductor-equipment/index.md: added SEMI/IEC 60079 links, upgraded badges

---

### 2026-03-08 — Phase 9 Complete: Interactive Standards Graph

- Added `docs/_data/standards_graph.yml` — 12 nodes (6 families), 14 edges (4 types)
- Added `docs/_includes/standards-graph.html` — Cytoscape.js 3.28.1, parameterized mini/full
- Added `/standards/graph/` full page with zoom, pan, hover highlights, edge tooltips
- Homepage Mermaid block replaced with mini Cytoscape graph (preset layout, click-navigable)
- Edge types: requires (amber), pairs-with (blue), enforces (green), aligns-with (gray)
- Planned nodes (IEC 60079, SEMI) shown as dashed/dimmed — auto-activate when corpus added
- NEC page: readability overhaul (TOC, quick-reference callout, scope/limitations merge, 2026 section as change-log cards with impact levels + engineer takeaways, phased workflow)
- NEC page: technical improvements (Art. 240 added, SCCR critical rule + 4 determination methods, Art. 670 scoped to facility connection only, standards table updated)

---

### 2026-03-08 — Phase 10 Queued: IEC 60079 + SEMI Corpus Gap-Fill

**Type:** Planning
**Status:** NOT STARTED — begin next session

- Plan doc: `docs/plans/2026-03-08-phase10-corpus-gap-fill.md`
- **IEC 60079 (6 RAG files):** Parts 0, 1, 10-1, 11, 14, 17 → `control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/`
- **SEMI S2/S8/S14 (3 RAG files):** → `control-standards/rag/standards_intelligence/us/semi/`
- **Site pages:** `/standards/hazardous-area/` family + `/standards/hazardous-area/iec-60079/`; `/standards/semiconductor/` family + `/standards/semiconductor/semi/`
- **Standards index:** add Hazardous Area and Semiconductor sections
- **NEC polish:** rename table column, verify 409.70/670.6, clean up nec_update.md
- Full task list with file paths in `project_state/project_state.md` Phase 10 section

---

### 2026-03-08 — Phase 8 Complete: NEC RAG Corpus Expanded to 19 Articles

**Type:** RAG Corpus / Content
**Status:** Complete

- Added Art 90 (scope and purpose) — NEC jurisdiction limits, AHJ authority, adoption process
- Added Art 100 (definitions) — authoritative NEC terminology (listed, labeled, SCCR, grounded conductor, EGC)
- Added Art 215 (feeders) — feeder conductor sizing, 125% continuous load rule, OCPD coordination
- Added Art 230 (services) — available fault current, service disconnect, neutral-to-ground bond rule
- Added Art 250.4 (grounding purposes) — synthesized from NEC 250.4 + Mike Holt 2020; system vs equipment grounding, GEC routing
- Added Art 500 (hazardous locations general) — Class I/II/III, Division 1/2, T-codes, explosion-proof equipment
- Added Art 504 (intrinsically safe systems) — IS design rules, zener barriers, galvanic isolators, FISCO model
- Added Art 505 (Zone 0/1/2) — IEC-aligned zone system, ATEX/IECEx equipment acceptance, EPL markings
- Added Art 700–702 (emergency/standby) — three-tier power architecture, transfer times, ATS requirements, safety system coordination
- Updated _index.yaml: 19 articles now indexed (was 12); coverage_notes.complete updated
- Updated NEC_COMPLETION_STATUS.md: 19/19 articles complete (~9,500 words)
- Updated NEC_OVERVIEW.md: new sections for General, Power Distribution, Hazardous Locations, Emergency Power

**NEC corpus now covers:** general/definitions, power distribution, grounding, hazardous locations (Class/Division + Zone), IS systems, emergency power, industrial control panels, motors, conductors, wiring methods, overcurrent protection

---

### 2026-03-08 — NEC RAG Gap-Fill: Art250.4 Added

**Type:** RAG Corpus / Content
**Status:** Partial (250.4 complete; 409.70, 670.6 outstanding)

- Created `NEC_2023__Art250_4__purposes_of_grounding_and_bonding.md` — synthesized from NEC 250.4 code text and Mike Holt 2020 instructional content. No verbatim NEC text. Covers: system grounding vs equipment grounding, bonding vs grounding distinction, effective ground-fault current path, GEC routing rationale (inductive reactance / skin effect), grounded and ungrounded system differences, common engineering errors.
- Updated `_index.yaml`: registered NEC2023-Art250-4 entry using `note` field (valid); corrected `coverage_notes.complete` to list all 13 article files actually present in the corpus.
- Source file: `control-standards/archive/superseded_designs/work_design/promoted_to_rag/Grounding, System and Equipment [250.4, 2020 NEC].md` (raw transcript — not committed to RAG).
- Remaining gaps: Art409.70 (surge protection) and Art670.6 (overvoltage protection) referenced on NEC site page but no dedicated RAG sub-files.

---

### 2026-03-08: Dark Mode / Theme Switching Added

**Type:** UX / CSS
**Status:** Complete

- Added CSS custom property variables for all previously hardcoded colors (topnav, cards, table stripes, lifecycle stages)
- Added `[data-theme="dark"]` token block and `@media (prefers-color-scheme: dark)` fallback
- Added inline flash-prevention script in `<head>` — resolves theme before first paint
- Added theme toggle button (☾/☀) to topnav
- Added toggle handler in `main.js` with `localStorage` persistence
- Default: follows OS `prefers-color-scheme`; user override saved across sessions
- Build clean

---

### 2026-03-08 — Standards Decision Workflow Enhancements

- Added `last_reviewed` and `standards_editions` to front matter
- Added Purpose section with audience list and standards scope table
- Added sequential Lifecycle Workflow Mermaid diagram
- Added decision questions (key question + outputs) to Steps 1–3
- Added Standard Scope Boundaries table (NFPA 79 / UL 508A / NEC)
- Added Common Engineering Mistakes section (6 items)
- Added Typical Machine Compliance Stack table with editions
- Added Worked Example — Automated Conveyor System
- File: `docs/crosswalks/standards-decision-workflow/index.md`

---

### 2026-03-08: Glossary Page Added

**Type:** Content / Reference
**Status:** Complete

- Added `docs/_data/glossary.yml` with 28 seed terms (SIL, PL, SL, SCCR, AHJ, HFT, SFF, MTTFd, DC, Category, PFH, PLC, SIS, SIF, LOPA, E-stop, AFC, AIC, VFD, SPD, NEC, NFPA, UL, IEC, ISO, SEMI, CE, OSHA)
- Added `docs/glossary/index.md` — A-Z anchor navigation, domain badges, cross-links to standard pages, lifecycle stages, and related terms
- Added glossary card CSS and domain badge color variants to `main.css`
- Added Glossary to Reference section in sidebar
- Build clean

---

### 2026-03-08: NEC Page — Compliance-Focused Update

**Type:** Content / Standards
**Status:** Complete

- Added "Use This Page For" section clarifying NEC scope vs NFPA 79, UL 508A, ISO 13849-1
- Added "What the NEC Does Not Cover" section (PL, SIL, safety arch, stop categories)
- Expanded Key Articles table: added Article 300, 409.70 (surge protection), 670.6 (overvoltage protection)
- Tightened Article 409 SCCR language — UL 508A SB is one approved method, not the only path
- Softened Article 670 / NFPA 79 relationship language to be more accurate
- Added adoption warning callout (AHJ edition verification)
- Added "Typical Machine Builder Workflow" step sequence
- Added "Machine Builder Compliance Checklist" (8-point pre-installation checklist)
- Replaced ASCII relationship diagram with a proper standards table and summary blockquote
- Build: 52 pages, clean

---

### 2026-03-08 — Phase 5 Complete: IEC 62443 Cybersecurity Corpus and Site Pages

**Summary:** IEC 62443 cybersecurity corpus created from scratch (no prior RAG files). Full site page with Zone/Conduit diagram, SL table, FR overview, SIL vs SL distinction, and safety checklist. Cybersecurity family index created. Standards index updated. Networked Safety PLC scenario updated.

**What changed:**
- Created `control-standards/rag/standards_intelligence/international/cybersecurity/iec_62443/` — new directory
- Created `_index.yaml` — corpus index
- Created `IEC62443_2_1__security_management.md` — CSMS, risk assessment process, asset inventory, policy elements, IT vs OT distinctions
- Created `IEC62443_3_3__system_security_requirements.md` — Zone/Conduit model, SL 1–4 definitions, SL-T/SL-C/SL-A, FR 1–7, selected SR table, safety Zone guidance
- Created `IEC62443_4_2__component_requirements.md` — four component types (ED/SA/HD/ND), SL-C concept, selected requirements by component, secure development (4-1), component selection guidance
- Created `IEC62443_lifecycle.md` — Assess/Implement/Maintain lifecycle, SL designation lifecycle perspective, IACS patch management procedure, incident response for OT, functional safety coordination points
- Created `docs/standards/cybersecurity/iec-62443/index.md` — full site page: SL table, SIL vs SL section, Zone/Conduit Mermaid diagram, FR overview, lifecycle flowchart, safety/security coordination table, practical checklist
- Created `docs/standards/cybersecurity/index.md` — cybersecurity family page with routing table and out-of-scope gaps documented
- Updated `docs/standards/index.md` — added Cybersecurity Standards section
- Updated `docs/scenarios/networked-safety-plc/index.md` — added IEC 62443 to related_standards; updated badge to Phase 5 Complete; updated routing note to link to IEC 62443 detail page
- Jekyll build clean — 52 pages

**Phase 5 status: COMPLETE**

---

### 2026-03-07 — Phase 4 Complete: Practical Safety Guides

**Summary:** Two new site pages added sourcing content from `control-standards/work/design/simple_safety_system_design.md`. No RAG changes.

**What changed:**
- Created `docs/scenarios/machine-safety-implementation/index.md` — Scenario 06: Practical Machine Safety Implementation. 10-step workflow (risk assessment → safety functions → architecture → device selection → wiring → safety logic → validation), SIL/PL equivalence table, Category B/1/2/3/4 selection table, example hydraulic+chemical machine safety stack, Mermaid input→PLC→output and Category 3 architecture diagrams.
- Created `docs/lifecycle/safety-wiring/index.md` — Safety Wiring Practices lifecycle page. 24 VDC SELV rationale, NC contact fail-safe logic, dual-channel separation requirements, diagnostic test pulse explanation, discrepancy time (20–100 ms), wire gauge (18 AWG default), insulation rating, NFPA 79/UL 508A color coding, ferrule and spring-clamp termination guidance, baseline dual-channel input specification table.
- `docs/scenarios/index.md` — added Scenario 06 card
- `docs/lifecycle/index.md` — added safety-wiring row to stage table
- `docs/lifecycle/safety-architecture/index.md` — added See Also link
- `docs/lifecycle/detailed-design/index.md` — added See Also link
- Jekyll build clean.

**Phase 4 status: COMPLETE**

---

### 2026-03-07 — Phase 3 Complete: IEC 61511 RAG Corpus and Site Page

**Summary:** IEC 61511 RAG corpus created and site page rewritten with Phase 3 Complete badge. Phase 3 is now fully complete across all four functional safety standards.

**What changed:**
- Created `control-standards/rag/standards_intelligence/international/functional_safety/iec_61511/_index.yaml`
- Created `IEC61511_2016__Part1__framework.md` — SIS/SIF concepts, three-part structure, lifecycle overview, IEC 61508 relationship, prior use clause, ISA 84 equivalence
- Created `IEC61511_2016__Clause08__sil_determination.md` — HAZOP inputs, LOPA equation, IPL credits, tolerable risk targets, worked LOPA example, risk graph overview, FTA, common mistakes
- Created `IEC61511_2016__Clause10__sis_design.md` — PFDavg equation, redundancy architectures (1oo1/1oo2/2oo3), sensor and final element design, logic solver selection, prior use clause, SRS contents
- Created `IEC61511_2016__Clause16__operation_maintenance.md` — proof testing theory, proof test coverage, bypass management, functional safety audit, modification (MOC) process, decommissioning
- Rewrote `docs/standards/functional-safety/iec-61511/index.md` — badge updated to Phase 3 Complete; added Quick Start, SIL/PFDavg table, LOPA overview with IPL credits, PFDavg calculation table, architecture comparison table, prior use clause, IEC 61511 vs machinery comparison table, common mistakes, practical checklist, lifecycle application table

**Phase 3 status: COMPLETE** — ISO 13849-1, IEC 62061, IEC 61508, IEC 61511 all done.

---

### 2026-03-06 — Phase 4 Queue Defined: Practical Safety Guides

**Summary:** Identified two new site pages to implement after Phase 3 completes, sourced from `control-standards/work/design/simple_safety_system_design.md`.

**What changed:**
- Added Phase 4 queue to `project_state/project_state.md`
- New untracked design file: `control-standards/work/design/simple_safety_system_design.md`

**Planned pages:**
- `docs/scenarios/machine-safety-implementation/index.md` — Practical Machine Safety Implementation (Scenario 05)
- `docs/lifecycle/safety-wiring/index.md` — Safety Wiring Practices lifecycle stage

**No RAG changes required** — source doc already in `control-standards/work/design/`.

---

### 2026-03-06 — Phase 3 Group 2: IEC 62061 RAG Corpus and Site Page Complete

**Summary:** Full IEC 62061 RAG corpus created; site page rewritten with Phase 3 Complete badge and detailed content. DC vs SFF distinction clarified post-review.

**What changed:**
- Created `control-standards/rag/standards_intelligence/international/functional_safety/iec_62061/` corpus (Clause 06, 07, 08, Annex B, plus index)
- IEC 62061 Clause 07 fix: corrected DC labels and clarified DC vs SFF distinction
- Deepened `docs/standards/functional-safety/iec-62061/index.md` — badge updated to Phase 3 Complete
- ISO 13849-1 site page: removed Annex B stub reference, corrected RAG status, clarified PLr table

**Phase 3 status after this group:** ISO 13849-1 complete, IEC 62061 complete. IEC 61508 and IEC 61511 remain.

---

### 2026-03-06 — Phase 3: ISO 13849-1 RAG Corpus and Site Page Complete

**Summary:** Full ISO 13849-1 RAG corpus created; site page rewritten with Phase 3 Complete badge and detailed content.

**What changed:**
- Created `control-standards/rag/standards_intelligence/international/functional_safety/iso_13849_1/_index.yaml` — corpus index listing all 6 files
- Created `ISO13849_2023__Clause04__design_strategy.md` — design strategy, safety function specification, PL level table, ISO 12100 relationship
- Created `ISO13849_2023__Clause05__srp_cs.md` — MTTFd, DC, CCF parameters; PL lookup table; PFHd and SIL equivalence
- Created `ISO13849_2023__Clause06__categories.md` — Categories B/1/2/3/4 requirements, summary table, common architecture examples
- Created `ISO13849_2023__Clause07__validation.md` — validation plan, FMEA, functional testing, fault exclusion, documentation requirements
- Created `ISO13849_2023__AnnexA__risk_assessment.md` — S/F/P parameters, full PLr table, worked example, PLe conditions
- Created `ISO13849_2023__AnnexF__ccf.md` — CCF definition, Annex F scoring table, path to 65 points, common pitfalls
- Deleted `file_structure.md` placeholder
- Rewrote `docs/standards/functional-safety/iso-13849-1/index.md` — 224 lines; badge updated to Phase 3 Complete; added Quick Start, full PLr table, PL/PFHd table, design parameters table, Category architecture table, worked E-stop example, PL vs SIL comparison, 6 common mistakes, practical checklist, lifecycle application table

### 2026-03-06 — Phase 2 Implementation Complete

**Summary:** All Phase 2 features implemented and committed to master.

**What changed:**
- `docs/assets/css/main.css` — full `@media print` block (hide nav/sidebar/context, full-width content, URL-after-links, page-break rules); diagram lightbox styles; lunr.js search dropdown styles; crosswalk comparison selector styles
- `docs/assets/js/main.js` — diagram lightbox IIFE (click `.mermaid` → full-screen SVG clone, close via ×/Escape/click-outside); lunr.js search IIFE (fetch search.json, index on load, arrow-key nav, XSS-safe DOM building)
- `docs/_layouts/default.html` — lunr.js CDN script tag added before `</body>`
- `docs/_includes/topnav.html` — search input with ARIA attributes and `data-search-url`
- `docs/assets/data/search.json` — new Jekyll Liquid template; renders valid JSON search index at build time
- `docs/crosswalks/compare/index.md` — new comparison selector page; two `<select>` dropdowns; hidden pair divs for NFPA79/IEC60204 and US electrical trio; vanilla JS selector logic
- `docs/crosswalks/index.md` — compare link added to crosswalk table

**Architecture:** All additive. Vanilla JS + CSS only. No new Jekyll plugins. CDN-only dependency (lunr.js).

**Next step:** `git push` then enable GitHub Pages (Settings → Pages → Source: GitHub Actions).

### 2026-03-06 — Phase 1 Jekyll Site Implementation

**Summary:** Built the complete Phase 1 GitHub Pages static site under `docs/`.

**What changed:**
- Created `docs/` Jekyll scaffold with `_config.yml`, `Gemfile`, and vendor bundle (Ruby 2.6 / Bundler 2.4.22 local)
- Built three-panel layout: CSS Grid (240px sidebar + 1fr main + 220px context), responsive to tablet/mobile
- Mermaid.js CDN integration (theme: neutral) in default layout
- 48 HTML pages across all planned sections
- GitHub Actions workflow at `.github/workflows/pages.yml` (deploys from master branch)
- Updated `.gitignore` to exclude `docs/_site/`, `docs/vendor/`, `docs/.jekyll-cache/`

**Site sections implemented:**
- Homepage: 8 content blocks (hero, standards cards, lifecycle ribbon, relationship diagram, industry matrix, scenarios, repo explorer, trust boundary)
- Standards: explorer landing, US Electrical (NEC, NFPA 79, UL 508A), International Machinery (IEC 60204-1), Functional Safety (ISO 12100, ISO 13849-1, IEC 62061, IEC 61508, IEC 61511)
- Lifecycle: landing + 11 stage pages
- Crosswalks: NFPA 79 ↔ IEC 60204-1, UL 508A/NEC/NFPA 79, Decision Workflow
- Scenarios: 5 pages (US Control Panel, Global Machine, Process Skid, Networked Safety PLC, Semiconductor Equipment)
- Industries: matrix landing + 9 industry overlay pages
- Software Stack, About

**Architecture decision:** Jekyll static site with custom CSS (no framework). Content sourced from RAG corpus paraphrase. `docs/` is presentation only — never modifies `rag/`.

**Next step:** Commit, push, enable GitHub Pages in repo settings (Source: GitHub Actions).

### 2026-03-06: Commit Automation Retargeted To Project-State Log

**Type:** Automation / Workflow
**Status:** Active

- Updated the Git hook installer and the installed pre-commit hook to stage `project_state/change_log.md` instead of the removed root `general_change_log.md`.
- Kept `project_state/change_log.md` as a manual project log instead of using it as an auto-generated generation-summary feed.
- Aligned project runbook and tooling docs with the new project-state tracking path.

### 2026-03-06: Project-State Workflow Established

**Type:** Documentation / Process
**Status:** Active

- Established `project_state/` as the operational tracking area for this project.
- Defined file ownership:
  - `project_state.md` for current phase, scope, and next implementation work
  - `environment.md` for runtime and deployment requirements
  - `how_to.md` for setup and run instructions
  - `change_log.md` for project-level change tracking
- Updated root documentation so the project state is discoverable from the repository root.
- Set the current delivery target to Phase 1 GitHub Pages deployment for personal use.

### 2026-03-05 — Phase 2 Planning Docs Added

**Type:** Planning / Documentation
**Status:** Active

- Added Phase 2 design doc: `docs/plans/2026-03-05-phase2-design.md`
- Added Phase 2 implementation plan: `docs/plans/2026-03-05-phase2-implementation.md`
- Features planned: print stylesheet, diagram lightbox, lunr.js inline search, crosswalk comparison selector
- Architecture: all additive changes to existing files; vanilla JS + CSS only; no build step; CDN-only deps
- Implementation structured as 2 releases (Release 1: print + lightbox; Release 2: search + comparison)

### 2026-03-05: Repository Reorganization Executed

**Type:** Structure
**Status:** Completed

- Consolidated the repository under `control-standards/` as the clear product root.
- Kept `control-standards/rag/` as the authoritative AI-readable knowledge path.
- Grouped standards content under `us/`, `international/`, and `crosswalks/`.

### 2026-01-15: Legacy Migration Tooling Created

**Type:** Historical Infrastructure
**Status:** Historical

- Migration helper scripts and migration documentation were created for an earlier repository layout.
- These records remain useful as project history but are not the primary workflow for the current structure.

## Notes

- Older migration and generation details remain available elsewhere in the repository as historical context.
- This file should stay focused on the active project and current implementation effort.

## 2026-03-11 — Phase 17: Cross-Layer Knowledge Routing

- Added `/workflows/` as first-class site section (Option A decision)
- 5 workflow pages: Motor Selection, Motor Troubleshooting, VFD Commissioning, Servo Commissioning, Electrical Review
- Extended training_catalog.yml: `related_workflows` field on 7 modules; Machine Lifecycle learning path added
- training-module.html layout updated to render Related Workflows block
- Sidebar Workflows section added (5 direct links)
- Workflow CSS: card grid, badges, wf-tags, related-workflows block
- Jekyll build: clean, 0.583 s, 107 pages
