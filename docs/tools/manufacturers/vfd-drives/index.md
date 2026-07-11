---
layout: default
title: "Variable Frequency Drive Manufacturers"
description: "Low-voltage variable frequency drive families from the major manufacturers."
breadcrumb:
  - name: "Tools"
    url: "/tools/"
  - name: "Manufacturers"
    url: "/tools/manufacturers/"
  - name: "VFDs"
review:
  standard: "— (directory; market information changes continuously)"
  edition: "—"
  status: "Partial coverage"
  coverage: "Major and notable vendors only; deliberately not exhaustive"
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Manufacturer Directory</span>
  <h1>Variable Frequency Drive Manufacturers</h1>
  <p>Low-voltage variable frequency drive families from the major manufacturers.</p>
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
    {% for m in site.data.manufacturers.vfd %}
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

Selection notes specific to VFDs:

- Match the drive to the **motor and application first** (torque profile,
  overload class, braking needs) — see the
  [motor selection workflow]({{ '/design/workflows/motor-selection/' | relative_url }}).
- **Network option cards** vary by family; confirm the exact protocol/card
  combination, not just the brand.
- Harmonics, EMC filtering, and cable-length limits are family-specific —
  check the application guide for the actual model.
- Commissioning guidance lives at
  [VFD commissioning]({{ '/lifecycle/guides/vfd-commissioning/' | relative_url }}).
