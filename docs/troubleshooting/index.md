---
layout: default
title: "Troubleshooting"
description: "Field troubleshooting entry point organized by symptom category — motors, VFDs, PLC systems, field I/O, networks, and safety circuits."
breadcrumb:
  - name: "Troubleshooting"
---

<div class="page-header">
  <span class="page-header__label">Troubleshooting</span>
  <h1>Troubleshooting</h1>
  <p>Entry point for field troubleshooting. Start from the symptom category and follow the linked workflow, reference, or commissioning template.</p>
</div>

<blockquote>
<strong>Scope:</strong> Routing page for field diagnosis. It is not an OEM fault manual or an SOP — it points at the right workflow, reference, or commissioning template for the symptom in front of you.
</blockquote>

## Categories

| Category | Where to start |
|---|---|
| Motors | [Motor troubleshooting decision tree]({{ '/troubleshooting/motors/' | relative_url }}) · [Motor symptom patterns — RAG browser]({{ '/tools/rag-browser/' | relative_url }}) |
| VFDs | [VFD commissioning — common faults]({{ '/implementation/vfd-commissioning/' | relative_url }}) · [Drive commissioning template]({{ '/implementation/commissioning-templates/drive-commissioning/' | relative_url }}) |
| PLC systems | [Async faults in distributed systems]({{ '/fundamentals/control/async-faults-distributed-systems/' | relative_url }}) · [Machine state model]({{ '/fundamentals/control/machine-state-model/' | relative_url }}) |
| Field I/O | [Electrical quantities reference]({{ '/fundamentals/electrical/electrical-quantities/' | relative_url }}) · [Basic circuit polarity template]({{ '/implementation/commissioning-templates/basic-circuit-polarity/' | relative_url }}) |
| Networks | [Networked safety PLC scenario]({{ '/implementation/scenarios/networked-safety-plc/' | relative_url }}) · [IEC 62443 cybersecurity]({{ '/standards/cybersecurity/iec-62443/' | relative_url }}) |
| Safety circuits | [Safety wiring]({{ '/verification/safety-wiring/' | relative_url }}) · [Interlocks and permissives]({{ '/fundamentals/control/interlocks-permissives-safety-trips/' | relative_url }}) |

## How to use this section

1. Confirm the machine is safe to inspect and test before anything else.
2. Identify the dominant symptom category from the table above.
3. Open the linked workflow or reference and follow it end-to-end — do not skip the "practical sequence" steps even when the fault seems obvious.
4. Record what was checked, what the measurements were, and what was changed. The [commissioning templates]({{ '/implementation/commissioning-templates/' | relative_url }}) contain checklist formats that double as field-notebook templates.

## Related Sections

- **Fundamentals** — [Electrical]({{ '/fundamentals/electrical/' | relative_url }}) · [Control Systems]({{ '/fundamentals/control/' | relative_url }}) · [Motors and Drives]({{ '/fundamentals/motors/' | relative_url }})
- **Implementation** — [Commissioning templates]({{ '/implementation/commissioning-templates/' | relative_url }}) · [Scenarios]({{ '/implementation/scenarios/' | relative_url }})
- **Verification** — [Safety wiring]({{ '/verification/safety-wiring/' | relative_url }}) · [Management of change]({{ '/verification/management-of-change/' | relative_url }})
- **Tools** — [Glossary]({{ '/tools/glossary/' | relative_url }}) · [RAG file browser]({{ '/tools/rag-browser/' | relative_url }})

---

{% include trust-boundary.html %}
