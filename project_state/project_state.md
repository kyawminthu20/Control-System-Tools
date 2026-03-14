# Project State

**Last Updated:** 2026-03-13
**Status:** Active
**Current Phase:** Phase 18 Track B COMPLETE — Field Engineering Section
**Next Phase:** Phase 18 Track C QUEUED — Reference Library Surfacing
**Delivery Target:** GitHub Pages static site for personal use

## Purpose

This file is the source of truth for the current project state, active implementation scope, and near-term backlog.

## Current Direction

Phase 17 is complete and the site is live on GitHub Pages. The next work shifts from cross-layer routing into surfacing canonical content that already exists in the RAG but is not yet a first-class site destination: Control Systems training, field engineering checklists, and reference-library material.

The site is a presentation and navigation layer on top of `control-standards/rag/`. Authoritative engineering and standards guidance stays in `control-standards/rag/`. The website never modifies RAG content.

## Current Reality

- Jekyll site deployed on GitHub Pages — `https://kyawminthu20.github.io/Control-System-Tools/`
- Last validated Jekyll build: 123 pages, clean build
- Three-panel layout (sidebar 240px + main content + context panel 220px)
- Mermaid.js CDN integration for all diagrams; Cytoscape.js 3.28.1 for interactive standards graph
- Google Analytics tag installed sitewide in `docs/_layouts/default.html` using measurement ID `G-RPL3G47EFZ`
- GitHub Actions deployment workflow at `.github/workflows/pages.yml`
- Site covers: homepage, all standards families (US Electrical, Machinery, Functional Safety, Cybersecurity, Hazardous Area, Semiconductor), 12 lifecycle pages including safety wiring, 9 scenarios, 6 crosswalk pages, 9 industry overlays, glossary (45 terms), training (40 surfaced modules across 4 groups), workflows (5 pages), field engineering (7 pages: landing + 6 commissioning checklists), software stack, and about / trust boundary
- Interactive standards graph: 12 nodes, 16 edges, including IEC 60079, IEC 61511, and SEMI
- Training groups: Electrical Fundamentals (9 modules), Motors/Drives (13), NEC (11), Control Systems (7)
- Field checklists and reference models exist in the canonical RAG but are not yet exposed as dedicated top-level site sections
- Root `main.py` remains a placeholder (not the site)

## Source Of Truth By Topic

- Current phase, status, and next implementation items: `project_state/project_state.md`
- Project-level change history: `project_state/change_log.md`
- Runtime, tooling, and deployment requirements: `project_state/environment.md`
- Setup, run, validation, and deployment steps: `project_state/how_to.md`
- Phase 18 control-systems site plan: `docs/plans/2026-03-11-phase18-control-systems-training.md`
- Field/reference expansion pre-plan: `docs/plans/2026-03-10-training-system-integration-preplan.md`
- Phase 19 engineering-workflow navigation plan: `docs/plans/2026-03-13-phase19-engineering-workflow-navigation.md`
- Authoritative standards content: `control-standards/rag/`
- Site source: `docs/`

## Phase 1 Scope — COMPLETED

- [x] Jekyll scaffold: `docs/_config.yml`, `docs/Gemfile`, Bundler vendor install
- [x] Three-panel CSS Grid layout: `docs/assets/css/main.css`
- [x] Layouts and includes: default.html, topnav, sidebar, context-panel, trust-boundary
- [x] Mermaid.js CDN integration (theme: neutral)
- [x] Homepage with all 8 content blocks (hero, standards cards, lifecycle ribbon, relationship diagram, industry matrix, scenarios, repo explorer)
- [x] Standards explorer landing + US Electrical family + Machinery family + Functional Safety family
- [x] Individual standard pages: NEC, NFPA 79, UL 508A, IEC 60204-1, ISO 12100, ISO 13849-1, IEC 62061, IEC 61508, IEC 61511
- [x] Lifecycle landing + 11 stage pages
- [x] Crosswalk pages: NFPA 79 ↔ IEC 60204-1, UL 508A/NEC/NFPA 79, Standards Decision Workflow
- [x] 5 scenario pages: US Control Panel, Global Machine, Process Skid, Networked Safety PLC, Semiconductor Equipment
- [x] Industry matrix landing + 9 industry pages
- [x] Software Stack and Cybersecurity routing page
- [x] About / trust boundary page
- [x] GitHub Actions pages.yml workflow

