# Phase 17 — Cross-Layer Knowledge Routing

**Date:** 2026-03-11
**Status:** Active
**Decision:** Workflows as first-class `/workflows/` site section (Option A)

## Goal

Turn the site from isolated documentation sections into a connected engineering knowledge
system. Training pages become gateways into standards, workflows, lifecycle stages, and
applied scenarios. Workflows surface as a first-class destination.

## Scope

### Task 1 — `/workflows/` landing page + sidebar

- `docs/workflows/index.md` — landing page with workflow cards by category
- `docs/_includes/sidebar.html` — Workflows section added

### Task 2 — Motor system workflow pages

Source: `control-standards/rag/design_framework/motor_systems/`

- `docs/workflows/motor-selection/index.md` — Motor Selection Workflow
- `docs/workflows/motor-troubleshooting/index.md` — Motor Troubleshooting Decision Tree
- `docs/workflows/vfd-commissioning/index.md` — VFD Commissioning Workflow
- `docs/workflows/servo-commissioning/index.md` — Servo Commissioning Workflow

### Task 3 — Electrical review workflow page

Source: `control-standards/rag/design_framework/electrical_review/`

- `docs/workflows/electrical-review/index.md` — Electrical Review Workflow
  (Ohm's law checks, network review, component sanity, signal/interface notes)

### Task 4 — Cross-layer data model extension

- `docs/_data/training_catalog.yml` — add `related_workflows` field to relevant modules
- `docs/_layouts/training-module.html` — render Related Workflows block on module pages

### Task 5 — Training module cross-links

Update `related_workflows` in catalog for:
- Motor training modules (induction, nameplates, VFD, servo) → motor workflows
- NEC application modules (SCCR, Art 430, Art 409) → relevant design-framework workflows
- Electrical fundamentals modules → electrical review workflow

Workflow pages include a "Related Training" block linking back.

### Task 6 — Machine Lifecycle training path

Add a new named learning path to `training_catalog.yml`:

- **Machine Lifecycle Engineering** — routes concept → design → safety → commissioning → troubleshooting
- Uses existing modules; no new module pages required

### Task 7 — Jekyll build validation

Clean build, verify cross-links.

## Out of Scope (Phase 18+)

- Commissioning checklists as site pages (Field Engineering section)
- Reference Library (equations, machine architecture)
- Control Systems training track (needs new RAG corpus)
- US/EU Compliance Wizard as interactive site tool

## Acceptance Criteria

- `/workflows/` exists as a sidebar destination with 5+ workflow pages
- Every workflow page links to related training modules
- Motor and NEC training pages surface Related Workflows blocks
- Machine Lifecycle path visible on training landing
- Jekyll build: clean
