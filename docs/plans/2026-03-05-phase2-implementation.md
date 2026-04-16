# Phase 2 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add print stylesheet, diagram lightbox, client-side search (lunr.js inline dropdown), and a crosswalk comparison selector to the Jekyll site.

**Architecture:** All features are additive to existing files (`main.css`, `main.js`, `default.html`, `topnav.html`). One new data file (`search.json`) and one new page (`/tools/crosswalks/compare/`). Vanilla JS only, no build step, CDN-only dependencies.

**Tech Stack:** Jekyll 4.3, vanilla CSS, vanilla JS, lunr.js (CDN), GitHub Pages (custom Actions build)

---

## Release 1

---

### Task 1: Print stylesheet

**Files:**
- Modify: `docs/assets/css/main.css` (append at end of file)

**Step 1: Append `@media print` block to `main.css`**

Add the following at the very end of `docs/assets/css/main.css`:

```css
/* ==========================================================================
   Print stylesheet
   ========================================================================== */
@media print {
  .topnav,
  .sidebar,
  .context-panel,
  .skip-link,
  #sidebar-toggle,
  .trust-boundary {
    display: none !important;
  }

  .site-body {
    display: block;
  }

  .main-content {
    margin: 0;
    padding: 0;
    max-width: 100%;
    width: 100%;
  }

  a[href]:after {
    content: " (" attr(href) ")";
    font-size: 0.85em;
    color: #555;
  }

  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }

  h2, h3 {
    page-break-after: avoid;
  }

  table {
    page-break-inside: avoid;
  }

  pre {
    page-break-inside: avoid;
    white-space: pre-wrap;
  }
}
```

**Step 2: Verify Jekyll builds cleanly**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
```

Expected: `done in X seconds` with no errors.

**Step 3: Manually verify print preview**

```bash
~/.gem/ruby/2.6.0/bin/bundle exec jekyll serve --detach
```

Open `http://127.0.0.1:4000/Control-System-Tools/` in a browser.
Open browser print preview (`Cmd+P` on macOS).
Expected: no sidebar, no topnav, full-width main content.
Kill the server: `kill $(lsof -ti :4000)`

**Step 4: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add docs/assets/css/main.css
git commit -m "feat: add print stylesheet (hide nav/sidebar, full-width content, URL after links)"
```

---

### Task 2: Diagram lightbox

**Files:**
- Modify: `docs/assets/css/main.css` (append lightbox styles)
- Modify: `docs/assets/js/main.js` (append lightbox IIFE)

**Step 1: Append lightbox styles to `main.css`**

Add after the print block at the end of `docs/assets/css/main.css`:

```css
/* ==========================================================================
   Diagram lightbox
   ========================================================================== */
.mermaid {
  cursor: zoom-in;
}

.lightbox-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.78);
  z-index: 500;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.lightbox-overlay.is-active {
  display: flex;
}

.lightbox-inner {
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  padding: 1.5rem;
  max-width: 90vw;
  max-height: 90vh;
  overflow: auto;
  position: relative;
}

.lightbox-inner svg {
  max-width: 100%;
  height: auto;
  display: block;
}

.lightbox-close {
  position: absolute;
  top: 0.5rem;
  right: 0.75rem;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: var(--color-text-muted);
  line-height: 1;
  padding: 0.25rem;
}

.lightbox-close:hover {
  color: var(--color-text);
}

