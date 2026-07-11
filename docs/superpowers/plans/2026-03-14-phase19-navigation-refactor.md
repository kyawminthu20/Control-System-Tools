# Phase 19 — Engineering Workflow Navigation Refactor

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Collapse the 10-section hardcoded sidebar into a 5-group data-driven navigation system with an Engineering Workflow hub page, without changing any existing content URLs.

**Architecture:** Create `docs/_data/navigation.yml` as the single source of truth for sidebar hierarchy. Refactor `docs/_includes/sidebar.html` to render from that data using Liquid loops. Add `/design/` as a workflow-first hub page. Expand `/tools/reference-hub/` landing to also surface lookup content (glossary, crosswalks, software stack, RAG browser).

**Tech Stack:** Jekyll 4.2, Liquid templating, YAML data files, vanilla HTML. No JavaScript changes. No URL moves.

**Baseline:** 131 pages, clean build. Jekyll: `cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build`.

---

## File Map

| Action | File | Purpose |
|---|---|---|
| Create | `docs/_data/navigation.yml` | Full 5-group sidebar hierarchy — sections, children, grandchildren, match rules |
| Create | `docs/engineering-workflow/index.md` | Workflow-first hub: lifecycle, workflows, commissioning templates, scenarios |
| Modify | `docs/tools/reference-hub/index.md` | Add Quick Reference section: glossary, crosswalks, software stack, RAG browser |
| Modify | `docs/_includes/sidebar.html` | Replace ~135 lines of hardcoded HTML with data-driven Liquid renderer (~45 lines) |

---

## Chunk 1: Data Model and Hub Pages

### Task 1: Create navigation.yml

**Files:**
- Create: `docs/_data/navigation.yml`

**Notes on the data model:**
- `match_prefixes`: array of URL prefixes that cause the section `<details>` to auto-open
- `always_open`: boolean — Standards section stays expanded on every page
- `children`: first-level nav items inside a section (rendered as `class="sub"`)
- `children[].children`: grandchildren, rendered indented (`style="padding-left:2.75rem"`) — used for Standards only
- `group_label`: boolean — renders as non-linked `<li class="sidebar__group-label">` (for future use)
- HTML entities (`&amp;`, `O&amp;G`) must be written as HTML in YAML so Liquid outputs them correctly

- [ ] **Step 1: Create `docs/_data/navigation.yml`**

```yaml
- label: "Engineering Workflow"
  url: "/design/"
  match_prefixes:
    - "/design/"
    - "/verification/lifecycle/"
    - "/design/workflows/"
    - "/implementation/commissioning-templates/"
    - "/implementation/scenarios/"
  children:
    - label: "Lifecycle"
      url: "/verification/lifecycle/"
    - label: "Workflows"
      url: "/design/workflows/"
    - label: "Commissioning Templates"
      url: "/implementation/commissioning-templates/"
    - label: "Scenarios"
      url: "/implementation/scenarios/"

- label: "Standards"
  url: "/standards/"
  always_open: true
  match_prefixes:
    - "/standards/"
  children:
    - label: "US Electrical"
      url: "/standards/us-electrical/"
      children:
        - label: "NEC (NFPA 70)"
          url: "/standards/us-electrical/nec/"
        - label: "NFPA 79"
          url: "/standards/us-electrical/nfpa-79/"
        - label: "UL 508A"
          url: "/standards/us-electrical/ul-508a/"
    - label: "International Machinery"
      url: "/standards/machinery/"
      children:
        - label: "IEC 60204-1"
          url: "/standards/machinery/iec-60204-1/"
    - label: "Functional Safety"
      url: "/standards/functional-safety/"
      children:
        - label: "ISO 12100"
          url: "/standards/functional-safety/iso-12100/"
        - label: "ISO 13849-1"
          url: "/standards/functional-safety/iso-13849-1/"
        - label: "IEC 62061"
          url: "/standards/functional-safety/iec-62061/"
        - label: "IEC 61508"
          url: "/standards/functional-safety/iec-61508/"
        - label: "IEC 61511"
          url: "/standards/functional-safety/iec-61511/"
    - label: "Cybersecurity"
      url: "/standards/cybersecurity/"
      children:
        - label: "IEC 62443"
          url: "/standards/cybersecurity/iec-62443/"
    - label: "Hazardous Area"
      url: "/standards/hazardous-area/"
      children:
        - label: "IEC 60079"
          url: "/standards/hazardous-area/iec-60079/"
    - label: "Semiconductor"
      url: "/standards/semiconductor/"
      children:
        - label: "SEMI S2/S8/S14"
          url: "/standards/semiconductor/semi/"
    - label: "Relationship Graph"
      url: "/standards/graph/"

- label: "Training"
  url: "/training/"
  match_prefixes:
    - "/training/"
  children:
    - label: "Electrical Fundamentals"
      url: "/fundamentals/electrical/"
    - label: "Motors, Drives, and Motion"
      url: "/fundamentals/motors/"
    - label: "NEC for Machines and Panels"
      url: "/training/nec-application/"
    - label: "Control Systems"
      url: "/fundamentals/control/"

- label: "Industries"
  url: "/industries/"
  match_prefixes:
    - "/industries/"
  children:
    - label: "Semiconductor"
      url: "/industries/semiconductor/"
    - label: "Food &amp; Beverage"
      url: "/industries/food-and-beverage/"
    - label: "Energy"
      url: "/industries/energy/"
    - label: "Petroleum / Oil &amp; Gas"
      url: "/industries/petroleum/"
    - label: "Marine"
      url: "/industries/marine/"
    - label: "Medical"
      url: "/industries/medical/"
    - label: "Nuclear"
      url: "/industries/nuclear/"
    - label: "Offshore"
      url: "/industries/offshore/"
    - label: "Commercial"
      url: "/industries/commercial/"

- label: "Reference"
  url: "/tools/reference-hub/"
  match_prefixes:
    - "/tools/reference-hub/"
    - "/tools/glossary/"
    - "/design/software-stack/"
    - "/tools/rag-browser/"
    - "/tools/crosswalks/"
    - "/repository/about/"
  children:
    - label: "Reference Models"
      url: "/tools/reference-hub/"
    - label: "Glossary"
      url: "/tools/glossary/"
    - label: "Crosswalks"
      url: "/tools/crosswalks/"
    - label: "Software Stack"
      url: "/design/software-stack/"
    - label: "RAG Files"
      url: "/tools/rag-browser/"
    - label: "About / Trust Boundary"
      url: "/repository/about/"
```

