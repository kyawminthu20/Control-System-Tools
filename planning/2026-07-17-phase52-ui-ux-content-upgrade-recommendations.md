# Phase 52 — UI/UX and Content Upgrade Recommendations

**Recorded:** 2026-07-17

**Status:** Proposed for owner review; no site implementation is authorised by this document

**Scope:** Published Jekyll field guide (`docs/`) and the project-state records that govern it

**Does not change:** Phase 49c remains unauthorised; no AI/ML authority ceiling or technical claim changes here

## Executive recommendation

The project does not need a visual rewrite or a new site framework. Its technical-manual design is
appropriate, the release gate is healthy, and the canonical taxonomy is already governed. The next
upgrade should make the existing depth easier to find, easier to assess, and easier to maintain.

Run Phase 52 as five bounded slices, in this order:

1. correct status and navigation defects;
2. make discovery work on mobile and tablet;
3. add task-first entry routes over the canonical taxonomy;
4. strengthen review metadata and high-risk content trust signals; and
5. consolidate the UI into reusable components and verify accessibility.

Pause broad content expansion while the highest-value pages are revalidated. New material may still
ship when it closes a documented safety, standards, or workflow gap.

## Audit baseline

The recommendation is based on the repository and generated site as of commit `abcc933`.

- `master` was clean and synchronized before this planning branch was created.
- Full release check: passed.
- Python tests: 180 passed; doctests: 10 passed.
- Jekyll build: clean; internal links: zero broken across 378 rendered files.
- Corpus boundary and quality checks: all 380 current AI-readable files passed at the latest Slice G
  delivery (the local planning audit immediately before Slice G saw 378).
- Reader-facing index pages inspected: 248.
- Legacy pages without a `review:` block: 166.
- Pages carrying governed status: 72 Review pending, 7 Partial coverage, 2 Reviewed, and 1 Needs
  revalidation.
- Duplicate URLs in `docs/_data/navigation.yml`: 6.
- UI surface: `docs/assets/css/main.css` is 2,722 lines and `docs/assets/js/main.js` is 579 lines.
- Mobile breakpoint currently hides search; tablet breakpoint removes the context panel.

The in-app visual browser was unavailable during the audit. Findings therefore come from the built
output, templates, data, CSS, JavaScript, release checks, and deployment record. Phase 52.2 must
include real-device/browser verification before it is complete.

## Product principles

1. **Task-first entry, taxonomy-stable storage.** Keep the governed top-level taxonomy. Add task
   journeys as an entry layer rather than inventing new top-level sections.
2. **Trust before breadth.** Make edition, coverage, status, and source limitations visible before
   adding more pages.
3. **Progressive disclosure.** Lead with the decision and workflow; keep clause depth and reference
   material available without forcing every reader through it.
4. **Mobile is an engineering use case.** Search, page outline, review facts, and related material
   must remain available on phones and tablets used in the field.
5. **Canonical data drives presentation.** Filters, badges, and status summaries derive from governed
   frontmatter or data files; JavaScript does not invent classifications.
6. **Accessibility is a release property.** Keyboard operation, focus management, contrast, reflow,
   and screen-reader state are acceptance criteria, not later polish.

## Phase 52.1 — State accuracy and navigation hygiene

**Priority:** P0

**Implementation authority:** Safe to begin after owner accepts this recommendation

### Work

- Replace stale current-phase labels in `project_state/project_state.md` with a short, factual current
  delivery and follow-up queue.
- Reconcile the six repeated navigation URLs:
  - `/lifecycle/guides/commissioning-templates/`
  - `/communications/ethernet-fundamentals/`
  - `/communications/ethernet-ip/`
  - `/communications/modbus-rtu-rs485/`
  - `/communications/dnp3/`
  - `/communications/wireshark-methodology/`
- Keep intentional cross-listings only when the second placement has a different, explicit label or
  relationship; otherwise remove the duplicate.
