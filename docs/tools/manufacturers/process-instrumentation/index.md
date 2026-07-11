---
layout: default
title: "Process Instrumentation Manufacturers"
description: "Pressure, temperature, flow, level, and analytical measurement manufacturers."
breadcrumb:
  - name: "Tools"
    url: "/tools/"
  - name: "Manufacturers"
    url: "/tools/manufacturers/"
  - name: "Instrumentation"
review:
  standard: "— (directory; market information changes continuously)"
  edition: "—"
  status: "Partial coverage"
  coverage: "Major and notable vendors only; deliberately not exhaustive"
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Manufacturer Directory</span>
  <h1>Process Instrumentation Manufacturers</h1>
  <p>Pressure, temperature, flow, level, and analytical measurement manufacturers.</p>
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
    {% for m in site.data.manufacturers.process_instrumentation %}
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

Selection notes specific to instrumentation:

- Select by **measurement problem first** (fluid, range, accuracy, process
  connection, hygienic/hazardous requirements), then by vendor.
- Hazardous-area installations need certificates matched to the area
  classification — see [IEC 60079]({{ '/standards/hazardous-area/iec-60079/' | relative_url }}).
- Check **calibration and spares logistics** locally; a superior instrument
  with no local calibration support is a liability.
- The `notes` column shows which measurement types each vendor is listed
  under in this directory.
