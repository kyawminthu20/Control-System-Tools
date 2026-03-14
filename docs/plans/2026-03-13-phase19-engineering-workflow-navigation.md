# Phase 19 — Engineering Workflow Navigation Refactor

**Date:** 2026-03-13
**Status:** Planning
**Depends on:** Phase 18 Track B/C complete (`/field-engineering/` and `/reference/` surfaced)

## Goal

Refactor the site navigation toward an engineering-workflow model without changing existing
content URLs. Phase 19 introduces workflow-oriented hub pages and a data-driven sidebar so
the site feels like an engineering navigation system rather than a repository index.

## Implementation boundaries

- Keep all current page URLs stable in this phase
- No redirects, page moves, or section renames in the initial implementation
- Do not create empty top-level sections for technologies, calculators, or broad troubleshooting
- Consume `/field-engineering/` and `/reference/` as dependencies from Phase 18 rather than redefining them

## Target information architecture

### Top-level sidebar groups

The Phase 19 sidebar will use these top-level groups:

1. Engineering Workflow
2. Standards
3. Training
4. Industries
5. Reference

### Demoted repo-shaped sections

These remain reachable but no longer appear as peer top-level groups:

- Scenarios
- Crosswalks
- Workflows

They are surfaced inside the new hub structure:

- `Engineering Workflow` links lifecycle pages, workflow pages, and field-engineering checklists
- `Reference` links glossary, software stack, RAG browser, and crosswalk entry points
- Scenarios remain discoverable through workflow and industry routing pages

## New site entrypoints

Phase 19 plans around these section destinations:

- `/engineering-workflow/`
- `/reference/`
- `/field-engineering/`

### Hub page intent

- `docs/engineering-workflow/index.md`
  - Landing page for engineer-intent routing
  - Groups lifecycle stages, practical workflows, and field checklists by task
- `docs/reference/index.md`
  - Landing page for fast-lookup content
  - Groups glossary, software stack, RAG browser, crosswalks, and future equations / architecture references
- `docs/field-engineering/index.md`
  - Produced in Phase 18 Track B and consumed by the new workflow-first navigation

## Navigation data model

Replace the hardcoded sidebar markup in `docs/_includes/sidebar.html` with a renderer backed by:

- `docs/_data/navigation.yml`

### Required capabilities

The data model must define the full sidebar hierarchy in one place and support:

- section label
- section destination URL
- nested child links
- optional nested grandchildren
- active-state derivation by URL prefix
- open/expanded state derivation by current page URL

### Recommended shape

Each top-level section should support:

```yaml
- label: "Engineering Workflow"
  url: "/engineering-workflow/"
  match_prefixes:
    - "/engineering-workflow/"
    - "/lifecycle/"
    - "/workflows/"
    - "/field-engineering/"
  children:
    - label: "Lifecycle"
      url: "/lifecycle/"
    - label: "Workflows"
      url: "/workflows/"
    - label: "Field Engineering"
      url: "/field-engineering/"
```

The sidebar include should render from this data rather than from manually duplicated HTML.

## Content mapping

### Engineering Workflow

Use existing content, grouped by task:

- `lifecycle/`
- `workflows/`
- `field-engineering/`
- selected scenario entry points where they support design/build/verify/operate navigation

### Standards

Keep the existing standards destinations as their own top-level reference area:

- `standards/`
- standards family pages
- standards graph

### Training

Keep the current training section as a top-level destination:

- `training/`
- topic-group landing pages

### Industries

Keep the current industry matrix and industry overlays as a top-level destination:

- `industries/`
- industry detail pages

### Reference

Group quick-reference and meta/reference content:

- `reference/`
- `glossary/`
- `software-stack/`
- `rag-browser/`
- crosswalk entry points
- future equations and machine-architecture reference pages

## Migration steps

1. Add `docs/_data/navigation.yml` with the full Phase 19 sidebar hierarchy.
2. Refactor `docs/_includes/sidebar.html` to render from navigation data.
3. Add `docs/engineering-workflow/index.md` as the new workflow-first hub.
4. Add `docs/reference/index.md` as the new fast-lookup hub.
5. Wire `field-engineering/` and `reference/` into the new sidebar once Phase 18 Track B/C pages exist.
6. Remove Scenarios, Crosswalks, and Workflows as top-level sidebar peers by routing them through the new grouped navigation.
7. Preserve all direct URLs so legacy bookmarks and internal links continue to work unchanged.

## Acceptance criteria

- Jekyll build completes cleanly after the sidebar is moved to a data-driven model
- Existing direct URLs remain valid and unchanged
- Sidebar renders all major site destinations without broken links
- `/engineering-workflow/` correctly routes to lifecycle, workflows, and field-engineering content
- `/reference/` correctly routes to glossary, software stack, rag browser, crosswalks, and future quick-reference material
- Active/open sidebar state works correctly for:
  - standards pages
  - training pages
  - workflow pages
  - lifecycle pages
  - engineering-workflow hub pages
  - reference hub pages
  - field-engineering pages
- Mobile and desktop sidebar behavior remains usable with the new grouped structure

## Out of scope

- Moving existing content into new URL trees
- Renaming current sections or adding redirects
- Creating a full technologies section
- Creating a broad tools/calculators section
- Building a general troubleshooting section beyond currently surfaced content