@media print {
  .lightbox-overlay { display: none !important; }
}
```

**Step 2: Append lightbox JS to `main.js`**

Add at the end of `docs/assets/js/main.js`:

```javascript
// Diagram lightbox
(function () {
  function initLightbox() {
    // Build overlay DOM with safe element creation (no dynamic innerHTML)
    var overlay = document.createElement('div');
    overlay.className = 'lightbox-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', 'Diagram enlarged view');

    var inner = document.createElement('div');
    inner.className = 'lightbox-inner';

    var closeBtn = document.createElement('button');
    closeBtn.className = 'lightbox-close';
    closeBtn.setAttribute('aria-label', 'Close diagram');
    closeBtn.textContent = '\u00D7';

    inner.appendChild(closeBtn);
    overlay.appendChild(inner);
    document.body.appendChild(overlay);

    function close() {
      overlay.classList.remove('is-active');
      var svgs = inner.querySelectorAll('svg');
      svgs.forEach(function (svg) { inner.removeChild(svg); });
    }

    closeBtn.addEventListener('click', close);

    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) close();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && overlay.classList.contains('is-active')) close();
    });

    document.querySelectorAll('.mermaid').forEach(function (el) {
      var svg = el.querySelector('svg');
      if (!svg) return;
      el.setAttribute('title', 'Click to enlarge');
      el.addEventListener('click', function () {
        inner.appendChild(svg.cloneNode(true));
        overlay.classList.add('is-active');
      });
    });
  }

  // Mermaid renders after DOMContentLoaded; use window load + small delay
  if (document.readyState === 'complete') {
    setTimeout(initLightbox, 150);
  } else {
    window.addEventListener('load', function () {
      setTimeout(initLightbox, 150);
    });
  }
})();
```

**Step 3: Verify build and lightbox works**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
~/.gem/ruby/2.6.0/bin/bundle exec jekyll serve --detach
```

Open `http://127.0.0.1:4000/Control-System-Tools/` and click a Mermaid diagram.
Expected: full-screen overlay with enlarged diagram; `×` button and Escape close it.
Kill server: `kill $(lsof -ti :4000)`

**Step 4: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add docs/assets/css/main.css docs/assets/js/main.js
git commit -m "feat: add diagram lightbox — click any Mermaid diagram to enlarge"
```

---

## Release 2

---

### Task 3: lunr.js CDN + search.json data file

**Files:**
- Modify: `docs/_layouts/default.html` (add lunr.js script tag)
- Create: `docs/assets/data/search.json`

**Step 1: Add lunr.js CDN to `default.html`**

In `docs/_layouts/default.html`, add this line directly **before** the closing `</body>` tag (after the `main.js` script tag):

```html
  <script src="https://cdn.jsdelivr.net/npm/lunr@2.3.9/lunr.min.js"></script>
```

The bottom of `default.html` should now look like:

```html
  <script src="{{ '/assets/js/main.js' | relative_url }}"></script>
  <script src="https://cdn.jsdelivr.net/npm/lunr@2.3.9/lunr.min.js"></script>
</body>
</html>
```

**Step 2: Create `docs/assets/data/search.json`**

Create `docs/assets/data/search.json` with this exact content (it is a Liquid template rendered by Jekyll):

```
---
layout: none
---
[
  {% assign first = true %}
  {% for page in site.pages %}
  {% if page.title %}
  {% unless page.url contains '/vendor/' or page.url contains '/assets/' or page.url contains '/plans/' %}
  {% unless first %},{% endunless %}
  {% assign first = false %}
  {"title":{{ page.title | jsonify }},"url":{{ page.url | relative_url | jsonify }},"content":{{ page.content | strip_html | normalize_whitespace | truncate: 220 | jsonify }},"section":{{ page.url | split: '/' | slice: 1 | first | jsonify }}}
  {% endunless %}
  {% endif %}
  {% endfor %}
]
```

**Step 3: Verify search.json produces valid JSON**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
python3 -m json.tool _site/assets/data/search.json > /dev/null && echo "Valid JSON" || echo "INVALID — check for trailing comma"
```

Expected: `Valid JSON`

If invalid: replace `normalize_whitespace` with `strip_newlines | replace: '  ', ' '` in `search.json`.

