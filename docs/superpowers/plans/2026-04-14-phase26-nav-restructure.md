# Phase 26 — Navigation Restructure and Link Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Physically reorganize ~156 Jekyll pages into a 10-group intent-based URL structure, install `jekyll-redirect-from` for backwards compatibility, rewrite `navigation.yml`, and drive the internal-broken-link count to zero.

**Architecture:** Install the `jekyll-redirect-from` plugin so every moved page can list its old URL(s) in `redirect_from:` front matter — Jekyll auto-generates meta-refresh stubs. A new Python tool `tools/check_internal_links.py` (stdlib only) walks the built `_site/` and fails on any broken internal `<a href>`. A committed migration map (`docs/_data/phase26_migration_map.yml`) is the authoritative old→new URL registry.

**Tech Stack:** Jekyll 4.3, `jekyll-redirect-from` plugin, Ruby 2.6.10 bundler at `~/.gem/ruby/2.6.0/bin/bundle`, Python 3.12+, `html.parser` stdlib only.

**Working directory:** `/Users/kyawminthu/Dev/Control System Tools` (master branch).

---

## Task 1: Install jekyll-redirect-from plugin

**Files:**
- Modify: `docs/Gemfile`
- Modify: `docs/_config.yml`

- [ ] **Step 1: Add gem to Gemfile**

Edit `docs/Gemfile` to add `jekyll-redirect-from` inside the `jekyll_plugins` group. After the change, the file should read:

```ruby
source "https://rubygems.org"

gem "jekyll", "~> 4.3"
gem "webrick", "~> 1.8"

group :jekyll_plugins do
  gem "jekyll-seo-tag"
  gem "jekyll-redirect-from"
end
```

- [ ] **Step 2: Add plugin to _config.yml**

Edit `docs/_config.yml` — extend the `plugins:` block to include the new plugin:

```yaml
plugins:
  - jekyll-seo-tag
  - jekyll-redirect-from
```

- [ ] **Step 3: Install the gem**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle install
```

Expected: `Bundle complete!` with `jekyll-redirect-from` listed as installed.

- [ ] **Step 4: Verify build still works**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
```

Expected: `done in X.XXX seconds.` — zero errors.

- [ ] **Step 5: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add docs/Gemfile docs/Gemfile.lock docs/_config.yml
git commit -m "feat(site): install jekyll-redirect-from plugin"
```

---

## Task 2: Create internal link checker tool

**Files:**
- Create: `tools/check_internal_links.py`

- [ ] **Step 1: Create the link checker**

Write `tools/check_internal_links.py` with the exact content below:

```python
#!/usr/bin/env python3
"""
Internal link checker for the Jekyll-built static site.

Usage:
    python3 tools/check_internal_links.py docs/_site/

Walks every .html file in the given directory, extracts every <a href>, and
verifies that each internal link resolves to a real file on disk.

Exits 0 if zero broken links, 1 otherwise.
"""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

BASEURL = "/Control-System-Tools"


class LinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        for name, value in attrs:
            if name == "href" and value:
                self.links.append(value)


def is_external(href: str) -> bool:
    parsed = urlparse(href)
    if parsed.scheme in ("http", "https", "mailto", "tel"):
        return True
    if href.startswith("//"):
        return True
    return False


def resolve(href: str, source: Path, site_root: Path) -> Path | None:
    # Strip fragment and query
    href = href.split("#", 1)[0].split("?", 1)[0]
    if not href:
        return None
    href = unquote(href)

    # Site-root-relative (respects baseurl)
    if href.startswith(BASEURL):
        href = href[len(BASEURL):] or "/"
    if href.startswith("/"):
        target = site_root / href.lstrip("/")
    else:
        target = (source.parent / href).resolve()

    # Jekyll collapses directory URLs to index.html
    if target.is_dir():
        target = target / "index.html"
    if target.suffix == "":
        candidate = target.with_suffix(".html")
        if candidate.exists():
            return candidate
        candidate = target / "index.html"
        if candidate.exists():
            return candidate

    return target


