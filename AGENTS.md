# Project Instructions for AI Agents

**Binding rule: before changing anything in this repository, read and follow
the standards in [`governance/`](governance/):**

1. [governance/PROJECT_ORGANIZATION.md](governance/PROJECT_ORGANIZATION.md) — what lives where, site taxonomy, naming/URL rules
2. [governance/CONTENT_STANDARDS.md](governance/CONTENT_STANDARDS.md) — site content: source discipline, copyright boundary, status vocabulary, page templates, voice rules
3. [governance/ENGINEERING_STANDARDS.md](governance/ENGINEERING_STANDARDS.md) — `cst` package, data files, templates, verification matrix
4. [governance/AI_WORKFLOW.md](governance/AI_WORKFLOW.md) — branch/commit/merge discipline, the phase loop, sub-agent rules, safety rails

These documents are authoritative. If an instruction elsewhere conflicts
with them, the governance documents win unless the user explicitly
overrides.

## Orientation

- Current state, phase, and next steps: [project_state/project_state.md](project_state/project_state.md)
- Tree reference (generated): [STRUCTURE_SUMMARY.md](STRUCTURE_SUMMARY.md)
- The repo has two tracks: the **Control Systems Engineering Field Guide**
  site (`docs/`) and the **`cst` Python toolkit** (`src/cst/`), both fed by
  the authoritative reference library at `control-standards/rag/`.

## Path Trust Tiers (summary — details in PROJECT_ORGANIZATION.md)

- **Canonical:** `control-standards/rag/` (prefer
  `standards_intelligence/` for standards questions),
  `control-standards/governance/`, `governance/`
- **Non-authoritative:** `control-standards/work/` — never cite as fact
- **Context only:** `control-standards/archive/`, `planning/`
- **AI-FORBIDDEN:** `control-standards/restricted/` and any
  `drafts_DO_NOT_READ/` path — do not read, cite, or git-track. Only touch
  if the user explicitly asks, and label the material as restricted.

## Non-Negotiables (full detail in the governance docs)

- Authoritative content is paraphrase — never copyrighted standards text,
  table values, or third-party material.
- New authoritative Markdown carries `AI_READ_ACCESS`, `CONTENT_CLASS`, and
  `STATUS` metadata; site pages carry the `review:` frontmatter block with
  the 5-term status vocabulary.
- AI-drafted content starts at "Review pending" — agents never mark their
  own work "Reviewed".
- Every meaningful change updates `project_state/`; validation gates run
  before merge (`uv run pytest`, Jekyll build, link check, boundary
  validator).
- No employer/customer data, credentials, network captures, or personal
  material in tracked files.
