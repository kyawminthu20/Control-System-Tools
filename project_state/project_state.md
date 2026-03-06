# Project State

**Last Updated:** 2026-03-06
**Status:** Active
**Current Phase:** Phase 1 — Jekyll site built, pending GitHub Pages deployment
**Delivery Target:** GitHub Pages static site for personal use

## Purpose

This file is the source of truth for the current project state, active implementation scope, and near-term backlog.

## Current Direction

Phase 1 Jekyll static site is implemented under `docs/`. GitHub Actions workflow is in place at `.github/workflows/pages.yml`. Final step: enable GitHub Pages in repo settings (Source: GitHub Actions).

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

## Remaining Steps to Ship

1. Commit all changes: `git add docs/ .github/ .gitignore`
2. Push to GitHub: `git push`
3. Enable GitHub Pages in repo settings: Settings → Pages → Source: GitHub Actions
4. Verify deployment runs and site is accessible at `https://kyawminthu.github.io/Control-System-Tools/`

## Phase 2 Backlog (after Phase 1 ships)

- Client-side search (lunr.js)
- Diagram lightbox/zoom
- Comparison mode for crosswalks
- Standards detail pages (functional-safety pages when corpus is complete)
- Interactive standards graph

## Content Gaps (documented with badges on site)

- ISO 13849-1, IEC 62061, IEC 61508, IEC 61511 — PLANNED in corpus, not confirmed complete [TO VERIFY]
- SEMI S2/S8/S14 — NOT IN CORPUS
- IEC 60079 (hazardous area) — not confirmed in corpus
- IEC 62443 detail pages — routing reference only
- Medical, nuclear, marine class rules — not in corpus