## Phase 1 — SHIPPED

Phase 1 is pushed, deployed, and live on GitHub Pages.

## Phase 2 Scope — COMPLETED

Plan: `docs/plans/2026-03-05-phase2-implementation.md`
Design: `docs/plans/2026-03-05-phase2-design.md`

- [x] Task 1: Print stylesheet (`main.css` — `@media print`)
- [x] Task 2: Diagram lightbox (`main.css` + `main.js`)
- [x] Task 3: lunr.js CDN + `search.json` data file
- [x] Task 4: Topnav search input + inline dropdown
- [x] Task 5: Crosswalk comparison selector page (`/crosswalks/compare/`)
- [x] Task 6: GitHub Pages enabled and site verified

## Phase 3 Backlog (historical carryover)

- Interactive standards graph — completed in Phase 9
- Functional-safety detail coverage — completed where corpus exists; future additions remain corpus-dependent
- SEMI S2/S8/S14 standard pages — completed in Phase 10

## Phase 4 Scope — COMPLETED

**Source:** `control-standards/work/design/simple_safety_system_design.md`

- [x] `docs/scenarios/machine-safety-implementation/index.md` — Scenario 06: Practical Machine Safety Implementation (10-step workflow, SIL/PL equivalence, Category B–4, device selection, example stack, Mermaid diagrams)
- [x] `docs/lifecycle/safety-wiring/index.md` — Safety Wiring Practices (24 VDC, NC contacts, dual-channel separation, wire gauge, color coding, termination, discrepancy time, baseline spec)
- [x] `docs/scenarios/index.md` — Scenario 06 card added
- [x] `docs/lifecycle/index.md` — safety-wiring row added to stage table
- [x] `docs/lifecycle/safety-architecture/index.md` — See Also link to safety-wiring added
- [x] `docs/lifecycle/detailed-design/index.md` — See Also link to safety-wiring added
- [x] Jekyll build clean (50 pages)

## Phase 5 Scope — IEC 62443 Cybersecurity Detail Pages — COMPLETED

**Rationale:** Cybersecurity is increasingly required alongside functional safety. Pairs with Scenario 04 (Networked Safety PLC). IEC 62443 corpus and full site pages close the visible gap.

### RAG Corpus (`control-standards/rag/standards_intelligence/international/cybersecurity/iec_62443/`)

- [x] `_index.yaml` — corpus index
- [x] `IEC62443_2_1__security_management.md` — IACS security management system, risk assessment process, security policy, asset inventory
- [x] `IEC62443_3_3__system_security_requirements.md` — Security Levels (SL 1–4), Zone/Conduit model, foundational requirements (FRs), system security requirements (SSRs)
- [x] `IEC62443_4_2__component_requirements.md` — component security requirements, embedded device requirements, software application requirements
- [x] `IEC62443_lifecycle.md` — IACS security lifecycle (assess → implement → maintain), patch management, incident response, SL-T vs SL-C distinction

### Site Pages

- [x] `docs/standards/cybersecurity/iec-62443/index.md` — full deepened page (badge: Phase 5 Complete), Zone/Conduit diagram, SL table, FR overview, lifecycle, SIL vs SL section, pairing with IEC 62061
- [x] `docs/standards/cybersecurity/index.md` — cybersecurity family page (IEC 62443 as full page entry)

### Nav / Index Updates

- [x] `docs/standards/index.md` — Cybersecurity section added with IEC 62443 entry
- [x] `docs/scenarios/networked-safety-plc/index.md` — IEC 62443 link added to related_standards; badge updated; routing note updated

### Build

- [x] Jekyll build clean — 52 pages

## Phase 6 Scope — Glossary — COMPLETED

**Rationale:** Engineers using the site encounter terms (SIL, PL, SCCR, AHJ, HFT, SFF, MTTFd)
across multiple pages with no single reference point. A cross-linked glossary closes this gap.