def check_file(html_file: Path, site_root: Path) -> list[tuple[str, str]]:
    extractor = LinkExtractor()
    try:
        extractor.feed(html_file.read_text(encoding="utf-8", errors="ignore"))
    except Exception as exc:
        return [("<parse-error>", f"{exc}")]

    broken: list[tuple[str, str]] = []
    for href in extractor.links:
        if is_external(href) or not href or href.startswith("#"):
            continue
        target = resolve(href, html_file, site_root)
        if target is None:
            continue
        if not target.exists():
            broken.append((href, str(target)))
    return broken


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_internal_links.py <site-root>", file=sys.stderr)
        return 2

    site_root = Path(sys.argv[1]).resolve()
    if not site_root.is_dir():
        print(f"error: {site_root} is not a directory", file=sys.stderr)
        return 2

    total_broken = 0
    broken_by_source: dict[str, list[tuple[str, str]]] = {}
    for html_file in sorted(site_root.rglob("*.html")):
        broken = check_file(html_file, site_root)
        if broken:
            rel = html_file.relative_to(site_root)
            broken_by_source[str(rel)] = broken
            total_broken += len(broken)

    if total_broken == 0:
        print(f"OK: no broken internal links ({len(list(site_root.rglob('*.html')))} files scanned)")
        return 0

    for source, links in broken_by_source.items():
        for href, target in links:
            print(f"{source}: {href} -> {target}")

    print(f"\nFAIL: {total_broken} broken internal link(s) across {len(broken_by_source)} file(s)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Make it executable**

```bash
chmod +x "/Users/kyawminthu/Dev/Control System Tools/tools/check_internal_links.py"
```

- [ ] **Step 3: Smoke-test against current site**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -3
cd ..
python3 tools/check_internal_links.py docs/_site/ 2>&1 | tail -20
```

Expected: either `OK: no broken internal links ...` or a list of broken links. Either way, the tool itself ran without tracebacks.

- [ ] **Step 4: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add tools/check_internal_links.py
git commit -m "feat(tools): add internal link checker (stdlib only)"
```

---

## Task 3: Baseline link audit — fix pre-existing broken links

**Files:** varies (whatever the link checker flags)

- [ ] **Step 1: Run the link checker and save the report**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
python3 tools/check_internal_links.py docs/_site/ > /tmp/phase26_baseline_links.txt 2>&1 || true
cat /tmp/phase26_baseline_links.txt
```

The output is a line-per-broken-link report: `SOURCE_PAGE: BROKEN_HREF -> RESOLVED_TARGET_PATH`.

- [ ] **Step 2: For each broken link, fix it in source markdown**

For each line in the report, locate the source page under `docs/` and correct the link in the markdown file:

- If the link should point to an existing page, update the URL to the correct path (with `baseurl` prefix if rendered-relative).
- If the referenced page no longer exists and is not coming back, remove or rewrite the link.
- If the link points to a file under `_includes` or `_layouts`, leave it alone — it's likely a Jekyll template concern.

NOTE: Do not "fix" broken links by creating empty stub pages. Either fix the URL or remove the link.

- [ ] **Step 3: Rebuild and re-check**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -3
cd ..
python3 tools/check_internal_links.py docs/_site/
```

Repeat Steps 2–3 until the checker exits 0.

- [ ] **Step 4: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add -u docs/
git commit -m "fix(links): baseline — resolve pre-existing broken internal links"
```

---

## Task 4: Create migration map

**Files:**
- Create: `docs/_data/phase26_migration_map.yml`

This file is the authoritative registry of every old→new URL move. Later migration tasks reference it. Keep entries in the order they appear here — migrations run group-by-group.

- [ ] **Step 1: Create the migration map**

Write `docs/_data/phase26_migration_map.yml`:

```yaml
# Phase 26 URL migration map — authoritative old→new URL registry.
# Each entry:
#   old:  site-root-relative OLD URL (with trailing slash)
#   new:  site-root-relative NEW URL (with trailing slash)
#   from: old source path under docs/ (without docs/ prefix, without index.md)
#   to:   new source path under docs/ (without docs/ prefix, without index.md)
#
# Groups are processed in order: fundamentals, design, implementation, verification, tools, training_trim.

fundamentals:
  # Electrical fundamentals
  - { old: /training/fundamentals/,                          new: /fundamentals/electrical/,                          from: training/fundamentals,                          to: fundamentals/electrical }
  - { old: /training/fundamentals/conductor-ampacity/,       new: /fundamentals/electrical/conductor-ampacity/,       from: training/fundamentals/conductor-ampacity,       to: fundamentals/electrical/conductor-ampacity }
  - { old: /training/fundamentals/diodes-transistors/,       new: /fundamentals/electrical/diodes-transistors/,       from: training/fundamentals/diodes-transistors,       to: fundamentals/electrical/diodes-transistors }
  - { old: /training/fundamentals/earthing-systems-iec/,     new: /fundamentals/electrical/earthing-systems-iec/,     from: training/fundamentals/earthing-systems-iec,     to: fundamentals/electrical/earthing-systems-iec }
  - { old: /training/fundamentals/electrical-equations-reference/, new: /fundamentals/electrical/electrical-equations-reference/, from: training/fundamentals/electrical-equations-reference, to: fundamentals/electrical/electrical-equations-reference }
  - { old: /training/fundamentals/electrical-quantities/,    new: /fundamentals/electrical/electrical-quantities/,    from: training/fundamentals/electrical-quantities,    to: fundamentals/electrical/electrical-quantities }
  - { old: /training/fundamentals/equivalent-circuit-methods/, new: /fundamentals/electrical/equivalent-circuit-methods/, from: training/fundamentals/equivalent-circuit-methods, to: fundamentals/electrical/equivalent-circuit-methods }
  - { old: /training/fundamentals/kirchhoff-laws/,           new: /fundamentals/electrical/kirchhoff-laws/,           from: training/fundamentals/kirchhoff-laws,           to: fundamentals/electrical/kirchhoff-laws }
  - { old: /training/fundamentals/passive-components/,       new: /fundamentals/electrical/passive-components/,       from: training/fundamentals/passive-components,       to: fundamentals/electrical/passive-components }
  - { old: /training/fundamentals/series-parallel-dividers/, new: /fundamentals/electrical/series-parallel-dividers/, from: training/fundamentals/series-parallel-dividers, to: fundamentals/electrical/series-parallel-dividers }
  # Control fundamentals
  - { old: /training/control-systems/,                       new: /fundamentals/control/,                             from: training/control-systems,                       to: fundamentals/control }
  - { old: /training/control-systems/async-faults-distributed-systems/, new: /fundamentals/control/async-faults-distributed-systems/, from: training/control-systems/async-faults-distributed-systems, to: fundamentals/control/async-faults-distributed-systems }
  - { old: /training/control-systems/control-loop-architectures/,       new: /fundamentals/control/control-loop-architectures/,       from: training/control-systems/control-loop-architectures,       to: fundamentals/control/control-loop-architectures }
  - { old: /training/control-systems/control-theory-overview/,          new: /fundamentals/control/control-theory-overview/,          from: training/control-systems/control-theory-overview,          to: fundamentals/control/control-theory-overview }
  - { old: /training/control-systems/deterministic-nondeterministic-control/, new: /fundamentals/control/deterministic-nondeterministic-control/, from: training/control-systems/deterministic-nondeterministic-control, to: fundamentals/control/deterministic-nondeterministic-control }
  - { old: /training/control-systems/industrial-pid/,                   new: /fundamentals/control/industrial-pid/,                   from: training/control-systems/industrial-pid,                   to: fundamentals/control/industrial-pid }
  - { old: /training/control-systems/interlocks-permissives-safety-trips/, new: /fundamentals/control/interlocks-permissives-safety-trips/, from: training/control-systems/interlocks-permissives-safety-trips, to: fundamentals/control/interlocks-permissives-safety-trips }
  - { old: /training/control-systems/machine-state-model/,              new: /fundamentals/control/machine-state-model/,              from: training/control-systems/machine-state-model,              to: fundamentals/control/machine-state-model }
  - { old: /training/control-systems/multi-axis-coordination/,          new: /fundamentals/control/multi-axis-coordination/,          from: training/control-systems/multi-axis-coordination,          to: fundamentals/control/multi-axis-coordination }
  - { old: /training/control-systems/pid-drone-control/,                new: /fundamentals/control/pid-drone-control/,                from: training/control-systems/pid-drone-control,                from_alt: null, to: fundamentals/control/pid-drone-control }
  - { old: /training/control-systems/pid-foundation/,                   new: /fundamentals/control/pid-foundation/,                   from: training/control-systems/pid-foundation,                   to: fundamentals/control/pid-foundation }
  - { old: /training/control-systems/pid-heater-control/,               new: /fundamentals/control/pid-heater-control/,               from: training/control-systems/pid-heater-control,               to: fundamentals/control/pid-heater-control }
  - { old: /training/control-systems/pid-intuition/,                    new: /fundamentals/control/pid-intuition/,                    from: training/control-systems/pid-intuition,                    to: fundamentals/control/pid-intuition }
  - { old: /training/control-systems/servo-tuning/,                     new: /fundamentals/control/servo-tuning/,                     from: training/control-systems/servo-tuning,                     to: fundamentals/control/servo-tuning }
  - { old: /training/control-systems/vibration-resonance/,              new: /fundamentals/control/vibration-resonance/,              from: training/control-systems/vibration-resonance,              to: fundamentals/control/vibration-resonance }
  # Motor & drive fundamentals
  - { old: /training/electrical-machines/,                   new: /fundamentals/motors/,                              from: training/electrical-machines,                   to: fundamentals/motors }
  - { old: /training/electrical-machines/ac-vs-dc-motors/,   new: /fundamentals/motors/ac-vs-dc-motors/,              from: training/electrical-machines/ac-vs-dc-motors,   to: fundamentals/motors/ac-vs-dc-motors }
  - { old: /training/electrical-machines/bldc-ev-drone-motors/, new: /fundamentals/motors/bldc-ev-drone-motors/,      from: training/electrical-machines/bldc-ev-drone-motors, to: fundamentals/motors/bldc-ev-drone-motors }
  - { old: /training/electrical-machines/dc-motor-basics/,   new: /fundamentals/motors/dc-motor-basics/,              from: training/electrical-machines/dc-motor-basics,   to: fundamentals/motors/dc-motor-basics }
  - { old: /training/electrical-machines/induction-motor-basics/, new: /fundamentals/motors/induction-motor-basics/, from: training/electrical-machines/induction-motor-basics, to: fundamentals/motors/induction-motor-basics }
  - { old: /training/electrical-machines/motor-control-methods/,  new: /fundamentals/motors/motor-control-methods/,  from: training/electrical-machines/motor-control-methods,  to: fundamentals/motors/motor-control-methods }
  - { old: /training/electrical-machines/motor-efficiency-losses/, new: /fundamentals/motors/motor-efficiency-losses/, from: training/electrical-machines/motor-efficiency-losses, to: fundamentals/motors/motor-efficiency-losses }
  - { old: /training/electrical-machines/motor-family-comparison/, new: /fundamentals/motors/motor-family-comparison/, from: training/electrical-machines/motor-family-comparison, to: fundamentals/motors/motor-family-comparison }
  - { old: /training/electrical-machines/motor-nameplates-slip-torque/, new: /fundamentals/motors/motor-nameplates-slip-torque/, from: training/electrical-machines/motor-nameplates-slip-torque, to: fundamentals/motors/motor-nameplates-slip-torque }
  - { old: /training/electrical-machines/motor-vfd-equations/, new: /fundamentals/motors/motor-vfd-equations/,        from: training/electrical-machines/motor-vfd-equations, to: fundamentals/motors/motor-vfd-equations }
  - { old: /training/electrical-machines/servo-drive-fundamentals/, new: /fundamentals/motors/servo-drive-fundamentals/, from: training/electrical-machines/servo-drive-fundamentals, to: fundamentals/motors/servo-drive-fundamentals }
  - { old: /training/electrical-machines/servo-feedback-inertia/, new: /fundamentals/motors/servo-feedback-inertia/,    from: training/electrical-machines/servo-feedback-inertia, to: fundamentals/motors/servo-feedback-inertia }
  - { old: /training/electrical-machines/vfd-fundamentals/,  new: /fundamentals/motors/vfd-fundamentals/,             from: training/electrical-machines/vfd-fundamentals,  to: fundamentals/motors/vfd-fundamentals }
  - { old: /training/electrical-machines/vfd-servo-architecture/, new: /fundamentals/motors/vfd-servo-architecture/, from: training/electrical-machines/vfd-servo-architecture, to: fundamentals/motors/vfd-servo-architecture }

design:
  - { old: /engineering-workflow/,                           new: /design/,                                           from: engineering-workflow,                           to: design }
  - { old: /reference/architecture/,                         new: /design/architecture/,                              from: reference/architecture,                         to: design/architecture }
  - { old: /reference/architecture/compliance-stack/,        new: /design/architecture/compliance-stack/,             from: reference/architecture/compliance-stack,        to: design/architecture/compliance-stack }
  - { old: /reference/architecture/machine-architecture-model/, new: /design/architecture/machine-architecture-model/, from: reference/architecture/machine-architecture-model, to: design/architecture/machine-architecture-model }
  - { old: /reference/architecture/machine-safety-architecture/, new: /design/architecture/machine-safety-architecture/, from: reference/architecture/machine-safety-architecture, to: design/architecture/machine-safety-architecture }
  - { old: /reference/motor-systems/,                        new: /design/motor-selection/,                           from: reference/motor-systems,                        to: design/motor-selection }
  - { old: /reference/motor-systems/motor-selection-matrix/, new: /design/motor-selection/motor-selection-matrix/,    from: reference/motor-systems/motor-selection-matrix, to: design/motor-selection/motor-selection-matrix }
  - { old: /software-stack/,                                 new: /design/software-stack/,                            from: software-stack,                                 to: design/software-stack }
  - { old: /workflows/,                                      new: /design/workflows/,                                 from: workflows,                                      to: design/workflows }
  - { old: /workflows/electrical-review/,                    new: /design/workflows/electrical-review/,               from: workflows/electrical-review,                    to: design/workflows/electrical-review }
  - { old: /workflows/motor-selection/,                      new: /design/workflows/motor-selection/,                 from: workflows/motor-selection,                      to: design/workflows/motor-selection }

implementation:
  - { old: /commissioning-templates/,                        new: /implementation/commissioning-templates/,           from: commissioning-templates,                        to: implementation/commissioning-templates }
  - { old: /commissioning-templates/basic-circuit-polarity/, new: /implementation/commissioning-templates/basic-circuit-polarity/, from: commissioning-templates/basic-circuit-polarity, to: implementation/commissioning-templates/basic-circuit-polarity }
  - { old: /commissioning-templates/capacitor-discharge/,    new: /implementation/commissioning-templates/capacitor-discharge/,    from: commissioning-templates/capacitor-discharge,    to: implementation/commissioning-templates/capacitor-discharge }
  - { old: /commissioning-templates/drive-commissioning/,    new: /implementation/commissioning-templates/drive-commissioning/,    from: commissioning-templates/drive-commissioning,    to: implementation/commissioning-templates/drive-commissioning }
  - { old: /commissioning-templates/motor-nameplate-overload/, new: /implementation/commissioning-templates/motor-nameplate-overload/, from: commissioning-templates/motor-nameplate-overload, to: implementation/commissioning-templates/motor-nameplate-overload }
  - { old: /commissioning-templates/motor-rotation-verification/, new: /implementation/commissioning-templates/motor-rotation-verification/, from: commissioning-templates/motor-rotation-verification, to: implementation/commissioning-templates/motor-rotation-verification }
  - { old: /commissioning-templates/pre-power-panel/,        new: /implementation/commissioning-templates/pre-power-panel/,        from: commissioning-templates/pre-power-panel,        to: implementation/commissioning-templates/pre-power-panel }
  - { old: /scenarios/,                                      new: /implementation/scenarios/,                         from: scenarios,                                      to: implementation/scenarios }
  - { old: /scenarios/global-machine/,                       new: /implementation/scenarios/global-machine/,          from: scenarios/global-machine,                       to: implementation/scenarios/global-machine }
  - { old: /scenarios/machine-safety-implementation/,        new: /implementation/scenarios/machine-safety-implementation/, from: scenarios/machine-safety-implementation, to: implementation/scenarios/machine-safety-implementation }
  - { old: /scenarios/networked-safety-plc/,                 new: /implementation/scenarios/networked-safety-plc/,    from: scenarios/networked-safety-plc,                 to: implementation/scenarios/networked-safety-plc }
  - { old: /scenarios/offshore-platform-control/,            new: /implementation/scenarios/offshore-platform-control/, from: scenarios/offshore-platform-control,            to: implementation/scenarios/offshore-platform-control }
  - { old: /scenarios/oil-gas-process-skid/,                 new: /implementation/scenarios/oil-gas-process-skid/,    from: scenarios/oil-gas-process-skid,                 to: implementation/scenarios/oil-gas-process-skid }
  - { old: /scenarios/process-skid/,                         new: /implementation/scenarios/process-skid/,            from: scenarios/process-skid,                         to: implementation/scenarios/process-skid }
  - { old: /scenarios/semiconductor-equipment/,              new: /implementation/scenarios/semiconductor-equipment/, from: scenarios/semiconductor-equipment,              to: implementation/scenarios/semiconductor-equipment }
  - { old: /scenarios/semiconductor-fab-tool/,               new: /implementation/scenarios/semiconductor-fab-tool/,  from: scenarios/semiconductor-fab-tool,               to: implementation/scenarios/semiconductor-fab-tool }
  - { old: /scenarios/us-industrial-control-panel/,          new: /implementation/scenarios/us-industrial-control-panel/, from: scenarios/us-industrial-control-panel,          to: implementation/scenarios/us-industrial-control-panel }
  - { old: /workflows/servo-commissioning/,                  new: /implementation/servo-commissioning/,               from: workflows/servo-commissioning,                  to: implementation/servo-commissioning }
  - { old: /workflows/vfd-commissioning/,                    new: /implementation/vfd-commissioning/,                 from: workflows/vfd-commissioning,                    to: implementation/vfd-commissioning }
  - { old: /lifecycle/build/,                                new: /implementation/lifecycle-build/,                   from: lifecycle/build,                                to: implementation/lifecycle-build }
  - { old: /lifecycle/pre-commissioning/,                    new: /implementation/lifecycle-pre-commissioning/,       from: lifecycle/pre-commissioning,                    to: implementation/lifecycle-pre-commissioning }
  - { old: /lifecycle/installation/,                         new: /implementation/lifecycle-installation/,            from: lifecycle/installation,                         to: implementation/lifecycle-installation }
  - { old: /lifecycle/commissioning/,                        new: /implementation/lifecycle-commissioning/,           from: lifecycle/commissioning,                        to: implementation/lifecycle-commissioning }

verification:
  - { old: /lifecycle/,                                      new: /verification/lifecycle/,                           from: lifecycle,                                      to: verification/lifecycle }
  - { old: /lifecycle/concept/,                              new: /verification/lifecycle/concept/,                   from: lifecycle/concept,                              to: verification/lifecycle/concept }
  - { old: /lifecycle/standards-selection/,                  new: /verification/lifecycle/standards-selection/,       from: lifecycle/standards-selection,                  to: verification/lifecycle/standards-selection }
  - { old: /lifecycle/risk-assessment/,                      new: /verification/risk-assessment/,                     from: lifecycle/risk-assessment,                      to: verification/risk-assessment }
  - { old: /lifecycle/safety-requirements-spec/,             new: /verification/safety-requirements-spec/,            from: lifecycle/safety-requirements-spec,             to: verification/safety-requirements-spec }
  - { old: /lifecycle/safety-architecture/,                  new: /verification/safety-architecture/,                 from: lifecycle/safety-architecture,                  to: verification/safety-architecture }
  - { old: /lifecycle/detailed-design/,                      new: /verification/lifecycle/detailed-design/,           from: lifecycle/detailed-design,                      to: verification/lifecycle/detailed-design }
  - { old: /lifecycle/draft-documentation/,                  new: /verification/lifecycle/draft-documentation/,       from: lifecycle/draft-documentation,                  to: verification/lifecycle/draft-documentation }
  - { old: /lifecycle/maintenance/,                          new: /verification/maintenance/,                         from: lifecycle/maintenance,                          to: verification/maintenance }
  - { old: /lifecycle/management-of-change/,                 new: /verification/management-of-change/,                from: lifecycle/management-of-change,                 to: verification/management-of-change }
  - { old: /lifecycle/safety-wiring/,                        new: /verification/safety-wiring/,                       from: lifecycle/safety-wiring,                        to: verification/safety-wiring }

tools:
  - { old: /rag-browser/,                                    new: /tools/rag-browser/,                                from: rag-browser,                                    to: tools/rag-browser }
  - { old: /glossary/,                                       new: /tools/glossary/,                                   from: glossary,                                       to: tools/glossary }
  - { old: /crosswalks/,                                     new: /tools/crosswalks/,                                 from: crosswalks,                                     to: tools/crosswalks }
  - { old: /crosswalks/compare/,                             new: /tools/crosswalks/compare/,                         from: crosswalks/compare,                             to: tools/crosswalks/compare }
  - { old: /crosswalks/iec60079-nec-500-505/,                new: /tools/crosswalks/iec60079-nec-500-505/,            from: crosswalks/iec60079-nec-500-505,                to: tools/crosswalks/iec60079-nec-500-505 }
  - { old: /crosswalks/iec61511-iec61508/,                   new: /tools/crosswalks/iec61511-iec61508/,               from: crosswalks/iec61511-iec61508,                   to: tools/crosswalks/iec61511-iec61508 }
  - { old: /crosswalks/nfpa79-iec60204/,                     new: /tools/crosswalks/nfpa79-iec60204/,                 from: crosswalks/nfpa79-iec60204,                     to: tools/crosswalks/nfpa79-iec60204 }
  - { old: /crosswalks/standards-decision-workflow/,         new: /tools/crosswalks/standards-decision-workflow/,     from: crosswalks/standards-decision-workflow,         to: tools/crosswalks/standards-decision-workflow }
  - { old: /crosswalks/ul508a-nec-nfpa79/,                   new: /tools/crosswalks/ul508a-nec-nfpa79/,               from: crosswalks/ul508a-nec-nfpa79,                   to: tools/crosswalks/ul508a-nec-nfpa79 }
  - { old: /reference/,                                      new: /tools/reference-hub/,                              from: reference,                                      to: tools/reference-hub }

training_trim:
  # Only /training/nec-application/ stays under /training/. Top-level /training/index.md is rewritten to a learning-paths landing page.
  - { old: /training/nec-application/,                       new: /training/nec-application/,                         from: training/nec-application,                       to: training/nec-application, note: "no move — keep in place" }
```

- [ ] **Step 2: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add docs/_data/phase26_migration_map.yml
git commit -m "feat(phase-26): add URL migration map"
```

---

## Task 5: Migrate Fundamentals group

**Files:** moves and edits inside `docs/training/fundamentals/`, `docs/training/control-systems/`, `docs/training/electrical-machines/` → `docs/fundamentals/`

- [ ] **Step 1: Create destination directories**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
mkdir -p fundamentals/electrical fundamentals/control fundamentals/motors
```

- [ ] **Step 2: Move each file per the `fundamentals` group in the migration map**

For every entry under `fundamentals:` in `docs/_data/phase26_migration_map.yml`, run:

```bash
git mv "docs/<from>/index.md" "docs/<to>/index.md"
```

Example for the first 3:

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git mv docs/training/fundamentals/index.md                     docs/fundamentals/electrical/index.md
git mv docs/training/fundamentals/conductor-ampacity/index.md  docs/fundamentals/electrical/conductor-ampacity/index.md
git mv docs/training/fundamentals/diodes-transistors/index.md  docs/fundamentals/electrical/diodes-transistors/index.md
```

Repeat for every entry under `fundamentals:`. When the source directory is empty after moves, remove it:

```bash
rmdir docs/training/fundamentals/conductor-ampacity
# ... for each now-empty dir
rmdir docs/training/fundamentals docs/training/control-systems docs/training/electrical-machines
```

- [ ] **Step 3: Add `redirect_from:` to every moved file**

For each moved file, edit its YAML front matter and add a `redirect_from:` block listing the old URL (both trailing-slash and `/index.html` variants). Example, for `docs/fundamentals/electrical/earthing-systems-iec/index.md`:

```yaml
---
layout: default
title: "IEC Earthing Systems"
# ...existing front matter...
redirect_from:
  - /training/fundamentals/earthing-systems-iec/
  - /training/fundamentals/earthing-systems-iec/index.html
---
```

Do this for every moved page in this group. The old URL comes from the `old` field in the migration map.

- [ ] **Step 4: Update any internal cross-links inside moved pages**

Cross-links from a fundamentals page to another fundamentals page should now use the new URL. Run a grep + edit:

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
grep -rln "/training/fundamentals/\|/training/control-systems/\|/training/electrical-machines/" docs/fundamentals/
```

For every file listed, open it and replace old paths with new paths per the migration map. Site-external pages (outside `docs/fundamentals/`) are handled in Task 14.

- [ ] **Step 5: Rebuild and verify**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -10
```

Expected: `done in X.XXX seconds.` Warnings about broken links from OTHER groups are OK (they still point to old URLs that haven't been moved yet — but those URLs still exist because those groups haven't migrated yet, so there should be no warnings).

- [ ] **Step 6: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add -A docs/
git commit -m "refactor(site): migrate fundamentals group to /fundamentals/ with redirects"
```

---

## Task 6: Migrate Design group

**Files:** moves per `design:` section of migration map.

- [ ] **Step 1: Create destination directories**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
mkdir -p design/architecture design/motor-selection design/software-stack design/workflows
```

- [ ] **Step 2: Move each file per the `design` group**

Follow the same pattern as Task 5, Step 2. Use `git mv` for every `from → to` in the `design:` block.

- [ ] **Step 3: Add `redirect_from:` to every moved file**

Same pattern as Task 5, Step 3.

- [ ] **Step 4: Update internal cross-links inside moved pages**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
grep -rln "/engineering-workflow/\|/reference/architecture/\|/reference/motor-systems/\|/software-stack/\|/workflows/electrical-review/\|/workflows/motor-selection/" docs/design/
```

Edit the listed files, replacing old paths with new per the migration map.

- [ ] **Step 5: Rebuild and verify**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -10
```

- [ ] **Step 6: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add -A docs/
git commit -m "refactor(site): migrate design group to /design/ with redirects"
```

---

## Task 7: Migrate Implementation group

Follow the same pattern as Tasks 5–6 for the `implementation:` section of the migration map.

- [ ] **Step 1: Create destinations**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
mkdir -p implementation/commissioning-templates implementation/scenarios \
         implementation/servo-commissioning implementation/vfd-commissioning \
         implementation/lifecycle-build implementation/lifecycle-pre-commissioning \
         implementation/lifecycle-installation implementation/lifecycle-commissioning
```

- [ ] **Step 2: `git mv` every file per `implementation:` entries**

Execute `git mv` for each `from → to` pair in the `implementation:` block of the migration map.

- [ ] **Step 3: Add `redirect_from:` front matter** to every moved file (old URL from map).

- [ ] **Step 4: Update cross-links inside moved pages**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
grep -rln "/commissioning-templates/\|/scenarios/\|/workflows/servo-commissioning/\|/workflows/vfd-commissioning/\|/lifecycle/build/\|/lifecycle/pre-commissioning/\|/lifecycle/installation/\|/lifecycle/commissioning/" docs/implementation/
```

Edit as needed.

- [ ] **Step 5: Build and commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -10
cd ..
git add -A docs/
git commit -m "refactor(site): migrate implementation group to /implementation/ with redirects"
```

---

## Task 8: Migrate Verification group

Same pattern for `verification:` block.

- [ ] **Step 1: Create destinations**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
mkdir -p verification/lifecycle verification/risk-assessment verification/safety-requirements-spec \
         verification/safety-architecture verification/maintenance verification/management-of-change \
         verification/safety-wiring
```

- [ ] **Step 2: `git mv` each file per `verification:` entries**

- [ ] **Step 3: Add `redirect_from:` to every moved file**

- [ ] **Step 4: Update cross-links inside moved pages**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
grep -rln "/lifecycle/" docs/verification/
```

Replace with new `/verification/...` paths per the map.

- [ ] **Step 5: Build and commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -10
cd ..
git add -A docs/
git commit -m "refactor(site): migrate verification group to /verification/ with redirects"
```

---

## Task 9: Migrate Tools group

Same pattern for `tools:` block.

- [ ] **Step 1: Create destinations**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
mkdir -p tools/rag-browser tools/glossary tools/crosswalks tools/reference-hub
```

- [ ] **Step 2: `git mv` each file per `tools:` entries**

- [ ] **Step 3: Add `redirect_from:` to every moved file**

- [ ] **Step 4: Update cross-links inside moved pages**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
grep -rln "/rag-browser/\|/glossary/\|/crosswalks/\|/reference/" docs/tools/
```

Replace with new `/tools/...` paths per the map.

- [ ] **Step 5: Build and commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -10
cd ..
git add -A docs/
git commit -m "refactor(site): migrate tools group to /tools/ with redirects"
```

---

## Task 10: Rewrite /training/ landing page

The `/training/` index now only covers structured learning paths (NEC application module stays here; fundamentals/control/motors moved to `/fundamentals/` in Task 5).

**Files:**
- Modify: `docs/training/index.md`

- [ ] **Step 1: Rewrite the training landing page**

Overwrite `docs/training/index.md` with a concise landing page focused on structured paths:

```markdown
---
layout: default
title: "Training — Structured Learning Paths"
description: "Structured learning paths that combine fundamentals and applied references — NEC for machines and panels, and more paths as they are built."
breadcrumb:
  - name: "Training"
---

<div class="page-header">
  <span class="page-header__label">Training</span>
  <h1>Training — Structured Learning Paths</h1>
</div>

<blockquote>
<strong>Scope:</strong> Structured learning paths. Foundational electrical, control, and motor content has moved to <a href="/fundamentals/">Fundamentals</a>.
</blockquote>

## Available Paths

| Path | Description |
|---|---|
| [NEC for Machines and Panels](/training/nec-application/) | Article 409, Article 430, SCCR workflow, disconnecting means, branch circuits vs. feeders |

## Related Sections

- [Fundamentals](/fundamentals/) — electrical, control theory, motors
- [Design](/design/) — design workflows
- [Verification](/verification/) — lifecycle stages, risk assessment, SIL/PL
```

- [ ] **Step 2: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add docs/training/index.md
git commit -m "refactor(site): rewrite /training/ landing for structured paths only"
```

---

## Task 11: Create Troubleshooting landing page

**Files:**
- Create: `docs/troubleshooting/index.md`

- [ ] **Step 1: Create the landing page**

```markdown
---
layout: default
title: "Troubleshooting"
description: "Troubleshooting references for motors, VFDs, PLC systems, field I/O, networks, and safety circuits. Organized by what the symptom looks like."
breadcrumb:
  - name: "Troubleshooting"
---

<div class="page-header">
  <span class="page-header__label">Troubleshooting</span>
  <h1>Troubleshooting</h1>
</div>

<blockquote>
<strong>Scope:</strong> Entry point for field troubleshooting. Organized by symptom category. Content is cross-linked from fundamentals, design, and commissioning references.
</blockquote>

## Categories

| Category | Where to start |
|---|---|
| Motors | [Motor troubleshooting workflow](/workflows/motor-troubleshooting/) · [Motor symptom patterns — RAG browser](/tools/rag-browser/) |
| VFDs | [VFD commissioning — common faults](/implementation/vfd-commissioning/) · [Drive commissioning template](/implementation/commissioning-templates/drive-commissioning/) |
| PLC systems | [Async faults in distributed systems](/fundamentals/control/async-faults-distributed-systems/) · [Machine state model](/fundamentals/control/machine-state-model/) |
| Field I/O | [Electrical quantities reference](/fundamentals/electrical/electrical-quantities/) · [Basic circuit polarity template](/implementation/commissioning-templates/basic-circuit-polarity/) |
| Networks | [Networked safety PLC scenario](/implementation/scenarios/networked-safety-plc/) · [IEC 62443 cybersecurity](/standards/cybersecurity/iec-62443/) |
| Safety circuits | [Safety wiring](/verification/safety-wiring/) · [Interlocks and permissives](/fundamentals/control/interlocks-permissives-safety-trips/) |

## Related

- [Fundamentals](/fundamentals/) — electrical theory, control theory, motor basics
- [Implementation](/implementation/) — commissioning templates, scenarios
- [Verification](/verification/) — safety validation, risk assessment
```

- [ ] **Step 2: Move the motor-troubleshooting workflow into this section**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git mv docs/workflows/motor-troubleshooting/index.md docs/troubleshooting/motors/index.md
rmdir docs/workflows/motor-troubleshooting 2>/dev/null || true
```

Then add `redirect_from:` front matter to `docs/troubleshooting/motors/index.md`:

```yaml
redirect_from:
  - /workflows/motor-troubleshooting/
  - /workflows/motor-troubleshooting/index.html
```

Update the Motors row in the landing table to:

```
| Motors | [Motor troubleshooting workflow](/troubleshooting/motors/) · [Motor symptom patterns — RAG browser](/tools/rag-browser/) |
```

- [ ] **Step 3: Remove now-empty /workflows/ directory**

If `docs/workflows/` is empty, remove `docs/workflows/index.md` (it was the landing page — superseded by `/design/workflows/` and `/implementation/`):

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
rm -f docs/workflows/index.md
rmdir docs/workflows 2>/dev/null || true
```

- [ ] **Step 4: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add -A docs/
git commit -m "feat(site): add /troubleshooting/ landing; move motor-troubleshooting"
```

---

## Task 12: Create Repository landing page

**Files:**
- Create: `docs/repository/index.md`
- Modify (move): `docs/about/index.md` → `docs/repository/about/index.md` (if /about/ exists)

- [ ] **Step 1: Create repository landing page**

```markdown
---
layout: default
title: "Repository and Project Info"
description: "GitHub repository link, contribution guide, and project metadata for Control System Standards Atlas."
breadcrumb:
  - name: "Repository"
---

<div class="page-header">
  <span class="page-header__label">Repository</span>
  <h1>Repository and Project Info</h1>
</div>

## Links

- **GitHub:** [kyawminthu20/Control-System-Tools](https://github.com/kyawminthu20/Control-System-Tools)
- **About this site:** [/repository/about/](/repository/about/)

## How This Site is Built

- Jekyll static site generator, deployed via GitHub Pages
- Authoritative content in `control-standards/rag/` (RAG corpus)
- Presentation layer in `docs/` (this Jekyll site)
- Per-phase change log under `project_state/change_log.md`
```

- [ ] **Step 2: Move /about/ to /repository/about/**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
mkdir -p docs/repository/about
git mv docs/about/index.md docs/repository/about/index.md
rmdir docs/about 2>/dev/null || true
```

Add `redirect_from:` to the moved file:

```yaml
redirect_from:
  - /about/
  - /about/index.html
```

- [ ] **Step 3: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add -A docs/
git commit -m "feat(site): add /repository/ landing; move /about/"
```

---

## Task 13: Rewrite navigation.yml to 10-group structure

**Files:**
- Rewrite: `docs/_data/navigation.yml`

- [ ] **Step 1: Replace the entire navigation.yml with the new 10-group structure**

Overwrite `docs/_data/navigation.yml` with:

```yaml
- label: "Home"
  url: "/"

- label: "Fundamentals"
  url: "/fundamentals/"
  match_prefixes:
    - "/fundamentals/"
  children:
    - label: "Electrical"
      url: "/fundamentals/electrical/"
    - label: "Control Theory"
      url: "/fundamentals/control/"
    - label: "Motors &amp; Drives"
      url: "/fundamentals/motors/"

- label: "Standards"
  url: "/standards/"
  match_prefixes:
    - "/standards/"
  children:
    - label: "US Electrical"
      url: "/standards/us-electrical/"
      children:
        - label: "NEC"
          url: "/standards/us-electrical/nec/"
        - label: "NFPA 79"
          url: "/standards/us-electrical/nfpa-79/"
        - label: "UL 508A"
          url: "/standards/us-electrical/ul-508a/"
    - label: "Machinery"
      url: "/standards/machinery/"
      children:
        - label: "IEC 60204-1"
          url: "/standards/machinery/iec-60204-1/"
    - label: "Functional Safety"
      url: "/standards/functional-safety/"
      children:
        - label: "IEC 61508"
          url: "/standards/functional-safety/iec-61508/"
        - label: "IEC 61511"
          url: "/standards/functional-safety/iec-61511/"
        - label: "IEC 62061"
          url: "/standards/functional-safety/iec-62061/"
        - label: "ISO 12100"
          url: "/standards/functional-safety/iso-12100/"
        - label: "ISO 13849-1"
          url: "/standards/functional-safety/iso-13849-1/"
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

- label: "Design"
  url: "/design/"
  match_prefixes:
    - "/design/"
  children:
    - label: "Architecture"
      url: "/design/architecture/"
      children:
        - label: "Machine Architecture Model"
          url: "/design/architecture/machine-architecture-model/"
        - label: "Machine Safety Architecture"
          url: "/design/architecture/machine-safety-architecture/"
        - label: "Compliance Stack"
          url: "/design/architecture/compliance-stack/"
    - label: "Motor Selection"
      url: "/design/motor-selection/"
      children:
        - label: "Motor Selection Matrix"
          url: "/design/motor-selection/motor-selection-matrix/"
    - label: "Software Stack"
      url: "/design/software-stack/"
    - label: "Design Workflows"
      url: "/design/workflows/"
      children:
        - label: "Electrical Review"
          url: "/design/workflows/electrical-review/"
        - label: "Motor Selection"
          url: "/design/workflows/motor-selection/"

- label: "Implementation"
  url: "/implementation/"
  match_prefixes:
    - "/implementation/"
  children:
    - label: "Commissioning Templates"
      url: "/implementation/commissioning-templates/"
    - label: "Scenarios"
      url: "/implementation/scenarios/"
    - label: "Servo Commissioning"
      url: "/implementation/servo-commissioning/"
    - label: "VFD Commissioning"
      url: "/implementation/vfd-commissioning/"
    - label: "Build Stage"
      url: "/implementation/lifecycle-build/"
    - label: "Installation"
      url: "/implementation/lifecycle-installation/"
    - label: "Pre-Commissioning"
      url: "/implementation/lifecycle-pre-commissioning/"
    - label: "Commissioning"
      url: "/implementation/lifecycle-commissioning/"

- label: "Verification"
  url: "/verification/"
  match_prefixes:
    - "/verification/"
  children:
    - label: "Risk Assessment"
      url: "/verification/risk-assessment/"
    - label: "Safety Requirements Spec"
      url: "/verification/safety-requirements-spec/"
    - label: "Safety Architecture"
      url: "/verification/safety-architecture/"
    - label: "Safety Wiring"
      url: "/verification/safety-wiring/"
    - label: "Maintenance"
      url: "/verification/maintenance/"
    - label: "Management of Change"
      url: "/verification/management-of-change/"
    - label: "Full Lifecycle Journey"
      url: "/verification/lifecycle/"

- label: "Industries"
  url: "/industries/"
  match_prefixes:
    - "/industries/"
  children:
    - label: "Semiconductor"
      url: "/industries/semiconductor/"
    - label: "Water/Wastewater"
      url: "/industries/water-wastewater/"
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

- label: "Troubleshooting"
  url: "/troubleshooting/"
  match_prefixes:
    - "/troubleshooting/"
  children:
    - label: "Motors"
      url: "/troubleshooting/motors/"

- label: "Training"
  url: "/training/"
  match_prefixes:
    - "/training/"
  children:
    - label: "NEC for Machines and Panels"
      url: "/training/nec-application/"

- label: "Tools"
  url: "/tools/"
  match_prefixes:
    - "/tools/"
  children:
    - label: "RAG Browser"
      url: "/tools/rag-browser/"
    - label: "Glossary"
      url: "/tools/glossary/"
    - label: "Crosswalks"
      url: "/tools/crosswalks/"
    - label: "Reference Hub"
      url: "/tools/reference-hub/"

- label: "Repository"
  url: "/repository/"
  match_prefixes:
    - "/repository/"
  children:
    - label: "About"
      url: "/repository/about/"
```

- [ ] **Step 2: Build and verify sidebar renders**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -10
```

Expected: clean build.

- [ ] **Step 3: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add docs/_data/navigation.yml
git commit -m "refactor(nav): rewrite navigation.yml to 10-group intent-based structure"
```

---

## Task 14: Site-wide cross-link sweep

After per-group moves, pages OUTSIDE the moved groups may still contain links to old URLs. These now 301-redirect via the plugin, but we want direct links.

- [ ] **Step 1: Find all remaining references to old paths**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
grep -rln -E "/training/fundamentals/|/training/control-systems/|/training/electrical-machines/|/engineering-workflow/|/reference/(architecture|motor-systems)/|/software-stack/|/workflows/(electrical-review|motor-selection|servo-commissioning|vfd-commissioning|motor-troubleshooting)/|/commissioning-templates/|/scenarios/|/lifecycle/|/rag-browser/|/glossary/|/crosswalks/|/about/" docs/ | grep -v "_site/"
```

- [ ] **Step 2: For each file listed, update old paths to new paths per the migration map**

Use Edit tool on each flagged file, replacing each old path with the new path from the migration map. Preserve trailing slash and fragment identifiers.

- [ ] **Step 3: Rebuild and run link checker**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
cd ..
python3 tools/check_internal_links.py docs/_site/ 2>&1 | tail -20
```

If broken links remain, fix them in source markdown and re-run.

- [ ] **Step 4: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add -A docs/
git commit -m "refactor(site): sweep — update all internal cross-links to new paths"
```

---

## Task 15: Final link audit — must exit 0

- [ ] **Step 1: Build and run checker**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs"
~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -10
cd ..
python3 tools/check_internal_links.py docs/_site/
echo "exit code: $?"
```

Expected: `OK: no broken internal links ...` and `exit code: 0`.

If NOT zero:
- Read each broken-link line: `SOURCE_PAGE: HREF -> RESOLVED_TARGET`
- Fix in source markdown
- Rebuild and re-run

Loop until the checker passes.

- [ ] **Step 2: Run AI boundary validator — no regression**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
python3 tools/validate_ai_boundaries.py 2>&1 | tail -10
```

Expected: same pre-existing 2 failures from Phase 25 (IEC61511.md, UPW_water_skid_scenario.md). No new failures.

- [ ] **Step 3: Commit only if fixes were made**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add -u docs/
git diff --cached --quiet || git commit -m "fix(links): final audit — resolve remaining broken links"
```

---

## Task 16: Update project_state and change_log

**Files:**
- Modify: `project_state/project_state.md`
- Modify: `project_state/change_log.md`

- [ ] **Step 1: Update `project_state/project_state.md`**

Edit:
- `**Last Updated:**` → `2026-04-14`
- `**Current Phase:**` → `Phase 26 COMPLETE — Navigation Restructure and Link Audit`
- `**Next Phase:**` → `Phase 27 PLANNING — TBD`
- Rewrite `## Current Direction` to note: Phase 26 complete — 10-group intent-based sidebar, physical URL reorganization with `jekyll-redirect-from` stubs, zero broken internal links verified by `tools/check_internal_links.py`.
- Update `## Current Reality` build line to note new URL structure and link checker.

- [ ] **Step 2: Update `project_state/change_log.md`**

Add at the top of `## Change History`:

```markdown
## 2026-04-14 — Phase 26 COMPLETE: Navigation Restructure and Link Audit

**Type:** Site Architecture / UX
**Status:** Complete

- Installed `jekyll-redirect-from` plugin (Gemfile + _config.yml)
- Created `tools/check_internal_links.py` (stdlib-only internal link checker)
- Baseline link audit — fixed pre-existing broken links
- Migrated ~156 Jekyll pages to new 10-group structure per `docs/_data/phase26_migration_map.yml`:
  - `/fundamentals/` (electrical, control, motors)
  - `/standards/` (unchanged)
  - `/design/` (architecture, motor selection, software stack, workflows)
  - `/implementation/` (commissioning templates, scenarios, lifecycle build/install/commissioning stages)
  - `/verification/` (risk assessment, SRS, safety architecture, lifecycle verification stages)
  - `/industries/` (unchanged)
  - `/troubleshooting/` (new section; motor-troubleshooting moved here)
  - `/training/` (trimmed to NEC application only)
  - `/tools/` (RAG browser, glossary, crosswalks, reference hub)
  - `/repository/` (new section; about page moved here)
- Every moved page has `redirect_from:` front matter — old URLs still resolve
- Rewrote `docs/_data/navigation.yml` to 10-group intent-based structure
- Created Troubleshooting and Repository landing pages
- Final link check: zero broken internal links (verified by `check_internal_links.py`)
- Jekyll build: clean
```

- [ ] **Step 3: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add project_state/project_state.md project_state/change_log.md
git commit -m "feat(phase-26): complete navigation restructure — project state update"
```

---

## Self-Review Against Spec

**Spec coverage check:**

| Spec requirement | Covered by task(s) |
|---|---|
| Install `jekyll-redirect-from` | Task 1 |
| Create `tools/check_internal_links.py` | Task 2 |
| Baseline link audit | Task 3 |
| 10-group URL structure | Tasks 5–9, 11, 12 (migrations) + Task 13 (nav) |
| Physical reorganization with redirects | Tasks 5–9, 11, 12 |
| `jekyll-redirect-from` in Gemfile + config | Task 1 |
| Rewrite `navigation.yml` | Task 13 |
| New Troubleshooting landing | Task 11 |
| New Repository landing | Task 12 |
| Migration map as committed reference | Task 4 |
| Update all internal cross-links | Tasks 5–9 (within-group), 14 (site-wide sweep) |
| Final link audit exits 0 | Task 15 |
| Clean Jekyll build | Tasks 1, 5–15 (verified each step) |
| project_state + change_log update | Task 16 |

No gaps found.

**Placeholder scan:** No TBDs, no "similar to", no placeholder comments.

**Type consistency:** Migration map structure is consistent across all usages. `redirect_from:` syntax is consistent per Jekyll plugin docs. Navigation.yml structure follows existing schema.
