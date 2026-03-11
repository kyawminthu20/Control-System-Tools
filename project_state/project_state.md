# Project State

**Last Updated:** 2026-03-10
**Status:** Active
**Current Phase:** Phase 14 COMPLETE — Training Curriculum Upgrade
**Next Phase:** Phase 15 QUEUED — Training Metadata and Module UX
**Delivery Target:** GitHub Pages static site for personal use

## Purpose

This file is the source of truth for the current project state, active implementation scope, and near-term backlog.

## Current Direction

Phase 13 is complete and the site is live on GitHub Pages. The next work shifts from corpus breadth to training experience depth. The immediate queue is to turn `/training/` from a browsable module index into a guided learning system with clearer entry points, learning paths, module metadata, and stronger NEC application coverage.

The site is a presentation and navigation layer on top of `control-standards/rag/`. Authoritative engineering and standards guidance stays in `control-standards/rag/`. The website never modifies RAG content.

## Current Reality

- Jekyll site deployed on GitHub Pages — `https://kyawminthu20.github.io/Control-System-Tools/`
- Jekyll build: ~60 pages, clean build (0.27 s locally)
- Three-panel layout (sidebar 240px + main content + context panel 220px)
- Mermaid.js CDN integration for all diagrams; Cytoscape.js 3.28.1 for interactive standards graph
- Google Analytics tag installed sitewide in `docs/_layouts/default.html` using measurement ID `G-RPL3G47EFZ`
- GitHub Actions deployment workflow at `.github/workflows/pages.yml`
- Site covers: homepage, all standards families (US Electrical, Machinery, Functional Safety, Cybersecurity, Hazardous Area, Semiconductor), 11 lifecycle stages + safety wiring, 8 scenarios, 3 crosswalks, 9 industry overlays (2 fully deepened), glossary (28 terms), software stack, about page
- Interactive standards graph: 12 nodes, 14 edges (does not yet include IEC 60079, IEC 61511, SEMI)
- Training section exists: 24 modules across 3 groups, but the landing page still behaves more like a browseable index than a guided curriculum
- Root `main.py` remains a placeholder (not the site)

## Source Of Truth By Topic

- Current phase, status, and next implementation items: `project_state/project_state.md`
- Project-level change history: `project_state/change_log.md`
- Runtime, tooling, and deployment requirements: `project_state/environment.md`
- Setup, run, validation, and deployment steps: `project_state/how_to.md`
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

## Phase 1 — SHIPPED (pending push + Pages enable)

All Phase 1 code is committed.

1. Push: `git push`
2. Enable GitHub Pages: Settings → Pages → Source: GitHub Actions
3. Verify: `https://kyawminthu20.github.io/Control-System-Tools/`

## Phase 2 Scope — COMPLETED

Plan: `docs/plans/2026-03-05-phase2-implementation.md`
Design: `docs/plans/2026-03-05-phase2-design.md`

- [x] Task 1: Print stylesheet (`main.css` — `@media print`)
- [x] Task 2: Diagram lightbox (`main.css` + `main.js`)
- [x] Task 3: lunr.js CDN + `search.json` data file
- [x] Task 4: Topnav search input + inline dropdown
- [x] Task 5: Crosswalk comparison selector page (`/crosswalks/compare/`)
- [ ] Task 6: Push + enable GitHub Pages (manual step)

## Phase 3 Backlog (after Phase 2 ships)

- Interactive standards graph
- Remaining functional-safety detail pages (when corpus is confirmed complete)
- SEMI S2/S8/S14 standard pages (not yet in corpus)

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

## Phase 15 Scope — Training Metadata And Module UX — QUEUED

**Goal:** Make the training catalog scannable by difficulty, effort, prerequisite knowledge, and job context.

### Metadata model
- [x] `docs/_data/training_catalog.yml` exists with level, time, type, focus, prerequisites, featured flag for all 24 modules (completed in Phase 14)
- [ ] Classify modules with additional status markers such as Code-heavy, Field-useful, Design-critical if needed
- [ ] Normalize per-module related-standards blocks on individual module pages

### Page/application work
- [ ] Surface metadata chips on the training landing page, group pages, and individual module pages
- [ ] Add expected outcomes to module summaries so users know what they will be able to do after finishing each module
- [ ] Normalize all module blurbs to practical, outcome-based wording
- [ ] If complexity stays reasonable in Jekyll, add filtering or sorting by level, type, and job focus
- [ ] Acceptance target: users should be able to choose a module without opening multiple pages just to discover difficulty or prerequisites

## Phase 16 Scope — NEC Training Expansion — QUEUED

**Goal:** Rebalance the training catalog so NEC application is not limited to only three modules.

### Canonical RAG additions
- [ ] Expand `control-standards/rag/training_modules/nec_application/` from 3 modules to at least 8-10 modules before corresponding site pages are considered complete
- [ ] Add training modules for branch circuits vs. feeders for motor loads
- [ ] Add training modules for disconnecting means for machinery
- [ ] Add training modules for grounding and bonding basics for control panels
- [ ] Add training modules for SCCR workflow for industrial control panels
- [ ] Add training modules for conductor and OCPD sizing worked examples
- [ ] Add training modules for Class 1 / Class 2 / remote-control circuits
- [ ] Add training modules for practical Article 430 workflow
- [ ] Add training modules for practical Article 409 workflow

### Site follow-through
- [ ] Publish matching site pages under `docs/training/nec-application/`
- [ ] Rebalance the `/training/` landing page so NEC work is visibly represented alongside fundamentals and machines
- [ ] Cross-link new NEC modules into standards and crosswalk pages where useful
- [ ] Acceptance target: the NEC track should support practical machine and panel design work, not only code-navigation basics

## Post-Phase 16 Planning Candidate — Training System Integration

Planning note: `docs/plans/2026-03-10-training-system-integration-preplan.md`

Not queued yet. This is a preparation note for the phase after the current training roadmap.

Target themes:

- connect Training -> Standards -> Application layers
- publish a new control-systems training route on the site once the current training roadmap is finished
- decide where advanced public-source engineering pages belong, starting with PID/drone material and a paraphrased Archer-vs-Joby eVTOL motor comparison
- decide whether workflows become a first-class site section or remain distributed through lifecycle/scenario/training routes
- surface field engineering and commissioning checklists as a site destination
- build a reference-library route for equations, machine architecture, and quick-reference content
- add safety and machine-architecture training once the current curriculum and NEC phases are complete