- [ ] **Step 2: Verify the YAML file parses without errors**

```bash
cd "." && ruby -e "require 'yaml'; YAML.load_file('docs/_data/navigation.yml'); puts 'OK'"
```

Expected output: `OK`

- [ ] **Step 3: Run Jekyll build — verify still 131 pages (data file only, no new pages)**

```bash
cd "docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -3 && find _site -name "index.html" | wc -l
```

Expected: clean build, `131`

- [ ] **Step 4: Commit**

```bash
cd "." && git add docs/_data/navigation.yml && git commit -m "feat(nav): add navigation.yml — 5-group sidebar data model"
```

---

### Task 2: Create engineering-workflow hub page

**Files:**
- Create: `docs/engineering-workflow/index.md`

- [ ] **Step 1: Create `docs/engineering-workflow/index.md`**

```markdown
---
layout: default
title: "Engineering Workflow"
description: "Workflow-first navigation for machine and panel design: lifecycle stages, engineering workflows, commissioning templates, and scenarios."
breadcrumb:
  - name: "Engineering Workflow"
---

<div class="page-header">
  <span class="page-header__label">Engineering Workflow</span>
  <h1>Engineering Workflow</h1>
  <p>Navigate from concept through commissioning by engineering task. Lifecycle stages provide structured progression; workflows guide decision points; commissioning templates support field verification.</p>
</div>

## Design &amp; Architecture

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/verification/lifecycle/' | relative_url }}">Machine Lifecycle</a></h3>
    <p>11-stage structured progression from concept through maintenance, with standards and decision gates at each step.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/verification/safety-architecture/' | relative_url }}">Safety Architecture</a></h3>
    <p>Functional layer separation, E-stop chain design, SIL/PL selection, and safety architecture constraints.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/verification/lifecycle/detailed-design/' | relative_url }}">Detailed Design</a></h3>
    <p>Electrical design stage: schematics, IO lists, panel layout, conductor sizing, and protection coordination.</p>
  </div>
</div>

## Select &amp; Size

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/design/workflows/motor-selection/' | relative_url }}">Motor Selection</a></h3>
    <p>Decision framework for motor-system family selection across induction, servo, BLDC, and stepper platforms.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/design/workflows/electrical-review/' | relative_url }}">Electrical Review</a></h3>
    <p>Systematic electrical design review: conductor sizing, protection coordination, grounding, and panel checklist.</p>
  </div>
</div>

## Commission &amp; Verify

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/implementation/commissioning-templates/' | relative_url }}">Commissioning Templates</a></h3>
    <p>Printable field checklists for panel energization, motor commissioning, drive startup, and circuit verification.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/implementation/vfd-commissioning/' | relative_url }}">VFD Commissioning</a></h3>
    <p>Step-by-step VFD startup: parameter entry, motor data, rotation check, and protection verification.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/implementation/servo-commissioning/' | relative_url }}">Servo Commissioning</a></h3>
    <p>Servo drive startup: feedback configuration, homing, tuning, and safety function verification.</p>
  </div>
</div>

## Troubleshoot

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/troubleshooting/motors/' | relative_url }}">Motor Troubleshooting</a></h3>
    <p>Decision tree for motor faults: thermal, mechanical, electrical, and drive-related fault branches.</p>
  </div>
</div>

## Scenarios

Industry and application scenarios showing how standards, lifecycle stages, and workflows combine for specific machine types.

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/implementation/scenarios/' | relative_url }}">All Scenarios</a></h3>
    <p>9 machine and industry scenarios — from US control panels and global machinery to semiconductor fab tools and offshore platforms.</p>
  </div>
</div>
```

