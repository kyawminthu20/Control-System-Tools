# Project State

**Last Updated:** 2026-03-06
**Status:** Active
**Current Phase:** Phase 1
**Delivery Target:** GitHub Pages static site for personal use

## Purpose

This file is the source of truth for the current project state, active implementation scope, and near-term backlog.

Use it to answer:

- what this project is building right now
- what is already in place
- what still needs to be implemented
- what phase the project is in

## Current Direction

Phase 1 is a personal-use GitHub Pages site that presents the repository's industrial automation standards knowledge in a web-friendly format.

The site should remain separate from the authoritative knowledge base. Authoritative engineering and standards guidance stays in `control-standards/rag/`. The website is a presentation and navigation layer on top of that content.

## Current Reality

- The repository already contains the core standards knowledge base under `control-standards/rag/standards_intelligence/`.
- The repository also contains planning and design prompts for a standards-focused web experience under `control-standards/work/design/`.
- The root Python app is still a minimal placeholder in `main.py`.
- There is not yet a real frontend, static-site build, or GitHub Pages deployment workflow.
- Local automation exists for structure summaries and automated change-log aggregation in `tools/`, with commit-time hook support targeting `project_state/change_log.md`.

## Source Of Truth By Topic

- Current phase, status, and next implementation items: `project_state/project_state.md`
- Project-level change history: `project_state/change_log.md`
- Runtime, tooling, and deployment requirements: `project_state/environment.md`
- Setup, run, validation, and deployment steps: `project_state/how_to.md`
- Authoritative standards content: `control-standards/rag/`

## Phase 1 Scope

- personal-use website only
- GitHub Pages compatible delivery
- static-site friendly architecture
- standards navigation and overview experience
- visual explanation of standards families, architecture layers, crosswalks, and scenarios

## Phase 1 Non-Goals

- no backend or server runtime
- no claim that the website itself is the authoritative standards source
- no reproduction of copyrighted standards text
- no assumption that incomplete functional-safety folders are fully populated

## What Is Already Implemented

- repository reorganization under `control-standards/`
- grouped standards layout under `us/`, `international/`, and `crosswalks/`
- scenario packages and reference models for standards routing
- root validation and automation scripts under `tools/`
- web-page planning prompts under `control-standards/work/design/`
- `project_state/` folder for operational tracking

## What Still Needs To Be Implemented

1. Choose the Phase 1 site structure for GitHub Pages.
2. Build the first static page or pages from the planning prompts.
3. Decide how web content will be sourced from authoritative files without mixing source and presentation.
4. Add the frontend asset structure for the GitHub Pages site.
5. Add a deployment workflow for GitHub Pages.
6. Add lightweight validation for site generation or content sync if needed.
7. Extend automation if desired so project-state updates become easier and less manual.

## Current Priorities

1. Keep project tracking current in `project_state/`.
2. Move from planning prompts to a concrete page implementation plan.
3. Keep the website layer aligned with the authoritative corpus and its boundaries.
4. Keep Phase 1 simple enough to ship as a personal-use static site.

## Constraints And Risks

- The authoritative standards content is uneven in depth across families, especially in some functional-safety areas.
- GitHub Pages requires a static-friendly delivery approach.
- The project should not blur the boundary between authoritative source content and presentation-layer summaries.
- Current runtime/application code does not yet represent the intended website.
