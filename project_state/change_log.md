# Project Change Log

**Last Updated:** 2026-07-10 (Tools Suite Phases 0–1 — repo hygiene + `cst` Python package)
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

## 2026-07-11 — Tools Suite Phase 2 — NEC/UL calculators

**Type:** Feature (cst package expansion)
**Status:** Complete on `feat/cst-phase2`.

- `cst.calc.ampacity` — NEC 310.15: base ampacity from user table, ambient correction via the 310.15(B) equation, bundle adjustment per Table 310.15(C)(1).
- `cst.calc.motor_branch` — full Art. 430 chain: table FLC → conductors at 125 % (430.22) → OCPD max per Table 430.52(C)(1) with next-size-up (240.6(A)) → overload per 430.32(A)(1) from nameplate FLA.
- `cst.calc.transformer` — FLA math + OCPD limits per Table 450.3(B) (primary-only and primary+secondary schemes, Note 1 next-size-up only where permitted).
- `cst.calc.sccr` — UL 508A SB4 weakest-link panel SCCR with NEC 409.22 available-fault check; never infers series ratings.
- `cst.calc.short_circuit` — infinite-bus transformer fault current + Bussmann point-to-point attenuation (C-value user-supplied; not embedded).
- Table loader now supports `data/standards_tables/samples/` fallback: clearly-marked SAMPLE files (common NEC 310.16 Cu-75°C and 430.250 460 V values) let everything run/test out of the box; results carry a SAMPLE warning; user files always win; `allow_sample=False` for design use.
- 5 new CLI subcommands: `ampacity`, `motor-branch`, `transformer`, `sccr`, `fault-current`.
- Tests: 97 passing (32 new), all doctests green.

