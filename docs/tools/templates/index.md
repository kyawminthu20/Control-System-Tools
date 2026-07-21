---
layout: default
title: "Engineering Templates"
description: "Downloadable original templates for controls work — design basis, SRS, I/O list, wire schedule, loop sheets, FAT protocol, MOC form, and more."
breadcrumb:
  - name: "Tools"
    url: "/tools/"
  - name: "Templates"
related_standards:
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
review:
  standard: "Original engineering templates (project content)"
  edition: "n/a — original templates"
  status: "Review pending"
  coverage: "Downloadable original templates; adapt to the project and governing editions before use."
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Engineering Tools</span>
  <h1>Engineering Templates</h1>
  <p>Original, reusable starting points for controls work. Every template is an example — adapt it to your project, standards, and organization before use.</p>
</div>

> **These are examples, not deliverables.** Each template needs
> project-specific review before use. None reproduce standards text or
> table values. Files marked *generated* are produced by the
> [Python toolkit]({{ '/tools/engineering-toolkit/' | relative_url }}) from a
> worked example I/O list — regenerate them from your own list to get real
> project documents instead of blank forms.

## What a Design Package Actually Contains

Before the templates, the shape of the thing they add up to. This is one worked
example — a pump and VFD control skid — carried through every document a
controls package normally produces, so you can see how they reference each
other rather than meeting them one blank form at a time.

<div class="diagram-card">
  <a href="{{ '/assets/images/design-package/control-system-design-package-example.png' | relative_url }}">
    <img src="{{ '/assets/images/design-package/control-system-design-package-example.png' | relative_url }}"
         alt="Control system design package example for a pump and VFD control skid, showing ten linked deliverables: a process and instrumentation diagram with tank, pump P-101, control valve and instruments LT-101, PT-101, FT-101; a network architecture diagram with engineering workstation, HMI, SCADA client, managed Ethernet switch, PLC, VFD and remote I/O; an electrical single line diagram from a 3-phase 480 VAC supply through a main disconnect and MCCB to the VFD, control power supply and panel heater; an I/O list mapping each tag to I/O type, signal type and PLC address; a cause and effect matrix mapping conditions such as high-high level and VFD fault to actions such as stop and trip; a panel layout drawing with dimensions; a written control sequence; PLC ladder logic showing a start/stop seal-in rung with permissives and a scale-and-move block for the speed reference; an HMI screen mockup; and a typical 4-20 mA instrument hookup detail."
         loading="lazy">
  </a>
  <figcaption>
    <strong>Example design package — pump &amp; VFD control skid.</strong>
    Ten deliverables that reference one another: the P&amp;ID names the tags, the
    I/O list addresses them, the cause &amp; effect matrix defines what they do,
    the ladder implements it, and the panel layout houses it. Click to enlarge.
    <br><br>
    <em>Products and part numbers shown are examples only</em> — they illustrate
    a typical architecture and are not a recommendation, endorsement, or
    statement of compatibility. Substitute your own vendor selections.
  </figcaption>
</div>

## Design

| Template | Format | Origin |
|---|---|---|
| [Controls design basis]({{ '/assets/templates/controls_design_basis.md' | relative_url }}) | Markdown | Original template |
| [Standards applicability register]({{ '/assets/templates/standards_applicability_register.csv' | relative_url }}) | CSV | Original template |
| [I/O list]({{ '/assets/templates/io_list_example.csv' | relative_url }}) | CSV | Worked example (toolkit input format) |
| [Instrument index]({{ '/assets/templates/instrument_index.csv' | relative_url }}) | CSV | Original template |
| [Control narrative]({{ '/assets/templates/control_narrative.md' | relative_url }}) | Markdown | Original template |
| [Cause &amp; effect matrix]({{ '/assets/templates/cause_and_effect_matrix.csv' | relative_url }}) | CSV | Original template |
| [Bill of materials]({{ '/assets/templates/bom_example.csv' | relative_url }}) | CSV | *Generated* from the example I/O list |
| [Wire / terminal schedule]({{ '/assets/templates/wire_schedule_example.csv' | relative_url }}) | CSV | *Generated* from the example I/O list |
| [Legend plate list]({{ '/assets/templates/legend_plates_example.csv' | relative_url }}) | CSV | *Generated* from the example I/O list |

## Safety and Compliance