- [x] `docs/_data/glossary.yml` — 28 seed terms across Safety, Electrical, Standards Bodies, Regulatory domains
- [x] `docs/glossary/index.md` — rendered page with A-Z anchor strip, domain badges, standard links, lifecycle links, See Also cross-links
- [x] `docs/assets/css/main.css` — glossary entry card styles and domain badge variants
- [x] `docs/_includes/sidebar.html` — Glossary added to Reference section
- [x] Jekyll build clean

## Phase 7 Scope — Theme Switching — COMPLETED

**Rationale:** Engineers use reference sites in varied lighting environments. Dark mode
reduces eye strain during late-night or low-light reading. Following OS preference
requires zero user interaction while still allowing manual override.

- [x] `docs/assets/css/main.css` — new CSS variables for hardcoded colors; `[data-theme="dark"]` token block; `@media (prefers-color-scheme: dark)` fallback; toggle button styles
- [x] `docs/_layouts/default.html` — inline flash-prevention script in `<head>`
- [x] `docs/_includes/topnav.html` — theme toggle button (☾/☀)
- [x] `docs/assets/js/main.js` — toggle handler with `localStorage` persistence
- [x] Jekyll build clean

## Phase 8 Scope — NEC RAG Gap-Fill — COMPLETE

**Plan:** `docs/plans/2026-03-08-nec-missing-articles.md`
**Goal:** Add 9 missing NEC 2023 article files + update index/status files.

### Task 1 — Art 90 + Art 100 — COMPLETE
- [x] `NEC_2023__Art090__scope_and_purpose.md`
- [x] `NEC_2023__Art100__definitions.md`

### Task 2 — Art 500 + Art 504 — COMPLETE
- [x] `NEC_2023__Art500__hazardous_locations_general.md`
- [x] `NEC_2023__Art504__intrinsically_safe_systems.md`

### Task 3 — Art 505 (Zone Classification) — COMPLETE
- [x] `NEC_2023__Art505__zone_0_1_2_gas_vapors.md`

### Task 4 — Art 215 + Art 230 (Feeders and Services) — COMPLETE
- [x] `NEC_2023__Art215__feeders.md`
- [x] `NEC_2023__Art230__services.md`

### Task 5 — Art 700–702 (Emergency/Standby Systems) — COMPLETE
- [x] `NEC_2023__Art700_702__emergency_standby_systems.md` (combined file)

### Task 6 — Update _index.yaml + NEC_COMPLETION_STATUS + NEC_OVERVIEW — COMPLETE
- [x] All 8 new articles registered in `_index.yaml` (19 total indexed)
- [x] `NEC_COMPLETION_STATUS.md` updated to 19 articles
- [x] `NEC_OVERVIEW.md` updated with new article sections

### Additional items (from Art250.4 session)
- [x] `NEC_2023__Art250_4__purposes_of_grounding_and_bonding.md` — committed
- [x] `_index.yaml` — NEC2023-Art250-4 entry added

## Phase 9 Scope — Interactive Standards Graph — COMPLETE

- [x] `docs/_data/standards_graph.yml` — 12 nodes, 14 edges
- [x] `docs/_includes/standards-graph.html` — Cytoscape.js include (mini + full modes)
- [x] `docs/standards/graph/index.md` — full interactive page
- [x] `docs/index.md` — mini graph replaces static Mermaid block
- [x] CSS legend and canvas styles in main.css
- [x] Cytoscape.js 3.28.1 CDN added to default layout

## Phase 10 Scope — Corpus Gap-Fill (IEC 60079 + SEMI S2/S8/S14) — COMPLETE

### IEC 60079 RAG Corpus
- [x] IEC60079_0__general_requirements.md
- [x] IEC60079_1__flameproof_Ex_d.md
- [x] IEC60079_10_1__area_classification_gas.md
- [x] IEC60079_11__intrinsically_safe_Ex_i.md
- [x] IEC60079_14__installation_design.md
- [x] IEC60079_17__inspection_maintenance.md
- [x] _index.yaml

### SEMI RAG Corpus
- [x] SEMI_S2__equipment_safety.md
- [x] SEMI_S8__ergonomics.md
- [x] SEMI_S14__fire_risk_assessment.md
- [x] _index.yaml

### Site Pages
- [x] docs/standards/hazardous-area/index.md
- [x] docs/standards/hazardous-area/iec-60079/index.md
- [x] docs/standards/semiconductor/index.md
- [x] docs/standards/semiconductor/semi/index.md
- [x] docs/standards/index.md updated (2 new families)
- [x] docs/scenarios/semiconductor-equipment/index.md updated