**Boundary note:** rule multipliers/percentages implemented in code with clause citations (same class of content as the corpus's worked examples); bulk table values (310.16, 430.250, Bussmann C) remain user-supplied per the licensing boundary. SAMPLE values are flagged for verification against a licensed copy.

## 2026-07-10 — Pre-public sanitization pass (user-approved)

**Type:** Repository sanitization + second history rewrite
**Reason:** Repo is going public. Full audit (secrets/PII/copyright, tree + history) found no credentials, no client/employer references, and a clean RAG corpus — but flagged verbatim third-party video transcripts, a backup tarball leaking the restricted tree, and personal learning material.

**Removed from tree AND purged from history** (copies archived in `~/Dev/_archive/repo-sanitize-removed-20260710/`; pre-sanitize mirror at `~/Dev/_archive/CST-pre-sanitize-backup-20260710.git`):
- 8 verbatim YouTube/webinar transcripts + 1 affiliate-links copy under `control-standards/work/design/` (Ryan Jackson 2026 NEC, Electrical Code Coach paid exam prep, NEC livestream, Engineering Mindset motors, Solid State Workshop circuit analysis, Praxis NFPA 79/70E webinar, temp links, mini_machine v2 status chat dump)
- History-only ghosts: `check_this.md`, the Mike Holt-derived grounding note
- `planning/backups/*.tgz` (pre-reorg snapshot containing drafts_DO_NOT_READ + business-IP module skeletons), `planning/manifests/` (leaked restricted filenames)
- Personal learning/AI-chat material: `planning/RUST/`, `planning/SCADA/`, `planning/motors/`, `safety_software_stack.md`, `ground_earth_visual.md`, `semi_facility/phase_20260413.md`
- `STRUCTURE_SUMMARY.md` history (old versions listed restricted filenames; regenerated clean)

**Tree-only fixes:**
- 37 derived-note files: links to removed raw transcripts converted to plain-text notes (derived paraphrased summaries were audited as fine and KEPT)
- `ul508_spacing.md`: 13 ephemeral images.openai.com URLs stripped
- All `/Users/kyawminthu/...` absolute paths scrubbed from 34 tracked files (repo-relative or `~` forms)
- `.claude/settings.json`: legacy `~/Dev/tools` permission removed
- `project_automator.py`: `restricted/`, `drafts_DO_NOT_READ/`, `archive/` excluded from the generated structure summary
- Commit author/committer email rewritten to the GitHub noreply address across all history

**Audited and cleared (no action):** RAG corpus paraphrasing (no reproduced NEC/UL tables), semi_facility (follows its public-content rules), GA4 ID, docs/ content, secrets/keys (zero hits tree + history), PII (only fictional examples), internal hostnames/IPs (none), employer/client names (none).

## 2026-07-10 — Git history rewrite: Udemy course purged from repo and remote

**Type:** Repository history rewrite (user-approved)
**Status:** Complete; rewritten `master` force-pushed to `origin`.
**Reason:** `planning/Python/` (168 MB third-party "Complete Python 3 Bootcamp" course, 1,141 files) was tracked since early history and present on the public GitHub remote — copyright exposure and 165 MB of pointless `.git` weight.

**What was done:**
- Full mirror backup first: `~/Dev/_archive/Control-System-Tools-pre-rewrite-backup.git` (169 MB, contains pre-rewrite history).
- Course files moved out of the repo to `~/Dev/_archive/udemy-python-bootcamp/`.
- The stale `phase-19-nav-refactor` worktree blocked filter-repo; its uncommitted changes were committed onto the `phase-19-nav-refactor` branch (and copied to `~/Dev/_archive/phase19-worktree-uncommitted/`), then the worktree was removed.
- `git filter-repo --invert-paths --path planning/Python` rewrote all 328 commits. `.git`: 171 MB → 5.9 MB. Zero refs touch `planning/Python` afterwards; 65/65 tests pass.
- Rewritten `master` force-pushed; 3 stale fully-merged remote branches deleted (`feat/control-systems-training-expansion`, `feat/phase22-semiconductor-facility-reference`, `feat/ul508a-content-depth`). Remote now carries only `master`.

**Consequences to know:**
- **All commit SHAs changed.** Any existing clone of this repo must be re-cloned (or hard-reset to the new history). Old SHAs in notes/links no longer resolve.
- GitHub may retain pre-rewrite objects in caches/unreachable storage for a while; a GitHub Support request can force-purge if needed.
- `planning/Python/` remains in `.gitignore` as a guard.

## 2026-07-10 — Tools Suite Phases 0–1 — repo hygiene + `cst` Python package

**Type:** New project track (Python tools suite) + repository hygiene
**Status:** Complete on `feat/cst-suite` (Phase 0: commit c027d72; Phase 1: follow-up commit).
**Reason:** Full repo audit (2026-07-10) found zero engineering-calculation code despite the "Control System Tools" name, plus active hygiene defects. User approved a 4-phase plan to grow the repo into a comprehensive, portfolio-grade engineering tools suite alongside the content site.

**Phase 0 changes (hygiene):**
- Untracked `planning/Python/` (168 MB Udemy course, 1,141 files — 54 % of tracked files; copyright exposure). History rewrite deferred pending user decision.
- `tools/project_automator.py` IGNORE_DIRS fixed (was indexing `.venv`/`docs/vendor`/`docs/_site`) — STRUCTURE_SUMMARY.md 600 KB → 99 KB.
- Fixed the 2 pre-existing broken homepage links; excluded `docs/plans/` + `docs/superpowers/` from the published site.
- Deleted 0-byte `generate_rag_index.py` and retired `_phase26_*` scripts; un-hardcoded `generate_standards_overview.py` root path.
- Re-synced the RAG→site mirror (5 stale BLDC/PMSM files).

**Phase 1 changes (package):**
- New installable package `src/cst/` with console script `cst` (hatchling, `uv sync`).
- `cst.common`: units (ASTM B258 AWG), Citation/CalcResult framework (every result carries standard references + assumptions), loader for user-supplied licensed table JSON.
- Calculators: `cst.calc.voltage_drop` (NEC K-factor method + minimum-wire-size search), `cst.motion.encoder` (counts↔units↔RPM scaling), `cst.calc.enclosure_thermal` (IEC/TR 60890-style temp rise + fan sizing).
- `data/standards_tables/`: committed schemas, gitignored values — licensed table data (NEC 310.16, 430.250, …) is supplied by the user, never committed.
- 50 new tests in `tests/cst/` (65 total pass); pytest declared as dev dependency; redundant `pypdf2` dropped.

**Architecture decision:** calculation logic open/committed, licensed numeric table values local-only — same copyright boundary as the RAG corpus. Roadmap: Phase 2 NEC/UL data-dependent calculators (blocked on user table data), Phase 3 panel/commissioning pipeline, Phase 4 PLC/diagnostics/docgen.

## 2026-05-06 — Phase 30.2 COMPLETE — IEC 60079 depth pass

**Type:** Site content / standards detail page upgrade
**Status:** Complete on `feat/phase30-standards-depth-pass`.
**Reason:** IEC 60079 detail page audited at 3/8 on the ISO 13849-1 template floor — missing Quick Start, Worked Example, Common Mistakes, Practical Checklist, Lifecycle Application; protection-method table did not distinguish corpus-backed parts from gap-flagged ones. Brought page up to floor compliance.

**Changes:**
- `docs/standards/hazardous-area/iec-60079/index.md` — 123 → 364 lines.
  - **Added** Quick Start (5 bullets), Corpus Coverage table (6 corpus parts + 6 gap-flagged parts), Per-Part Depth (60079-0 / -1 / -10-1 / -11 / -14 / -17), Worked Example (4–20 mA IS loop on ethylene Zone 1 with full entity-parameter math), Common Mistakes (6 numbered), Practical Checklist (Area classification / Equipment / Installation / Inspection groups), Lifecycle Application table.
  - **Expanded** the existing Equipment Marking System tables (EPL→Zone, gas groups, T-codes) and added the 50 °C autoignition margin rule.
  - **Replaced** the brief NEC Article 500–505 note with a fuller mapping table linked to the IEC 60079 ↔ NEC 500–505 crosswalk page.
  - **Kept** the existing page header, hazardous-area family link, and Related Standards block.

**Plan vs RAG correction (recurrence).** The Phase 30.2 plan called for per-part depth on Ex e (60079-7) and Ex p (60079-2), but neither part is in the RAG corpus. Verified against `_index.yaml` before drafting (lesson learned in 30.1 successfully applied). Per-part depth covers the 6 corpus-backed parts only; Ex e, Ex p, and other family members appear in the Corpus Coverage gap-flag table. Plan's Common Mistake #6 (Ex e motor thermal protection) replaced with a corpus-backed mistake — field-modifying an Ex enclosure.

**Validation:**
- Jekyll build: clean (1.19 s).
- All 12 outgoing internal links from the rewritten page resolve.
- `validate_ai_boundaries.py`: 2 pre-existing failures, no new regressions.
- One external URL (`https://www.iecex.com/`) generated by mistake and removed before commit per the rule against generating external URLs.

**Corpus quality:** unlike the NFPA 79 corpus in Phase 30.1, the IEC 60079 corpus is clean — no stray LLM prompts, no empty placeholders, consistent front-matter. Nothing to flag.

## 2026-05-06 — Phase 30.1 COMPLETE — NFPA 79 depth pass

**Type:** Site content / standards detail page upgrade
**Status:** Complete on `feat/phase30-standards-depth-pass`.
**Reason:** NFPA 79 detail page audited at 3/8 on the ISO 13849-1 template floor — missing Quick Start, Worked Example, Common Mistakes, Practical Checklist; chapter table had wrong titles. Brought page up to floor compliance.

**Changes:**
- `docs/standards/us-electrical/nfpa-79/index.md` — 110 → 246 lines.
  - **Added** Quick Start (5 bullets), Per-Chapter Depth (9 chapters: 4, 5, 6, 7, 8, 9, 15, 16, 19), Worked Example (UL-listed packaging machine), Common Mistakes (6 numbered), Practical Checklist (Design / Build / Ship & Install), Lifecycle Application table.
  - **Replaced** the previous "Key Chapters" table (which had Ch 6/7 swapped and used "Protection of equipment" — an IEC 60204-1 phrase, not an NFPA 79 chapter title) with a corrected 14-row Chapter Reference table.
  - **Replaced** the thin "Lifecycle Stages" section with a Lifecycle Application table linking to all six site lifecycle-stage pages.
  - **Kept** the page header, Standard Overview table, "Relationship to NEC and UL 508A" diagram, "PL / SIL Relevance" cross-reference, and Related Standards block.

**Plan vs RAG correction.** The Phase 30.1 plan as drafted on 2026-04-29 assumed a different NFPA 79 chapter layout than NFPA 79:2024 actually uses. Mapping verified against `control-standards/rag/standards_intelligence/us/nfpa79/_index.yaml` and chapter front-matter. Page drafted against the verified corpus mapping, not the stale plan. See `project_state/project_state.md` for the per-chapter delta table. Same verification step is queued ahead of 30.2.

**Validation:**
- Jekyll build: clean (1.351 s, 268 HTML files).
- All 13 outgoing links from the rewritten page resolve. Two pre-existing broken links elsewhere on the site (homepage → `/industries/food-beverage/` and `/industries/offshore-marine/`) are not Phase 30.1 regressions; flagged for a separate hygiene task.
- `validate_ai_boundaries.py`: 2 pre-existing failures, no new regressions.

**Corpus hygiene findings (out of scope for Phase 30, queued separately).** The NFPA 79 RAG files contain stray LLM prompts at chapter ends (Ch 6, 7, 8, 15, 16, 17, 18), empty placeholder values for numerical ranges (Ch 4 temperatures, Ch 17 bend-radius), an internal-numbering bug (Ch 6 says "intent of Chapter 7"), and a suspect "Table 7.2.7" cite in Ch 15. These do not affect site content because the rewrite only used independently verifiable facts.

## 2026-04-29 — Phase 30 plan recorded — Standards Depth Pass (planning only, no code)

**Type:** Planning / project_state authored
**Status:** Plan recorded; implementation not started.
**Reason:** Live-site audit revealed standards detail pages all carry "Complete" badges but actual depth varies ~3×. ISO 13849-1 and IEC 62061 set an 8-section template (Quick Start, per-clause depth, Worked Example, Common Mistakes, Practical Checklist, Lifecycle Application, plus Standard Overview and Related Standards). NFPA 79, IEC 60079, IEC 60204-1, and SEMI S2/S8/S14 are at 3/8 or below. Family overview pages are list-only when they should help a user choose between members.

**What was added:**
- New "## Phase 30 — Standards Depth Pass (Planned)" section in `project_state/project_state.md` between Current Direction and the Phase 29.4 entry.
- Header `Next Phase` line in `project_state.md` updated to point to Phase 30 with the audit summary.
- Phase 30 plan contents:
  - Audit findings table (per-page template-completeness scores).
  - Family-page audit table.
  - Eight sub-phases (30.1 through 30.8) with file paths, RAG sources, exact section additions per page, worked-example specifications with concrete numbers (e.g. NFPA 79 packaging machine, IEC 60079 ethylene-tank IS loop with entity-parameter math, IEC 60204-1 CNC machine, SEMI PVD tool, IEC 62443 networked safety PLC), and Common Mistakes specifications.
  - Cross-cutting principles (RAG is authoritative; worked examples must be concrete; no new corpus claims; build clean every sub-phase).
  - Recommended sequencing.
  - Sub-phase validation checklist.
  - Out-of-scope statement.
  - Branch and commit discipline.

**No code changes in this entry.** Implementation begins when Phase 30.1 (NFPA 79) starts on `feat/phase30-standards-depth-pass`.

## 2026-04-29 — Terminology pass: "confidential" → "proprietary" / "sensitive"

**Type:** Editorial / public-content tone
**Status:** Complete
**Reason:** "Confidential" framing in the BLDC pages made the public site sound like it was hiding restricted material. Replaced with engineering-accurate words. IEC 62443 standard terminology kept (with a clarifying note added).

**Renamed:**

- `docs/fundamentals/motors/bldc-reference/index.md` — three section headings + body references: "confidential BLDC system" → "proprietary BLDC system", "confidential system" → "proprietary system", "confidential-system worksheet" → "proprietary-system worksheet".
- `control-standards/rag/training_modules/electrical_machines/bldc_motor_reference.md` — same three replacements (RAG source kept in sync with site).
- `planning/motors/bldc.md` — same three replacements + the opening line ("right way to approach a confidential system" → "right way to approach a proprietary system").
- `planning/semi_facility/governance/public_content_rules.md` — "confidential alarm lists" → "sensitive alarm lists" in the Not-allowed list.

**Kept (with terminology footnote added):**

IEC 62443 cybersecurity docs use "Data Confidentiality" / "Confidentiality" as the literal CIA-triad security-property name from the standard (FR 4). Renaming would misquote the standard. Per user direction (Option B), the term is kept and a one-line note has been added to each file:

> *Terminology: "Confidentiality" here is the IEC 62443 security property (the C in C-I-A) — protection from unauthorized disclosure, not a content-classification label.*

Files with the note (7 total — public summary plus 3 RAG-file mirror pairs):

- `docs/standards/cybersecurity/iec-62443/index.md` — after the FR table.
- `docs/assets/rag-files/.../IEC62443_3_3__system_security_requirements.md` + `control-standards/rag/.../IEC62443_3_3...md` — after the FR table.
- `docs/assets/rag-files/.../IEC62443_2_1__security_management.md` + `control-standards/rag/.../IEC62443_2_1...md` — after the IT-vs-IACS comparison table.
- `docs/assets/rag-files/.../IEC62443_4_2__component_requirements.md` + `control-standards/rag/.../IEC62443_4_2...md` — directly under the "Common Findings" heading.

**Kept (validator):**

- `tools/validate_ai_boundaries.py:22` — `"CONFIDENTIAL"` is a forbidden-keyword string the validator scans for. Removing it would weaken the rule that prevents this very issue.

**Validation:** `jekyll build` clean, 1.078 s. No structural changes.

## 2026-04-29 — Phase 29.4 complete: Standards Finder faceted filter (Sketch B)

**Type:** UX enhancement / progressive enhancement
**Status:** Complete
**Scope:** Faceted-filter chip UI added to the Standards Finder page; vanilla-JS filter logic; no new content.

**Files touched:**

- `docs/tools/standards-finder/index.md` — added `.finder-filters` block with 2 chip rows (Market: US/Global/Industry; What you're building: Machinery, Process, Hazloc, Cyber, Industry overlay), result-count display, Clear button, empty-state message. Tagged each `.scenario-card` with `data-finder-region` and `data-finder-domain` (multi-value where honest, e.g. Networked Safety PLC = `machinery cyber`). Tagged each grouping `<section>` with `data-finder-section` so empty sections collapse on filter. Added `id="escape-hatch"` to the closing "None of these fit?" section so the empty-state message can deep-link to it.
- `docs/assets/css/main.css` — new `.finder-filters` block (~95 lines): chip pill styling, active state via `aria-pressed="true"`, dashed-divider meta row with count + clear, dark-mode parity via existing color tokens, `.is-hidden` helper for cards/sections.
- `docs/assets/js/main.js` — appended ~85-line IIFE. No-ops if `[data-finder-filters]` not present. Filter logic: OR within a facet row, AND across rows. Updates `aria-pressed` on chips, hides non-matching cards via `.is-hidden`, hides any section whose cards are all hidden, updates result-count text, toggles Clear button visibility, surfaces an empty-state message when zero match.

**Facet tagging (region / domain):**

- 01 US ICP — `us` / `machinery`
- 02 Global Machine — `us global` / `machinery`
- 03 Process Skid — `us global` / `process`
- 04 Networked Safety PLC — `us global` / `machinery cyber`
- 05 Semi Equipment — `industry` / `industry-overlay`
- 06 Practical Machine Safety — `us global` / `machinery`
- 07 O&G Onshore Skid — `us` / `process hazloc`
- 08 Semi Fab Tool — `industry` / `industry-overlay machinery`
- 09 Offshore Platform — `industry` / `process hazloc industry-overlay`

**Progressive enhancement:** the existing `.finder-jump` anchor strip is kept underneath the filter block. No-JS readers still get the original scenario-card listing with section anchors — the filter is additive, not load-bearing.

**No URL persistence in this phase.** Deferred to a possible Phase 29.4.1 if the personal-use case actually demands shareable filter URLs.

**Validation:**

- `jekyll build`: clean, 1.261 s.
- `_site/tools/standards-finder/index.html`: 9 cards carry `data-finder-region`, 8 `.finder-chip` buttons (3 region + 5 domain), 5 `data-finder-section` markers, 1 `.finder-empty` element.
- `validate_ai_boundaries.py`: 2 pre-existing failures (UPW_water_skid_scenario.md, plus one other) — same baseline as Phase 29.3, unrelated.
- `validate_reorg.sh all`: 48/50 baseline.

**What this phase did not change:**

- No scenario content rewritten or added.
- No deprecation of the comparison crosswalks page.
- No edits to other Tools pages, sidebar, or the homepage.

## 2026-04-27 — Phase 29.3 complete: Standards Finder page (scenario-card entry)

**Type:** Information architecture / new page
**Status:** Complete
**Scope:** New page at `/tools/standards-finder/` + homepage re-routes + nav entry

The Phase 29 homepage promised a "Find applicable standards" entry point but routed both the hero CTA and the Start Here card to `/tools/crosswalks/` — a comparison tool, not a finder. Phase 29.3 ships the actual finder.

New page (`docs/tools/standards-finder/index.md`):
- Sketch C from the IA brainstorm — scenario-card entry, no JS, no faceted filter.
- `.finder-jump` anchor-chip strip + 5 grouped sections covering the 9 existing engineering scenarios reused from `docs/implementation/scenarios/`.
- Sections: US-market machines & panels (Scen. 01, 06) · Global / EU machines (02) · Process safety SIS/ESD (03, 07) · Networked & cyber-physical safety (04) · Industry-specific stacks (05, 08, 09).
- Closing escape-hatch routes to crosswalks (comparison) and the standards atlas (browse) so users who don't match a scenario don't dead-end.

CSS (`docs/assets/css/main.css`):
- `.finder-jump` block — bordered horizontal anchor strip, theme-token only, no overrides needed.

Re-routes (`docs/index.md`):
- Hero CTA "Find applicable standards" → `/tools/standards-finder/`.
- Start Here card "I need applicable standards" → `/tools/standards-finder/` + copy refreshed to match the Finder's scenario-first framing.

Navigation (`docs/_data/navigation.yml`):
- Added `Standards Finder` as the first child under Tools (above RAG Browser).

Validated: clean Jekyll build (1.078 s), 9 scenario cards + 5 jump anchors render on the Finder, both homepage entry points re-route correctly, validators show only baseline failures.

## 2026-04-27 — Phase 29.2 complete: Extend local sidebar pilot to 3 more topic groups

**Type:** Information architecture
**Status:** Complete
**Scope:** Pure data change in `docs/_data/training_catalog.yml`

The Phase 28 local-sidebar pilot covered only `electrical-machines` (Motors). Phase 29.2 extends it to three more groups, going from 1/4 → 4/4 of the topic groups in the catalog.

Data (`docs/_data/training_catalog.yml`):
- Added `sidebar_buckets:` ordering arrays to `fundamentals`, `control-systems`, and `nec-application` topic_groups.
- Tagged all 34 modules in those groups with `sidebar_bucket:` and gave 32 of them a `nav_title:` for sidebar-friendly labels.

Bucket taxonomies:
- **Electrical Fundamentals** (9 modules): Circuit Analysis · Components & Devices · Practical Wiring · Quick References.
- **Control Systems** (14 modules): Foundations · PID Methods · Machine Logic & Safety · Distributed Systems · Motion & Tuning.
- **NEC for Machines and Panels** (11 modules): Foundations · Motors & Article 430 · Panels & Article 409 · Machine-Side Wiring.

No template, CSS, or JS changes — the Phase 28 router (`docs/_includes/sidebar.html`) automatically opts a topic group in once any of its modules carry a `sidebar_bucket`. Validated: clean Jekyll build (1.057 s), local sidebar rendering on a sample page from each new group, baseline validators unchanged.

## 2026-04-27 — Phase 29.1 complete: Sidebar theme-compatibility tiers A–D

**Type:** UI polish / accessibility
**Status:** Complete
**Scope:** Phase 28 local sidebar (Motors pilot) + global sidebar aria-current

Single batch covering the four sidebar tiers that had been queued during Phase 29 planning.

CSS (`docs/assets/css/main.css`):
- Tier A — `[data-theme="dark"] .sidebar__chip--{b,i,a,ref,concept,code,core}` overrides mirroring the existing dark page-chip palette so local-sidebar level/type chips read in dark mode.
- Tier B — `.sidebar--local .sidebar__section-meta` gains a subtle `box-shadow` (separate light/dark values); global sidebar caret switched from text-swap (▶/▼) to a rotating ▸ chevron with a 0.15s ease, harmonizing with the local sidebar; `.sidebar__bucket-summary` letter-spacing tightened 0.07em → 0.05em.
- Tier C — `.sidebar__bucket[open] > .sidebar__bucket-summary` brightens to `var(--color-text)`; `.sidebar__chip` and `.sidebar__bucket-count` get `border-radius: 4px`.

Data (`docs/_data/training_catalog.yml`):
- Tier C — added `nav_title` for 6 Motors modules previously using their full titles in the sidebar (Induction/DC/Servo modules + Motor Family Comparison + BLDC/PMSM References).

Includes (`docs/_includes/sidebar-global.html`):
- Tier D — added `aria-current="page"` alongside `class="active"` on section, child, and grandchild links (local sidebar already had this since Phase 28).

Validated: clean Jekyll build (1.146 s), `validate_ai_boundaries.py` and `validate_reorg.sh all` show only pre-existing baseline failures.

## 2026-04-21 — Phase 29 complete: Homepage front-door rework (task-router, dedicated home layout)

**Type:** Information architecture / landing page
**Status:** Complete
**Scope:** `/` only; interior pages unchanged

Reworked the homepage from a reference-first atlas index into a task-first front door. The interior `default.html` layout was forcing the global sidebar, right-side context panel, and trust-boundary block onto `/`, competing with the topnav as a third navigation system. Phase 29 addresses that.

Includes / layouts:
- `docs/_layouts/home.html` — new. Topnav + scripts, no sidebar, no context panel, no trust-boundary, no breadcrumb. Uses a centered `.home-main` instead of the three-panel CSS Grid.
- `docs/_layouts/default.html` — untouched; interior surface stays byte-for-byte identical.

Content (`docs/index.md`):
- Hero rewritten with a plain-language promise: "Find the right standards path for your machine, panel, or safety system." 3 CTAs route to the decision workflow, scenarios, and training.
- New "Start here" 6-card task grid (decision / US panel / US+EU machine / safety / troubleshooting / training).
- Scenarios moved up from sixth section to second.
- Standards Families card grid kept but raw corpus paths (`rag/...`) removed from card bodies.
- Industry Matrix table replaced with 6 industry tile links.
- Standards Graph reduced to a one-line teaser + link.
- Repository tree moved into a collapsed `<details>` block at the bottom labelled for power users.

Topnav (`docs/_includes/topnav.html`):
- Search placeholder + ARIA "Search standards…" → "Search standards, workflows, training…".

Styling (`docs/assets/css/main.css`):
- New block at the existing home-styles area: `.home-body`, `.home-main`, `.home-hero` family, `.start-grid` / `.start-card` family, `.home-section` + intro, `.industry-tiles` / `.industry-tile` family, `.home-deep-dive` with text-swap caret matching the sidebar pattern. Reuses `--color-*` tokens so dark mode works automatically.

Validation:
- Jekyll clean build, 1.14 s.
- Home has 0 sidebars + 0 context panels; 6 Start Here cards + 6 industry tiles verified in built HTML.
- Interior pages (/standards/, Motors pilot page) unchanged.
- AI-boundary validator: 2 pre-existing failures.
- `validate_reorg.sh all`: 48/50 baseline.

## 2026-04-21 — Phase 28 complete: Sidebar pilot for Motors/Fundamentals (local section tree)

**Type:** Navigation architecture
**Status:** Complete
**Scope:** Sidebar architecture change, pilot scoped to `/fundamentals/motors/`

Replaced the single global sidebar include with a router that picks between a local section tree and the existing global sidebar. Pilot runs on one topic group; global fallback is byte-for-byte identical to the pre-pilot sidebar on every other page.

Includes:
- `docs/_includes/sidebar.html` — now a router. Matches `page.url` against `training_catalog.topic_groups[].url`; if the active group's modules carry `sidebar_bucket` tags, it includes the local sidebar, else the global.
- `docs/_includes/sidebar-global.html` — new, contains the pre-pilot markup verbatim.
- `docs/_includes/sidebar-training-group.html` — new, renders section meta + buckets (with counts) + module rows with compact chips (B/I/A, Ref/Concept/Code, Core) + nav_title-driven short labels + a TOC mount point under the active module.

Data (`docs/_data/training_catalog.yml`):
- Added `sidebar_buckets` order under `topic_groups[electrical-machines]` (Foundations / Drive Systems / Selection & Comparison / Deep References / Quick References).
- Tagged all 18 Motors modules with `sidebar_bucket`; 11 of them also received a `nav_title` for tighter sidebar text.

Styling (`docs/assets/css/main.css`):
- `--sidebar-width` bumped 240 → 288 (global token; affects all sidebars).
- New CSS block scoped to `.sidebar--local` and its children, including a chip palette and a `.sidebar__toc` active-heading indicator.

JS (`docs/assets/js/main.js`):
- New IIFE that only runs when `.sidebar.sidebar--local` exists.
- Persists open bucket state per topic group in `localStorage` (`sidebar-buckets:<group>`).
- On active module pages, scans `.main-content h2[id], h3[id]` and injects them into the TOC; an IntersectionObserver keeps the nearest heading highlighted while scrolling. No static fallback — JS-only enhancement.

Landing page (`docs/fundamentals/motors/index.md`):
- Rebuilt from one flat table into 5 bucket-grouped tables, iterating the same `sidebar_buckets` array so the landing and sidebar cannot drift out of sync.
- Module-count copy corrected 13 → 18; intro copy tweaked to mention the Phase 27 BLDC/PMSM deep references.

Validation:
- Jekyll build: clean, 1.185s.
- 3 motors pages inspected for local sidebar + correct bucket rendering + active state + TOC mount.
- 3 non-pilot pages inspected — all get the global sidebar (fallback verified).
- `validate_ai_boundaries.py`: 2 pre-existing failures, no new regressions.
- `validate_reorg.sh all`: 48/50 baseline unchanged.

Deferred:
- Extending the local sidebar to other topic groups (Control Systems, Electrical Fundamentals, NEC) — data-only changes when ready.
- Search / filter inside the local sidebar.
- Sidebar TOC fallback for no-JS users.

## 2026-04-21 — Phase 27.7 complete: BLDC vs PMSM Comparison UX polish + factual pass

**Type:** Page-level UX polish + factual correctness
**Status:** Complete
**Scope:** `docs/fundamentals/motors/bldc-vs-pmsm/index.md` only

Applied the same pattern that landed in Phase 27.6, adapted for a decision-framed comparison page. No new pages, no new CSS; reused `.glance-grid`, `.card`, `.scenario-grid`, `.scenario-card`.

UX:
- Trimmed `## Purpose` from a 170-word paragraph to 3 bullets (Use this when / Choose BLDC if / Choose PMSM if).
- Added a 4-card "At a glance" decision strip under Purpose (BLDC wins / PMSM wins / Induction still valid / Don't choose by motor name).
- Added a 5-card "Jump to" nav: Construction, Control, Feedback, Decision Matrix, Scenarios. All anchor IDs verified.
- Moved `## Decision matrix` from after the scenarios to before them — high-value content now lands early.
- Rebuilt all 10 scenario walkthroughs (A–J) as scan cards at the top of `## Scenario walkthroughs`, each with Winner / Why / When other side wins / Stack, each linking to its existing detail H3. All 10 anchor IDs verified.

Factual / tone fixes:
- Softened `PMSM = ... always driven with sinusoidal (FOC)` → `typically driven with sinusoidal commutation or FOC`, with an explicit module-scope note.
- Corrected `DC-link undervoltage during hard regen` → `overvoltage` with correct physics.
- Softened `full stop` and `the right answer in 2026` phrasing in the takeaway section while keeping the core engineering advice.

Validation:
- Jekyll build: clean, 1.134s.
- `validate_ai_boundaries.py`: 2 pre-existing failures only (no new regressions).
- `validate_reorg.sh all`: 48/50 baseline unchanged.

## 2026-04-21 — Phase 27.6 complete: BLDC/PMSM Implementation Guide UX polish + factual pass

**Type:** Page-level UX polish + factual correctness
**Status:** Complete
**Scope:** `docs/fundamentals/motors/bldc-pmsm-implementation/index.md` only

First-pass rework of the deepest motors page to make it feel less like a generic template. No new pages, no new layouts, no new CSS — reused `.glance-grid`, `.card`, `.card-grid`, `.scenario-grid`, `.scenario-card`.

UX:
- Trimmed `## Purpose` from a 200-word paragraph to 3 bullets (When/What/Will-not).
- Added a "Choose fast" 4-card decision strip (Choose BLDC / Choose PMSM / Watch-outs / Build sequence).
- Added a 6-card "Jump to" nav (Architecture / Control / Sizing / Drive Choice / Wiring / Checklist); all kramdown anchor IDs verified.
- Rebuilt the 8 `Practical implementation scenarios` as scan cards (Motor / Drive / Control / Why it wins), each linking to the existing detail H3 below.
- Moved `## Known industry brands` to a compact 3-column appendix table (Category / Typical vendors / Fit) at the end of the page.
- Cardified `## Implementation checklist` into 5 `.card-grid` cards (Motor / Drive / Wiring / Control / Testing). 44 task-list checkboxes render correctly inside the cards via kramdown `markdown="1"`.

Factual fixes:
- Scenario 1 drone: "PWM command ... DShot protocol" → "Digital throttle, DShot (150/300/600/1200 kbit serial) signaling — not PWM".
- Common failure modes: "DC-link **undervoltage** during regen" → "DC-link **overvoltage** during regen" with corrected physics.
- Power wiring: softened "125% of motor FLA" into an explicit NEC 430.22 citation for single continuous-duty motor branch circuits, with pointers to NEC 430.24/430.33 and IEC 60204-1 §12 for other cases.
- Contactor: rewrote to distinguish lockout / SS1-Cat-0/1 use from certified STO use.
- Feedback shield: replaced absolute "at drive end only" with a drive-manual-driven note covering single-end vs 360° both-end practice.

Validation:
- Jekyll build: clean, 1.219s.
- `validate_ai_boundaries.py`: 2 pre-existing failures only (no new regressions).
- `validate_reorg.sh all`: 48/50 baseline unchanged.

## 2026-04-21 — Phase 27.5 complete: Visual wiring guides for BLDC and PMSM

**Type:** Phase completion (follow-up to Phase 27)
**Status:** Complete

Phase 27 shipped five BLDC/PMSM modules with wiring **tables** but minimal visuals — scenario architecture flows were 3-node `Source → Drive → Motor` blocks and the Reference modules had no wiring diagrams. Phase 27.5 closes that gap with engineer-grade Mermaid wiring visuals across all four in-scope motor pages.

**Seven new Mermaid diagrams added** using a new cable-class `classDef` convention (power=red, phase=near-black, feedback=blue, safety=orange, bus=green, shield=dashed gray):

- Implementation Guide §14: cable-group legend + table (D5), plus three archetype diagrams (D4) — Battery BLDC, Integrated PMSM servo, Shared DC-bus multi-axis PMSM
- BLDC Reference: wiring archetype (at-a-glance view of all 5 wiring groups) (D2)
- PMSM Reference: industrial servo wiring (3φ AC, EMI filter, drive with STO/fieldbus/brake, motor cable, encoder) (D3)
- Motor Selection Scenarios: upgraded 3 trivial flows + added new Scenario 2 wiring diagram (D1)

**Two pinout reference tables added** (baseline for this content class — didn't exist before):

- BLDC Reference: Hall connector pinout (IEC 60757 colors)
- PMSM Reference: Encoder connector pinout (incremental + absolute protocols + temp + shield)

**New PMSM Reference section:** `## Wiring and integration` (servo wiring + encoder pinout + STO dual-channel note + cross-link to Servo Commissioning Workflow).

**Nine cross-links added** between the diagrams across BLDC Reference, PMSM Reference, BLDC vs PMSM Comparison, Motor Selection Scenarios, and Implementation Guide — all resolve via kramdown-generated heading IDs.

Jekyll build clean, AI boundary validator shows only the 2 pre-existing failures, `validate_reorg.sh all` at 48/50 baseline, internal link checker exit 0 (273 files). RAG files and site files stay in sync.

No new pages, no routing changes — purely content enrichment layered on top of the Phase 27 footprint.

## 2026-04-20 — Phase 27 complete: BLDC/PMSM motor implementation

**Type:** Phase completion
**Status:** Complete

Five new motor reference modules shipped from planning → RAG → site:

- BLDC Motor Reference (`/fundamentals/motors/bldc-reference/`)
- PMSM Motor Reference (`/fundamentals/motors/pmsm-reference/`)
- BLDC vs PMSM Comparison (`/fundamentals/motors/bldc-vs-pmsm/`) — Core/featured, with application-fit and choice-rationale scenarios
- BLDC and PMSM Implementation Guide (`/fundamentals/motors/bldc-pmsm-implementation/`) — Core/featured, with basic wiring / control / drive patterns
- Motor Selection Scenarios (`/fundamentals/motors/motor-selection-scenarios/`) — Core/featured, three engineering-grade archetypes (fan/pump, precision axis, AGV) with per-scenario drive, wiring, tuning, measurement, and failure-mode detail

Existing `bldc-ev-drone-motors` module enriched with a drone-class BLDC vs EV-class PMSM/IPMSM deep comparison section (15 subsections sourced from `planning/motors/scenarios.md` block 3, including 2 new Mermaid architecture diagrams and inline citations to TI/Microchip/Beckhoff/Tektronix). File grew from 180 → 429 lines.

RAG corpus at `control-standards/rag/training_modules/electrical_machines/` grew from 13 → 18 files. Training catalog `electrical-machines` group `module_count` 13 → 18. Cross-links added from `bldc-ev-drone-motors` and `motor-family-comparison` modules to the five new modules.

Site HTML file count: baseline + 5. Jekyll build clean, AI boundary validator shows only the 2 pre-existing failures, `validate_reorg.sh all` at 48/50 baseline, internal link checker exit 0 (273 files scanned).

Superseded planning files removed: `planning/motors/pmsm.md` (placeholder), `planning/motors/motors_comparisons.md` (redundant with existing `motor-family-comparison` site module). `planning/motors/scenarios.md` retained as staging history (source for Module 5 and for `bldc-ev-drone-motors` enrichment).

Convention adjustments during execution:
- RAG file headers use HTML-comment format (not YAML frontmatter as plan originally spec'd) — matches the existing 13 files in the same directory.
- External citations rendered as inline plain-text markdown links, not kramdown footnotes.
- `bldc.md` source had no Mermaid diagrams (used plain text ASCII) so Module 1's Mermaid diagram expectations were not met — content complete otherwise.

## 2026-04-20 — Motors planning: BLDC vs PMSM deep dive + full implementation reference

**Type:** Planning / Content staging
**Status:** Drafts in `planning/motors/`

Two new files added to the motors planning set:

1. `planning/motors/bldc_vs_pmsm.md` — focused head-to-head engineering comparison
2. `planning/motors/bldc_pmsm_implementation.md` — full 16-section production-grade implementation reference (replaces a master-prompt template that was in the file)

`bldc_pmsm_implementation.md` covers: executive overview, end-to-end system architecture with Mermaid diagrams, BLDC vs PMSM comparison table, control methods (6-step, sinusoidal, FOC with Clarke/Park flow diagram), practical math (V = Ri + Ldi/dt + K_e·ω, T = K_t·I, ω_e = p·ω_m, mechanical equation), drive architecture (inverter / gate driver / MCU / current sensing / feedback interface), motor selection (hobby vs industrial), drive selection (ESC/VESC/ODrive vs Siemens/Beckhoff/Kollmorgen/Yaskawa/Rockwell/Mitsubishi/etc.), hobby vs industrial comparison, cost-performance tradeoff, measurement and testing (why RMS meters fail on PWM, correct instrument set, power analyzer role), 8 practical scenarios (drone, conveyor, cobot, low-cost automation, semiconductor stage, CNC spindle, e-bike, servo press), industry brand classification, wiring and integration (shielding, grounding, cable practice), common failure modes, full implementation checklist.

Scope of the new document:

- Physical construction differences (SPM vs IPM, concentrated vs distributed windings, saliency, reluctance torque)
- Back-EMF shape as the root cause of all control-strategy differences
- Control strategies: 6-step trapezoidal, sinusoidal commutation, FOC/vector
- Drive / inverter architecture comparison (shared power stage; differences in MCU, feedback, PWM, control loop rates, functional safety)
- Feedback options and match to control strategy
- Torque ripple quantified per scheme
- Speed range and field weakening (SPM vs IPM)
- Efficiency and cost structure
- 10 real-world scenarios (HVAC EC fan, e-bike, servo press, conveyor, drone, CNC spindle, cobot joint, semiconductor wafer handler, power tool, retrofit)
- Decision matrix for architecture selection
- Common field failure modes specific to each family
- Suggested follow-up planning docs (FOC math, field weakening, commissioning, servo tuning, drive hardware review)

This stays in `planning/` — it is not yet promoted to `control-standards/rag/` or built into the Jekyll site. Next step when ready: promote relevant portions into `rag/training_modules/electrical_machines/` and expand the `fundamentals/motors/` site section.

## 2026-04-16 — Control Theory Overview page rebuild

**Type:** Content / Training Enhancement
**Status:** Complete

Rebuilt `docs/fundamentals/control/control-theory-overview/index.md` from a text-dense 151-line concept dump into a visual map page. Same topics, new presentation:

- Hero Mermaid diagram showing the full feedback loop (reference → controller → plant → sensors → estimator → feedback)
- 4-card "at a glance" summary row (Plant, Controller, Sensors/Estimator, Verification) using new `.glance-grid` CSS
- Side-by-side open-loop vs closed-loop comparison with separate Mermaid diagrams using new `.compare-columns` CSS
- "Where PID fits" layered architecture diagram showing PID as one block in a larger system
- Controller families decision matrix (7 rows, 4 columns including industrial use level)
- Estimator/observer flow diagram with method table (added Luenberger observer)
- Verification process strip (model → simulation → frequency response → margins → hardware test)
- "Where to go next" 6-row routing table replacing the old 2-link footer

Added `.glance-grid` and `.compare-columns` CSS utility classes to `main.css`. Fixed kramdown markdown-inside-HTML rendering with `markdown="1"` attributes. No new pages, no layout changes, no JS.

Jekyll build clean (268 files). Internal link checker exit 0.

## 2026-04-16 — Sidebar Enumeration for Control Theory & Crosswalks

**Type:** Navigation / Discoverability
**Status:** Complete

Hybrid response to the 2026-04-16 site audit finding that `docs/_data/navigation.yml` listed `/fundamentals/control/` and `/tools/crosswalks/` as hubs without enumerating children, leaving 20+ reachable pages invisible in the sidebar.

- **Control Theory**: added 3 curated entry modules (Control Theory Overview, PID — Intuitive Foundation, PID Intuition in Practice). Full 14-page catalog continues to render on the landing page's data-driven table — sidebar stays scannable.
- **Crosswalks**: full enumeration of all 6 crosswalk pages (NFPA 79 ↔ IEC 60204-1, UL 508A / NEC / NFPA 79, IEC 61511 ↔ IEC 61508, IEC 60079 ↔ NEC 500/505, Standards Decision Workflow, Standards Comparison Tool).
- Semiconductor Facility subtree (11+3 pages) **not** added to sidebar — its landing already presents all systems in a descriptive table that would be hard to replicate cleanly as flat nav entries.

Jekyll build clean (268 files); internal link checker exit 0; visual verification of both built pages confirms new entries render at correct depth.

## 2026-04-16 — Trust-Boundary Deduplication

**Type:** Site / Content Hygiene
**Status:** Complete

Removed duplicate trust-boundary notices on 18 site pages. Root cause: `docs/_layouts/default.html:52` already auto-includes `trust-boundary.html` on every page, so per-page inline `{% include trust-boundary.html %}` calls produced two notices back-to-back. Five pages in `/industries/semiconductor/facility/` additionally wrapped the include in a redundant `<div class="trust-boundary">` parent, rendering an empty styled wrapper around the include's own div.

Pages fixed:
- `docs/training/index.md`, `docs/repository/index.md`, `docs/troubleshooting/index.md`, `docs/fundamentals/index.md`, `docs/implementation/index.md`, `docs/tools/index.md`, `docs/verification/index.md`, `docs/design/workflows/index.md`
- `docs/design/workflows/motor-selection/index.md`, `docs/design/workflows/electrical-review/index.md`
- `docs/implementation/vfd-commissioning/index.md`, `docs/implementation/servo-commissioning/index.md`, `docs/troubleshooting/motors/index.md`
- `docs/industries/semiconductor/facility/commissioning/index.md`, `.../crosswalks/index.md`, `.../instrumentation/vendor-families/index.md`, `.../instrumentation/device-families/index.md`, `.../instrumentation/alarm-strategy/index.md`

Verification: Jekyll build clean (1.327 s), internal link checker exit 0 (268 files scanned), zero built HTML pages now contain the trust-boundary heading more than once. The planning doc at `docs/superpowers/plans/2026-04-11-phase23-facility-build-phases-3-4.md` contains the include in example snippets but has no frontmatter, so Jekyll does not process its Liquid — left untouched.

## 2026-04-15 — Phase 26 COMPLETE: Navigation Restructure and Link Audit

**Type:** Site Architecture / UX
**Status:** Complete

Twelve-batch restructure that replaces the legacy 5-group sidebar with a 10-group intent-based navigation, physically relocates ~156 Jekyll pages into the new hierarchy, installs redirect infrastructure, and drives the internal link checker to zero broken links.

- Installed `jekyll-redirect-from` plugin (Gemfile + _config.yml) and created `tools/check_internal_links.py` (stdlib-only internal link checker) — Batch 1.
- Authoritative old→new URL registry persisted at `docs/_data/phase26_migration_map.yml`.
- Group migrations (Batches 2–5): fundamentals/control/motors moved from `/training/*` to `/fundamentals/electrical|control|motors/`; engineering-workflow/software-stack/workflows/reference-architecture/reference-motor-systems moved to `/design/...`; commissioning-templates, scenarios, and four build-side lifecycle stages moved to `/implementation/...`; seven verification-oriented lifecycle stages moved to `/verification/...`.
- Tools migration (Batch 6): rag-browser, glossary, crosswalks (+6 sub-pages), and reference landing moved to `/tools/...`. Word-boundary-safe link rewriter introduced after the first attempt hit a double-prefix bug.
- Training landing (Batch 7) trimmed to structured-paths only; only `/training/nec-application/` remains under `/training/`.
- Troubleshooting section (Batch 8) created; motor-troubleshooting moved from `/workflows/` into `/troubleshooting/motors/`; `/workflows/` tree deleted.
- Repository section (Batch 9) created; `/about/` moved to `/repository/about/`.
- Navigation rewrite (Batch 10): `docs/_data/navigation.yml` fully rewritten to 11 top-level groups (Home, Fundamentals, Standards, Design, Implementation, Verification, Industries, Troubleshooting, Training, Tools, Repository). Four top-level landings (`/fundamentals/`, `/implementation/`, `/verification/`, `/tools/`) created so sidebar group labels do not 404.
- Cross-link sweep (Batch 11): 501 residual references to pre-Phase-26 URLs rewritten across 49 files — `training_catalog.yml` (105), `field_checklists.yml` (22), `topnav.html`, plus dozens of industry/scenario/training/standards pages. Skipped `redirect_from:` frontmatter, the migration map, `rag_tree.json`, generated RAG assets under `docs/assets/rag-files/`, and the Phase 26 plan + design spec (contain old URLs as data).
- Final audit (Batch 12): Jekyll build clean (267 HTML files), internal link check exit 0 (267 scanned), AI-boundary validator shows same 2 pre-existing Phase 25 failures with no new regressions, reorg validator 48/50 (same pre-existing baseline).

Every moved page carries `redirect_from:` frontmatter covering bare + `/index.html` variants, so three years of accumulated deep links (fundamentals/control-systems/electrical-machines, engineering-workflow, workflows/*, commissioning-templates, scenarios, lifecycle/*, field-engineering, reference, rag-browser, glossary, crosswalks, about) continue to resolve.

## 2026-04-15 — Phase 26 Batch 11 COMPLETE: Site-wide cross-link sweep

**Type:** Site structure / Cross-link sweep
**Status:** Complete

- Swept 501 residual references to pre-Phase-26 URLs across 49 files (training/fundamentals, training/control-systems, training/electrical-machines, engineering-workflow, software-stack, workflows/* split between design/implementation/troubleshooting, commissioning-templates, scenarios, all lifecycle/* stages split across verification/implementation, field-engineering, legacy reference/architecture + motor-systems, legacy /rag-browser/ /glossary/ /crosswalks/ /about/).
- Used a word-boundary-safe rewriter with ordered longest-first replacements (so `/tools/rag-browser/` is not rewritten into `/tools/tools/rag-browser/`).
- Preserved `redirect_from:` frontmatter entries (they must keep the old URLs for the plugin). Skipped `docs/_data/phase26_migration_map.yml`, `docs/_data/rag_tree.json`, `docs/assets/rag-files/**`, and the Phase 26 plan/design spec (those contain old URLs as data).
- `docs/_data/training_catalog.yml` (105 refs) and `docs/_data/field_checklists.yml` (22 refs) are the biggest single-file updates — the catalog no longer round-trips every module URL through a 301 redirect.
- `docs/field-engineering/index.md` meta-refresh shim retained and retargeted to `/implementation/commissioning-templates/`.
- Jekyll build clean (267 HTML files). Internal link check exit 0 (267 scanned). AI-boundary validator: only the 2 pre-existing Phase 25 failures, no new regressions.

## 2026-04-15 — Phase 26 Batch 10 COMPLETE: navigation.yml rewrite + 4 top-level landings

**Type:** Site structure / Navigation rewrite
**Status:** Complete

- Added 4 top-level landing pages required by the new nav structure — `docs/fundamentals/index.md`, `docs/implementation/index.md`, `docs/verification/index.md`, `docs/tools/index.md`. Each page presents sub-group cards, a scope blockquote, and cross-links into adjacent sections. Without these landings, sidebar group labels (which are clickable) would have 404'd.
- Fully rewrote `docs/_data/navigation.yml` from the prior 5-group historical layout to the 11-group intent-based structure: Home, Fundamentals, Standards, Design, Implementation, Verification, Industries, Troubleshooting, Training, Tools, Repository. Match prefixes realigned; legacy "Engineering Workflow" and "Reference" meta-groups dropped.
- Standards group retains the full per-family hierarchy (US Electrical → NEC/NFPA 79/UL 508A, Machinery → IEC 60204-1, Functional Safety → IEC 61508/61511/62061/ISO 12100/ISO 13849-1, Cybersecurity → IEC 62443, Hazardous Area → IEC 60079, Semiconductor → SEMI, plus the Relationship Graph).
- Jekyll build clean (267 HTML files); internal link check exit 0.

## 2026-04-15 — Phase 26 Batch 9 COMPLETE: Repository landing + About relocation

**Type:** Site structure / New section + page move
**Status:** Complete

- Added `docs/repository/index.md` — Repository and Project Info landing with the GitHub link, a build-stack summary (Jekyll, Mermaid, Cytoscape, jekyll-redirect-from, internal link checker), a content-source-of-truth table pointing at `project_state/`, and a contributing note.
- Moved `docs/about/index.md` to `docs/repository/about/index.md` with `redirect_from:` for `/about/` + `/about/index.html`. Breadcrumb retargeted to `Repository › About`.
- `docs/_includes/topnav.html` — top-nav "About" link updated to `/repository/about/`.
- `docs/_data/navigation.yml` — dropped the `/about/` prefix + About child from the Reference group, added a new Repository top-level group (children: About / Trust Boundary).
- Empty `docs/about/` directory removed.
- Jekyll build clean (263 HTML files); internal link check exit 0.

## 2026-04-15 — Phase 26 Batch 8 COMPLETE: Troubleshooting section

**Type:** Site structure / New section
**Status:** Complete

- Created `/troubleshooting/` section with landing + Motors subpage. Landing organizes field diagnosis entry points into 6 symptom categories (Motors, VFDs, PLC systems, Field I/O, Networks, Safety circuits), each pointing at the right existing workflow, fundamentals reference, or commissioning template.
- Moved `docs/workflows/motor-troubleshooting/index.md` to `docs/troubleshooting/motors/index.md` with `redirect_from:` stanza, updated breadcrumb, and refreshed cross-links (fundamentals/motors, design/workflows/motor-selection, implementation/vfd-commissioning, implementation/servo-commissioning, implementation/commissioning-templates/motor-rotation-verification).
- Sweep of `/workflows/motor-troubleshooting/` → `/troubleshooting/motors/` across 5 source pages and 2 data files (`design/workflows/index.md`, `design/workflows/motor-selection/index.md`, `design/index.md`, `implementation/vfd-commissioning/index.md`, `implementation/servo-commissioning/index.md`, `_data/training_catalog.yml`, `_data/field_checklists.yml`).
- Removed `docs/workflows/` entirely — the empty `electrical-review/` and `motor-selection/` shells from Batch 3 were deleted along with the motor-troubleshooting subdir.
- Added Troubleshooting group to `docs/_data/navigation.yml` (children: Motors). Full nav restructure to the 10-group target is still reserved for plan Task 13.
- Jekyll build clean (261 HTML files); internal link check exit 0.

## 2026-04-15 — Phase 26 Batch 7 COMPLETE: Training landing trim

**Type:** Site structure / Navigation refactor
**Status:** Complete

- Rewrote `docs/training/index.md` as a thin structured-paths landing. Only NEC-for-Machines-and-Panels remains under `/training/`; foundational electrical, control, and motors content has lived under `/fundamentals/` since Batch 2 and is no longer enumerated on the training page.
- Replaced the old catalog-driven Start-Here grid, Learning-Paths grid, topic-group cards, all-modules table, and related-standards list with a short path table plus a "Related Sections" pointer block.
- Link targets retargeted to existing sub-landings (`/fundamentals/electrical/`, `/design/architecture/`, `/verification/lifecycle/`, `/implementation/scenarios/`, `/tools/reference-hub/`, etc.) rather than bare `/fundamentals/`, `/verification/`, `/implementation/`, `/tools/` — those top-level landings don't exist yet and are out of scope for Batch 7.
- `docs/_data/training_catalog.yml` untouched — it is still consumed by the three `/fundamentals/*` group landings, the NEC-application index, and the `training-module` layout.
- Jekyll build clean (259 HTML files); internal link check exit 0.

## 2026-04-15 — Phase 26 Batch 6 COMPLETE: Tools group migration

**Type:** Site structure / Navigation refactor
**Status:** Complete

- Moved 10 pages from `/rag-browser/`, `/glossary/`, `/crosswalks/`, and `/reference/` into the new `/tools/` hierarchy (`/tools/rag-browser/`, `/tools/glossary/`, `/tools/crosswalks/...`, `/tools/reference-hub/`).
- Added `redirect_from:` (bare + `/index.html` variants) to every moved file so old URLs continue to resolve via `jekyll-redirect-from`.
- Repo-wide cross-link sweep: 143 replacements across 39 files using a word-boundary-safe rewriter (`tools/_phase26_batch6_update_links.py`) that avoids double-prefix pollution like `/tools/tools/...`.
- Also backfilled straggler references to `/reference/architecture/*` and `/reference/motor-systems/*` (originally moved to `/design/` in Batch 3) within the six design pages.
- `docs/_data/navigation.yml` Reference group updated to point at `/tools/...` URLs.
- Removed empty source directories: `docs/rag-browser/`, `docs/glossary/`, `docs/crosswalks/`, `docs/reference/`.
- Fixed relative-link regression in `tools/crosswalks/compare/index.md` where `../../standards/` no longer resolves from the deeper path; rewrote to absolute `{{ '/standards/' | relative_url }}`.
- Jekyll build clean (259 HTML files); internal link check exit 0.

## 2026-04-13 — Phase 24 COMPLETE: Training visual upgrades

**Type:** Content / Training Enhancement
**Status:** Complete

### Task 2 — Semiconductor Fab Tool scenario page visual aids

- Added `## Design Workflow Overview` flowchart (LR, 4-phase) after the Standard Stack table
- Added `## Process Start Permissive Flow` flowchart (5-permissive gate chain: exhaust, gas detector, doors, HV/RF, manual reset → gas/RF enable)
- Added `## Fault Trip Sequence` flowchart (4 fault types → Safety PLC → close NC valves + disable RF/HV + stop motion + alarm → latch → manual reset → standby)
- Added `### HV Access Interlock Flow` inside Key Engineering Decisions (discharge loop with polling)
- Added `### Cybersecurity Zone Diagram` inside Key Engineering Decisions (fab host → firewall → tool controller; Safety PLC shown as hardwired-only, not network-reachable)
- Jekyll build: clean

---

## 2026-04-13 — Phase 24 Task 1 complete: IEC earthing systems visual upgrades

**Type:** Content / Training Enhancement
**Status:** Complete

- Added visual summary flowchart (fault return path decision tree) after the IEC letter-code tables
- Added compact Mermaid topology diagrams for each of the five earthing systems (TN-C, TT, TN-C-S, TN-S, IT)
- Added per-system blockquote callout cards (fault return / protection / main risk)
- Added "Machine designer takeaway" bold paragraph after each system's callout
- Replaced the existing 5-column comparison table with an expanded version including "Typical clearing method" column and bold System names
- Added "Selection logic — what are you optimizing for?" flowchart section before "The practical questions to ask"
- Jekyll build remains clean (no errors or warnings)

## 2026-04-12 — Phase 24 planning seeded with earthing-systems visual upgrade

**Type:** Project Direction
**Status:** Planned

- Updated `project_state/project_state.md` so the next tracked phase is `Phase 24 PLANNING — Training Visual Upgrades`
- Queued a visual enhancement pass for `docs/training/fundamentals/earthing-systems-iec/index.md`
- Recorded `planning/ground_earth_visual.md` as the implementation note for the earthing-systems page upgrade
- Captured the expected scope: overview fault-path visual, five compact system diagrams, decision tree, comparison table cleanup, and short per-system callout cards

## 2026-04-12 — Phase 23 Complete: Semiconductor Facility Build Phases 3 & 4

**Type:** Content / Standards Reference
**Status:** Complete

- Promoted 3 instrumentation staging files to RAG corpus (`device_family_library.md`, `vendor_families.md`, `alarm_and_measurement_strategy.md`)
- Authored new `commissioning_reference.md` RAG file; updated `_index.yaml` with 4 new entries
- Built 5 new Jekyll pages:
  - `/instrumentation/device-families/` — device family library grouped by function
  - `/instrumentation/vendor-families/` — manufacturer comparison by measurement class (pressure, flow, UPW, MFCs, gas detection, level, vacuum, cleanroom)
  - `/instrumentation/alarm-strategy/` — alarm philosophy, measurement windows, alarm classes, safe-state design
  - `/commissioning/` — phase-based commissioning framework with readiness criteria and system-specific notes
  - `/crosswalks/` — system-to-system dependency map and standards-to-systems crosswalk
- Added "In This Section" navigation block to instrumentation landing page
- Updated `navigation.yml` (instrumentation sub-pages + Commissioning + System Crosswalks under facility)
- Updated facility `index.md` scope table
- Jekyll build: clean, 157 pages

## 2026-04-11 — Phase 22 Complete: Semiconductor Facility Reference (10 pages)

Second slice — four additional pages:

- HVAC and Cleanroom (room pressure cascade, ISO 14644, particle monitoring)
- Bulk Chemical Distribution (storage, transfer sequencing, containment, SEMI F39/F57)
- Safety and Shutdown Architecture (4-layer shutdown model, cause-and-effect, SIL integration)
- Common Control Philosophy (modes, state machine, permissives/interlocks/trips, safe-state rules)
- Facility overview and semiconductor industry page updated; navigation extended
- Jekyll build: clean, 152 pages

## 2026-04-11 — Phase 22 First Slice: Semiconductor Facility Reference

- Fixed AI boundary headers on 7 RAG files; validate_ai_boundaries.py now passes 316/316
- Committed `planning/semi_facility/` staging area to git
- Promoted 10 staging files to `control-standards/rag/design_framework/semiconductor_facility/` with proper headers and `_index.yaml`
- Built 6 new Jekyll pages under `docs/industries/semiconductor/facility/`:
  - Facility overview + standards selection flowchart
  - Bulk Specialty Gas Systems
  - UPW and Wastewater Systems
  - Exhaust and Abatement Systems
  - Tool-Facility Interface
  - Instrumentation Reference (full use matrix by system)
- Added Semiconductor Facility sub-tree to `docs/_data/navigation.yml`
- Cross-linked from existing semiconductor industry page
- Jekyll build: clean, 148 pages (up from 142)

## 2026-03-27 — Control Systems Training Expansion (7 new modules)

- Added 7 training modules to `docs/training/control-systems/` from `planning/phase_27march26/` content:
  - Machine State Model (FSM types, state design, fault handling)
  - Interlocks, Permissives & Safety Trips (definitions, logic separation, bypass design)
  - Async Faults in Distributed Systems (detection, classification, response, recovery)
  - Deterministic vs Non-Deterministic Control (real-time requirements, architecture separation)
  - Servo Tuning Strategy (loop-by-loop workflow, resonance detection, notch filters, feedforward)
  - Vibration and Resonance (causes, detection, mechanical and control mitigation)
  - Multi-Axis Coordination (master-slave, electronic gearing, interpolation, gantry)
- Updated `_data/training_catalog.yml`: 7 module entries added, module_count 7 → 14, description updated
- Jekyll build: clean
- `planning/phase_27march26/things_to_fix.md` (lifecycle improvements) deferred — separate task

## 2026-03-22 — Phase 21: Lifecycle Stage Page Expansion

- Expanded all 12 lifecycle stage pages (Stages 01–11 plus Safety Wiring) from thin stubs (41–74 lines) to comprehensive engineering references (580–1000+ lines)
- Created 2 new pages: Stage 3.5 (Safety Requirements Specification) and Stage 12 (Management of Change)
- Updated `docs/lifecycle/index.md` with expanded introduction section and 13-stage table (all stages now comprehensive)
- All lifecycle pages now follow consistent content pattern: purpose/scope, key decisions, related standards, practical guidance, checklists, cross-links to training/workflows/reference material
- No new pages added beyond the 2 planned new stages; lifecycle section maintains stable URL structure
- Jekyll build: clean, 132 pages (no change in page count from Phase 20)

## 2026-03-15 — Phase 20: Software Safety Stack Deepening

- Updated RAG source `Software_Safety_and_Intrinsic_Safety_Standards.md`: IEC 61131-3 edition note updated to 2025; Normal PLC / Safety PLC / SIS comparison table added; E-stop section fully replaced with canonical tag names (SI_ESTOP_CH1, ESTOP_HEALTHY, SAFETY_ENABLE), 7-rung pseudocode, I/O list, sequence of operation, documentation and logging checklists; Rockwell GuardLogix and Siemens S7-1500F vendor patterns added
- Updated `/software-stack/` site page: edition note updated; comparison table section added; E-stop section replaced with expanded content including Mermaid wiring/architecture flowchart and state machine diagram; vendor patterns in `<details>` expandable blocks
- No new pages; no navigation changes; build remains clean at 132 pages

### 2026-03-15 — Phase 20 changed to software safety routing work

- Updated `project_state/project_state.md` so the next tracked phase is now `Phase 20 QUEUED — Software Safety, Traceability, and Cybersecurity Routing`
- Added a Phase 20 queue section sourced from `planning/safety_software_stack.md`
- Replaced the previous Phase 20 scenario-driven learning candidate as the active next-phase entry in project state

### 2026-03-15 — Software stack reference flow rebuilt from planning + RAG

- Rewrote `control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md` into a tighter reference flow: scope boundary, quick answers, routing, traceability/logging, redundancy, worked E-stop example, cybersecurity, wiring, intrinsic safety, and implementation deliverables
- Merged high-value practical content from `planning/safety_software_stack.md` into the canonical RAG source without pulling the planning file itself into the site or RAG browser
- Updated `docs/software-stack/index.md` to match the new flow and remove the older IEC 61131-3 presentation that was less aligned with the practical question the page is answering
- Jekyll build: clean after rewrite; AI boundary validator still reports pre-existing unrelated violations elsewhere in the RAG corpus

### 2026-03-14 — Project state reconciled after Phase 19 completion

- Updated `project_state/project_state.md` to reflect that Phases 18 and 19 are fully complete with no active implementation backlog remaining from those tracks
- Changed `Next Phase` from `Phase 20 TBD` to `Phase 20 CANDIDATE — Scenario-Driven Learning Layer`
- Rewrote the `Current Direction` section to reflect planning-mode status rather than queued Phase 18/19 implementation work
- Removed the stale `Phase 18 Backlog` and `Phase 19 Queue` sections and replaced them with a Phase 20 candidate summary sourced from the cross-layer integration pre-plan

### 2026-03-14 — Phase 19: Engineering Workflow Navigation Refactor

- Created `docs/_data/navigation.yml` — 5-group sidebar data model (Engineering Workflow, Standards, Training, Industries, Reference)
- Refactored `docs/_includes/sidebar.html` from 135-line hardcoded HTML to ~60-line data-driven Liquid renderer
- Added `/engineering-workflow/` hub page with 5 task-grouped sections (Design & Architecture, Select & Size, Commission & Verify, Troubleshoot, Scenarios)
- Expanded `/reference/` landing page with Quick Reference section (Glossary, Crosswalks, Software Stack, RAG File Browser)
- Demoted Scenarios, Crosswalks, and Workflows from top-level sidebar into Engineering Workflow and Reference hub groups
- Jekyll build: clean, 132 pages

### 2026-03-14 — Phase 18 Track C: Reference Section + Commissioning Templates Redesign

- Added `/reference/` section: landing page + 4 content pages (machine architecture model, machine safety architecture, compliance stack, motor selection matrix)
- Added new "Reference Models" sidebar block with Architecture and Motor Systems sub-groups + `.sidebar__group-label` CSS
- Renamed `/field-engineering/` → `/commissioning-templates/`: 7 pages moved, old sub-pages removed, redirect at `/field-engineering/`
- Updated `field-checklist.html` layout: label renamed to "Commissioning Templates", template header block (6-field fill-in grid), checkbox DOM transformation script, back-link updated
- CSS additions: `.template-header`, `.checklist-item`, `.sidebar__group-label`, print checkbox styles
- URL updates: `field_checklists.yml` (6 entries), `training_catalog.yml` (13 URLs across 11 modules), 5 workflow pages
- Cross-links added: motor-selection workflow → motor-selection-matrix; semiconductor-equipment scenario → machine-architecture-model; semiconductor industry → compliance-stack
- Jekyll build: clean, 0.446 s, **129 pages** (matches spec target)

### 2026-03-13 — FE Study Tools: `.doc` File Support

- feat(fe_study): `.doc` file support — LibreOffice headless conversion, `howto_doc` family (P2 priority), cached under `_converted/`
- Conversion: LibreOffice headless (`soffice --headless --convert-to docx`), cached in `_converted/`
- Covers all `.doc` files under `planning/FE_Study/How to/`
- Filtered: `~$*.doc` temp/lock files excluded from scanning
- Full test suite: 15/15 PASS

### 2026-03-13 — Phase 18 Track B: Field Engineering Section

- Added `/field-engineering/` site section with 7 pages (landing + 6 commissioning checklists)
- New `field-checklist` layout with Liquid data lookup from `field_checklists.yml`, "When to use" box, cross-links block, and print-optimized view
- Created `docs/_data/field_checklists.yml` flat YAML catalog driving all checklist metadata
- CSS additions: `.checklist-body` (☐ pseudo-element), `.field-checklist__cross-links`, `.cross-links-group`, print hiding rules
- Reverse links: `related_checklists` key added to 11 training module entries in `training_catalog.yml`; `training-module.html` updated to render them
- Reverse links: "Related Checklists" sections appended to 5 workflow pages
- Sidebar: Field Engineering section with 7 links and active state logic
- Jekyll build: clean, 123 pages

### 2026-03-13 — Phase 19 engineering-workflow navigation refactor queued

- Added plan doc: `docs/plans/2026-03-13-phase19-engineering-workflow-navigation.md`
- Queued Phase 19 in `project_state/project_state.md` as the next navigation refactor after Phase 18 Track C
- Recorded that the first refactor pass will keep current URLs stable, add workflow/reference hub pages, and move the sidebar toward a data-driven model

### 2026-03-13 — Phase 18 Track A: Control Systems training surfaced (9 new pages)

- Added `/training/control-systems/` group landing page and 7 module pages: Control Theory Overview, PID Foundation, PID Intuition, Industrial PID Implementation, Control Loop Architectures, PID Heater Control, PID Drone Control
- Added `/training/fundamentals/earthing-systems-iec/` page covering IEC TN-C/TT/TN-C-S/TN-S/IT earthing systems with comparison table
- Updated `docs/_data/training_catalog.yml`: control-systems topic group (7 modules), Control Systems Engineering learning path, start-here audience entry, fundamentals count 8→9, earthing module entry
- Updated sidebar: Control Systems link added under Training section
- Fundamentals group index updated: description and module count 8→9
- Jekyll build: clean, 116 pages (up from 107)

### 2026-03-13 — Project-state backlog reconciled after Phase 17

- Updated `project_state/project_state.md` to reflect the actual post-Phase-17 site state: 107-page clean build, 45-term glossary, 9 scenarios, 6 crosswalk pages, 32 surfaced training modules, 5 workflow pages, and standards graph coverage that already includes IEC 60079, IEC 61511, and SEMI
- Clarified `Next Phase` as `Phase 18 QUEUED — Field Engineering, Reference Library, and Control Systems Training`
- Replaced the stale note that Control Systems training needs new RAG corpus; canonical `training_modules/control_systems/` content already exists, so the remaining work is site surfacing and navigation
- Marked the old GitHub Pages deployment notes as completed and converted the old Phase 3 backlog note into historical carryover status
- Added direct references in `project_state/project_state.md` to the Phase 18 control-systems plan and the field/reference pre-plan

### 2026-03-10 — Phase 16 complete: NEC training expansion — 11-module NEC track

- Expanded NEC application training track from 3 to 11 modules (8 new RAG files + 8 new site pages)
- New RAG files in `control-standards/rag/training_modules/nec_application/`: branch_circuits_vs_feeders_motor_loads.md, disconnecting_means_for_machinery.md, grounding_bonding_control_panels.md, sccr_workflow.md, conductor_ocpd_sizing_examples.md, class1_class2_remote_control_circuits.md, article_430_practical_workflow.md, article_409_practical_workflow.md
- All 8 RAG files mirrored to `docs/assets/rag-files/training_modules/nec_application/`
- `control-standards/rag/training_modules/nec_application/_index.yaml` updated to 11 files
- `docs/_data/training_catalog.yml`: 8 new module entries added; nec-application topic_group module_count updated to 11; panel-design-nec learning path expanded with 4 new URLs
- `docs/training/nec-application/index.md`: description updated to 11 modules; recommended entry modules expanded to 4; page header updated
- `docs/training/nec-application/motor-panel-code-application/index.md`: footer next-link updated to point to branch-circuits-vs-feeders
- `docs/_data/rag_tree.json` regenerated (249 .md files, 5 top-level entries)
- Jekyll build: clean (0.529 s)

### 2026-03-10 — Phase 16 partial: four additional NEC site pages (pages 5–8)

- Added `docs/training/nec-application/conductor-ocpd-sizing/index.md` — step-by-step Art 430 sizing: table FLC, 125% conductor, 115%/125% overload, Table 430.52 OCPD, Table 250.122 EGC; full worked examples for 10 HP and 25 HP motors; Art 430.24 feeder formula with three-motor example; quick-reference HP sizing table (1–50 HP at 460/480 V); common mistakes table; won't-start exception explained
- Added `docs/training/nec-application/class1-class2-circuits/index.md` — Art 725 circuit classification (Class 1/2/3), supply-listing rule, 24 VDC PLC I/O as Class 2, Mermaid classification flowchart, Art 725.136 separation rules (separate duct / barrier), NFPA 79 color coding (blue=24 VDC, red=120 VAC), common mistakes table
- Added `docs/training/nec-application/article-430-workflow/index.md` — Art 430 Parts routing table (Parts I–X), Art 430.6(A) table-not-nameplate rule, Mermaid motor-circuit question router, standard 5-step sizing sequence (table FLC → conductor → overload → OCPD → disconnect), full worked example for 25 HP 460 V through all 5 steps, won't-start exception procedure, NFPA 79 alignment notes
- Added `docs/training/nec-application/article-409-workflow/index.md` — Art 409 ICP scope (factory-built assembly), Art 409.20 supply conductor sizing formula (125% largest motor + 100% others + 125% resistance heating), worked example with 25 HP + 10 HP motors, Art 409.110 required markings table (SCCR, FLC, enclosure type), Art 409.22 OCPD sizing, Art 409 vs. UL 508A comparison table (code vs. product standard), ICP (Art 409) vs. MCC (Art 430 Part F) comparison table, pre-shipment inspection checklist
- All four pages use `layout: training-module`, correct breadcrumbs, prev/next navigation, and Mermaid diagrams where specified
- Prev/next chain now complete: sccr-workflow → conductor-ocpd-sizing → class1-class2-circuits → article-430-workflow → article-409-workflow (terminus)

### 2026-03-10 — Phase 16 partial: four new NEC site pages

- Added `docs/training/nec-application/branch-circuits-vs-feeders/index.md` — branch circuit vs. feeder boundary, Art 430.22 125% conductor rule, Art 430.24 multi-motor feeder formula, Mermaid circuit flow, nameplate vs. table FLC common mistake
- Added `docs/training/nec-application/disconnecting-means/index.md` — Art 430.102 in-sight rule (visible + ≤50 ft), permitted disconnect types (HP-rated switch, MCCB, molded-case switch), NFPA 79 §6.2 lockable main disconnect, group disconnect exception Art 430.112, VFD placement rule (input side only), Mermaid VFD flow
- Added `docs/training/nec-application/grounding-bonding-panels/index.md` — grounding vs. bonding distinction, EGC sizing from Table 250.122 (earth rod is not the fault-current path), EGC sizing reference table (15A–200A), neutral/ground separation at downstream panels, enclosure bonding, VFD grounding notes, Mermaid 4-wire feeder flow
- Added `docs/training/nec-application/sccr-workflow/index.md` — SCCR definition, NEC 409.110 marking requirement, available fault current concept, UL 508A Supplement SB 4-step component method, current-limiting device raise strategy, Mermaid SB workflow diagram, 5 kA contactor default trap
- All pages use `layout: training-module`, correct breadcrumb, prev/next navigation, and Mermaid diagrams
- `training_catalog.yml` entries for these 4 modules still pending

### 2026-03-10 — Phase 15 complete: Training Module UX

- Created `docs/_layouts/training-module.html` — dedicated layout that looks up module metadata from `training_catalog.yml` by `page.url` and renders level chip, time, type, focus, Core badge, outcome sentence, and prerequisites before page content
- Added CSS: `.module-meta-bar`, `.module-outcome`, `.module-prereqs` to `main.css`
- Batch-updated all 24 module pages: layout changed to `training-module`, hardcoded page-header div removed, breadcrumb labels updated to new display names (Electrical Fundamentals, Motors Drives and Motion, NEC for Machines and Panels)
- Jekyll build: clean, 0.535 s

### 2026-03-10 — Phase 14 complete: Training Curriculum Upgrade

- Created `docs/_data/training_catalog.yml` — shared data model for all 24 modules with level, time, type, focus, prerequisites, featured flag, learning paths, start-here entries, and related standards
- Added training-specific CSS section to `docs/assets/css/main.css` — verification note, start-here cards, learning-path cards, training chips/badges (beginner/intermediate/advanced/concept/reference/code/featured), module table wrapper, related-standards strip, mobile responsive rules
- Rewrote `docs/training/index.md` — now a curriculum hub with verification note, start-here audience cards, four learning paths, browse-by-topic cards, data-driven all-modules table with metadata, and a related-standards strip; trust-boundary include retained at bottom
- Upgraded `docs/training/fundamentals/index.md` — new display label "Electrical Fundamentals", group intro, recommended entry modules, metadata-rich table driven from catalog
- Upgraded `docs/training/electrical-machines/index.md` — renamed to "Motors, Drives, and Motion", group intro, recommended entry modules, metadata-rich table
- Upgraded `docs/training/nec-application/index.md` — renamed to "NEC for Machines and Panels", group intro, recommended entry modules, metadata-rich table, note about Phase 16 expansion
- Updated sidebar labels to match new display names (URLs unchanged)
- Jekyll build: clean, 0.391 s

### 2026-03-11 — Post-Phase 16 site planning expanded for control-systems and eVTOL content

- Updated `docs/plans/2026-03-10-training-system-integration-preplan.md` to reserve a future `docs/training/control-systems/` route for the new PID/control-loop material
- Added a candidate scenario/page for a paraphrased public-source Archer vs. Joby eVTOL motor architecture comparison
- Recorded page rules that future public-source application notes should be paraphrased engineering analysis rather than raw transcript dumps or authoritative standards guidance
- Updated `project_state/project_state.md` post-Phase 16 target themes without changing the queued Phase 14-16 sequence

### 2026-03-10 — Training system integration pre-plan added

- Added planning-prep note: `docs/plans/2026-03-10-training-system-integration-preplan.md`
- Captured the current architecture gap between training, standards, lifecycle, scenarios, workflows, field checklists, and reference material
- Documented a post-Phase 16 candidate breakdown for:
  - cross-layer knowledge routing
  - field engineering and reference-library surfacing
  - safety and machine-architecture training expansion
  - scenario-driven learning
- Updated `project_state/project_state.md` with a post-Phase 16 planning candidate reference without changing the current queued Phase 14-16 sequence

### 2026-03-10 — Phase 14 training curriculum planning docs added

- Added design doc: `docs/plans/2026-03-10-phase14-training-curriculum-design.md`
- Added implementation plan: `docs/plans/2026-03-10-phase14-training-curriculum-implementation.md`
- Updated `project_state/project_state.md` Phase 14 section to reference the new planning docs
- Planning direction keeps current URLs stable while redesigning `/training/` around Start Here, Learning Paths, metadata-backed tables, filters, standards links, and a top-of-page verification note

### 2026-03-10 — Training page review converted into queued Phase 14-16 work

- `project_state/project_state.md` — next planned work changed from generic maintenance to `Phase 14 QUEUED — Training Curriculum Upgrade`
- Recorded that the current `/training/` section is complete but still behaves more like a browsable module index than a guided learning system
- Added `Phase 14 Scope — Training Curriculum Upgrade` for Start Here entry points, learning paths, audience framing, stronger hierarchy, outcome-focused copy, and a top-of-page verification note
- Added `Phase 15 Scope — Training Metadata And Module UX` for module chips and metadata fields covering level, time, prerequisites, type, role focus, and optional filtering/sorting
- Added `Phase 16 Scope — NEC Training Expansion` to grow NEC training from 3 modules to at least 8-10 modules with practical Article 409/430, SCCR, bonding, OCPD, and control-circuit topics

### 2026-03-10 — Phase 13 COMPLETE — all secondary backlog items done

- `docs/crosswalks/iec61511-iec61508/index.md` — new crosswalk: process SIS (IEC 61511) vs. functional safety foundation (IEC 61508); lifecycle comparison, SIL framework, architecture constraints, prior use, clause cross-reference (~250 lines)
- `docs/crosswalks/iec60079-nec-500-505/index.md` — new crosswalk: Zone vs. Division hazardous area; classification tables, EPL, gas groups, equipment marking, protection types, Zone/Division selection flow (~260 lines)
- `docs/crosswalks/index.md` — 2 new rows added
- `docs/_includes/sidebar.html` — 2 new crosswalk sidebar links
- All remaining Phase 13 backlog items confirmed complete: industry pages (5), standards graph (IEC 60079/61511/SEMI nodes), glossary (45 terms)
- Build: clean

### 2026-03-09 — Training site pages complete (24 modules)

- `docs/training/index.md` — landing page, 24 modules in 3 groups
- `docs/training/fundamentals/` — 8 pages: circuit theory, components, equations, conductor sizing
- `docs/training/electrical-machines/` — 13 pages: motors, drives, servo systems
- `docs/training/nec-application/` — 3 pages: code reading, table navigation, motor/panel application
- Sidebar updated with Training section (Training → Fundamentals / Electrical Machines / NEC Application)
- Build: 85 pages, clean

---

### 2026-03-09 — Motor interview source note promoted into additional training and design files

- `control-standards/work/design/check_this.md` — used as a read-only source for motor interview-style fundamentals, VFD electrical design points, and troubleshooting patterns; source file left unchanged.
- `control-standards/rag/training_modules/electrical_machines/` — added `motor_and_vfd_equations_reference.md`, `motor_efficiency_power_factor_and_losses.md`, `motor_control_methods_and_operating_regions.md`, and `servo_feedback_and_inertia_matching.md`; updated the module README and `_index.yaml`.
- `control-standards/rag/design_framework/motor_systems/` — added `motor_cable_and_protection_review.md` and `motor_symptom_troubleshooting_patterns.md`; updated the module README and `_index.yaml`.

---

### 2026-03-09 — Phase 12 Complete: Offshore / Marine Industry Overlay

- `DNV_OS_D201__electrical_installations.md` — RAG module: marine grade, IT earthing, LSOH cable, DP class, ESD/F&G class requirements, class approval workflow
- `ABS_offshore_electrical_control.md` — RAG module: ABS class notations, type approval, IT earthing implications, emergency power requirements
- `docs/industries/offshore/index.md` — full reference page: standards matrix by phase, DNV/ABS selection flow, IT earthing, LSOH, 11-item compliance checklist
- `docs/industries/marine/index.md` — deepened with IMO regulatory framework, IEC 60092 series structure, marine vs. offshore comparison; IEC 60092 corpus gap documented
- `docs/scenarios/offshore-platform-control/index.md` — Scenario 09: 4-phase workflow, ESD level hierarchy, Mermaid power/ESD architecture diagram, IT earthing and FAT decisions
- Scenarios index and sidebar updated

---

### 2026-03-09 — Electrical Knowledge Integration complete

Promoted three transcript-derived electrical learning sources into the existing canonical RAG layers.
No new parallel layer created. All content routes into existing `training_modules/`, `design_framework/`,
`commissioning_checklists/checklists/`, and `standards_intelligence/crosswalks/overlap_notes/`.

Design doc: `docs/plans/2026-03-08-electrical-intelligence-integration-design.md`

#### training_modules/fundamentals/ (new)

- 7 files: `electrical_quantities_and_circuit_language`, `series_parallel_and_divider_methods`,
  `kirchhoff_laws_and_systematic_analysis`, `equivalent_circuit_methods`,
  `electrical_equations_reference`, `passive_components_resistors_capacitors`,
  `diodes_transistors_and_switching_basics`

#### training_modules/electrical_machines/ (expanded)

- 3 core motor files + 6 additional: `vfd_fundamentals`, `servo_drive_fundamentals`,
  `ac_vs_dc_motor_comparison`, `motor_family_comparison`,
  `brushless_dc_ev_and_drone_motor_comparison`, `vfd_and_servo_architecture_diagrams`

#### training_modules/nec_application/ (new)

- 3 files: `nec_code_reading_fundamentals`, `working_space_and_table_navigation`,
  `motor_and_panel_code_application`

#### design_framework/electrical_review/ (new)

- 4 files: `ohms_law_and_power_check_workflow`, `basic_resistive_network_review`,
  `component_selection_basics`, `simple_signal_and_interface_circuit_notes`

#### design_framework/motor_systems/ (expanded)

- 13 total files including: selection workflow, nameplate checklist, star-delta notes,
  VFD integration review, commissioning workflows, troubleshooting decision tree,
  comparison matrices, integrated-drive architecture notes

#### commissioning_checklists/checklists/ (expanded)

- 6 files: motor rotation/overload, nameplate/overload setting, circuit polarity,
  capacitor discharge, drive commissioning, pre-power panel check

#### standards_intelligence/crosswalks/overlap_notes/ (gap fill)

- `overlap__motors_drives.md`
- `overlap_nfpa79_iec60204__motors_drives.md`

---

### 2026-03-09 — Integrated motor-drive architecture notes extracted from work-note source

- `control-standards/work/design/check_this.md` — used as a read-only source for integrated drive-on-motor content; source file left unchanged during extraction.
- `control-standards/rag/design_framework/motor_systems/` — added `integrated_motor_drive_architecture_comparison.md`, `industrial_vs_ev_vs_drone_motor_drive_standards_matrix.md`, `motor_mounted_drive_thermal_and_emc_design_notes.md`, `integrated_drive_failure_modes_and_tradeoffs.md`, and `integrated_drive_serviceability_and_field_replacement_review.md`.
- `control-standards/rag/design_framework/motor_systems/README.md` and `_index.yaml` — updated to include the new integrated-drive architecture note set.

---

### 2026-03-09 — Motor comparison pages extracted from work-note source

- `control-standards/work/design/check_this.md` — used as a read-only source for new motor comparison and architecture content; source file left unchanged during the extraction pass.
- `control-standards/rag/training_modules/electrical_machines/` — added `motor_family_comparison.md`, `ac_vs_dc_motor_comparison.md`, `vfd_and_servo_architecture_diagrams.md`, and `brushless_dc_ev_and_drone_motor_comparison.md`; updated the module README and `_index.yaml`.
- `control-standards/rag/design_framework/motor_systems/motor_selection_comparison_matrix.md` — added a concept-stage motor-family selection matrix; updated the module README and `_index.yaml`.

---

### 2026-03-09 — Motor comparison/diagram source note normalized for RAG promotion prep

- `control-standards/work/design/check_this.md` — converted a raw generated draft on motor, VFD, servo, BLDC, EV, and drone comparison pages into a scoped promotion-prep note.
- The note now identifies which content should enrich existing motor fundamentals files, which new RAG files are high-value next additions, and which EV/drone topics should remain lower-priority unless the repository scope expands.

---

### 2026-03-09 — Motor/VFD/servo RAG modules expanded from updated work note

- `control-standards/work/design/check_this.md` — used as a source note for additional motor-drive training, workflow, and checklist content; source left in place as work material.
- `control-standards/rag/training_modules/electrical_machines/` — added `vfd_fundamentals.md` and `servo_drive_fundamentals.md`, and updated the module README and `_index.yaml`.
- `control-standards/rag/design_framework/motor_systems/` — added `motor_troubleshooting_decision_tree.md`, `vfd_commissioning_workflow.md`, and `servo_commissioning_workflow.md`, and updated the module README and `_index.yaml`.
- `control-standards/rag/commissioning_checklists/checklists/drive_commissioning.md` — added a field checklist for first drive power-up and early verification; checklist README and `_index.yaml` updated accordingly.

---

### 2026-03-09 — Templates folder refreshed to current project conventions

- `control-standards/templates/README.md` — rewritten to match the current repo structure and actual available templates.
- `control-standards/templates/md_headers/` — refreshed `rag_approved_header.md` and `draft_only_header.md`, and added `archived_header.md` in the current metadata style.
- `control-standards/templates/checklists/checklist_template.md` — added a real checklist starter.
- `control-standards/templates/design_guides/design_guide_template.md` — added a design-guide starter.
- `control-standards/templates/reports/report_template.md` — added a report starter.
- `control-standards/templates/work_notes/work_note_template.md` — added a work-note starter for transcript-derived and normalized source notes.

---

### 2026-03-09 — Pre-power commissioning checklist promoted from work note

- `control-standards/work/design/check_this.md` — normalized as a commissioning source note for pre-power panel and incoming-supply verification.
- `control-standards/rag/commissioning_checklists/checklists/pre_power_panel_and_incoming_supply_check.md` — added a new pre-power checklist covering incoming supply, upstream protection, panel inspection, grounding/bonding, staged energization, and stored-energy awareness.
- `control-standards/rag/commissioning_checklists/README.md` and `checklists/README.md` — updated to reflect the expanded checklist set.
- `control-standards/rag/commissioning_checklists/checklists/_index.yaml` — updated with the new pre-power checklist.

---

### 2026-03-09 — Fundamentals training modules expanded from circuit-analysis source set

- `control-standards/rag/training_modules/fundamentals/` — added seven missing fundamentals modules covering circuit language, series/parallel methods, Kirchhoff laws, equivalent-circuit methods, electrical equations, passive components, and diode/transistor switching basics.
- `control-standards/rag/training_modules/fundamentals/README.md` — updated to reflect the expanded fundamentals module set.
- `control-standards/rag/training_modules/fundamentals/_index.yaml` — updated with the new module list.

---

### 2026-03-09 — Electrical integration design and implementation docs rewritten

- `docs/plans/2026-03-08-electrical-intelligence-integration-design.md` — replaced the obsolete `electrical_intelligence/` parallel-layer design with the current canonical architecture using `training_modules`, `design_framework`, `commissioning_checklists/checklists`, and `standards_intelligence`.
- `docs/plans/2026-03-08-electrical-intelligence-integration-plan.md` — replaced the stale implementation plan with a current executable backlog focused on the remaining circuit-analysis promotions and current validation constraints.

---

### 2026-03-09 — Electrical integration requirements doc added

- `docs/plans/2026-03-08-electrical-intelligence-integration-requirements.md` — added a concrete requirement list covering architecture, source readiness, metadata, target files, engineering-rule constraints, validation, and acceptance criteria for rewriting the Phase 11 electrical integration docs.

---

### 2026-03-09 — Missing electrical-intelligence components promoted into current RAG architecture

- `control-standards/work/design/project_implementation_gaps/nec_exam_prep_topics/` — added a normalized source package from `electrical exam prep.md`, including README and integration guidance based on the source's real content.
- `control-standards/rag/training_modules/` — added root README/index plus new `electrical_machines/` and `nec_application/` submodules with induction-motor, DC-motor, nameplate/slip/torque, NEC code-reading, table-navigation, and article-routing modules.
- `control-standards/rag/design_framework/electrical_review/` — added quick electrical review workflows for Ohm's law, resistive networks, component selection, and simple interface circuits.
- `control-standards/rag/design_framework/motor_systems/` — added motor selection, nameplate review, star/delta supply matching, and VFD integration review notes.
- `control-standards/rag/commissioning_checklists/` — added root README/index plus starter field checklists for circuit polarity/power, capacitor discharge awareness, and motor startup verification.
- `control-standards/rag/standards_intelligence/crosswalks/overlap_notes/` — added the previously missing `motors_drives` overlap notes for UL 508A/NEC/NFPA 79 and NFPA 79/IEC 60204-1 routing.

---

### 2026-03-09 — Design framework minimum viable set created

- `control-standards/rag/design_framework/README.md` — added module purpose and scope note.
- `control-standards/rag/design_framework/_index.yaml` — added seeded-content index for the design framework.
- `control-standards/rag/design_framework/design_guides/02_power_distribution_guide.md` — added applied power-distribution workflow guide.
- `control-standards/rag/design_framework/constraints/grounding_bonding_rules.yaml` — added reusable grounding and bonding ruleset.
- `control-standards/rag/design_framework/us_eu_compliance_wizard/` — added wizard README, spec, rules, and delta-report template to satisfy existing internal references.

---

### 2026-03-09 — Google tag added sitewide

- `docs/_layouts/default.html` — added the Google tag (`gtag.js`) snippet in `<head>` with measurement ID `G-RPL3G47EFZ`, which applies to every page using the default Jekyll layout.
- `project_state/project_state.md` — updated current-state tracking to record sitewide analytics installation.
- `project_state/environment.md` — recorded the active measurement ID and layout location for site analytics.
- Corrected the documented live GitHub Pages URL to `https://kyawminthu20.github.io/Control-System-Tools/`.

---

### 2026-03-09 — Conductor ampacity topic promoted into standards and training

- `control-standards/rag/training_modules/fundamentals/conductor_ampacity_and_termination_temperature.md` — new fundamentals training module covering ampacity, bundling, ambient correction, terminal temperature limits, and protection logic.
- `control-standards/rag/training_modules/fundamentals/README.md` — new fundamentals training-module index note.
- `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art240__overcurrent_protection.md` — corrected the Article 240.4 conductor-protection reference and expanded the conductor/OCPD coordination workflow.
- `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art310__conductors_for_general_wiring.md` — replaced placeholder artifacts with cleaner ampacity, current-carrying-conductor, and termination-temperature guidance.

---

### 2026-03-08 — UL 508A website update: scenario and lifecycle pages

- `docs/scenarios/us-industrial-control-panel/index.md` — major rework: 4 thin engineering decisions expanded to 12 topic-aligned decisions covering listing basis, enclosures, layout, spacing/creepage, wiring, SCCR (weakest-link), grounding, control circuits, motor controllers, transformers, marking, and E-stop; added inspection readiness checklist table.
- `docs/lifecycle/detailed-design/index.md` — key activities updated: old UL section number references replaced with descriptive topic references; SCCR bullet expanded with weakest-link logic; spacing/creepage bullet improved; deliverables table updated to match current RAG module names.

---

### 2026-03-08 — UL 508A spacing/creepage/clearance module populated

- `UL508A_2022__spacing_creepage_clearance.md` — populated from project working note: clearance vs creepage definitions, voltage-based heuristics (0–150 V, 151–300 V, 301–600 V), live parts review logic, mitigation methods (barriers, finger-safe, routing, layout), field inspection failure patterns.
- `docs/standards/us-electrical/ul-508a/index.md` — topic table updated (removed "in progress" marker); spacing/creepage section added between Enclosures and Wiring Methods.
- All 11 UL 508A RAG modules now populated.

---

### 2026-03-08 — UL 508A RAG populated; website updated

- All 11 UL 508A RAG modules filled from `_TODO_` to substantive practical guidance (10 populated; `spacing_creepage_clearance` still TODO).
- `docs/standards/us-electrical/ul-508a/index.md` — major rework: RAG-aligned topic table, practical topic sections for all 10 populated modules, expanded SCCR weakest-link section, marking/documentation section.
- `docs/crosswalks/ul508a-nec-nfpa79/index.md` — minor: expanded grounding row with safety vs noise grounding distinction.
- `docs/lifecycle/build/index.md` — expanded panel build activity into detailed UL 508A build checklist (layout, wiring, grounding, enclosure integrity, SCCR, nameplate).

---

### 2026-03-08 — Phase 11 Complete: Industry Overlay Depth

- `docs/industries/petroleum/index.md` — full reference page: standards matrix by phase, selection flow, checklist; all gap badges removed
- `docs/industries/semiconductor/index.md` — full reference page: SEMI badges updated to complete, applicability matrix, SEMI S2 compliance flow
- `docs/scenarios/oil-gas-process-skid/index.md` — Scenario 07: onshore O&G ESD/F&G/HIPPS with IEC 61511 + IEC 60079 + NEC workflow, Mermaid SIS diagram, engineering decisions
- `docs/scenarios/semiconductor-fab-tool/index.md` — Scenario 08: etch/CVD fab tool with SEMI S2/S14 gas control system, Mermaid interlock diagram, engineering decisions
- Scenarios index and sidebar updated with new entries

---

### 2026-03-08 — Phase 10 Complete: IEC 60079 + SEMI Corpus Gap-Fill

#### IEC 60079 (Hazardous Area)

- 6 new RAG files: Parts 0, 1, 10-1, 11, 14, 17
- \_index.yaml indexing all 6 parts
- 2 site pages: hazardous-area family landing + IEC 60079 standard page

#### SEMI S2/S8/S14 (Semiconductor Equipment Safety)

- 3 new RAG files: S2 (equipment safety), S8 (ergonomics), S14 (fire risk)
- \_index.yaml indexing all 3 standards
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
- Updated \_index.yaml: 19 articles now indexed (was 12); coverage_notes.complete updated
- Updated NEC_COMPLETION_STATUS.md: 19/19 articles complete (~9,500 words)
- Updated NEC_OVERVIEW.md: new sections for General, Power Distribution, Hazardous Locations, Emergency Power

**NEC corpus now covers:** general/definitions, power distribution, grounding, hazardous locations (Class/Division + Zone), IS systems, emergency power, industrial control panels, motors, conductors, wiring methods, overcurrent protection

---

### 2026-03-08 — NEC RAG Gap-Fill: Art250.4 Added

**Type:** RAG Corpus / Content
**Status:** Partial (250.4 complete; 409.70, 670.6 outstanding)

- Created `NEC_2023__Art250_4__purposes_of_grounding_and_bonding.md` — synthesized from NEC 250.4 code text and Mike Holt 2020 instructional content. No verbatim NEC text. Covers: system grounding vs equipment grounding, bonding vs grounding distinction, effective ground-fault current path, GEC routing rationale (inductive reactance / skin effect), grounded and ungrounded system differences, common engineering errors.
- Updated `_index.yaml`: registered NEC2023-Art250-4 entry using `note` field (valid); corrected `coverage_notes.complete` to list all 13 article files actually present in the corpus.
- Source file: `control-standards/archive/superseded_designs/work_design/promoted_to_rag/Grounding, System and Equipment [250.4, 2020 NEC].md` (raw transcript — not committed to RAG).
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

## 2026-03-11 — Phase 17: Cross-Layer Knowledge Routing

- Added `/workflows/` as first-class site section (Option A decision)
- 5 workflow pages: Motor Selection, Motor Troubleshooting, VFD Commissioning, Servo Commissioning, Electrical Review
- Extended training_catalog.yml: `related_workflows` field on 7 modules; Machine Lifecycle learning path added
- training-module.html layout updated to render Related Workflows block
- Sidebar Workflows section added (5 direct links)
- Workflow CSS: card grid, badges, wf-tags, related-workflows block
- Jekyll build: clean, 0.583 s, 107 pages
