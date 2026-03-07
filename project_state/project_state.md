# Project State

**Last Updated:** 2026-03-06
**Status:** Active
**Current Phase:** Phase 3 in progress — ISO 13849-1 RAG corpus complete; IEC 62061 next
**Delivery Target:** GitHub Pages static site for personal use

## Purpose

This file is the source of truth for the current project state, active implementation scope, and near-term backlog.

## Current Direction

Phase 1 and Phase 2 are complete and committed. All Phase 2 features have been implemented: print stylesheet, diagram lightbox, lunr.js inline search, and crosswalk comparison selector. Next: push all commits and enable GitHub Pages (Settings → Pages → Source: GitHub Actions).

The site is a presentation and navigation layer on top of `control-standards/rag/`. Authoritative engineering and standards guidance stays in `control-standards/rag/`. The website never modifies RAG content.

## Current Reality

- Jekyll site implemented under `docs/` — 48 HTML pages build successfully
- Three-panel layout (sidebar 240px + main content + context panel 220px)
- Mermaid.js CDN integration for all diagrams
- GitHub Actions deployment workflow at `.github/workflows/pages.yml`
- Site covers: homepage (8 blocks), all standards families, 11 lifecycle stages, 5 scenarios, 3 crosswalks, 9 industry overlays, software stack, about page
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
3. Verify: `https://kyawminthu.github.io/Control-System-Tools/`

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

## Phase 4 Queue — Practical Safety Guides (next after Phase 3)

**Source:** `control-standards/work/design/simple_safety_system_design.md`

Two new site pages to surface practical machine safety knowledge from the design file:

### Page 1 — New Scenario: Practical Machine Safety Implementation
- **File:** `docs/scenarios/machine-safety-implementation/index.md`
- **Label:** Scenario 05
- **Content:** 10-step machine builder workflow (risk assessment → safety functions → hardware architecture → validation), SIL/PL equivalence table, Category B/1/2/3/4 selection, example machine safety stack (hydraulic + chemical machine), hardware device selection and vendors
- **Standards referenced:** ISO 13849-1, IEC 62061, IEC 61508, NFPA 79
- **Mermaid diagram:** Input → Safety PLC → Output flow

### Page 2 — New Lifecycle Page: Safety Wiring Practices
- **File:** `docs/lifecycle/safety-wiring/index.md`
- **Content:** 24 VDC rationale (SELV, device ecosystem, diagnostics), NC vs NO contact logic (fail-safe default), wire gauge (18 AWG), color coding (NFPA 79/UL 508A), termination (ferrules, spring clamps, vibration resistance), discrepancy time (20–100 ms guidance), baseline dual-channel input spec
- **Standards referenced:** NFPA 79, IEC 60204-1, IEC 61140

### Nav / index updates also required
- `docs/scenarios/index.md` — add Scenario 05 entry
- `docs/lifecycle/index.md` — add safety-wiring stage entry
- `docs/lifecycle/safety-architecture/index.md` — add "See also: Safety Wiring Practices" link
- `docs/lifecycle/detailed-design/index.md` — add cross-reference to wiring page

### Notes
- No new RAG files needed; source doc is already in `control-standards/work/design/`
- Do not fragment content across existing lifecycle pages

## Content Gaps (documented with badges on site)

- ISO 13849-1 — Phase 3 corpus complete (6 RAG files)
- IEC 62061, IEC 61508, IEC 61511 — PLANNED in corpus, not confirmed complete [TO VERIFY]
- SEMI S2/S8/S14 — NOT IN CORPUS
- IEC 60079 (hazardous area) — not confirmed in corpus
- IEC 62443 detail pages — routing reference only
- Medical, nuclear, marine class rules — not in corpus
