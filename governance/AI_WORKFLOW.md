# AI Workflow

**Authoritative.** How any AI agent (Claude, Codex, or other) operates in
this repository. [AGENTS.md](../AGENTS.md) and [CLAUDE.md](../CLAUDE.md)
bind agents to this document.

## 1. Read Order (before changing anything)

1. `AGENTS.md` / `CLAUDE.md` (auto-loaded entry points)
2. `governance/PROJECT_ORGANIZATION.md` — where things live
3. The standard for what you're touching:
   [CONTENT_STANDARDS.md](CONTENT_STANDARDS.md) or
   [ENGINEERING_STANDARDS.md](ENGINEERING_STANDARDS.md)
4. `project_state/project_state.md` — current phase and open threads

**Path trust tiers** (unchanged from long-standing policy):
`control-standards/rag/` is canonical; `work/` is non-authoritative;
`archive/` is context; **`control-standards/restricted/` and any
`drafts_DO_NOT_READ/` path are AI-forbidden** — do not read, cite, or track.

## 2. Branch, Commit, Merge

- Never commit directly to `master`. One phase = one branch:
  `feat/phaseNN-short-slug` (or `fix/`, `docs/`, `chore/`).
- Conventional commits: `type(scope): message`. Substantive commits list
  what changed and why in the body.
- Merge to `master` with `--ff-only` after ALL validation gates pass
  (repo history is deliberately linear). Push triggers the Pages deploy;
  verify the deploy went green and spot-check live URLs.
- Author identity: the GitHub noreply email, never a personal address.

## 3. The Phase Loop (every meaningful unit of work)

1. Branch
2. Build the change per the applicable standard
3. Run the verification matrix (ENGINEERING_STANDARDS.md §5)
4. **Update `project_state/`** — this is not optional:
   - `change_log.md`: dated entry — what, why, validation results
   - `project_state.md`: header (Last Updated / Current Phase / Next Phase)
   - `environment.md` / `how_to.md`: only if requirements or commands changed
5. Commit → ff-merge → push → verify deploy + live pages
6. Report honestly: failures are reported as failures, skips as skips

## 4. Sub-Agent Orchestration

When fanning work out to parallel writer/worker agents:

- Give all agents ONE shared spec (frontmatter shape, section structure,
  voice rules) and point them at the relevant governance file(s).
- Sub-agents never edit `project_state/` — parallel edits collide. The
  coordinator records tracking once, after assembly.
- The coordinator verifies every delivered file (frontmatter present, voice
  rules, cross-link slugs) before building — agents get slugs wrong.
- New AI-drafted pages are `status: "Review pending"`. An agent never marks
  content "Reviewed".

## 5. Handling External Reviews and New Information

Lessons already paid for — follow them:

- Save incoming review documents to `planning/YYYY-MM-DD-<source>.md`
  (tracked) before acting.
- **Validate every claim against the current repo/site before adopting.**
  Reviews are often written against stale builds, wrong platforms (MkDocs
  advice for a Jekyll site), or non-JS scrapes ("Mermaid is broken" when it
  renders fine — check in a real browser).
- Triage into: false positive (document why) / fix now / phased backlog.
  Record decisions and the backlog in `project_state/change_log.md` so
  nothing silently drops.
- Genuinely good catches get fixed even when embarrassing; credit the
  review in the change log.

## 6. Safety Rails

- **Destructive operations** (history rewrites, force-push, deleting
  pre-existing files/worktrees, changing repo visibility or Pages config)
  require explicit user approval per operation — and a backup first
  (mirror clone to `~/Dev/_archive/`). Repo visibility changes are always
  the user's own action.
- **Sanitization is standing policy:** no third-party copyrighted material
  (courses, transcripts, vendor docs), no employer/customer data, no real
  network captures, no credentials, no personal-learning material in
  tracked files. When in doubt, ask before committing.
- Moved pages keep their old URLs working (`redirect_from`); check for
  self-redirect collisions including the `/index.html` form.
- The corpus mirror (`docs/assets/rag-files/`) and other generated files
  are never hand-edited.

## 7. Session Hygiene

- Use the quick commands in `CLAUDE.md`; prefer `uv run` for Python.
- `STRUCTURE_SUMMARY.md` is generated — regenerate, don't hand-edit.
- If a task will span sessions, leave the next step in
  `project_state/project_state.md` under **Next Phase** — that field is the
  hand-off contract between sessions.