**Step 4: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add docs/_layouts/default.html docs/assets/data/search.json
git commit -m "feat: add lunr.js CDN and Jekyll search index (search.json)"
```

---

### Task 4: Topnav search input + inline dropdown

**Files:**
- Modify: `docs/_includes/topnav.html` (add search input)
- Modify: `docs/assets/css/main.css` (append search styles)
- Modify: `docs/assets/js/main.js` (append search logic)

**Step 1: Add search input to `topnav.html`**

Replace the full content of `docs/_includes/topnav.html` with:

```html
<nav class="topnav">
  <a href="{{ '/' | relative_url }}" class="topnav__brand">CS Standards Atlas</a>
  <ul class="topnav__links">
    <li><a href="{{ '/standards/' | relative_url }}"{% if page.url contains '/standards/' %} class="active"{% endif %}>Standards</a></li>
    <li><a href="{{ '/lifecycle/' | relative_url }}"{% if page.url contains '/lifecycle/' %} class="active"{% endif %}>Lifecycle</a></li>
    <li><a href="{{ '/industries/' | relative_url }}"{% if page.url contains '/industries/' %} class="active"{% endif %}>Industries</a></li>
    <li><a href="{{ '/scenarios/' | relative_url }}"{% if page.url contains '/scenarios/' %} class="active"{% endif %}>Scenarios</a></li>
    <li><a href="{{ '/tools/crosswalks/' | relative_url }}"{% if page.url contains '/tools/crosswalks/' %} class="active"{% endif %}>Crosswalks</a></li>
    <li><a href="{{ '/software-stack/' | relative_url }}"{% if page.url contains '/software-stack/' %} class="active"{% endif %}>Software Stack</a></li>
    <li><a href="{{ '/about/' | relative_url }}"{% if page.url contains '/about/' %} class="active"{% endif %}>About</a></li>
  </ul>
  <div class="topnav__search">
    <input
      type="search"
      id="search-input"
      class="topnav__search-input"
      placeholder="Search standards&#8230;"
      autocomplete="off"
      aria-label="Search standards"
      aria-autocomplete="list"
      aria-controls="search-dropdown"
      data-search-url="{{ '/assets/data/search.json' | relative_url }}"
    >
    <div class="search-dropdown" id="search-dropdown" role="listbox" aria-label="Search results"></div>
  </div>
  <button class="topnav__hamburger" id="sidebar-toggle" aria-label="Toggle sidebar">&#9776;</button>
</nav>
```

**Step 2: Append search styles to `main.css`**

Add at the end of `docs/assets/css/main.css`:

```css
/* ==========================================================================
   Search
   ========================================================================== */
.topnav__search {
  position: relative;
  margin-left: auto;
  margin-right: 0.75rem;
}

.topnav__search-input {
  background: #2a2a2a;
  border: 1px solid #444;
  color: #e8e8e8;
  font-family: var(--font-sans);
  font-size: 0.8rem;
  padding: 0.3rem 0.6rem;
  width: 180px;
  outline: none;
}

.topnav__search-input::placeholder {
  color: #888;
}

.topnav__search-input:focus {
  border-color: var(--color-accent);
  width: 220px;
  transition: width 0.15s;
}

.search-dropdown {
  display: none;
  position: absolute;
  top: calc(100% + 4px);
  right: 0;
  min-width: 280px;
  background: #fff;
  border: 1px solid var(--color-border);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  z-index: 200;
  max-height: 320px;
  overflow-y: auto;
}

.search-dropdown.is-open {
  display: block;
}

.search-result {
  display: block;
  padding: 0.5rem 0.75rem;
  color: var(--color-text);
  border-bottom: 1px solid var(--color-border);
  text-decoration: none;
}

.search-result:last-child {
  border-bottom: none;
}

.search-result:hover,
.search-result.is-selected {
  background: var(--color-bg-panel);
}

.search-result__section {
  display: block;
  font-size: 0.7rem;
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.1rem;
}

.search-result__title {
  font-size: 0.875rem;
  font-weight: 500;
}