- Correct the Phase 50.5 tracking statement: the licensed-table work is already on `master`.
- Add a small current-state summary and move historical narrative under `project_state/history/` as
  already planned in Phase 50.8. Do this as a separate slice so history remains reviewable.

### Acceptance

- Current phase, current delivery, next action, owner decisions, and blocked work are discoverable in
  the first 40 lines of `project_state.md`.
- No tracking statement contradicts `git log`.
- Navigation contains no unexplained duplicate URL.
- Jekyll build and internal-link check remain green.

## Phase 52.2 — Mobile discovery and responsive context

**Priority:** P0

### Work

- Keep search available below 768 px. Use a header search action opening a full-width dialog or
  dedicated search panel; do not require the desktop input to fit in the mobile bar.
- Add search result facets derived from page metadata: section, page type, lifecycle stage, standards
  family, and review status. Preserve the selected state in query parameters.
- Replace the context panel's tablet disappearance with a collapsible **Page facts and related
  material** drawer containing review metadata, related standards, lifecycle links, and repository
  source path.
- Add a compact mobile **On this page** outline for long pages.
- Update the mobile sidebar button and drawer to maintain `aria-expanded`, trap focus while open,
  close on Escape, and restore focus to the trigger.
- Wrap wide tables in labelled horizontal-scroll containers and keep sticky headers local to those
  containers.

### Acceptance

- Search is keyboard- and touch-operable at 320, 375, 768, 1024, and desktop widths.
- Search and drawers remain useful without a pointing device.
- No content or control is lost solely because the context panel is hidden.
- Tables reflow or scroll without forcing whole-page horizontal scrolling.
- Manual checks pass in current Safari, Chrome, and Firefox, including light and dark modes.

## Phase 52.3 — Task-first information architecture

**Priority:** P1

### Work

Keep the governed navigation taxonomy, but make four questions the primary entry routes:

1. What am I designing?
2. Where will it be installed?
3. Which lifecycle stage am I in?
4. What problem am I troubleshooting?

- Simplify the homepage's first journey to the standards finder, core scenarios, lifecycle entry,
  and troubleshooting. Move standards families, industries, graph, and source-browser detail into a
  secondary **Explore the field guide** region.
- Extend the local-section sidebar pattern beyond its training pilot to large Standards, Design,
  Lifecycle, Communications, and Tools sections.
- Give each local sidebar the current section, page sequence, on-page outline, parent landing page,
  and related workflow—not the entire global tree.
- Add clear **Start here**, **Next step**, and **Use this when** language to section landing pages.
- Do not create a new top-level navigation section without the owner decision required by
  `governance/PROJECT_ORGANIZATION.md`.

### Acceptance

- A new reader can reach an applicable standards path from the homepage in no more than two choices.
- A returning reader can search from every viewport.
- A reader within a deep section can identify parent, current page, adjacent page, and related
  workflow without returning to the homepage.
- No page becomes orphaned and top navigation remains consistent with the sidebar taxonomy.

## Phase 52.4 — Editorial trust and content depth

**Priority:** P0 for safety/standards pages; P1 for the broader rollout

### Work

- Rebuild IEC 62061 from the consolidated 2021+AMD1:2024+AMD2:2026, CSV Edition 2.2 source. It is the
  only page currently at Needs revalidation and must be rebuilt rather than patched.
- Roll out `review:` metadata to the 166 legacy pages in risk order. Do not bulk-mark any page
  Reviewed. Record explicit exemptions for non-content or redirect pages so the release metric is
  meaningful.
- First author-review queue:
  1. standards finder and homepage decision claims;
  2. NEC, NFPA 79, UL 508A, IEC 60204-1, IEC 62061, ISO 12100, and ISO 13849-1;
  3. commissioning, maintenance, and wiring guides;
  4. highest-use scenarios; and
  5. the eight Review-pending AI-integration pages.