## Phase 11 Scope — Industry Overlay Depth — COMPLETE

### Petroleum / Oil & Gas
- [x] `docs/industries/petroleum/index.md` — deepened: standards matrix by phase, selection flow, checklist, all gap badges removed
- [x] `docs/scenarios/oil-gas-process-skid/index.md` — Scenario 07: ESD/F&G/HIPPS onshore skid

### Semiconductor
- [x] `docs/industries/semiconductor/index.md` — deepened: standards matrix by phase, SEMI S2 flow, all SEMI badges updated
- [x] `docs/scenarios/semiconductor-fab-tool/index.md` — Scenario 08: etch/CVD tool with gas control, HV interlocks

### Nav
- [x] `docs/scenarios/index.md` — Scenario 07 and 08 cards added
- [x] `docs/_includes/sidebar.html` — both new scenarios added

## Phase 12 Scope — Offshore / Marine Industry Overlay — COMPLETE

### RAG Corpus
- [x] `control-standards/rag/standards_intelligence/international/offshore/DNV_OS_D201__electrical_installations.md`
- [x] `control-standards/rag/standards_intelligence/international/offshore/ABS_offshore_electrical_control.md`
- [x] `control-standards/rag/standards_intelligence/international/offshore/_index.yaml`

### Site Pages
- [x] `docs/industries/offshore/index.md` — deepened: DNV/ABS standards matrix, IT earthing, LSOH, class approval checklist
- [x] `docs/industries/marine/index.md` — deepened: IMO framework, IEC 60092 overview, class society comparison
- [x] `docs/scenarios/offshore-platform-control/index.md` — Scenario 09: ESD/F&G/power management, IT earthing, LSOH, class FAT workflow

### Nav
- [x] `docs/scenarios/index.md` — Scenario 09 card added
- [x] `docs/_includes/sidebar.html` — Offshore Platform scenario link added

## RAG Layer — Electrical Knowledge Integration — COMPLETE

Design doc: `docs/plans/2026-03-08-electrical-intelligence-integration-design.md`

Transcript-derived electrical learning content promoted into the existing canonical RAG layers.

- [x] `training_modules/fundamentals/` — 7 circuit analysis + components files
- [x] `training_modules/electrical_machines/` — 9 motor/drive/servo files
- [x] `training_modules/nec_application/` — 3 NEC code-reading and application files
- [x] `design_framework/electrical_review/` — 4 calculation workflow files
- [x] `design_framework/motor_systems/` — 13 motor/drive design and workflow files
- [x] `commissioning_checklists/checklists/` — 6 motor, drive, and circuit checklist files
- [x] `standards_intelligence/crosswalks/overlap_notes/` — 2 motors/drives crosswalk files

EV motor files held as WIP. No new parallel layer created.

## Content Gaps (documented with badges on site)

- ISO 13849-1 — corpus complete (6 RAG files)
- IEC 62061 — corpus complete (4 RAG files + index)
- IEC 61508 — corpus complete (4 RAG files + index)
- IEC 61511 — corpus complete (4 RAG files + index)
- IEC 62443 — corpus complete (4 RAG files + index)
- IEC 60079 (hazardous area) — corpus complete (6 RAG files + index)
- SEMI S2/S8/S14 — corpus complete (3 RAG files + index)
- Medical, nuclear, marine class rules — not in corpus (no plan)

## Phase 13 Backlog (Secondary Backlog)

### RAG File Browser — COMPLETE
- [x] `tools/generate_rag_tree.py` — walks `control-standards/rag/`, outputs nested JSON
- [x] `docs/_data/rag_tree.json` — 236 file buttons, 7 top-level entries
- [x] `docs/_layouts/rag-browser.html` — two-panel layout (tree + content); marked.js + DOMPurify CDN
- [x] `docs/_includes/rag-tree-nodes.html` — recursive Jekyll include for nested `<details>` tree
- [x] `docs/rag-browser/index.md` — page at `/rag-browser/`
- [x] `docs/assets/js/rag-browser.js` — click handler, GitHub raw fetch, DOMPurify sanitization, mermaid re-init
- [x] `docs/assets/css/main.css` — RAG browser section (tree panel, file content, prose, states)
- [x] `docs/_includes/sidebar.html` — "RAG Files" link added to Reference section