.search-dropdown__empty {
  padding: 0.6rem 0.75rem;
  color: var(--color-text-muted);
  font-size: 0.875rem;
}

@media (max-width: 768px) {
  .topnav__search { display: none; }
}

@media print {
  .topnav__search { display: none !important; }
}
```

**Step 3: Append search JS to `main.js`**

Add at the end of `docs/assets/js/main.js`.

Note: all result DOM nodes are built with `createElement` and `textContent` to avoid XSS — do not replace with innerHTML string building.

```javascript
// Client-side search (lunr.js)
(function () {
  var searchInput = document.getElementById('search-input');
  var searchDropdown = document.getElementById('search-dropdown');
  if (!searchInput || !searchDropdown) return;

  var lunrIndex = null;
  var docs = [];
  var selectedIndex = -1;

  var searchUrl = searchInput.getAttribute('data-search-url');

  fetch(searchUrl)
    .then(function (r) { return r.json(); })
    .then(function (data) {
      docs = data;
      lunrIndex = lunr(function () {
        this.field('title', { boost: 10 });
        this.field('section', { boost: 5 });
        this.field('content');
        this.ref('url');
        data.forEach(function (doc) { this.add(doc); }, this);
      });
    })
    .catch(function () { /* search unavailable — silent fail */ });

  function sectionLabel(s) {
    if (!s) return '';
    return s.charAt(0).toUpperCase() + s.slice(1).replace(/-/g, ' ');
  }

  function clearDropdown() {
    while (searchDropdown.firstChild) {
      searchDropdown.removeChild(searchDropdown.firstChild);
    }
  }

  function buildResultNode(doc) {
    // Use safe DOM methods — no innerHTML with dynamic data
    var a = document.createElement('a');
    a.className = 'search-result';
    a.href = doc.url;
    a.setAttribute('role', 'option');

    var sec = sectionLabel(doc.section);
    if (sec) {
      var secSpan = document.createElement('span');
      secSpan.className = 'search-result__section';
      secSpan.textContent = sec;
      a.appendChild(secSpan);
    }

    var titleSpan = document.createElement('span');
    titleSpan.className = 'search-result__title';
    titleSpan.textContent = doc.title;
    a.appendChild(titleSpan);

    return a;
  }

  function renderResults(results) {
    selectedIndex = -1;
    clearDropdown();

    if (!results.length) {
      var empty = document.createElement('div');
      empty.className = 'search-dropdown__empty';
      empty.textContent = 'No results';
      searchDropdown.appendChild(empty);
      searchDropdown.classList.add('is-open');
      return;
    }

    results.slice(0, 8).forEach(function (r) {
      var doc = docs.find(function (d) { return d.url === r.ref; });
      if (!doc) return;
      searchDropdown.appendChild(buildResultNode(doc));
    });

    searchDropdown.classList.add('is-open');
  }

  function close() {
    searchDropdown.classList.remove('is-open');
    clearDropdown();
    selectedIndex = -1;
  }

  searchInput.addEventListener('input', function () {
    var q = searchInput.value.trim();
    if (!q || !lunrIndex) { close(); return; }
    var results = lunrIndex.search(q + '*');
    if (!results.length) results = lunrIndex.search(q);
    renderResults(results);
  });

  searchInput.addEventListener('keydown', function (e) {
    var items = searchDropdown.querySelectorAll('.search-result');
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      selectedIndex = Math.min(selectedIndex + 1, items.length - 1);
      items.forEach(function (el, i) { el.classList.toggle('is-selected', i === selectedIndex); });
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      selectedIndex = Math.max(selectedIndex - 1, -1);
      items.forEach(function (el, i) { el.classList.toggle('is-selected', i === selectedIndex); });
    } else if (e.key === 'Enter' && selectedIndex >= 0) {
      e.preventDefault();
      items[selectedIndex].click();
    } else if (e.key === 'Escape') {
      close();
      searchInput.blur();
    }
  });

  document.addEventListener('click', function (e) {
    if (!searchInput.contains(e.target) && !searchDropdown.contains(e.target)) {
      close();
    }
  });
})();
```

**Step 4: Verify build and search**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
~/.gem/ruby/2.6.0/bin/bundle exec jekyll serve --detach
```