- Replace aggregate family-level Reviewed badges unless every represented claim is covered by the
  status. Prefer computed summaries such as **2 reviewed · 3 pending · 1 partial**.
- Review homepage language that can overstate legal enforcement or equivalence. Put jurisdiction,
  adoption, AHJ, and scope caveats next to the relevant choice.
- Add a standard quick-decision block to technical pages:
  - applies when;
  - does not apply when;
  - required inputs;
  - expected output;
  - governing references; and
  - verification status.
- Split very long lifecycle pages into an overview, procedure, checklist, and reference layer when
  the current page exceeds a practical single-task scope. Preserve redirects for any URL moves.
- Link applicable field-guide pages to verified `cst` commands, expected outputs, citations, and
  SAMPLE-data warnings so the site and toolkit operate as one product.

### Acceptance

- IEC 62061 no longer carries Needs revalidation after owner review; AI work alone cannot mark it
  Reviewed.
- Every reader-facing technical page either has governed review metadata or a documented exemption.
- Homepage badges do not imply broader review coverage than the underlying pages support.
- High-risk pages lead with applicability and limitations before detailed instruction.
- Toolkit examples show provenance and visibly distinguish SAMPLE results from design-use results.

## Phase 52.5 — UI component consolidation and accessibility gate

**Priority:** P1; begin after the interaction patterns in 52.2–52.3 are accepted

### Work

- Inventory repeated UI patterns and extract includes/classes for page headers, trust strips,
  cards, callouts, responsive tables, local navigation, filters, empty states, and pagination.
- Split the monolithic stylesheet and script by component or responsibility while preserving the
  no-framework, GitHub Pages-compatible architecture.
- Remove repeated inline styles from content pages and route them through governed components.
- Establish design tokens for spacing, type scale, control sizes, focus rings, status colours, and
  content widths. Status meaning must never depend on colour alone.
- Add an automated HTML/accessibility check to the site profile, plus a small manual matrix for
  keyboard, screen-reader announcements, 200% zoom, reduced motion, print, and dark mode.
- Consider build-time Mermaid rendering only as a separately measured enhancement for no-JavaScript
  reading and indexing; current live rendering is known to work.

### Acceptance

- New pages can be built from documented components without copying page-specific style blocks.
- All interactive controls expose name, role, state, and visible keyboard focus.
- The site remains usable at 200% zoom and 320 CSS px without loss of information.
- Light, dark, print, no-JavaScript, and Mermaid-failure states have deliberate fallbacks.
- Full release gate and the new accessibility checks pass.

## Deferred and owner decisions

The following are not silently authorised by this recommendation:

- Phase 49c chemical/biological authority work remains blocked on evidence closure, adversarial
  review, and explicit owner authorisation.
- The Phase 50.13 AI method-selector classification vocabulary still needs owner sign-off before
  canonical data or selector implementation changes.
- Analytics require a privacy decision: purpose, events, retention, disclosure, and whether current
  Google Analytics remains appropriate. Do not add behavioural tracking as part of a UI slice by
  default.
- Only the owner may mark AI-drafted pages Reviewed.

## Follow-up order

| Order | Slice | Outcome | Depends on |
|---:|---|---|---|
| 1 | 52.1 | Accurate state and clean navigation | Owner accepts recommendation |
| 2 | 52.2 | Mobile search, responsive context, accessible drawers/tables | 52.1 |
| 3 | 52.4a | IEC 62061 rebuild + high-risk trust corrections | Licensed/current references + owner review |
| 4 | 52.3 | Task-first homepage and local navigation | 52.2 interaction pattern |
| 5 | 52.4b | Review-metadata rollout and content layering | Exemption policy + owner review capacity |
| 6 | 52.5 | Component consolidation and accessibility gate | 52.2–52.3 patterns stable |

Every implementation slice follows the normal branch → build → verification → project-state update
→ commit → fast-forward merge → deploy verification loop. This planning document itself makes no
content claim Reviewed and changes no site behaviour.
