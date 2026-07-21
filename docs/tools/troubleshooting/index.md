---
layout: default
title: "Troubleshooting"
description: "Field troubleshooting entry point organized by symptom category — motors, VFDs, PLC systems, field I/O, networks, and safety circuits."
breadcrumb:
  - name: "Troubleshooting"
redirect_from:
  - /troubleshooting/
review:
  standard: "Field troubleshooting practice — symptom-driven diagnostic trees"
  edition: "n/a — practice reference"
  status: "Review pending"
  coverage: "Troubleshooting tree index; OEM documentation and site safety procedures govern any intervention."
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Troubleshooting</span>
  <h1>Troubleshooting</h1>
  <p>Entry point for field troubleshooting. Start from the symptom category and follow the linked workflow, reference, or commissioning template.</p>
</div>

<blockquote>
<strong>Scope:</strong> Routing page for field diagnosis. It is not an OEM fault manual or an SOP — it points at the right workflow, reference, or commissioning template for the symptom in front of you.
</blockquote>

## Decision Trees by Symptom

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/tools/troubleshooting/vfd-faults/' | relative_url }}">VFD Faults</a></h3>
    <p>Overvoltage, overcurrent, overtemp, ground fault, and "faults but I don't know why" — by fault category, routed to the wiring guides.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/tools/troubleshooting/motor-wont-start/' | relative_url }}">Motor Won't Start</a></h3>
    <p>Does the contactor pull in? Branch from there into control-circuit vs power-side vs mechanical causes.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/tools/troubleshooting/analog-signal-faults/' | relative_url }}">Analog Signal Faults</a></h3>
    <p>4–20 mA and 0–10 V reading zero, full-scale, noisy, or offset — bisect the loop to find where it breaks.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/tools/troubleshooting/comms-dropouts/' | relative_url }}">Communication Dropouts</a></h3>
    <p>Total vs intermittent, one device vs a segment — triage that routes into the Communications diagnostics workflow.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/tools/troubleshooting/motors/' | relative_url }}">Motor Symptoms</a></h3>
    <p>General motor symptom decision tree — noise, heat, vibration, and performance patterns.</p>
  </div>
</div>

## Other Starting Points

| Category | Where to start |
|---|---|
| PLC systems | [Async faults in distributed systems]({{ '/fundamentals/control/async-faults-distributed-systems/' | relative_url }}) · [Machine state model]({{ '/fundamentals/control/machine-state-model/' | relative_url }}) |
| Safety circuits | [Safety circuit wiring]({{ '/design/wiring/safety-circuit/' | relative_url }}) · [Interlocks and permissives]({{ '/fundamentals/control/interlocks-permissives-safety-trips/' | relative_url }}) |
| Wiring practice | [Wiring &amp; installation guides]({{ '/design/wiring/' | relative_url }}) — the underlying wiring for every symptom above |

## How to use this section

1. Confirm the machine is safe to inspect and test before anything else.
2. Identify the dominant symptom category from the table above.
3. Open the linked workflow or reference and follow it end-to-end — do not skip the "practical sequence" steps even when the fault seems obvious.
4. Record what was checked, what the measurements were, and what was changed. The [commissioning templates]({{ '/lifecycle/guides/commissioning-templates/' | relative_url }}) contain checklist formats that double as field-notebook templates.

## Related Sections

- **Fundamentals** — [Electrical]({{ '/fundamentals/electrical/' | relative_url }}) · [Control Systems]({{ '/fundamentals/control/' | relative_url }}) · [Motors and Drives]({{ '/fundamentals/motors/' | relative_url }})
- **Implementation** — [Commissioning templates]({{ '/lifecycle/guides/commissioning-templates/' | relative_url }}) · [Scenarios]({{ '/tools/scenarios/' | relative_url }})
- **Verification** — [Safety wiring]({{ '/lifecycle/safety-wiring/' | relative_url }}) · [Management of change]({{ '/lifecycle/management-of-change/' | relative_url }})
- **Tools** — [Glossary]({{ '/tools/glossary/' | relative_url }}) · [RAG file browser]({{ '/tools/rag-browser/' | relative_url }})
