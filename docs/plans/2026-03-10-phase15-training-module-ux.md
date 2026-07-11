# Phase 15: Training Module UX Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Surface level, time, type, outcome, and prerequisites on every individual training module page so users can evaluate a module without opening multiple tabs.

**Architecture:** Create a dedicated `training-module` Jekyll layout that looks up the current page's metadata from `training_catalog.yml` by URL, then renders a metadata bar, outcome sentence, and prerequisites block before the page content. Batch-update all 24 module pages to use the new layout and remove the now-redundant hardcoded page-header div.

**Tech Stack:** Jekyll 4.x, Liquid, existing training chip CSS from Phase 14. No new dependencies.

---

## Before You Start

Read these files first:

- `docs/_data/training_catalog.yml` — module metadata source of truth
- `docs/training/fundamentals/electrical-quantities/index.md` — representative module page (no related_standards in front matter)
- `docs/training/electrical-machines/vfd-fundamentals/index.md` — module page with inline related standards section
- `docs/training/nec-application/nec-code-reading/index.md` — module page with related_standards front matter key
- `docs/assets/css/main.css` — look at the `/* Training curriculum */` section (Phase 14 additions) for existing chip classes
- `docs/_layouts/default.html` — understand what the base layout provides

Build command:

```bash
cd "docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build
```

Expected result: clean build, no Liquid errors.

---

## File Map

| File | Action | Responsibility |
|------|--------|----------------|
| `docs/_layouts/training-module.html` | Create | Renders page-header + metadata bar + outcome + prerequisites + `{{ content }}` |
| `docs/assets/css/main.css` | Modify | Add `.module-meta-bar`, `.module-outcome`, `.module-prereqs` styles |
| `docs/training/fundamentals/*/index.md` (8 files) | Modify | Change layout, remove page-header div, update breadcrumb label |
| `docs/training/electrical-machines/*/index.md` (13 files) | Modify | Same |
| `docs/training/nec-application/*/index.md` (3 files) | Modify | Same |
| `project_state/project_state.md` | Modify | Mark Phase 15 complete |
| `project_state/change_log.md` | Modify | Add Phase 15 entry |

**Do not modify:** Group index pages (`docs/training/*/index.md`), `training_catalog.yml`, or any RAG files.

---

## Task 1: Create the training-module layout

**Files:**
- Create: `docs/_layouts/training-module.html`

**Work:**

- [ ] Create `docs/_layouts/training-module.html` with this exact content:

```html
---
layout: default
---

{% assign module_meta = site.data.training_catalog.modules | where: "url", page.url | first %}

<div class="page-header">
  <span class="page-header__label">Training{% if module_meta %} — {{ module_meta.group_label }}{% endif %}</span>
  <h1>{{ page.title }}</h1>
</div>

{% if module_meta %}
<div class="module-meta-bar">
  {% if module_meta.level == "Beginner" %}<span class="training-chip chip-beginner">{{ module_meta.level }}</span>
  {% elsif module_meta.level == "Intermediate" %}<span class="training-chip chip-intermediate">{{ module_meta.level }}</span>
  {% elsif module_meta.level == "Advanced" %}<span class="training-chip chip-advanced">{{ module_meta.level }}</span>{% endif %}
  <span class="module-meta-item"><strong>Time:</strong> {{ module_meta.time }}</span>
  <span class="module-meta-item"><strong>Type:</strong> {{ module_meta.type }}</span>
  <span class="module-meta-item"><strong>Focus:</strong> {{ module_meta.focus }}</span>
  {% if module_meta.featured %}<span class="training-chip chip-featured">Core</span>{% endif %}
</div>

<div class="module-outcome">
  <strong>After this module:</strong> {{ module_meta.summary }}
</div>

{% if module_meta.prerequisites and module_meta.prerequisites.size > 0 %}
<div class="module-prereqs">
  <strong>Prerequisites:</strong>
  {% for prereq in module_meta.prerequisites %}
    <span class="module-prereq-item">{{ prereq }}</span>{% unless forloop.last %},{% endunless %}
  {% endfor %}
</div>
{% endif %}
{% endif %}

{{ content }}
```