### Training site pages — COMPLETE
- [x] `docs/training/index.md` — landing page, 24 modules, 3 groups
- [x] `docs/training/fundamentals/` — 8 pages
- [x] `docs/training/electrical-machines/` — 13 pages
- [x] `docs/training/nec-application/` — 3 pages
- [x] Sidebar: Training section added

### Thin industry pages — COMPLETE
- [x] `docs/industries/energy/index.md` — deepened: phase table, selection flow, key decisions, checklist
- [x] `docs/industries/food-and-beverage/index.md` — deepened: washdown, hygienic design gaps noted, checklist
- [x] `docs/industries/medical/index.md` — deepened: IEC 60601-1/ISO 14971 gaps noted, corpus status table, checklist
- [x] `docs/industries/nuclear/index.md` — deepened: IEEE 603/IEC 61513 gaps noted, corpus status table, checklist
- [x] `docs/industries/commercial/index.md` — deepened: NEC/IBC scope, Class 2 wiring, AHJ submittal, checklist

### Standards graph expansion — COMPLETE
- [x] IEC 60079 node — `docs/_data/standards_graph.yml` (12+ nodes; hazardous area family)
- [x] IEC 61511 node — functional safety family
- [x] SEMI S2/S8/S14 node — semiconductor family
- [x] Edges: IEC 60079 ↔ NEC (Zone via Art. 505), IEC 60079 ↔ IEC 61511 (hazardous-area process protection), SEMI ↔ IEC 60204-1, SEMI ↔ ISO 12100

### Glossary expansion — COMPLETE
- [x] Expanded from 28 terms to 45 terms
- [x] Added O&G/SEMI/hazardous-area terms: SIF, SRS, LOPA, PFDavg, IPL, EPL, T-code, Ex ia, SECS/GEM, PTI

### Crosswalk additions — COMPLETE
- [x] `docs/crosswalks/iec61511-iec61508/index.md` — IEC 61511 ↔ IEC 61508 (application vs. foundation); lifecycle comparison, SIL framework, architecture constraints, prior use, clause cross-reference
- [x] `docs/crosswalks/iec60079-nec-500-505/index.md` — IEC 60079 ↔ NEC Art. 500/505 (Zone vs. Division); classification tables, EPL, gas groups, equipment marking, protection types, installation rules
- [x] `docs/crosswalks/index.md` — updated with 2 new rows
- [x] `docs/_includes/sidebar.html` — 2 new crosswalk links added

## Phase 14 Scope — Training Curriculum Upgrade — COMPLETE

**Driver:** Training page review on 2026-03-10 found that `/training/` is structurally sound but still reads as a raw index instead of a learning system.
Plan: `docs/plans/2026-03-10-phase14-training-curriculum-implementation.md`
Design: `docs/plans/2026-03-10-phase14-training-curriculum-design.md`

### Landing page reframing
- [x] `docs/training/index.md` — replaced generic intro with learner-oriented copy; verification note; Start Here audience cards; learning paths; browse-by-topic cards; data-driven all-modules table with metadata chips; related standards strip; trust-boundary include retained
- [x] `docs/_data/training_catalog.yml` — shared data model for all 24 modules (level, time, type, focus, prerequisites, featured flag, learning paths, start-here, related standards)

### Learning structure
- [x] Four named learning paths: Controls Engineering Foundations, Motor and Drive Engineering, Industrial Panel Design (NEC Focus), Troubleshooting and Field Service
- [x] Three browse tracks renamed: Electrical Fundamentals, Motors, Drives, and Motion, NEC for Machines and Panels
- [x] All module summaries rewritten as outcome-focused descriptions in the catalog

### Information hierarchy
- [x] All Modules table replaces flat list — metadata columns (track, level, time, type); featured/core rows visually distinguished; mobile columns hidden via `.hide-mobile`
- [x] Training CSS section added to `docs/assets/css/main.css` — training chips, start-here cards, learning-path cards, related-standards strip, responsive rules
- [x] Group pages upgraded with group intro, recommended entry modules, and catalog-driven metadata tables
- [x] Sidebar labels updated to match display names (URLs unchanged)
- [x] Jekyll build: clean, 0.391 s

