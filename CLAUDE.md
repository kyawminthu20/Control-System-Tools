# Claude Workflow

**Binding rule: the repo-wide standards live in [`governance/`](governance/)
— PROJECT_ORGANIZATION, CONTENT_STANDARDS, ENGINEERING_STANDARDS, and
AI_WORKFLOW. Read the one covering what you're touching BEFORE changing it,
and follow it. Governance docs win over any conflicting instruction unless
the user explicitly overrides.**

## Project

Two tracks in one repo, both fed by the authoritative reference library:
- **Site** — Control Systems Engineering Field Guide (`docs/`, Jekyll,
  GitHub Pages; 9-section taxonomy, presentation layer only)
- **Toolkit** — the `cst` Python package (`src/cst/`): standards-cited
  calculators, panel/commissioning generators, PLC utilities, diagnostics

Key directories:
- `control-standards/rag/` — authoritative reference library (source of truth)
- `governance/` — repo-wide standards (binding)
- `src/cst/` + `tests/` — the toolkit and its test suite
- `data/standards_tables/` — licensed table values (user-supplied, gitignored; schemas committed)
- `tools/` — repo automation and validation scripts only
- `project_state/` — operational tracking (phase, changes, env, runbook)

## Quick Commands

```bash
uv sync                                  # install (editable) incl. cst CLI + dev deps
uv run pytest                            # full test suite (must be green before merge)
uv run cst --help                        # the toolkit CLI (22 subcommands)
python3 tools/project_automator.py       # refresh structure summary
python3 tools/validate_ai_boundaries.py  # validate AI content boundaries
python3 tools/generate_rag_tree.py       # sync corpus -> site mirror (manual, drifts!)
uv run python tools/generate_site_templates.py  # regenerate downloadable templates
python3 tools/check_internal_links.py docs/_site  # link check (after build)
bash tools/validate_reorg.sh all         # validate repo structure
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build   # build site
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll serve   # serve locally (http://localhost:4000/Control-System-Tools/)
```

> Python >=3.12 required; `uv` preferred. Ruby 2.6.10 (system macOS) +
> Bundler 2.4.22 locally; CI uses Ruby 3.2. Pushing `master` deploys the
> site via GitHub Actions — verify the run goes green.

Use `project_state/` as the operational memory for this repository.

## Required Automation Behavior

After any meaningful change, update the relevant files in `project_state/` as part of the same task.

Do not leave implementation changes without updating project tracking.

## File Ownership

- `project_state/project_state.md`
  - current phase
  - current implementation state
  - active priorities
  - what should be implemented next

- `project_state/change_log.md`
  - dated project-level changes
  - architecture or workflow changes
  - implementation milestones

- `project_state/environment.md`
  - versions
  - runtime requirements
  - tooling requirements
  - deployment requirements
  - environment variables

- `project_state/how_to.md`
  - setup steps
  - run steps
  - validation commands
  - deployment steps

## Update Triggers

Update `project_state/project_state.md` when:

- the phase changes
- the scope changes
- the current implementation state changes
- priorities or next implementation items change

Update `project_state/change_log.md` when:

- code changes materially
- documentation workflow changes
- architecture decisions change
- deployment direction changes

Update `project_state/environment.md` when:

- Python, Node, package, or tool requirements change
- build or deployment tooling changes
- environment variables are introduced or removed
- GitHub Pages or hosting assumptions change

Update `project_state/how_to.md` when:

- setup commands change
- run commands change
- validation commands change
- build or deploy steps change

## Current Project Direction

- Live site (public repo + GitHub Pages): https://kyawminthu20.github.io/Control-System-Tools/
- Authoritative knowledge stays in `control-standards/rag/`; the site is a
  presentation layer and never modifies it
- The `cst` toolkit is Python-first; the site documents it, never ports it to JS
- Current phase and next steps: `project_state/project_state.md`

## Site Architecture

- Jekyll 4.3, vanilla HTML/CSS/JS — no frameworks
- `baseurl: "/Control-System-Tools"` — internal links use `{{ '/path/' | relative_url }}`
- Three-panel CSS Grid layout (sidebar 240px + main 1fr + context 220px)
- Mermaid.js via CDN for diagrams (renders client-side — non-JS scrapers see raw blocks; that is expected)
- `docs/` is the Jekyll source root; `_config.yml` lives there
- Taxonomy, page templates, status vocabulary, and voice rules: `governance/CONTENT_STANDARDS.md`

## Use Existing Automation

When relevant, use the local automation scripts to keep repository documentation current:

- `python3 tools/project_automator.py`
- `python3 tools/validate_ai_boundaries.py`
- `python3 tools/fix_ai_boundaries.py`
- `bash tools/validate_reorg.sh all`

## Tool Usage

Prefer the Bash tool for file operations, searches, and shell commands. You are not required to use dedicated Read/Edit/Grep/Glob tools when Bash is faster or more convenient.

## End-Of-Task Checklist

1. Make the requested changes.
2. Update the affected files under `project_state/`.
3. Run relevant automation or validation if the changes warrant it.
4. Report what changed and any remaining gaps.