Open `http://127.0.0.1:4000/Control-System-Tools/`. Type "nfpa" in the topnav search input.
Expected: dropdown with results including "NFPA 79" labelled under "Standards".
Test: arrow keys move selection; Enter navigates to selected result; Escape closes.
Kill server: `kill $(lsof -ti :4000)`

**Step 5: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add docs/_includes/topnav.html docs/assets/css/main.css docs/assets/js/main.js
git commit -m "feat: add lunr.js inline search dropdown to topnav"
```

---

### Task 5: Crosswalk comparison selector page

**Files:**
- Create: `docs/crosswalks/compare/index.md`
- Modify: `docs/assets/css/main.css` (append comparison styles)
- Modify: `docs/crosswalks/index.md` (add compare link)

**Step 1: Append comparison selector styles to `main.css`**

Add at the end of `docs/assets/css/main.css`:

```css
/* ==========================================================================
   Crosswalk comparison selector
   ========================================================================== */
.compare-selector {
  display: flex;
  gap: 1rem;
  align-items: center;
  margin: 1.5rem 0;
  flex-wrap: wrap;
}

.compare-selector select {
  border: 1px solid var(--color-border);
  background: var(--color-bg);
  font-family: var(--font-sans);
  font-size: 0.9rem;
  padding: 0.4rem 0.6rem;
  min-width: 180px;
}

.compare-selector__vs {
  font-weight: 600;
  color: var(--color-text-muted);
}

.compare-result {
  margin-top: 1.5rem;
}

.compare-result[hidden] {
  display: none;
}

.compare-no-data {
  background: var(--color-bg-panel);
  border: 1px solid var(--color-border);
  padding: 1rem;
  color: var(--color-text-muted);
  font-size: 0.9rem;
  margin-top: 1.5rem;
}

.compare-no-data[hidden] {
  display: none;
}
```

**Step 2: Create `docs/crosswalks/compare/index.md`**

Create the file. The inline `<script>` block uses only `textContent` and property access — no dynamic HTML injection:

```markdown
---
layout: default
title: "Standards Comparison"
description: "Select any two standards to view their overlap and relationship."
breadcrumb:
  - name: "Crosswalks"
    url: "/tools/crosswalks/"
  - name: "Compare"
related_standards:
  - name: "NFPA 79 vs IEC 60204-1"
    url: "/tools/crosswalks/nfpa79-iec60204/"
  - name: "UL 508A / NEC / NFPA 79"
    url: "/tools/crosswalks/ul508a-nec-nfpa79/"
  - name: "Standards Decision Workflow"
    url: "/tools/crosswalks/standards-decision-workflow/"
---

<div class="page-header">
  <span class="page-header__label">Crosswalks</span>
  <h1>Standards Comparison</h1>
  <p>Select two standards to view their overlap matrix. Only pairs with documented crosswalk data are shown.</p>
</div>

<div class="compare-selector">
  <select id="compare-a" aria-label="First standard">
    <option value="">— Select standard A —</option>
    <option value="nec">NEC (NFPA 70)</option>
    <option value="nfpa79">NFPA 79</option>
    <option value="ul508a">UL 508A</option>
    <option value="iec60204">IEC 60204-1</option>
    <option value="iso12100">ISO 12100</option>
    <option value="iso13849">ISO 13849-1</option>
    <option value="iec62061">IEC 62061</option>
    <option value="iec61508">IEC 61508</option>
    <option value="iec61511">IEC 61511</option>
  </select>
  <span class="compare-selector__vs">vs</span>
  <select id="compare-b" aria-label="Second standard">
    <option value="">— Select standard B —</option>
    <option value="nec">NEC (NFPA 70)</option>
    <option value="nfpa79">NFPA 79</option>
    <option value="ul508a">UL 508A</option>
    <option value="iec60204">IEC 60204-1</option>
    <option value="iso12100">ISO 12100</option>
    <option value="iso13849">ISO 13849-1</option>
    <option value="iec62061">IEC 62061</option>
    <option value="iec61508">IEC 61508</option>
    <option value="iec61511">IEC 61511</option>
  </select>