- [ ] **Step 2: Run Jekyll build — verify 132 pages**

```bash
cd "docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -3 && find _site -name "index.html" | wc -l
```

Expected: clean build, `132`

- [ ] **Step 3: Commit**

```bash
cd "." && git add docs/engineering-workflow/index.md && git commit -m "feat(site): add /design/ workflow-first hub page"
```

---

### Task 3: Expand reference landing page

**Files:**
- Modify: `docs/tools/reference-hub/index.md`

The existing landing has two card-grid sections (Architecture Models, Motor Systems). Add a third section for quick-lookup content.

- [ ] **Step 1: Read `docs/tools/reference-hub/index.md`** to locate the closing trust-boundary note at the bottom.

- [ ] **Step 2: Insert Quick Reference section** immediately before the closing trust-boundary `<div>`:

```html
<h2>Quick Reference</h2>
<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/tools/glossary/' | relative_url }}">Glossary</a></h3>
    <p>45 cross-linked terms across Safety, Electrical, Standards Bodies, and Regulatory domains.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/tools/crosswalks/' | relative_url }}">Crosswalks</a></h3>
    <p>Side-by-side standard comparisons: NFPA 79 ↔ IEC 60204-1, IEC 61511 ↔ IEC 61508, IEC 60079 ↔ NEC 500/505, and more.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/design/software-stack/' | relative_url }}">Software Stack</a></h3>
    <p>Site technology stack, Jekyll configuration, and deployment notes.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/tools/rag-browser/' | relative_url }}">RAG File Browser</a></h3>
    <p>Browse all canonical RAG source files directly — standards, training modules, design frameworks, and commissioning checklists.</p>
  </div>
</div>
```

- [ ] **Step 3: Run Jekyll build — verify 132 pages, clean build**

```bash
cd "docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -3 && find _site -name "index.html" | wc -l
```

Expected: clean build, `132`

- [ ] **Step 4: Commit**

```bash
cd "." && git add docs/tools/reference-hub/index.md && git commit -m "feat(reference): add Quick Reference section to landing page"
```

---

## Chunk 2: Sidebar Refactor

### Task 4: Refactor sidebar.html to data-driven renderer

**Files:**
- Modify: `docs/_includes/sidebar.html`

This replaces ~135 lines of hardcoded HTML with ~45 lines of Liquid. The renderer logic:

1. For each `section` in `site.data.navigation`: check if `page.url` contains any of `section.match_prefixes` → set `in_section = true`
2. Render `<details open>` if `section.always_open` OR `in_section`
3. First `<li>` inside each section is the section landing link
4. Loop `section.children`: render as `class="sub"` links
5. If a child has `children`: loop grandchildren as `class="sub" style="padding-left:2.75rem"` links
6. Active class: add `active` to the most specific matching link (grandchild preferred over child)

**Active-state logic:**
- For grandchildren (leaf nodes): active if `page.url contains grandchild.url`
- For children with no grandchildren: active if `page.url == child.url`
- For children with grandchildren: active if `page.url contains child.url` AND none of the grandchildren match (parent highlight when on the family landing page)
- For section top link: active if `page.url == section.url`

- [ ] **Step 1: Replace the full contents of `docs/_includes/sidebar.html`** with:

```html
<nav class="sidebar" id="sidebar">
  {% for section in site.data.navigation %}
    {% assign in_section = false %}
    {% if section.match_prefixes %}
      {% for prefix in section.match_prefixes %}
        {% if page.url contains prefix %}{% assign in_section = true %}{% endif %}
      {% endfor %}
    {% else %}
      {% if page.url contains section.url %}{% assign in_section = true %}{% endif %}
    {% endif %}

    <details class="sidebar__section"{% if section.always_open or in_section %} open{% endif %}>
      <summary>{{ section.label }}</summary>
      <ul class="sidebar__links">
        <li>
          <a href="{{ section.url | relative_url }}"{% if page.url == section.url %} class="active"{% endif %}>{{ section.label }}</a>
        </li>

        {% for child in section.children %}
          {% if child.group_label %}
            <li class="sidebar__group-label">{{ child.label }}</li>
          {% else %}
            {% assign child_has_active_gc = false %}
            {% if child.children %}
              {% for grandchild in child.children %}
                {% if page.url contains grandchild.url %}{% assign child_has_active_gc = true %}{% endif %}
              {% endfor %}
            {% endif %}

            {% assign child_active = false %}
            {% if child.children %}
              {% if page.url contains child.url and child_has_active_gc == false %}{% assign child_active = true %}{% endif %}
            {% else %}
              {% if page.url == child.url %}{% assign child_active = true %}{% endif %}
            {% endif %}

            <li>
              <a href="{{ child.url | relative_url }}" class="sub{% if child_active %} active{% endif %}">{{ child.label }}</a>
            </li>

            {% if child.children %}
              {% for grandchild in child.children %}
                {% assign gc_active = false %}
                {% if page.url contains grandchild.url %}{% assign gc_active = true %}{% endif %}
                <li>
                  <a href="{{ grandchild.url | relative_url }}" class="sub{% if gc_active %} active{% endif %}" style="padding-left:2.75rem">{{ grandchild.label }}</a>
                </li>
              {% endfor %}
            {% endif %}

          {% endif %}
        {% endfor %}

      </ul>
    </details>
  {% endfor %}
</nav>
```

- [ ] **Step 2: Run Jekyll build — verify clean build, 132 pages**

```bash
cd "docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -3 && find _site -name "index.html" | wc -l
```

Expected: clean build, `132`

- [ ] **Step 3: Verify sidebar section count in built output**

```bash
grep -c "<details class=\"sidebar__section\"" "docs/_site/index.html"
```

Expected: `5`

- [ ] **Step 4: Verify Standards grandchildren are rendered**

```bash
grep "padding-left:2.75rem" "docs/_site/standards/index.html" | wc -l
```

Expected: at least `12` (NEC, NFPA 79, UL 508A, IEC 60204-1, ISO 12100, ISO 13849-1, IEC 62061, IEC 61508, IEC 61511, IEC 62443, IEC 60079, SEMI = 12 grandchild links)

- [ ] **Step 5: Verify Engineering Workflow section auto-opens on a lifecycle page**

```bash
grep -B 1 "<summary>Engineering Workflow" "docs/_site/lifecycle/index.html" | head -5
```

Expected: the line before `<summary>Engineering Workflow` contains `<details class="sidebar__section" open>`.

- [ ] **Step 6: Verify Standards section is always open on a non-standards page (e.g., training)**

```bash
grep -B 1 "<summary>Standards" "docs/_site/training/index.html" | head -5
```

Expected: the line before `<summary>Standards` contains `<details class="sidebar__section" open>`.

- [ ] **Step 7: Commit**

```bash
cd "." && git add docs/_includes/sidebar.html && git commit -m "feat(nav): data-driven sidebar from navigation.yml — 5-group structure"
```

---

## Chunk 3: Project State Update

### Task 5: Update project state

**Files:**
- Modify: `project_state/project_state.md`
- Modify: `project_state/change_log.md`

- [ ] **Step 1: Update `project_state/project_state.md`**
  - Header: phase → "Phase 19 COMPLETE", next → "Phase 20 TBD"
  - Current Reality: update build page count to 132; update sidebar description to "data-driven from `navigation.yml`, 5 top-level groups"
  - Add Phase 19 completed scope section

- [ ] **Step 2: Update `project_state/change_log.md`**

Add entry:

```
### 2026-03-14 — Phase 19: Engineering Workflow Navigation Refactor

- Created `docs/_data/navigation.yml` — 5-group sidebar data model (Engineering Workflow, Standards, Training, Industries, Reference)
- Refactored `docs/_includes/sidebar.html` from 135-line hardcoded HTML to 45-line data-driven Liquid renderer
- Added `/design/` hub page: 5 task-grouped sections (Design, Select, Commission, Troubleshoot, Scenarios)
- Expanded `/tools/reference-hub/` landing page with Quick Reference section (glossary, crosswalks, software stack, RAG browser)
- Demoted Scenarios, Crosswalks, Workflows from top-level sidebar into Engineering Workflow and Reference groups
- Jekyll build: clean, 132 pages
```

- [ ] **Step 3: Commit**

```bash
cd "." && git add project_state/ && git commit -m "chore: update project state — Phase 19 complete"
```
