---
layout: default
title: "SCADA & HMI Software"
description: "Widely deployed supervisory control and visualization platforms — commercial and open source."
breadcrumb:
  - name: "Tools"
    url: "/tools/"
  - name: "Manufacturers"
    url: "/tools/manufacturers/"
  - name: "SCADA / HMI"
review:
  standard: "— (directory; market information changes continuously)"
  edition: "—"
  status: "Partial coverage"
  coverage: "Major and notable vendors only; deliberately not exhaustive"
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Manufacturer Directory</span>
  <h1>SCADA & HMI Software</h1>
  <p>Widely deployed supervisory control and visualization platforms — commercial and open source.</p>
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
    {% for m in site.data.manufacturers.scada_hmi %}
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

Selection notes specific to SCADA/HMI:

- **Licensing model** (per-tag, per-client, per-server, unlimited) often
  decides total cost more than the license price itself.
- Driver/connector coverage for your exact device mix beats feature lists.
- **Open-source platforms** require your own answer for support, cybersecurity
  patching, validation, redundancy, and long-term maintenance before
  industrial use.
- Pair any SCADA decision with an
  [IEC 62443]({{ '/standards/cybersecurity/iec-62443/' | relative_url }})
  zone/conduit review — the SCADA layer is the classic IT/OT boundary.