</div>

<p class="compare-no-data" id="compare-no-data" hidden>
  No documented crosswalk exists for this pair in the local corpus.
  See the <a href="../">Crosswalks index</a> for available comparisons,
  or consult <a href="../../standards/">individual standard pages</a> for relationship context.
</p>

<!-- Pair: NFPA 79 vs IEC 60204-1 -->
<div class="compare-result" id="pair-nfpa79-iec60204" hidden>

## NFPA 79:2024 vs IEC 60204-1:2018

Both cover electrical equipment of machines. Use when designing for US + EU markets. Design to the **most restrictive** requirement from each standard.

[View full crosswalk →](../nfpa79-iec60204/)

| Topic Area | NFPA 79 | IEC 60204-1 | Equivalence |
|------------|---------|-------------|-------------|
| Scope boundary | Ch. 1 | Clause 1 | High |
| Incoming supply / Disconnect | Ch. 5 | Clause 5 | Very High |
| Protection against electric shock | Ch. 7 | Clause 6 | High |
| Equipment protection (overcurrent) | Ch. 6 | Clause 7 | High |
| Grounding / Bonding | Ch. 8 | Clause 8 | Very High |
| Control circuits / E-stop | Ch. 9 | Clause 9 | Very High |
| Operator interface | Ch. 10 | Clause 10 | High |
| Control equipment / Enclosures | Ch. 11 | Clause 11 | High |
| Motors and drives | Ch. 12 | Clause 12 | High |
| Wiring / Conductors | Ch. 14 | Clause 12 | Medium |
| Marking and documentation | Ch. 19 | Clause 17 | High |
| Verification and testing | Ch. 20 | Clause 15 | High |

**Key difference — wire colors:**

| Conductor | NFPA 79 | IEC 60204-1 |
|-----------|---------|-------------|
| Protective Earth | Green or bare | Yellow-green (required) |
| Neutral | White or gray | Blue |
| Phase conductors | Black, red, blue | Brown, black, gray |

</div>

<!-- Pair: US Electrical family (UL 508A / NEC / NFPA 79) -->
<div class="compare-result" id="pair-us-electrical" hidden>

## US Electrical Standards: UL 508A / NEC / NFPA 79

These three standards form the US electrical compliance stack. They overlap but have distinct scopes.

[View full crosswalk →](../ul508a-nec-nfpa79/)

| Standard | Primary Scope | When It Applies |
|----------|---------------|-----------------|
| NEC (NFPA 70) | Electrical wiring in buildings | Always — governs supply wiring to the panel |
| NFPA 79 | Electrical equipment on industrial machinery | Machinery with motors, actuators, control circuits |
| UL 508A | Industrial control panel construction | When UL listing is required (most US installations) |

| Topic | NEC | NFPA 79 | UL 508A |
|-------|-----|---------|---------|
| Scope | Premises wiring | Machine electrical equipment | Control panel construction |
| Branch circuit protection | Governs | References NEC | References both |
| Wire sizing | NEC tables | Follows NEC inside enclosure | Follows NEC |
| Grounding | Art. 250 | Ch. 8 references NEC | Follows NFPA 79 / NEC |
| E-stop / Safety | Not covered | Ch. 9 | Not covered |
| Listing / Marking | Not a listing std | Not a listing std | UL listing mark |
| Panel enclosure | Not covered | Ch. 11 | Detailed requirements |

</div>

