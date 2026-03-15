# Design Spec: Reference Section + Commissioning Templates Redesign

**Date:** 2026-03-14
**Phase:** 18 Track C + Field Engineering Redesign
**Status:** Approved for implementation

---

## 1. Scope

Two parallel deliverables:

1. **New `/reference/` section** — surface 4 canonical RAG files as first-class site pages, grouped into two sub-sections.
2. **Commissioning Templates redesign** — rename `/field-engineering/` to `/commissioning-templates/`, add template header block and checkbox UI to all 6 checklist pages.

---

## 2. Reference Section

### 2.1 URL Structure

```
/reference/                                     ← landing page
/reference/architecture/
  machine-architecture-model/                   ← 7-Layer Industrial Machine Architecture Model
  machine-safety-architecture/                  ← Universal Machine Safety Architecture Template
  compliance-stack/                             ← 15-Standard Minimum Compliance Stack
/reference/motor-systems/
  motor-selection-matrix/                       ← Motor Selection Comparison Matrix
```

### 2.2 RAG Source Files

| Page | Source |
|------|--------|
| Machine Architecture Model | `control-standards/rag/standards_intelligence/reference_models/7-Layer Industrial Machine Architecture Model.md` |
| Machine Safety Architecture | `control-standards/rag/standards_intelligence/reference_models/Universal Machine Safety Architecture.md` |
| Compliance Stack | `control-standards/rag/standards_intelligence/reference_models/15-Standard Minimum Compliance Stack.md` |
| Motor Selection Matrix | `control-standards/rag/design_framework/motor_systems/motor_selection_comparison_matrix.md` |

### 2.3 Landing Page

- Layout: `default`
- Two `workflow-card-grid` sections: **Architecture Models** and **Motor Systems**
- Same card pattern as `/workflows/index.md`
- Introductory note: "Quick-reference models and matrices derived from the canonical RAG. Not a substitute for the applicable standard."

### 2.4 Individual Pages

- Layout: `default`
- Content faithfully translated from RAG source (headers, tables, Mermaid diagrams preserved)
- Mermaid flowchart present in motor-selection-matrix — render via existing Mermaid CDN integration
- Each page footer: trust-boundary note referencing RAG source file path
- Breadcrumb: use front matter `breadcrumb:` array matching existing site pattern:
  ```yaml
  breadcrumb:
    - name: "Reference"
      url: "/reference/"
    - name: "Architecture"
      url: "/reference/architecture/"
    - name: "Machine Architecture Model"
  ```

### 2.5 Sidebar

The existing `Reference` `<details>` block (lines 89–97 of `sidebar.html`) contains Software Stack, Glossary, RAG Files, and About — meta-site pages. **Do not modify that block.**

Add a **new** `<details>` block labeled **"Reference Models"** immediately before the existing Reference block:

```html
<details class="sidebar__section">
  <summary>Reference Models</summary>
  <ul class="sidebar__links">
    <li><a href="{{ '/reference/' | relative_url }}">All Reference Models</a></li>
    <li class="sidebar__group-label">Architecture</li>
    <li><a href="{{ '/reference/architecture/machine-architecture-model/' | relative_url }}" class="sub">Machine Architecture</a></li>
    <li><a href="{{ '/reference/architecture/machine-safety-architecture/' | relative_url }}" class="sub">Safety Architecture</a></li>
    <li><a href="{{ '/reference/architecture/compliance-stack/' | relative_url }}" class="sub">Compliance Stack</a></li>
    <li class="sidebar__group-label">Motor Systems</li>
    <li><a href="{{ '/reference/motor-systems/motor-selection-matrix/' | relative_url }}" class="sub">Motor Selection Matrix</a></li>
  </ul>
</details>
```

`sidebar__group-label` items are non-linked labels. Add CSS rule:
```css
.sidebar__group-label { font-size: 0.7rem; text-transform: uppercase; color: var(--color-text-muted); padding: 0.4rem 1rem 0.1rem; letter-spacing: 0.05em; }
```

### 2.6 Cross-links

- Motor Selection Matrix ← add "Related References" section to `/workflows/motor-selection/index.md`
- Machine Architecture Model ← add "Related References" link to `/scenarios/semiconductor-equipment/index.md`
- Compliance Stack ← add "Related References" link to `/industries/semiconductor/index.md`
- Training catalog cross-link for motor-selection-matrix: **deferred** — no matching training module page exists; add as a future catalog entry note only

---

## 3. Commissioning Templates Redesign

### 3.1 URL Change

| Old URL | New URL |
|---------|---------|
| `/field-engineering/` | `/commissioning-templates/` |
| `/field-engineering/pre-power-panel/` | `/commissioning-templates/pre-power-panel/` |
| `/field-engineering/basic-circuit-polarity/` | `/commissioning-templates/basic-circuit-polarity/` |
| `/field-engineering/capacitor-discharge/` | `/commissioning-templates/capacitor-discharge/` |
| `/field-engineering/motor-nameplate-overload/` | `/commissioning-templates/motor-nameplate-overload/` |
| `/field-engineering/motor-rotation-verification/` | `/commissioning-templates/motor-rotation-verification/` |
| `/field-engineering/drive-commissioning/` | `/commissioning-templates/drive-commissioning/` |

