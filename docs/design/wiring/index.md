---
layout: default
title: "Wiring & Installation Guides"
description: "Device-by-device wiring guides — sizing, protection, grounding, and noise mitigation with the standards cited: VFDs, PLCs, remote I/O, analog signals, encoders, servo drives, and communication cabling."
breadcrumb:
  - name: "Design"
    url: "/design/"
  - name: "Wiring & Installation"
repo_path: "control-standards/rag/design_framework/wiring_practices/"
---

<div class="page-header">
  <span class="page-header__label">Wiring &amp; Installation</span>
  <h1>Wiring &amp; Installation Guides</h1>
  <p>How devices actually get wired — conductor sizing, protection, grounding, shielding, and noise mitigation, device by device, with the governing standards cited and the field lessons included.</p>
</div>

> **Safety.** These guides are educational references, not work instructions.
> Electrical work is performed de-energized and verified by qualified
> personnel under your site's LOTO procedures, following the device
> manufacturer's manual and the authority having jurisdiction.

Every guide follows the same structure: what you're wiring → what you need
before starting → sizing &amp; protection (with
[toolkit]({{ '/tools/engineering-toolkit/' | relative_url }}) support) →
power wiring → control/signal wiring → grounding &amp; EMC → common
mistakes → verification checks → standards references.

## Foundations

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/design/wiring/vfd/' | relative_url }}">How to Wire a VFD</a></h3>
    <p>Line side, load side, motor cable and shielding, reflected wave, braking, control I/O — the flagship guide.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/design/wiring/wire-sizing/' | relative_url }}">Wire Sizing Walkthrough</a></h3>
    <p>From nameplate to conductor, OCPD, and overload — one worked chain, computed with the cst toolkit and cited to the NEC.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/design/wiring/grounding-bonding/' | relative_url }}">Panel Grounding &amp; Bonding</a></h3>
    <p>The three jobs people conflate — fault return, equipotential bonding, and functional grounding — and the practice for each.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/design/wiring/emc-noise-mitigation/' | relative_url }}">Noise &amp; EMC Mitigation</a></h3>
    <p>Separation classes, source suppression, shield policy, and panel-level EMC practice — separate first, shield second, filter third.</p>
  </div>
</div>

## Planned Guides

The program covers the full device set — added wave by wave (roadmap in the
repo's `governance/ROADMAP.md`):

| Wave | Devices |
|---|---|
| Controllers &amp; I/O | PLC wiring · Remote I/O stations · Industrial PCs (IPCs) · 4–20 mA current loops · 0–10 V signals |
| Motion &amp; feedback | Servo drives (power, feedback, STO, brake) · Encoders (differential vs single-ended, cable practice) |
| Infrastructure &amp; safety | Communication cable installation · Safety circuit wiring · Motor starters · Control power distribution · RTD &amp; thermocouple wiring |

## Related

- [Engineering toolkit]({{ '/tools/engineering-toolkit/' | relative_url }}) — the sizing calculators these guides use
- [Templates]({{ '/tools/templates/' | relative_url }}) — wire schedules, loop sheets, checklists
- [Communications physical layer]({{ '/communications/' | relative_url }}) — copper, fiber, RS-485 installation practice
- [Lifecycle commissioning guides]({{ '/lifecycle/guides/commissioning-templates/' | relative_url }})