**Notes:**
- The layout wraps `default`, so all existing site chrome (topnav, sidebar, context panel) is inherited.
- The `page.url` lookup will return `/fundamentals/electrical/electrical-quantities/` etc., which matches the `url` fields in `training_catalog.yml` exactly.
- If `module_meta` is nil (no match), the layout degrades gracefully — page-header still renders with just the title.
- `{{ content }}` renders everything from the module page's Markdown body (the page-header div will be removed in Task 3, so there is no double header).

---

## Task 2: Add CSS for module metadata elements

**Files:**
- Modify: `docs/assets/css/main.css`

**Work:**

- [ ] Find the end of the `/* Training curriculum */` section (look for `.rag-error` to orient, then the training block ends before the next comment).
- [ ] Append these rules inside the training CSS section, before the closing `@media (max-width: 640px)` block:

```css
/* Module metadata bar */
.module-meta-bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
  margin: 0.75rem 0 1rem;
  padding: 0.6rem 0.75rem;
  background: var(--color-bg-alt);
  border: 1px solid var(--color-border);
  border-radius: 4px;
  font-size: 0.85rem;
}
.module-meta-item {
  color: var(--color-text-muted);
  white-space: nowrap;
}
.module-meta-item strong {
  color: var(--color-text);
}

/* Module outcome block */
.module-outcome {
  background: var(--color-bg-alt);
  border-left: 3px solid var(--color-accent, #2563eb);
  border-radius: 0 4px 4px 0;
  padding: 0.65rem 1rem;
  margin-bottom: 1.5rem;
  font-size: 0.9rem;
}

/* Module prerequisites */
.module-prereqs {
  font-size: 0.875rem;
  margin-bottom: 1.25rem;
  color: var(--color-text-muted);
}
.module-prereqs strong {
  color: var(--color-text);
}
.module-prereq-item {
  margin-left: 0.25rem;
}
```

**Notes:**
- These use `--color-bg-alt` and `--color-accent` which are now properly defined (fixed in Phase 14 code review).
- No new color variables needed.

---

## Task 3: Batch-update all 24 module pages

**Files:**
- Modify: all 24 `index.md` files in `docs/training/fundamentals/*/`, `docs/training/electrical-machines/*/`, `docs/training/nec-application/*/`

**Work:**

Three changes per file:
1. Change `layout: default` → `layout: training-module` in front matter
2. Remove the `<div class="page-header">...</div>` block (always 3 lines)
3. Update the breadcrumb second-entry name to match the new display labels

Use these scripts from the repo root:

- [ ] **Step 1: Change layout in all 24 module pages**

```bash
cd "."

for dir in \
  docs/training/fundamentals/conductor-ampacity \
  docs/training/fundamentals/diodes-transistors \
  docs/training/fundamentals/electrical-equations-reference \
  docs/training/fundamentals/electrical-quantities \
  docs/training/fundamentals/equivalent-circuit-methods \
  docs/training/fundamentals/kirchhoff-laws \
  docs/training/fundamentals/passive-components \
  docs/training/fundamentals/series-parallel-dividers \
  docs/training/electrical-machines/ac-vs-dc-motors \
  docs/training/electrical-machines/bldc-ev-drone-motors \
  docs/training/electrical-machines/dc-motor-basics \
  docs/training/electrical-machines/induction-motor-basics \
  docs/training/electrical-machines/motor-control-methods \
  docs/training/electrical-machines/motor-efficiency-losses \
  docs/training/electrical-machines/motor-family-comparison \
  docs/training/electrical-machines/motor-nameplates-slip-torque \
  docs/training/electrical-machines/motor-vfd-equations \
  docs/training/electrical-machines/servo-drive-fundamentals \
  docs/training/electrical-machines/servo-feedback-inertia \
  docs/training/electrical-machines/vfd-fundamentals \
  docs/training/electrical-machines/vfd-servo-architecture \
  docs/training/nec-application/motor-panel-code-application \
  docs/training/nec-application/nec-code-reading \
  docs/training/nec-application/working-space-table-navigation
do
  sed -i '' 's/^layout: default$/layout: training-module/' "$dir/index.md"
done
echo "Layout swap done"
```