Create redirect page at `docs/field-engineering/index.md` (replace existing) using:
```html
<meta http-equiv="refresh" content="0; url={{ '/commissioning-templates/' | relative_url }}">
```

### 3.2 Data Model Update

`docs/_data/field_checklists.yml` — update `url` field for all 6 entries from `/field-engineering/…` to `/commissioning-templates/…`.

### 3.3 Template Header Block

Rendered above checklist body on every checklist page. CSS grid, no JS required.

```html
<div class="template-header">
  <div class="template-header__field"><span class="template-header__label">Project</span><span class="template-header__line"></span></div>
  <div class="template-header__field"><span class="template-header__label">Date</span><span class="template-header__line"></span></div>
  <div class="template-header__field"><span class="template-header__label">Equipment</span><span class="template-header__line"></span></div>
  <div class="template-header__field"><span class="template-header__label">Technician</span><span class="template-header__line"></span></div>
  <div class="template-header__field"><span class="template-header__label">Location</span><span class="template-header__line"></span></div>
  <div class="template-header__field"><span class="template-header__label">Reviewed by</span><span class="template-header__line"></span></div>
</div>
```

### 3.4 Checkbox Items — Rendering Mechanism

Checklist source `.md` files author items as plain Markdown list items (`- Item text`), which Jekyll renders as `<ul><li>` HTML. The `field-checklist.html` layout renders these via `{{ content }}`.

**Mechanism: DOM transformation via inline JavaScript.** After page content loads, a small script finds all `li` elements inside `.checklist-body` and wraps them with `<label class="checklist-item"><input type="checkbox"> …</label>`. No Markdown changes required.

Script (injected at bottom of `field-checklist.html` layout, after `{{ content }}`):

```html
<script>
  document.querySelectorAll('.checklist-body li').forEach(function(li) {
    var cb = document.createElement('input');
    cb.type = 'checkbox';
    cb.className = 'checklist-item__checkbox';
    li.insertBefore(cb, li.firstChild);
    li.classList.add('checklist-item');
  });
</script>
```

Checkbox state is not persisted — print/field use only.

### 3.5 Layout Changes (`docs/_layouts/field-checklist.html`)

Update in this order:

1. Change hardcoded `<span class="page-header__label">Field Engineering</span>` to `<span class="page-header__label">Commissioning Templates</span>`
2. Inject `.template-header` block immediately before `<div class="checklist-body">{{ content }}</div>`
3. Add checkbox DOM transformation script after `{{ content }}`
4. Retain existing cross-links block at bottom
5. Update back-link href from `/field-engineering/` to `/commissioning-templates/`

### 3.6 CSS Additions (`docs/assets/css/main.css`)

```css
/* Template header */
.template-header {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.6rem 1.5rem;
  border: 1px solid var(--color-border);
  border-radius: 4px;
  padding: 1rem 1.25rem;
  margin-bottom: 1.5rem;
}
.template-header__field {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
}
.template-header__label {
  font-size: 0.8rem;
  white-space: nowrap;
  color: var(--color-text-muted);
}
.template-header__line {
  flex: 1;
  border-bottom: 1px solid var(--color-border);
  min-width: 60px;
}

/* Checklist items */
.checklist-body li.checklist-item {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
  list-style: none;
  padding: 0.2rem 0;
}
.checklist-body ul { padding-left: 0; }

/* Print */
@media print {
  .checklist-item__checkbox {
    -webkit-appearance: none;
    appearance: none;
    width: 11px;
    height: 11px;
    border: 1px solid #000;
    flex-shrink: 0;
    margin-top: 2px;
  }
}
```

### 3.7 Sidebar Rename (`docs/_includes/sidebar.html`)

- Change `<summary>Field Engineering</summary>` → `<summary>Commissioning Templates</summary>`
- Update all 7 `href` values from `/field-engineering/…` to `/commissioning-templates/…`
- Update all `page.url contains` active-class checks from `'field-engineering'` to `'commissioning-templates'`

### 3.8 Inbound Link Updates

**`docs/_data/training_catalog.yml`** — 13 URL strings across 11 modules reference `/field-engineering/` in their `related_checklists` field. Update all 13 to `/commissioning-templates/`.

**Workflow pages** — 5 pages under `docs/workflows/` contain hardcoded "Related Checklists" links to `/field-engineering/` URLs. Update each href to `/commissioning-templates/`.

**`docs/_layouts/field-checklist.html`** — back-link href (addressed in Section 3.5).

---

## 4. Build Target

Clean Jekyll build. Expected page count: **~129 pages**

- Baseline: 123 pages
- New reference pages: +5 (1 landing + 4 content pages)
- Field-engineering redirect page: +1
- Commissioning-templates pages: net 0 (7 existing pages moved, not added)
- **Total: 129**

---

## 5. What This Does Not Include

- No new RAG content created
- No new layouts created (reference pages use `default`; checklist layout updated in place)
- No persistent checkbox state (localStorage) — print/field use only
- No PDF export
- No equations page (Phase 19 scope)
- No `motor-selection-comparison-matrix` training catalog entry (deferred)
