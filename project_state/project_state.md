# Project State

**Last Updated:** 2026-04-11
**Status:** Active
**Current Phase:** Phase 22 COMPLETE — Semiconductor Facility Reference
**Next Phase:** Phase 23 PLANNING — TBD
**Delivery Target:** GitHub Pages static site for personal use

## Purpose

This file is the source of truth for the current project state, active implementation scope, and near-term backlog.

## Current Direction

Phases 19–21 are complete. Phase 22 (Semiconductor Facility Reference) first slice is implemented. The facility reference section covers gas systems, UPW and wastewater, exhaust and abatement, tool-facility interfaces, and instrumentation — promoted from planning/semi_facility/ staging area into the RAG corpus and Jekyll site.

All 13 lifecycle stage pages (Stages 1–11 plus Safety Requirements Spec and Management of Change) are now comprehensive engineering references. The lifecycle pages serve as the primary navigation hub for all phases of system development, from initial concept through maintenance.

The site is a presentation and navigation layer on top of `control-standards/rag/`. Authoritative engineering and standards guidance stays in `control-standards/rag/`. The website never modifies RAG content.

## Current Reality

- Jekyll site deployed on GitHub Pages — `https://kyawminthu20.github.io/Control-System-Tools/`
- Last validated Jekyll build: 152 HTML files, clean build (verified 2026-04-11; Phase 22 complete — 10 facility pages total)
- Three-panel layout (sidebar 240px + main content + context panel 220px); sidebar data-driven from `docs/_data/navigation.yml` with 5 top-level groups (Engineering Workflow, Standards, Training, Industries, Reference)
- Mermaid.js CDN integration for all diagrams; Cytoscape.js 3.28.1 for interactive standards graph
- Google Analytics tag installed sitewide in `docs/_layouts/default.html` using measurement ID `G-RPL3G47EFZ`
- GitHub Actions deployment workflow at `.github/workflows/pages.yml`
- Site covers: homepage, all standards families (US Electrical, Machinery, Functional Safety, Cybersecurity, Hazardous Area, Semiconductor), 13 lifecycle stage pages (all comprehensive references), 9 scenarios, 6 crosswalk pages, 9 industry overlays, glossary (45 terms), training (41 surfaced modules across 4 groups), workflows (5 pages), commissioning templates (7 pages), software stack, reference models (4 pages), and about / trust boundary
- Interactive standards graph: 12 nodes, 16 edges, including IEC 60079, IEC 61511, and SEMI
- Training groups: Electrical Fundamentals (9 modules), Motors/Drives (13), NEC (11), Control Systems (14)
- Commissioning checklists at `/commissioning-templates/` (Phase 18 Track B+C): 7 pages with template header fill-in block, checkbox UI, cross-links; `/field-engineering/` redirects to new URL
- Reference models at `/reference/` (Phase 18 Track C): 5 pages covering machine architecture, safety architecture, compliance stack, and motor selection matrix; sidebar "Reference Models" block added
- Root `main.py` remains a placeholder (not the site)

## Tools — FE Study Automation

**FE Study Pipeline** (`tools/fe_study/`)

The FE study tools automate content extraction and inventory from the `planning/FE_Study/` directory. The pipeline scans, extracts, and catalogs How-To and training documents.

### `.doc` File Support (P2 Priority)

- **Conversion:** LibreOffice headless (`soffice --headless --convert-to docx`) for `.doc` → `.docx` conversion
- **Caching:** Converted files cached under `planning/FE_Study/How to/_converted/` for reuse
- **Family/Priority:** `howto_doc` family, P2 (important but not urgent)
- **Scope:** All `.doc` files under `planning/FE_Study/How to/`
- **Filtering:** Temporary/lock files (`~$*.doc`) automatically excluded from scanning
- **Status:** Implemented and tested (15/15 tests PASS; scan, extract, and build_record branches functional)

## Source Of Truth By Topic

- Current phase, status, and next implementation items: `project_state/project_state.md`
- Project-level change history: `project_state/change_log.md`
- Runtime, tooling, and deployment requirements: `project_state/environment.md`
- Setup, run, validation, and deployment steps: `project_state/how_to.md`
- Phase 20 software safety routing source: `planning/safety_software_stack.md`
- Phase 18 control-systems site plan: `docs/plans/2026-03-11-phase18-control-systems-training.md`
- Cross-layer integration pre-plan and Phase 20 candidates: `docs/plans/2026-03-10-training-system-integration-preplan.md`
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

## Phase 18 Track C — Reference Section + Commissioning Templates Redesign — COMPLETE

**Design spec:** `docs/superpowers/specs/2026-03-14-reference-section-commissioning-templates-design.md`