- [ ] **Step 2: Remove the page-header div block from all 24 pages**

Each page has exactly this block (with variations in the label text only):

```
<div class="page-header">
  <span class="page-header__label">Training — ...</span>
  <h1>...</h1>
</div>
```

Use Python to remove it (more reliable than sed for multi-line):

```bash
python3 - <<'PYEOF'
import re, os

module_dirs = [
  "docs/training/fundamentals/conductor-ampacity",
  "docs/training/fundamentals/diodes-transistors",
  "docs/training/fundamentals/electrical-equations-reference",
  "docs/training/fundamentals/electrical-quantities",
  "docs/training/fundamentals/equivalent-circuit-methods",
  "docs/training/fundamentals/kirchhoff-laws",
  "docs/training/fundamentals/passive-components",
  "docs/training/fundamentals/series-parallel-dividers",
  "docs/training/electrical-machines/ac-vs-dc-motors",
  "docs/training/electrical-machines/bldc-ev-drone-motors",
  "docs/training/electrical-machines/dc-motor-basics",
  "docs/training/electrical-machines/induction-motor-basics",
  "docs/training/electrical-machines/motor-control-methods",
  "docs/training/electrical-machines/motor-efficiency-losses",
  "docs/training/electrical-machines/motor-family-comparison",
  "docs/training/electrical-machines/motor-nameplates-slip-torque",
  "docs/training/electrical-machines/motor-vfd-equations",
  "docs/training/electrical-machines/servo-drive-fundamentals",
  "docs/training/electrical-machines/servo-feedback-inertia",
  "docs/training/electrical-machines/vfd-fundamentals",
  "docs/training/electrical-machines/vfd-servo-architecture",
  "docs/training/nec-application/motor-panel-code-application",
  "docs/training/nec-application/nec-code-reading",
  "docs/training/nec-application/working-space-table-navigation",
]

pattern = re.compile(
    r'<div class="page-header">\s*<span class="page-header__label">[^<]*</span>\s*<h1>[^<]*</h1>\s*</div>\s*\n',
    re.MULTILINE
)

base = "."
for d in module_dirs:
    path = os.path.join(base, d, "index.md")
    with open(path) as f:
        content = f.read()
    new_content = pattern.sub('', content)
    if new_content != content:
        with open(path, 'w') as f:
            f.write(new_content)
        print(f"Cleaned: {d}")
    else:
        print(f"No match (check manually): {d}")
PYEOF
```

Expected: 24 lines printed, each showing "Cleaned: ..."

- [ ] **Step 3: Update breadcrumb labels to new display names**