| Template | Format | Origin |
|---|---|---|
| [Safety requirements specification (SRS)]({{ '/assets/templates/safety_requirements_spec.md' | relative_url }}) | Markdown | Original template |
| [Electrical drawing review checklist]({{ '/assets/templates/electrical_drawing_review_checklist.md' | relative_url }}) | Markdown | Original template |
| [Alarm rationalization sheet]({{ '/assets/templates/alarm_rationalization.csv' | relative_url }}) | CSV | Original template |
| [Management of change form]({{ '/assets/templates/management_of_change_form.md' | relative_url }}) | Markdown | Original template |
| [Cybersecurity asset inventory]({{ '/assets/templates/cybersecurity_asset_inventory.csv' | relative_url }}) | CSV | Original template (IEC 62443-2-1 aligned columns) |

## Commissioning

| Template | Format | Origin |
|---|---|---|
| [Loop test sheet]({{ '/assets/templates/loop_sheet_example.md' | relative_url }}) | Markdown | *Generated* — one per I/O point from your list |
| [FAT protocol]({{ '/assets/templates/fat_protocol_example.md' | relative_url }}) | Markdown | *Generated* from the example I/O list |
| [Commissioning punch list]({{ '/assets/templates/commissioning_punch_list.csv' | relative_url }}) | CSV | Original template |
| [Test instrument record]({{ '/assets/templates/test_instrument_record.csv' | relative_url }}) | CSV | Original template |

## Communications & Networks

| Template | Format | Origin |
|---|---|---|
| [IP address register]({{ '/assets/templates/ip_address_register.csv' | relative_url }}) | CSV | Original template |
| [Switch port schedule]({{ '/assets/templates/switch_port_schedule.csv' | relative_url }}) | CSV | Original template |
| [VLAN register]({{ '/assets/templates/vlan_register.csv' | relative_url }}) | CSV | Original template |
| [Firewall communication matrix]({{ '/assets/templates/firewall_comm_matrix.csv' | relative_url }}) | CSV | Original template |
| [Device & firmware inventory]({{ '/assets/templates/device_firmware_inventory.csv' | relative_url }}) | CSV | Original template |
| [Baseline capture log]({{ '/assets/templates/network_baseline_capture_log.csv' | relative_url }}) | CSV | Original template |

These pair with the [Industrial Communications]({{ '/communications/' | relative_url }})
section — the capture log in particular supports the
[baseline-comparison step]({{ '/communications/wireshark-methodology/' | relative_url }})
of the diagnostics methodology.

## AI & Model Lifecycle

| Template | Format | Origin |
|---|---|---|
| [AI / model evidence ledger]({{ '/assets/templates/ai_model_evidence_ledger.md' | relative_url }}) | Markdown | Original template (NIST AI RMF Govern/Map/Measure/Manage aligned) |
| [Twin data-contract schema]({{ '/assets/templates/twin_data_contract.schema.json' | relative_url }}) | JSON Schema | *Generated* — draft 2020-12, from the same field definitions `cst twin-validate` enforces |
| [Twin payload example]({{ '/assets/templates/twin_payload_example.json' | relative_url }}) | JSON | *Generated* — a worked advisory payload that satisfies the schema |

Pairs with [Validation &amp; Lifecycle]({{ '/design/ai-integration/validation-lifecycle/' | relative_url }})
in the AI &amp; ML Integration section — one ledger per learned component, kept from design time through
retirement. It structures the evidence behind a model's allowed authority; it does not grant authority.

The twin schema and payload pair with [The Digital Twin]({{ '/design/ai-integration/digital-twin/' | relative_url }}):
they define what a payload must carry for a non-learned gate to be *able* to judge it — identity,
both timestamps, model and calibration provenance, a freshness bound, and the requested authority level.
Being schema-valid means a proposal is well-formed enough to evaluate; it is never a safety verdict, and
the ceiling it is judged against comes from the method register, not from the payload's own claim.

## Documentation

| Template | Format | Origin |
|---|---|---|
| [Design package]({{ '/assets/templates/design_package_example.md' | relative_url }}) | Markdown | *Generated* — I/O summary + BOM + wire schedule + cited calculations in one document |

## Generating These From Your Own I/O List

The *generated* files above come from one command each. With the
[toolkit]({{ '/tools/engineering-toolkit/' | relative_url }}) installed:

```bash
cst bom your_io_list.csv                      # bill of materials
cst wire-schedule your_io_list.csv            # wire/terminal schedule
cst loop-sheets your_io_list.csv --out-dir loops/
cst fat your_io_list.csv --panel CP-01
cst design-package your_io_list.csv --project "Your Project"
```
