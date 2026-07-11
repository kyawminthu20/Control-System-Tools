# Theme Switching Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add dark mode with a manual toggle button that defaults to OS preference and persists the user's choice in `localStorage`.

**Architecture:** CSS custom properties already cover all theme-sensitive colors. Task 1 converts remaining hardcoded colors to variables and adds a `[data-theme="dark"]` override block plus a `@media (prefers-color-scheme: dark)` fallback. Task 2 adds an inline `<script>` in `<head>` that sets `data-theme` before first paint (no flicker). Tasks 3–4 add the toggle button and click handler.

**Tech Stack:** Jekyll 4.2 · vanilla CSS custom properties · vanilla JS · `localStorage` · `matchMedia`

---

## Task 1: CSS — variables + dark token block

**Files:**
- Modify: `docs/assets/css/main.css`

The topnav already uses hardcoded dark colors (it's a dark bar in light mode too). Cards, tables, and lifecycle stages use hardcoded `#ffffff`. This task converts those to variables, then adds the dark overrides.

**Step 1: Add new variables to `:root`**

In `docs/assets/css/main.css`, find the `:root` block (lines 13–32). Replace it with:

```css
:root {
  /* Light theme tokens */
  --color-bg:         #f8f8f6;
  --color-bg-panel:   #f2f2ef;
  --color-bg-code:    #eeecea;
  --color-bg-elevated: #ffffff;
  --color-bg-stripe:  #fafaf8;
  --color-border:     #c8c8c4;
  --color-border-mid: #a0a09a;
  --color-text:       #1e1e1e;
  --color-text-muted: #5a5a58;
  --color-accent:     #2b5797;
  --color-accent-hover: #1e3e6e;
  --color-warn:       #8b6914;
  --color-warn-bg:    #fdf6e3;
  --color-lifecycle-hover: #e8eff8;

  /* Topnav tokens (dark bar in both modes) */
  --color-topnav-bg:           #1a1a1a;
  --color-topnav-text:         #e8e8e8;
  --color-topnav-text-strong:  #ffffff;
  --color-topnav-border:       #333333;
  --color-topnav-link:         #c0c0c0;
  --color-topnav-hover-bg:     #2a2a2a;
  --color-topnav-btn-border:   #555555;

  --font-sans:  system-ui, -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
  --font-mono:  ui-monospace, "SFMono-Regular", "SF Mono", Menlo, Consolas, monospace;

  --sidebar-width:  240px;
  --context-width:  220px;
  --topnav-height:  44px;
}
```

**Step 2: Replace hardcoded colors in content elements**

In `docs/assets/css/main.css`, make these exact replacements:

| Find (exact) | Replace with |
|---|---|
| `tr:nth-child(even) td {\n  background: #fafaf8;\n}` | `tr:nth-child(even) td {\n  background: var(--color-bg-stripe);\n}` |
| `.card {\n  border: 1px solid var(--color-border);\n  padding: 1rem;\n  background: #ffffff;\n}` | `.card {\n  border: 1px solid var(--color-border);\n  padding: 1rem;\n  background: var(--color-bg-elevated);\n}` |
| `  background: #ffffff;\n}\n.lifecycle-stage:last-child` | `  background: var(--color-bg-elevated);\n}\n.lifecycle-stage:last-child` |
| `.lifecycle-stage:hover {\n  background: #e8eff8;\n}` | `.lifecycle-stage:hover {\n  background: var(--color-lifecycle-hover);\n}` |
| `.scenario-card {\n  border: 1px solid var(--color-border);\n  padding: 1rem;\n  background: #ffffff;\n}` | `.scenario-card {\n  border: 1px solid var(--color-border);\n  padding: 1rem;\n  background: var(--color-bg-elevated);\n}` |

**Do NOT change** `.mermaid-wrap { background: #ffffff }` — Mermaid SVGs generate their own light backgrounds; leave as-is.
**Do NOT change** `.hero__cta:hover { color: #ffffff }` — intentional white text on accent button.

**Step 3: Replace hardcoded topnav colors**

In the topnav section of `main.css`, make these replacements:

| Find | Replace |
|---|---|
| `background: #1a1a1a;` (inside `.topnav {`) | `background: var(--color-topnav-bg);` |
| `color: #e8e8e8;` (inside `.topnav {`) | `color: var(--color-topnav-text);` |
| `color: #ffffff;` (inside `.topnav__brand {`) | `color: var(--color-topnav-text-strong);` |
| `color: #ffffff;` (inside `.topnav__brand:hover {`) | `color: var(--color-topnav-text-strong);` |
| `border-left: 1px solid #333;` | `border-left: 1px solid var(--color-topnav-border);` |
| `color: #c0c0c0;` (inside `.topnav__links a {`) | `color: var(--color-topnav-link);` |
| `border-right: 1px solid #333;` | `border-right: 1px solid var(--color-topnav-border);` |
| `color: #ffffff;` (inside `.topnav__links a:hover`) | `color: var(--color-topnav-text-strong);` |
| `background: #2a2a2a;` | `background: var(--color-topnav-hover-bg);` |
| `border: 1px solid #555;` (inside `.topnav__hamburger {`) | `border: 1px solid var(--color-topnav-btn-border);` |
| `color: #e0e0e0;` (inside `.topnav__hamburger {`) | `color: var(--color-topnav-link);` |

**Step 4: Add dark token block and media query**

Append the following to the end of `docs/assets/css/main.css`:

```css
/* --- Dark theme ------------------------------------------------------------ */
[data-theme="dark"] {
  --color-bg:            #1a1a1a;
  --color-bg-panel:      #242424;
  --color-bg-code:       #2a2a2a;
  --color-bg-elevated:   #252525;
  --color-bg-stripe:     #1f1f1f;
  --color-border:        #3a3a3a;
  --color-border-mid:    #505050;
  --color-text:          #e8e8e6;
  --color-text-muted:    #9a9a98;
  --color-accent:        #6b9fd4;
  --color-accent-hover:  #8ab8e8;
  --color-warn:          #d4a84b;
  --color-warn-bg:       #2a2000;
  --color-lifecycle-hover: #1e2a38;

  /* Topnav slightly darker in dark mode */
  --color-topnav-bg:      #0f0f0f;
  --color-topnav-border:  #222222;
  --color-topnav-hover-bg: #1f1f1f;
  --color-topnav-btn-border: #444444;
}

/* OS-level dark preference — fallback when JS hasn't set data-theme yet,
   and for users who have not manually selected light mode. */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --color-bg:            #1a1a1a;
    --color-bg-panel:      #242424;
    --color-bg-code:       #2a2a2a;
    --color-bg-elevated:   #252525;
    --color-bg-stripe:     #1f1f1f;
    --color-border:        #3a3a3a;
    --color-border-mid:    #505050;
    --color-text:          #e8e8e6;
    --color-text-muted:    #9a9a98;
    --color-accent:        #6b9fd4;
    --color-accent-hover:  #8ab8e8;
    --color-warn:          #d4a84b;
    --color-warn-bg:       #2a2000;
    --color-lifecycle-hover: #1e2a38;
    --color-topnav-bg:      #0f0f0f;
    --color-topnav-border:  #222222;
    --color-topnav-hover-bg: #1f1f1f;
    --color-topnav-btn-border: #444444;
  }
}

/* Theme toggle button in topnav */
.topnav__theme-toggle {
  background: none;
  border: 1px solid var(--color-topnav-btn-border);
  color: var(--color-topnav-link);
  padding: 0.2rem 0.5rem;
  cursor: pointer;
  font-size: 0.95rem;
  margin-left: 0.5rem;
  line-height: 1;
  flex-shrink: 0;
}
.topnav__theme-toggle:hover {
  color: var(--color-topnav-text-strong);
  border-color: var(--color-topnav-btn-border);
}
```

**Step 5: Run Jekyll build — must be clean**

```bash
cd ./docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -4
```

Expected: `done in X seconds.` — no errors.

**Step 6: Commit**

```bash
cd .
git add docs/assets/css/main.css
git commit -m "feat(theme): add dark token CSS — variables, dark block, media query"
```

---

## Task 2: Flash-prevention inline script in `<head>`

**Files:**
- Modify: `docs/_layouts/default.html`

**Step 1: Add inline script to `<head>`**

In `docs/_layouts/default.html`, find this line:

```html
  <link rel="stylesheet" href="{{ '/assets/css/main.css' | relative_url }}">
```

Replace it with:

```html
  <link rel="stylesheet" href="{{ '/assets/css/main.css' | relative_url }}">
  <script>
    (function () {
      var saved = localStorage.getItem('theme');
      var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      var theme = saved ? saved : (prefersDark ? 'dark' : 'light');
      document.documentElement.setAttribute('data-theme', theme);
    })();
  </script>
```

This runs synchronously before any paint — the `data-theme` attribute is set on `<html>` before CSS is applied, so the correct color tokens are used from frame 1.

**Step 2: Run Jekyll build — must be clean**

```bash
cd ./docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -4
```

**Step 3: Verify the inline script appears in built HTML**

```bash
grep -c "localStorage.getItem" ./docs/_site/index.html
```

Expected: `1`

**Step 4: Commit**

```bash
cd .
git add docs/_layouts/default.html
git commit -m "feat(theme): add flash-free theme resolution script to <head>"
```

---

## Task 3: Add toggle button to topnav

**Files:**
- Modify: `docs/_includes/topnav.html`

**Step 1: Add the toggle button**

In `docs/_includes/topnav.html`, find this line at the end of the nav:

```html
  <button class="topnav__hamburger" id="sidebar-toggle" aria-label="Toggle sidebar">&#9776;</button>
```

Replace with:

```html
  <button class="topnav__theme-toggle" id="theme-toggle" aria-label="Switch to dark mode">&#9790;</button>
  <button class="topnav__hamburger" id="sidebar-toggle" aria-label="Toggle sidebar">&#9776;</button>
```

`&#9790;` = ☾ (crescent moon — shown in light mode, meaning "click for dark").
`&#9728;` = ☀ (sun — shown in dark mode, meaning "click for light"). The JS handler swaps these.

**Step 2: Run Jekyll build — must be clean**

```bash
cd ./docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -4
```

**Step 3: Commit**

```bash
cd .
git add docs/_includes/topnav.html
git commit -m "feat(theme): add theme toggle button to topnav"
```

---

## Task 4: Toggle handler in `main.js` + project state

**Files:**
- Modify: `docs/assets/js/main.js`
- Modify: `project_state/project_state.md`
- Modify: `project_state/change_log.md`

**Step 1: Add toggle handler to `main.js`**

In `docs/assets/js/main.js`, append the following block at the end of the file:

```javascript
// Theme toggle
(function () {
  var btn = document.getElementById('theme-toggle');
  if (!btn) return;

  function updateBtn(theme) {
    btn.textContent = theme === 'dark' ? '\u2600' : '\u263E'; // ☀ or ☾
    btn.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
  }

  // Sync button icon with current theme (set by inline head script)
  var current = document.documentElement.getAttribute('data-theme') || 'light';
  updateBtn(current);

  btn.addEventListener('click', function () {
    var next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateBtn(next);
  });
})();
```

**Step 2: Run Jekyll build — must be clean**

```bash
cd ./docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -4
```

**Step 3: Verify toggle handler in built JS**

```bash
grep -c "theme-toggle" ./docs/_site/assets/js/main.js
```

Expected: `1` or more.

**Step 4: Update `project_state/project_state.md`**

Add the following section after the Phase 6 (Glossary) scope block:

```markdown
## Phase 7 Scope — Theme Switching — COMPLETED

**Rationale:** Engineers use reference sites in varied lighting environments. Dark mode
reduces eye strain during late-night or low-light reading. Following OS preference
requires zero user interaction while still allowing manual override.

- [x] `docs/assets/css/main.css` — new CSS variables for hardcoded colors; `[data-theme="dark"]` token block; `@media (prefers-color-scheme: dark)` fallback; toggle button styles
- [x] `docs/_layouts/default.html` — inline flash-prevention script in `<head>`
- [x] `docs/_includes/topnav.html` — theme toggle button (☾/☀)
- [x] `docs/assets/js/main.js` — toggle handler with `localStorage` persistence
- [x] Jekyll build clean
```

**Step 5: Update `project_state/change_log.md`**

Insert the following at the top of the change history (before the most recent entry):

```markdown
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
```

**Step 6: Commit everything**

```bash
cd .
git add docs/assets/js/main.js project_state/project_state.md project_state/change_log.md
git commit -m "feat(theme): add toggle handler + update project state for Phase 7"
```
