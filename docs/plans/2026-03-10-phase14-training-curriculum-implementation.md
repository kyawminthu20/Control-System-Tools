# Phase 14: Training Curriculum Upgrade - Implementation Plan

**Goal:** Convert `/training/` from a flat module directory into a curriculum-style landing page and group-page system with learner entry points, learning paths, metadata-aware tables, and standards cross-links.

**Architecture:** Keep the current training URLs and module pages intact. Introduce a shared data source in `docs/_data/`, add training-specific UI styles, then rewrite the landing and group pages to render from the catalog.

**Tech Stack:** Jekyll 4.x, Markdown, Liquid, existing site CSS, vanilla JS. No new dependencies.

**Design doc:** `docs/plans/2026-03-10-phase14-training-curriculum-design.md`

## Before You Start

Read these files first:

- `docs/training/index.md`
- `docs/training/fundamentals/index.md`
- `docs/training/electrical-machines/index.md`
- `docs/training/nec-application/index.md`
- `docs/_layouts/default.html`
- `docs/assets/css/main.css`
- `project_state/project_state.md` (Phase 14 section)

Build command:

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build
```

Expected result: clean build with no Liquid or front matter errors.

## Task 1: Add the shared training catalog model

**Files:**

- Create: `docs/_data/training_catalog.yml`

**Work:**

- Add top-level sections for:
  - `intro`
  - `verification_note`
  - `start_here`
  - `learning_paths`
  - `topic_groups`
  - `related_standards`
  - `modules`
- Populate all 24 current modules with at least:
  - title
  - URL
  - group
  - display group label
  - short outcome-focused summary
  - level
  - time estimate
  - focus
  - type
  - prerequisites
  - badges
- Mark the most important modules as `featured: true` so they can receive stronger visual treatment.

**Notes:**

- Keep URLs aligned with the current pages.
- Use the stronger display labels but do not rename directory paths.
- Keep NEC track metadata honest; do not imply coverage that does not yet exist.

## Task 2: Add training UI assets

**Files:**

- Modify: `docs/assets/css/main.css`

**Work:**

- Add CSS for:
  - top verification note
  - start-here cards
  - learning-path cards
  - training chips / badges
  - table wrapper and responsive table behavior

**Implementation guidance:**

- Keep the markup compatible with later filter work.
- The Phase 14 page should still be fully usable without any training-specific JS.

## Task 3: Rewrite the landing page

**Files:**

- Modify: `docs/training/index.md`

**Work:**

- Replace the current intro with learner-oriented copy from the design doc.
- Add the short verification note near the top.
- Add a `Start Here` section with three audience entry points:
  - new to industrial controls
  - working with motors and drives
  - designing control panels or machines
- Add a `Learning Paths` section with:
  - Controls Engineering Foundations
  - Motor and Drive Engineering
  - Industrial Panel Design (NEC Focus)
  - Troubleshooting and Field Service
- Add `Browse by Topic` cards using these display labels:
  - Electrical Fundamentals
  - Motors, Drives, and Motion
  - NEC for Machines and Panels
- Replace the flat markdown list with a data-driven `All Modules` table.
- Add a `Related Standards` section linking to NEC, UL 508A, NFPA 79, and IEC 60204-1.

**Acceptance criteria:**

- A first-time visitor can identify where to start within seconds.
- The page reads as a curriculum hub, not only a repository index.
- Metadata makes it possible to scan the catalog without opening every module page.

## Task 4: Upgrade the three group pages

**Files:**

- Modify: `docs/training/fundamentals/index.md`
- Modify: `docs/training/electrical-machines/index.md`
- Modify: `docs/training/nec-application/index.md`
- Modify: `docs/_includes/sidebar.html`

**Work:**

- Update each group page to use the new display labels while keeping URLs unchanged.
- Add a short group-specific intro that states who the group is for.
- Add a small `Recommended entry modules` subsection near the top of each group page.
- Replace topic-only tables with metadata-rich tables driven from `training_catalog.yml`.
- Update sidebar labels to match the stronger display names.

**Notes:**

- Sidebar links must keep the same destinations.
- If the shorter URL-facing labels are still needed for space, keep the full names on page headings and use concise sidebar variants only if necessary.

## Task 5: QA the landing-page standards gateway and trust-boundary placement

**Files:**

- Modify only if needed: `docs/training/index.md`

**Work:**

- Confirm the top verification note complements the existing trust-boundary include instead of duplicating it.
- Verify the `Related Standards` section routes correctly to:
  - `/standards/us-electrical/nec/`
  - `/standards/us-electrical/ul-508a/`
  - `/standards/us-electrical/nfpa-79/`
  - `/standards/machinery/iec-60204-1/`
- Ensure the page still works when users scroll directly to the bottom trust boundary.

## Task 6: Build and review

**Checks:**

- Run a full Jekyll build.
- Open `/training/` locally and test:
  - desktop table readability
  - mobile stacking behavior
  - badge rendering
  - topic-card links
  - standards links
- Spot check the three group pages for heading, copy, and table consistency.

## Suggested Implementation Order

1. Data model
2. CSS support
3. Landing page rewrite
4. Group page rewrites
5. Sidebar label update
6. Full build and manual review
7. Update `project_state/` and `project_state/change_log.md` after implementation

## Explicit Deferrals to Later Phases

### Phase 15

- Add page-scoped JS support in `docs/_layouts/default.html` if the final filter approach needs it
- Add lightweight landing-page filters for level, topic, and application
- Add metadata chips and expected outcomes to individual module pages
- Standardize per-module related-standards blocks
- Expand filtering or sorting if the first pass is too limited

### Phase 16

- Add new NEC training modules in the canonical RAG layer
- Publish matching NEC training pages
- Rebalance the landing page once NEC coverage is no longer only three modules

## Out of Scope

- Adding new RAG modules in Phase 14
- Rewriting every individual training module page now
- Changing URL slugs or folder names
- Adding external JS libraries
