# Project State

**Last Updated:** 2026-03-05
**Status:** Active
**Current Phase:** Phase 1 deployment pending (push + Pages enable) — Phase 2 implementation plan ready
**Delivery Target:** GitHub Pages static site for personal use

## Purpose

This file is the source of truth for the current project state, active implementation scope, and near-term backlog.

## Current Direction

Phase 1 Jekyll static site is complete and committed. Phase 2 design doc and implementation plan are written (`docs/plans/`). Next: execute Phase 2 implementation plan (print stylesheet, diagram lightbox, lunr.js search, crosswalk comparison page), then push all commits and enable GitHub Pages.

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

All Phase 1 code is committed. Branch is 2 commits ahead of origin.

1. Push: `git push`
2. Enable GitHub Pages: Settings → Pages → Source: GitHub Actions
3. Verify: `https://kyawminthu.github.io/Control-System-Tools/`

## Phase 2 Scope — Implementation Plan Ready

Plan: `docs/plans/2026-03-05-phase2-implementation.md`
Design: `docs/plans/2026-03-05-phase2-design.md`

- [ ] Task 1: Print stylesheet (`main.css` — `@media print`)
- [ ] Task 2: Diagram lightbox (`main.css` + `main.js`)
- [ ] Task 3: lunr.js CDN + `search.json` data file
- [ ] Task 4: Topnav search input + inline dropdown
- [ ] Task 5: Crosswalk comparison selector page (`/crosswalks/compare/`)
- [ ] Task 6: Push, verify deployment, update project state

## Phase 3 Backlog (after Phase 2 ships)

- Interactive standards graph
- Remaining functional-safety detail pages (when corpus is confirmed complete)
- SEMI S2/S8/S14 standard pages (not yet in corpus)

## Content Gaps (documented with badges on site)

- ISO 13849-1, IEC 62061, IEC 61508, IEC 61511 — PLANNED in corpus, not confirmed complete [TO VERIFY]
- SEMI S2/S8/S14 — NOT IN CORPUS
- IEC 60079 (hazardous area) — not confirmed in corpus
- IEC 62443 detail pages — routing reference only
- Medical, nuclear, marine class rules — not in corpus