## Phase 15 Scope — Training Metadata And Module UX — COMPLETE

**Goal:** Make the training catalog scannable by difficulty, effort, prerequisite knowledge, and job context.

### Metadata model
- [x] `docs/_data/training_catalog.yml` exists with level, time, type, focus, prerequisites, featured flag for all 24 modules (completed in Phase 14)
- [x] Modules classified with Core (featured) badge; level/type/focus fields serve as status markers
- [x] Per-module metadata surfaced on individual pages via dedicated layout

### Page/application work
- [x] `docs/_layouts/training-module.html` — dedicated layout that looks up module metadata from catalog by `page.url`; renders level chip, time, type, focus, Core badge, outcome sentence, and prerequisites before page content
- [x] CSS added: `.module-meta-bar`, `.module-outcome`, `.module-prereqs`
- [x] All 24 module pages updated: `layout: training-module`, page-header div removed (layout handles it), breadcrumb labels updated to new display names
- [x] Jekyll build: clean, 0.535 s
- [x] Acceptance target met: every module page shows difficulty, time, type, outcome, and prerequisites without opening any other page

## Phase 16 Scope — NEC Training Expansion — COMPLETE

**Goal:** Rebalance the training catalog so NEC application is not limited to only three modules.

### Canonical RAG additions
- [x] Expand `control-standards/rag/training_modules/nec_application/` from 3 to 11 modules
- [x] branch_circuits_vs_feeders_motor_loads.md
- [x] disconnecting_means_for_machinery.md
- [x] grounding_bonding_control_panels.md
- [x] sccr_workflow.md
- [x] conductor_ocpd_sizing_examples.md
- [x] class1_class2_remote_control_circuits.md
- [x] article_430_practical_workflow.md
- [x] article_409_practical_workflow.md

### Site follow-through
- [x] 8 new site pages under `docs/training/nec-application/`
- [x] `docs/_data/training_catalog.yml` — 8 new entries, module_count updated to 11, panel-design-nec path expanded
- [x] NEC group index page: description updated to 11 modules, recommended entry modules updated
- [x] Footer nav chain complete across all 11 NEC modules
- [x] `docs/_data/rag_tree.json` regenerated (249 files)
- [x] Jekyll build: clean (0.529 s)
- [x] Acceptance target met: NEC track covers practical machine and panel design work end-to-end

## Phase 17 Scope — Cross-Layer Knowledge Routing — COMPLETE

**Plan:** `docs/plans/2026-03-11-phase17-cross-layer-routing.md`
**Decision:** Workflows as first-class `/workflows/` site section (Option A)

### `/workflows/` section
- [x] `docs/workflows/index.md` — landing page with workflow cards by category
- [x] `docs/workflows/motor-selection/index.md` — Motor Selection Workflow
- [x] `docs/workflows/motor-troubleshooting/index.md` — Motor Troubleshooting Decision Tree
- [x] `docs/workflows/vfd-commissioning/index.md` — VFD Commissioning Workflow
- [x] `docs/workflows/servo-commissioning/index.md` — Servo Commissioning Workflow
- [x] `docs/workflows/electrical-review/index.md` — Electrical Review Workflow

### Cross-layer data model
- [x] `docs/_data/training_catalog.yml` — `related_workflows` field added to 7 modules; Machine Lifecycle learning path added
- [x] `docs/_layouts/training-module.html` — Related Workflows block rendered on module pages

### Navigation
- [x] `docs/_includes/sidebar.html` — Workflows section added (5 workflow links)
- [x] `docs/assets/css/main.css` — Workflow card grid, badges, wf-tags, related-workflows block CSS

### Build
- [x] Jekyll build: clean, 0.583 s, 107 pages

## Phase 18 Track A — Control Systems Training Surfacing — COMPLETE

**Plan:** `docs/plans/2026-03-11-phase18-control-systems-training.md`

