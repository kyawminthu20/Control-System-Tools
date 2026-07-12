---
layout: default
title: "PLC Software"
description: "Programming industrial controllers — IEC 61131-3 languages, ladder logic, program structure, state machines, application algorithms, PackML/ISA-88/ISA-95, vendor architectures, and safety application patterns."
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
    <h3><a href="{{ '/fundamentals/plc-software/ladder-logic/' | relative_url }}">Ladder Logic</a></h3>
    <p>Contacts, coils, seal-ins, one-shots, scan order, and the discipline — I/O mapping, command vs feedback, alarm hysteresis — that keeps ladder maintainable.</p>
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
    <h3><a href="{{ '/fundamentals/plc-software/algorithms-equipment-staging/' | relative_url }}">Algorithms &amp; Equipment Staging</a></h3>
    <p>FIFOs, queues, shift registers, and the staging family — lead-lag, runtime equalization, demand staging, load shedding — for multi-unit equipment.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/fundamentals/plc-software/packml-isa88-isa95/' | relative_url }}">PackML, ISA-88 &amp; ISA-95</a></h3>
    <p>The standard state, procedural, and enterprise-integration models — and how they wrap, not replace, the machine's own sequence.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/fundamentals/plc-software/vendor-architectures/' | relative_url }}">Vendor Architectures</a></h3>
    <p>How Siemens OB/FB/DB, Rockwell tags and AOIs, and Beckhoff TwinCAT each implement the shared IEC 61131-3 model — a translation guide.</p>
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