- [x] `/reference/` landing page (2 card groups: Architecture, Motor Systems)
- [x] `/reference/architecture/machine-architecture-model/` — 7-Layer model from RAG
- [x] `/reference/architecture/machine-safety-architecture/` — Universal safety architecture template
- [x] `/reference/architecture/compliance-stack/` — 15-Standard minimum compliance stack
- [x] `/reference/motor-systems/motor-selection-matrix/` — Motor selection flowchart + matrix
- [x] Sidebar "Reference Models" block with `.sidebar__group-label` sub-groups
- [x] `.sidebar__group-label` CSS added to `main.css`
- [x] `/field-engineering/` → `/commissioning-templates/` rename: 7 pages moved, redirect at old index
- [x] `field-checklist.html` layout: label updated, template header block, checkbox DOM script, back-link updated
- [x] CSS: `.template-header`, `.checklist-item`, print checkbox styles
- [x] `field_checklists.yml`: all 6 URL entries updated
- [x] `training_catalog.yml`: 13 URL references updated across 11 modules
- [x] 5 workflow pages: all `/field-engineering/` hrefs updated
- [x] Cross-links: motor-selection workflow → motor-selection-matrix; semiconductor-equipment scenario → machine-architecture-model; semiconductor industry → compliance-stack
- [x] Jekyll build: clean, 129 pages

## Phase 19 Scope — Engineering Workflow Navigation Refactor — COMPLETED

**Plan:** `docs/plans/2026-03-13-phase19-engineering-workflow-navigation.md`

- [x] Created `docs/_data/navigation.yml` — 5-group sidebar data model (Engineering Workflow, Standards, Training, Industries, Reference)
- [x] Refactored `docs/_includes/sidebar.html` from 135-line hardcoded HTML to ~60-line data-driven Liquid renderer
- [x] Added `/engineering-workflow/` hub page with 5 task-grouped sections (Design & Architecture, Select & Size, Commission & Verify, Troubleshoot, Scenarios)
- [x] Expanded `/reference/` landing page with Quick Reference section (Glossary, Crosswalks, Software Stack, RAG File Browser)
- [x] Demoted Scenarios, Crosswalks, and Workflows from top-level sidebar into Engineering Workflow and Reference hub groups
- [x] Jekyll build: clean, 132 pages

## Phase 20 Scope — Software Safety Stack Deepening — COMPLETE

**Sources:** `planning/safety_software_stack.md`, `docs/superpowers/specs/2026-03-15-software-safety-stack-phase20-design.md`

- [x] RAG corpus updated: IEC 61131-3:2025 edition note; Normal PLC vs Safety PLC vs SIS comparison table; expanded E-stop section with canonical tag names, I/O list, 7-rung pseudocode, sequence of operation, documentation checklist, logging checklist; Rockwell GuardLogix and Siemens S7-1500F vendor patterns
- [x] `/software-stack/` site page updated: edition note, comparison table section, expanded E-stop with Mermaid wiring/architecture and state machine diagrams, vendor-specific `<details>` blocks
- [x] Jekyll build: clean, 132 pages

## Phase 21 Scope — Lifecycle Stage Page Expansion — COMPLETE

**Objective:** Transform all lifecycle stage pages from thin stubs into comprehensive engineering references with detailed guidance, decision criteria, cross-links, and practical examples.

### Pages Expanded (Existing → Full)
- [x] `docs/lifecycle/index.md` — lifecycle overview with introduction section and 13-stage table
- [x] `docs/lifecycle/concept/index.md` — Stage 01 (42 lines → ~300 lines)
- [x] `docs/lifecycle/standards-selection/index.md` — Stage 02 (59 lines → ~500 lines)
- [x] `docs/lifecycle/risk-assessment/index.md` — Stage 03 (62 lines → ~600 lines)
- [x] `docs/lifecycle/safety-architecture/index.md` — Stage 04 (67 lines → ~770 lines)
- [x] `docs/lifecycle/detailed-design/index.md` — Stage 05 (58 lines → ~680 lines)
- [x] `docs/lifecycle/draft-documentation/index.md` — Stage 06 (41 lines → ~580 lines)
- [x] `docs/lifecycle/build/index.md` — Stage 07 (74 lines → ~760 lines)
- [x] `docs/lifecycle/installation/index.md` — Stage 08 (46 lines → ~580 lines)
- [x] `docs/lifecycle/pre-commissioning/index.md` — Stage 09 (46 lines → ~800 lines)
- [x] `docs/lifecycle/commissioning/index.md` — Stage 10 (60 lines → ~1000 lines)
- [x] `docs/lifecycle/maintenance/index.md` — Stage 11 (57 lines → ~1000 lines)

### Pages Created (New)
- [x] `docs/lifecycle/safety-requirements-spec/index.md` — Stage 3.5 (new)
- [x] `docs/lifecycle/management-of-change/index.md` — Stage 12 (new)

