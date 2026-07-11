---
layout: default
title: "PLC / PAC & Safety Controller Manufacturers"
description: "Programmable logic and automation controllers, including the safety-controller specialists."
breadcrumb:
  - name: "Tools"
    url: "/tools/"
  - name: "Manufacturers"
    url: "/tools/manufacturers/"
  - name: "PLC / PAC"
review:
  standard: "— (directory; market information changes continuously)"
  edition: "—"
  status: "Partial coverage"
  coverage: "Major and notable vendors only; deliberately not exhaustive"
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Manufacturer Directory</span>
  <h1>PLC / PAC & Safety Controller Manufacturers</h1>
  <p>Programmable logic and automation controllers, including the safety-controller specialists.</p>
</div>

> Curated list of major and notable vendors — absence means nothing, and
> inclusion is not endorsement. Ownership, branding, and availability change;
> confirm with the manufacturer. See the
> [directory notice]({{ '/tools/manufacturers/' | relative_url }}).

## Vendors

<div style="overflow-x:auto;">
<table>
  <thead>
    <tr><th>Manufacturer</th><th>Region</th><th>Notable families</th><th>Typical protocols</th><th>Notes</th></tr>
  </thead>
  <tbody>
    {% for m in site.data.manufacturers.plc_pac %}
    <tr>
      <td>{{ m.name }}</td>
      <td>{{ m.region }}</td>
      <td>{{ m.families }}</td>
      <td>{{ m.protocols }}</td>
      <td>{{ m.notes }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
</div>

## Selection Notes

Selection notes specific to controllers:

- **Ecosystem lock-in is real.** The controller choice usually decides the
  engineering software, HMI pairing, preferred network, and the skill set you
  hire for. Weigh the ecosystem, not the CPU datasheet.
- **Safety-rated variants** (e.g. safety PLCs) need certification evidence for
  the claimed PL/SIL — see [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }})
  and [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}).
- **Lifecycle status matters more than features** — controllers live 15–25
  years in service; check the vendor's active/mature/end-of-life designation.
