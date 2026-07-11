---
layout: default
title: "Servo & Motion Control Manufacturers"
description: "Servo drive/motor families and CNC / machine-tool motion platforms."
breadcrumb:
  - name: "Tools"
    url: "/tools/"
  - name: "Manufacturers"
    url: "/tools/manufacturers/"
  - name: "Servo / Motion"
review:
  standard: "— (directory; market information changes continuously)"
  edition: "—"
  status: "Partial coverage"
  coverage: "Major and notable vendors only; deliberately not exhaustive"
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Manufacturer Directory</span>
  <h1>Servo & Motion Control Manufacturers</h1>
  <p>Servo drive/motor families and CNC / machine-tool motion platforms.</p>
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
    {% for m in site.data.manufacturers.servo_motion %}
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

Selection notes specific to motion:

- **Controller-drive pairing dominates**: most platforms perform best (or
  only work fully) with their own motion controller and network
  (e.g. deterministic Ethernet variants).
- Registration, camming, and gearing features differ sharply between
  families — list the required motion functions before comparing.
- Encoder/feedback compatibility and cable systems are proprietary more
  often than not; budget accordingly.
- Commissioning guidance lives at
  [servo commissioning]({{ '/lifecycle/guides/servo-commissioning/' | relative_url }}).
