# Project Change Log

**Last Updated:** 2026-03-08
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
- Source file: `control-standards/work/design/Grounding, System and Equipment [250.4, 2020 NEC].md` (raw transcript — not committed to RAG).
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