```bash
python3 - <<'PYEOF'
import os

replacements = {
    'name: "Fundamentals"': 'name: "Electrical Fundamentals"',
    'name: "Electrical Machines"': 'name: "Motors, Drives, and Motion"',
    'name: "NEC Application"': 'name: "NEC for Machines and Panels"',
}

base = "."
dirs = [
    "docs/training/fundamentals/conductor-ampacity",
    "docs/training/fundamentals/diodes-transistors",
    "docs/training/fundamentals/electrical-equations-reference",
    "docs/training/fundamentals/electrical-quantities",
    "docs/training/fundamentals/equivalent-circuit-methods",
    "docs/training/fundamentals/kirchhoff-laws",
    "docs/training/fundamentals/passive-components",
    "docs/training/fundamentals/series-parallel-dividers",
    "docs/training/electrical-machines/ac-vs-dc-motors",
    "docs/training/electrical-machines/bldc-ev-drone-motors",
    "docs/training/electrical-machines/dc-motor-basics",
    "docs/training/electrical-machines/induction-motor-basics",
    "docs/training/electrical-machines/motor-control-methods",
    "docs/training/electrical-machines/motor-efficiency-losses",
    "docs/training/electrical-machines/motor-family-comparison",
    "docs/training/electrical-machines/motor-nameplates-slip-torque",
    "docs/training/electrical-machines/motor-vfd-equations",
    "docs/training/electrical-machines/servo-drive-fundamentals",
    "docs/training/electrical-machines/servo-feedback-inertia",
    "docs/training/electrical-machines/vfd-fundamentals",
    "docs/training/electrical-machines/vfd-servo-architecture",
    "docs/training/nec-application/motor-panel-code-application",
    "docs/training/nec-application/nec-code-reading",
    "docs/training/nec-application/working-space-table-navigation",
]

for d in dirs:
    path = os.path.join(base, d, "index.md")
    with open(path) as f:
        content = f.read()
    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
    if new_content != content:
        with open(path, 'w') as f:
            f.write(new_content)
        print(f"Updated: {d}")
    else:
        print(f"No change: {d}")
PYEOF
```

**Notes:**
- The `sed -i ''` syntax is macOS-specific (required for this environment).
- The Python scripts handle multi-line removal and YAML label replacement more safely than sed.
- After all three steps, spot-check 3 files manually (one from each group).

---

## Task 4: Build and spot-check

**Work:**

- [ ] Run Jekyll build:

```bash
cd "docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build
```

Expected: clean build, no Liquid errors, no "uninitialized constant" warnings.

- [ ] Spot-check `_site/training/fundamentals/electrical-quantities/index.html`:
  - Should contain `module-meta-bar` div
  - Should contain `module-outcome` div
  - Should NOT contain a duplicate `<div class="page-header">`

- [ ] Spot-check `_site/training/electrical-machines/vfd-fundamentals/index.html`:
  - Should show `chip-intermediate` chip
  - Should show "30 min" and "Concept + Practice"
  - Should show prerequisites: "Induction Motor Basics"

- [ ] Spot-check `_site/training/nec-application/motor-panel-code-application/index.html`:
  - Should show `chip-featured` Core badge
  - Should show prerequisites: two items

---

## Task 5: Update project state

**Files:**
- Modify: `project_state/project_state.md`
- Modify: `project_state/change_log.md`

**Work:**

- [ ] In `project_state.md`:
  - Change `Current Phase: Phase 14 COMPLETE` → `Phase 15 COMPLETE`
  - Change `Next Phase: Phase 15 QUEUED` → `Phase 16 QUEUED — NEC Training Expansion`
  - Mark all Phase 15 checkboxes as complete

- [ ] In `change_log.md`, add entry:

```
### 2026-03-10 — Phase 15 complete: Training Module UX

- Created `docs/_layouts/training-module.html` — dedicated layout that looks up
  metadata from training_catalog.yml by page URL and renders level chip, time,
  type, focus, outcome sentence, and prerequisites before page content
- Added CSS for .module-meta-bar, .module-outcome, .module-prereqs to main.css
- Updated all 24 module pages: layout changed to training-module, hardcoded
  page-header div removed (layout now handles it), breadcrumb labels updated
  to new display names
- Jekyll build: clean
```

---

## Explicit Deferrals to Phase 16

- Adding new NEC RAG modules (8–10 new training files)
- Publishing new NEC training pages under `docs/training/nec-application/`
- Rebalancing the landing page once NEC coverage grows
- Filtering/sorting on training landing page (deferred from Phase 15 — not needed given the catalog already surfaces metadata in the table)

## Out of Scope

- Changing any URL slugs or folder names
- Editing RAG source files
- Adding new content to existing module pages
- Changing the default layout used by non-training pages