### Control Systems group (7 modules)
- [x] `docs/training/control-systems/index.md` — group landing page
- [x] `docs/training/control-systems/control-theory-overview/index.md`
- [x] `docs/training/control-systems/pid-foundation/index.md`
- [x] `docs/training/control-systems/pid-intuition/index.md`
- [x] `docs/training/control-systems/industrial-pid/index.md`
- [x] `docs/training/control-systems/control-loop-architectures/index.md`
- [x] `docs/training/control-systems/pid-heater-control/index.md`
- [x] `docs/training/control-systems/pid-drone-control/index.md`

### Fundamentals group addition — IEC Earthing Systems
- [x] `docs/training/fundamentals/earthing-systems-iec/index.md` — IEC Earthing System Types (TN-C, TT, TN-C-S, TN-S, IT)

### Data model and navigation
- [x] `docs/_data/training_catalog.yml` — control-systems topic group, 7 module entries, Control Systems Engineering learning path, start-here audience card, fundamentals count 8→9, earthing module entry
- [x] `docs/_includes/sidebar.html` — Control Systems link added under Training section

### Build
- [x] Jekyll build: clean, 0.629 s, 116 pages

## Phase 18 Track B — Field Engineering Section — COMPLETE

- [x] `docs/_data/field_checklists.yml` — flat YAML catalog (6 entries)
- [x] `docs/_layouts/field-checklist.html` — new layout with Liquid data lookup, cross-links, back link
- [x] CSS additions to `docs/assets/css/main.css` — `.checklist-body`, `.field-checklist__cross-links`, print rules
- [x] `docs/field-engineering/index.md` — landing page with workflow-card-grid
- [x] 6 checklist pages under `docs/field-engineering/`
- [x] Sidebar: Field Engineering section added
- [x] Reverse links: `related_checklists` in 11 training modules + "Related Checklists" sections in 5 workflow pages
- [x] Jekyll build: clean, 123 pages

## Phase 18 Backlog — Field Engineering, Reference Library, and Control Systems Training

**Canonical content ready to surface:**
- `commissioning_checklists/checklists/` — 6 field-facing checklists
- `design_framework/motor_systems/motor_selection_comparison_matrix.md`
- `standards_intelligence/reference_models/7-Layer Industrial Machine Architecture Model.md`
- `standards_intelligence/reference_models/Universal Machine Safety Architecture.md`
- `standards_intelligence/reference_models/15-Standard Minimum Compliance Stack.md`
- `training_modules/control_systems/` — 7 control-theory and PID training files
- `training_modules/fundamentals/earthing_systems_iec.md`

### Track A — Control Systems training surfacing

**Plan:** `docs/plans/2026-03-11-phase18-control-systems-training.md`

- `/training/control-systems/` group landing page
- 7 site module pages mapped to the existing control-systems RAG corpus
- `docs/_data/training_catalog.yml` updates: new `control-systems` topic group, 7 module entries, learning path, and start-here route
- Sidebar update: Control Systems link under Training
- `/training/fundamentals/earthing-systems-iec/` page plus fundamentals catalog/count update

### Track B — Field Engineering / Commissioning surfacing

- `/field-engineering/` or `/commissioning/` section with checklist pages
- Publish selected commissioning checklists from canonical RAG as site pages
- Link checklist pages back into lifecycle, workflow, and training routes where appropriate

### Track C — Reference library surfacing

- `/reference/` section for equations, machine architecture, and quick-reference content
- Surface machine architecture and compliance-stack reference models already present in canonical RAG
- Consolidate fast-lookup material that is currently distributed across training and standards pages

### Key clarification

- Control Systems RAG corpus already exists; Phase 18 work is site surfacing and navigation, not new PID/control-loop source-file creation

## Phase 19 Queue — Engineering Workflow Navigation Refactor

**Plan:** `docs/plans/2026-03-13-phase19-engineering-workflow-navigation.md`

- Queue position: starts after Phase 18 Track C is complete
- Preserve all current URLs during the first navigation refactor pass
- Replace the hardcoded sidebar with a data-driven model backed by `docs/_data/navigation.yml`
- Add `/engineering-workflow/` as the workflow-first hub for lifecycle, workflows, and field checklists
- Add `/reference/` as the fast-lookup hub for glossary, software stack, RAG browser, crosswalk entry points, and future equations / architecture references
- Demote Scenarios, Crosswalks, and Workflows from top-level sidebar peers into the new grouped navigation model
- Keep Standards, Training, and Industries as top-level sections in the Phase 19 information architecture
