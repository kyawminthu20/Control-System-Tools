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
- Breadcrumb: `Reference > [sub-group] > [page title]`

### 2.5 Sidebar

Extend existing Reference `<details>` block:

```
Reference
  Software Stack              (existing)
  — Architecture —
  Machine Architecture        (new, sub)
  Safety Architecture         (new, sub)
  Compliance Stack            (new, sub)
  — Motor Systems —
  Motor Selection Matrix      (new, sub)
```

Section dividers rendered as non-linked `<li class="sidebar__group-label">` items.

### 2.6 Cross-links

- Motor Selection Matrix ← linked from `/workflows/motor-selection/` (Related References section)
- Motor Selection Matrix ← linked from training modules: `motor-selection-comparison-matrix` catalog entry
- Machine Architecture Model ← linked from `/scenarios/semiconductor-equipment/` (Related References)
- Compliance Stack ← linked from `/industries/semiconductor/` (Related References)

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

Old `/field-engineering/` URL — redirect page using `<meta http-equiv="refresh" content="0; url=...">`.

### 3.2 Data Model Update

`docs/_data/field_checklists.yml` — update `url` field for all 6 entries from `/field-engineering/…` to `/commissioning-templates/…`.

### 3.3 Template Header Block

Rendered above checklist body on every checklist page. CSS grid, no JS.

```
┌──────────────────────────────────────────────────────┐
│  Project: ___________________  Date: ______________   │
│  Equipment: _________________  Technician: _________  │
│  Location: __________________  Reviewed by: ________  │
└──────────────────────────────────────────────────────┘
```

HTML structure:

```html
<div class="template-header">
  <div class="template-header__field"><span>Project</span><span class="template-header__line"></span></div>
  <div class="template-header__field"><span>Date</span><span class="template-header__line"></span></div>
  <!-- ... -->
</div>
```

### 3.4 Checkbox Items

Each checklist item rendered as:

```html
<label class="checklist-item">
  <input type="checkbox"> Item text
</label>
```

- Checkbox state functional in browser (not persisted — print use case)
- `@media print`: checkboxes rendered as `□` via `appearance: none; border: 1px solid #000; width: 12px; height: 12px`

### 3.5 Layout Changes

Update `docs/_layouts/field-checklist.html`:
1. Inject `.template-header` block before checklist content
2. Wrap checklist items in `.checklist-item` labels with checkboxes
3. Retain existing cross-links block at bottom

### 3.6 CSS Additions

New rules in `docs/assets/css/main.css`:
- `.template-header` — 2-column CSS grid, border, padding, print-friendly
- `.template-header__field` — flex row with label + underline fill
- `.template-header__line` — `flex: 1; border-bottom: 1px solid`
- `.checklist-item` — block display, padding, checkbox alignment
- `@media print` — checkbox square rendering, hide interactive chrome

### 3.7 Sidebar Rename

Change label from "Field Engineering" to "Commissioning Templates" in `docs/_includes/sidebar.html`. Update all `href` values from `/field-engineering/…` to `/commissioning-templates/…`.

### 3.8 Inbound Link Updates

All pages that link to `/field-engineering/` must be updated:
- Training module pages with `related_checklists` cross-links (11 modules)
- Workflow pages with "Related Checklists" sections (5 pages)
- `field-checklist.html` layout back-link

---

## 4. Build Target

Clean Jekyll build. Expected page count: ~132 pages (123 existing + 5 new reference pages + 6 moved commissioning pages replacing field-engineering + 1 redirect = net +6).

---

## 5. What This Does Not Include

- No new RAG content created
- No new layouts created (reference pages use `default`; checklist layout updated in place)
- No persistent checkbox state (localStorage) — print/field use only
- No PDF export
- No equations page (Phase 19 scope)