### Content Pattern (All Pages)
Each expanded lifecycle stage page includes:
- Purpose and scope summary
- Key decisions and decision criteria
- Related standards and standards guidance
- Practical guidance with checklists or step-by-step instructions
- Cross-links to related training modules, workflows, and reference material
- See Also links to adjacent lifecycle stages

### Build
- [x] Jekyll build: clean, 132 pages (no change from Phase 20)

## Phase 22 State — Semiconductor Facility Reference (In Progress)

**Last verified:** 2026-04-11

### Step 0 — Hygiene — COMPLETE
- [x] AI_READ_ACCESS headers fixed on 7 RAG files (IEC 62443 + reference models)
- [x] `validate_ai_boundaries.py` passes 305/305 (now 316/316 after RAG promotion)
- [x] `validate_reorg.sh all` passes 49/50 (archive check is pre-existing known gap)
- [x] `planning/semi_facility/` committed as draft (was untracked)

### Step 1 — Promote System and Instrumentation Notes into RAG — COMPLETE
- [x] Created `control-standards/rag/design_framework/semiconductor_facility/` with `_index.yaml`
- [x] 10 files promoted from staging with updated headers (AI_READ_ACCESS: ALLOWED, CONTENT_CLASS: DERIVED_REFERENCE):
  - `bulk_specialty_gas.md`
  - `bulk_chemical_distribution.md`
  - `upw_and_wastewater.md`
  - `exhaust_abatement_vacuum.md`
  - `hvac_and_cleanroom.md`
  - `safety_and_shutdown.md`
  - `tool_facility_interface.md`
  - `common_control_philosophy.md`
  - `instrumentation_use_matrix.md`
  - `instrumentation_selection.md`

### Step 2 — Build Jekyll Section (First Slice) — COMPLETE
- [x] `docs/industries/semiconductor/facility/index.md` — overview + standards selection flowchart + cross-cutting design threads
- [x] `docs/industries/semiconductor/facility/bulk-specialty-gas/index.md`
- [x] `docs/industries/semiconductor/facility/upw-wastewater/index.md`
- [x] `docs/industries/semiconductor/facility/exhaust-abatement/index.md`
- [x] `docs/industries/semiconductor/facility/tool-facility-interface/index.md`
- [x] `docs/industries/semiconductor/facility/instrumentation/index.md`

### Step 3 — Wire Navigation and Cross-Links — COMPLETE
- [x] `docs/_data/navigation.yml` — Semiconductor Facility sub-tree added under Industries > Semiconductor
- [x] `docs/industries/semiconductor/index.md` — Semiconductor Facility Reference table added at bottom
- [x] Jekyll build: clean, **148 pages**

### Second Slice — COMPLETE
- [x] `docs/industries/semiconductor/facility/hvac-cleanroom/index.md` — room pressure cascade, ISO 14644, particle monitoring
- [x] `docs/industries/semiconductor/facility/bulk-chemical/index.md` — storage, transfer sequencing, containment, SEMI F39/F57
- [x] `docs/industries/semiconductor/facility/safety-shutdown/index.md` — 4-layer shutdown model, cause-and-effect, SIL integration
- [x] `docs/industries/semiconductor/facility/control-philosophy/index.md` — modes, state machine, permissives/interlocks/trips, safe-state rules
- [x] Facility overview page updated to include all 9 system pages
- [x] Navigation.yml updated with 4 new entries
- [x] Semiconductor industry page cross-link table updated
- [x] Jekyll build: clean, **152 pages**

**Original planning context:**

### Baseline Reality

- Jekyll site and GitHub Pages deploy are real and working: `docs/_config.yml` + `.github/workflows/pages.yml`
- Actual build output: **142 HTML files** (earlier entries said 132 — corrected)
- Existing semiconductor coverage is **equipment-focused**, not facility-focused:
  - `docs/industries/semiconductor/index.md`
  - `docs/standards/semiconductor/index.md`
  - `docs/scenarios/semiconductor-fab-tool/index.md`
- `planning/semi_facility/` is draft-only and currently untracked in git, but is **much more complete than it looks** — see Staging Inventory below

### Staging Inventory (`planning/semi_facility/`)

The staging area already covers `build_sequence.md` Phase 1 (governance, systems map, standards gap map) and Phase 2 (normalized utility system notes). It is effectively at Phase 3 territory. The bottleneck is **promotion and presentation**, not content creation.

