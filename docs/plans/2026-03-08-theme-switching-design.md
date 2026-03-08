# Theme Switching — Design Document

**Date:** 2026-03-08
**Status:** Approved
**Phase:** Reference / UX

---

## Purpose

Add dark mode support with a manual toggle that defaults to the OS preference (`prefers-color-scheme`). User choice persists across sessions via `localStorage`.

---

## Architecture

Three components — no new dependencies, no build step.

### 1. CSS

- Convert topnav hardcoded colors (`#1a2a3a`, white text) to `--color-topnav-bg` / `--color-topnav-text` variables in `:root`
- Add `[data-theme="dark"]` block on `<html>` overriding all `--color-*` variables
- Add `@media (prefers-color-scheme: dark)` block with identical overrides — applies when no saved preference exists and JS is unavailable

### 2. Inline script in `<head>` (flash prevention)

A small `<script>` tag in `docs/_layouts/default.html` before any CSS renders. It:
1. Reads `localStorage.getItem('theme')`
2. Falls back to `window.matchMedia('(prefers-color-scheme: dark)').matches`
3. Sets `document.documentElement.setAttribute('data-theme', resolvedTheme)`

This runs synchronously before paint — eliminates flash of wrong theme.

### 3. `main.js` toggle handler + topnav button

- `topnav.html`: add `<button class="topnav__theme-toggle" id="theme-toggle" aria-label="Toggle theme">☾</button>` between search and hamburger
- `main.js`: toggle handler reads current `data-theme`, flips it, saves to `localStorage`, updates button icon

---

## Dark Color Palette

| Variable | Light | Dark |
|----------|-------|------|
| `--color-bg` | `#f8f8f6` | `#1a1a1a` |
| `--color-bg-panel` | `#f2f2ef` | `#242424` |
| `--color-bg-code` | `#eeecea` | `#2a2a2a` |
| `--color-border` | `#c8c8c4` | `#3a3a3a` |
| `--color-border-mid` | `#a0a09a` | `#505050` |
| `--color-text` | `#1e1e1e` | `#e8e8e6` |
| `--color-text-muted` | `#5a5a58` | `#9a9a98` |
| `--color-accent` | `#2b5797` | `#6b9fd4` |
| `--color-accent-hover` | `#1e3e6e` | `#8ab8e8` |
| `--color-warn` | `#8b6914` | `#d4a84b` |
| `--color-warn-bg` | `#fdf6e3` | `#2a2000` |
| `--color-topnav-bg` | `#1a2a3a` | `#111820` |
| `--color-topnav-text` | `#ffffff` | `#e8e8e6` |

---

## Toggle Button

- Placed in topnav: right of search input, left of hamburger
- Unicode icons only: `☾` (light mode — click for dark), `☀` (dark mode — click for light)
- `aria-label="Toggle theme"` for accessibility
- Icon set correctly on page load by inline script (no flicker)

---

## Files Changed

| File | Action |
|------|--------|
| `docs/assets/css/main.css` | Convert topnav hardcoded colors to variables; add `[data-theme="dark"]` block; add `@media (prefers-color-scheme: dark)` block |
| `docs/_layouts/default.html` | Add inline `<script>` in `<head>` for flash-free theme resolution |
| `docs/_includes/topnav.html` | Add theme toggle button |
| `docs/assets/js/main.js` | Add toggle click handler |

---

## Out of Scope

- Mermaid diagram theme switching (neutral theme works in both light and dark)
- Per-page theme overrides
- System tray / OS integration beyond `prefers-color-scheme`
- Transition animations between themes
