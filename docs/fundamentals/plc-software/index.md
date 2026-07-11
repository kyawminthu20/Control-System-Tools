---
layout: default
title: "PLC Software"
description: "Programming industrial controllers — IEC 61131-3 languages, program structure, state machines, and safety application patterns."
breadcrumb:
  - name: "Fundamentals"
    url: "/fundamentals/"
  - name: "PLC Software"
related_standards:
  - name: "IEC 61131-3"
    url: "/standards/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
---

<div class="page-header">
  <span class="page-header__label">PLC Software</span>
  <h1>PLC Software &amp; IEC 61131-3</h1>
  <p>How industrial controllers are programmed — the standard languages, how to structure a program, state-machine design, and where safety application software fits.</p>
</div>

Programming practice is where a good electrical design either comes to life or
becomes unmaintainable. These pages cover the vendor-neutral model defined by
**IEC 61131-3** and the structuring practices that survive commissioning and
the next engineer — implementations diverge, so always consult your platform's
documentation.

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/fundamentals/plc-software/languages-overview/' | relative_url }}">Languages Overview</a></h3>
    <p>The five IEC 61131-3 languages — LD, FBD, ST, SFC, IL — and when each is the right tool.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/fundamentals/plc-software/program-structure/' | relative_url }}">Program Structure</a></h3>
    <p>POUs, tasks, variable scope, and modular reusable design — structuring for maintainability.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/fundamentals/plc-software/state-machines/' | relative_url }}">State Machines</a></h3>
    <p>Why explicit state machines beat sprawling ad-hoc logic, and three ways to implement them.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/fundamentals/plc-software/safety-application-patterns/' | relative_url }}">Safety Application Patterns</a></h3>
    <p>Safety-rated controllers, certified function blocks, and keeping the safety application separate and traceable.</p>
  </div>
</div>

## Related

- [Engineering toolkit]({{ '/tools/engineering-toolkit/' | relative_url }}) — tag database and IEC 61131-3 identifier rules
- [Wiring &amp; installation guides]({{ '/design/wiring/' | relative_url }}) — the hardware the software drives
- [Functional safety standards]({{ '/standards/functional-safety/' | relative_url }})