**systems/** — 7 normalized system notes (~80 lines each):
- `bulk_specialty_gas_systems.md`
- `bulk_chemical_distribution_and_wet_process.md`
- `upw_and_wastewater_systems.md`
- `exhaust_abatement_and_vacuum.md`
- `hvac_and_cleanroom_environment.md`
- `safety_and_shutdown_architecture.md`
- `tool_facility_interface.md`
- `common_control_philosophy.md`

**instrumentation/** — 6 files including site-ready reference material:
- `semiconductor_facility_instrumentation_use_matrix.md` (153 lines)
- `manufacturer_product_family_comparison.md` (151 lines)
- `selection_principles.md`, `measurement_and_alarm_strategy.md`, `device_family_map.md`

**standards/** — structured selection flowchart, plain-language family explanations, full candidate table (`candidate_standards_map.md`)

**sources/** — 30+ sources registered with trust labels and next-action notes (`public_source_register.md`)

Total: ~1,434 lines across 15 substantive files.

### Repo Hygiene Issues (fast fixes, do first)

- `python3 tools/validate_ai_boundaries.py` fails on **7 RAG files** missing `AI_READ_ACCESS`: all 4 IEC 62443 files + `IEC62443_lifecycle.md` + `15-Standard Minimum Compliance Stack.md`. Mechanical header fix, ~15 minutes.
- `bash tools/validate_reorg.sh all` shows 48/50 — both failures are downstream of the AI boundary script. Once the 7 files are fixed, validator passes cleanly.

### Approach

Implement the semiconductor facility reference **inside the existing Jekyll site**, not a separate repo.

- Treat it as a **facility-side utilities and interface library**, distinct from the current equipment-oriented SEMI content
- Root the Jekyll section at `/industries/semiconductor/facility/` — existing semiconductor overlay stays the entry point
- Promote system and instrumentation notes → `control-standards/rag/design_framework/semiconductor_facility/`
- Promote standards family notes → `control-standards/rag/standards_intelligence/international/semiconductor/semi_facility/`
- Add nav entry under existing Industries > Semiconductor block in `docs/_data/navigation.yml`

### Implementation Order

**Step 0 — Hygiene (15 min)**
- Add `AI_READ_ACCESS: ALLOWED` header to the 7 failing RAG files
- Commit `planning/semi_facility/` as draft (untracked, needs to be in git)
- Verify `validate_reorg.sh all` passes 50/50

**Step 1 — Promote system and instrumentation notes into RAG**

Target directory: `control-standards/rag/design_framework/semiconductor_facility/`

| Staging file | RAG target |
|---|---|
| `systems/bulk_specialty_gas_systems.md` | `bulk_specialty_gas.md` |
| `systems/bulk_chemical_distribution_and_wet_process.md` | `bulk_chemical_distribution.md` |
| `systems/upw_and_wastewater_systems.md` | `upw_and_wastewater.md` |
| `systems/exhaust_abatement_and_vacuum.md` | `exhaust_abatement_vacuum.md` |
| `systems/hvac_and_cleanroom_environment.md` | `hvac_and_cleanroom.md` |
| `systems/safety_and_shutdown_architecture.md` | `safety_and_shutdown.md` |
| `systems/tool_facility_interface.md` | `tool_facility_interface.md` |
| `systems/common_control_philosophy.md` | `common_control_philosophy.md` |
| `instrumentation/semiconductor_facility_instrumentation_use_matrix.md` | `instrumentation_use_matrix.md` |
| `instrumentation/selection_principles.md` | `instrumentation_selection.md` |

Add `AI_READ_ACCESS: ALLOWED` + `CONTENT_CLASS: DERIVED_REFERENCE` on each file at promotion. Do not restructure — content is clean.

**Step 2 — Build the Jekyll section (first slice)**

Pages to build, in order:
1. `docs/industries/semiconductor/facility/index.md` — overview + standards stack (use selection flowchart from `candidate_standards_map.md`)
2. `docs/industries/semiconductor/facility/bulk-specialty-gas/` — from promoted RAG
3. `docs/industries/semiconductor/facility/upw-wastewater/` — from promoted RAG
4. `docs/industries/semiconductor/facility/exhaust-abatement/` — from promoted RAG
5. `docs/industries/semiconductor/facility/tool-facility-interface/` — from promoted RAG
6. `docs/industries/semiconductor/facility/instrumentation/` — use matrix is essentially site-ready

Second slice (after first slice ships): HVAC, chemicals, safety/shutdown architecture.

**Step 3 — Wire navigation and crosslinks**
- Add `Semiconductor Facility` entry under Industries > Semiconductor in `navigation.yml`
- Cross-link from `docs/industries/semiconductor/index.md` into facility section
- Add See Also links on existing SEMI S2/S8/S14, IEC 61511, NFPA 79, NEC pages where relevant

### Source Files for Phase 22

- `planning/semi_facility/README.md` — corpus overview and promotion rules
- `planning/semi_facility/standards/candidate_standards_map.md` — standards targets and selection flowchart
- `planning/semi_facility/roadmap/build_sequence.md` — original 4-phase build order (Phase 1+2 already done)
- `planning/semi_facility/systems/facility_systems_map.md` — system scope boundaries
- `planning/semi_facility/sources/public_source_register.md` — source governance (30+ sources registered)