<script>
(function () {
  var selA = document.getElementById('compare-a');
  var selB = document.getElementById('compare-b');
  var noData = document.getElementById('compare-no-data');

  var pairs = {
    'nfpa79+iec60204':  'pair-nfpa79-iec60204',
    'iec60204+nfpa79':  'pair-nfpa79-iec60204',
    'nec+nfpa79':       'pair-us-electrical',
    'nfpa79+nec':       'pair-us-electrical',
    'nec+ul508a':       'pair-us-electrical',
    'ul508a+nec':       'pair-us-electrical',
    'nfpa79+ul508a':    'pair-us-electrical',
    'ul508a+nfpa79':    'pair-us-electrical'
  };

  function update() {
    var a = selA.value;
    var b = selB.value;

    document.querySelectorAll('.compare-result').forEach(function (el) {
      el.hidden = true;
    });
    noData.hidden = true;

    if (!a || !b || a === b) return;

    var pairId = pairs[a + '+' + b];
    if (pairId) {
      var result = document.getElementById(pairId);
      if (result) result.hidden = false;
    } else {
      noData.hidden = false;
    }
  }

  selA.addEventListener('change', update);
  selB.addEventListener('change', update);
})();
</script>
```

**Step 3: Add compare link to `docs/crosswalks/index.md`**

Open `docs/crosswalks/index.md` and find the list of crosswalk page links. Add the following line to the list:

```markdown
- [Standards Comparison Tool](/tools/crosswalks/compare/) — select any two standards to view their overlap matrix
```

**Step 4: Verify build and comparison page**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
~/.gem/ruby/2.6.0/bin/bundle exec jekyll serve --detach
```

Open `http://127.0.0.1:4000/Control-System-Tools/crosswalks/compare/`.
Select "NFPA 79" and "IEC 60204-1" — equivalency table should appear.
Select "ISO 13849-1" and "IEC 61511" — "No documented crosswalk" message should appear.
Kill server: `kill $(lsof -ti :4000)`

**Step 5: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add docs/crosswalks/compare/index.md docs/crosswalks/index.md docs/assets/css/main.css
git commit -m "feat: add crosswalk comparison selector page with NFPA79/IEC60204 and US electrical pairs"
```

---

### Task 6: Push and verify deployment

**Step 1: Push all commits**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git push
```

**Step 2: Monitor GitHub Actions**

```bash
gh run list --limit 3
gh run watch
```

Expected: workflow completes, site deploys.

**Step 3: Verify live site**

Open `https://kyawminthu.github.io/Control-System-Tools/` and confirm:
- Search input in topnav — type "nfpa", dropdown appears
- Click a Mermaid diagram — lightbox appears
- Browser print preview — clean, no sidebar
- `/tools/crosswalks/compare/` — comparison selector works

**Step 4: Update project state**

Update `project_state/project_state.md`:
- Phase: **Phase 2 complete**
- Move Phase 2 items to completed
- Add Phase 3 backlog: interactive standards graph, remaining standard detail pages

Update `project_state/change_log.md` with a `2026-03-05` entry for Phase 2.

**Step 5: Commit project state**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add project_state/
git commit -m "docs: update project state for Phase 2 completion"
git push
```

---

## Files changed summary

| File | Tasks |
|------|-------|
| `docs/assets/css/main.css` | 1, 2, 4, 5 — print, lightbox, search, comparison styles |
| `docs/assets/js/main.js` | 2, 4 — lightbox and search JS |
| `docs/_layouts/default.html` | 3 — lunr.js CDN |
| `docs/_includes/topnav.html` | 4 — search input |
| `docs/assets/data/search.json` | 3 — Jekyll search index |
| `docs/crosswalks/compare/index.md` | 5 — comparison selector page |
| `docs/crosswalks/index.md` | 5 — add compare link |
| `project_state/project_state.md` | 6 — phase update |
| `project_state/change_log.md` | 6 — change log |
