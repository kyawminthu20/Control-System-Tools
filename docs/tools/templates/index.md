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
