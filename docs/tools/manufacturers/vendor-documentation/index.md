---
layout: default
title: "Official Vendor Documentation Index — PLC & IPC"
description: "A curated index of official Siemens, Allen-Bradley/Rockwell, and Beckhoff documentation — master portals, programming and system manuals, I/O references, and the exact-model lookup method that gets you the current revision."
breadcrumb:
  - name: "Tools"
    url: "/tools/"
  - name: "Manufacturers"
    url: "/tools/manufacturers/"
  - name: "Vendor Documentation"
repo_path: "docs/_data/manufacturers/vendor_doc_links.yml"
review:
  standard: "— (vendor documentation index; publications and revisions change continuously)"
  edition: "Link set as curated July 2026; liveness-checked 2026-07-12"
  status: "Review pending"
  coverage: "129 curated official-documentation links plus 8 master portals for three vendors (Siemens, Allen-Bradley/Rockwell, Beckhoff) — deliberately not exhaustive; always confirm the current revision at the vendor portal."
  last_reviewed: "July 2026"
related_standards:
  - name: "PLC / IPC hardware families"
    url: "/tools/manufacturers/plc-hardware-families/"
  - name: "Vendor programming architectures"
    url: "/fundamentals/plc-software/vendor-architectures/"
---

<div class="page-header">
  <span class="page-header__label">Manufacturer Directory</span>
  <h1>Official Vendor Documentation Index — PLC &amp; IPC</h1>
  <p>The official manuals, portals, and publication numbers for Siemens, Allen-Bradley/Rockwell, and Beckhoff controllers, I/O, and industrial PCs — and the lookup method that gets you the <em>current</em> revision, not a stale PDF.</p>
</div>

> **Scope.** This index points at **official vendor documentation only** — no
> third-party tutorials, no mirrors. It covers the major current controller
> families of three vendors; a literal list of every CPU, I/O module, and IPC
> order number would run to thousands of documents, so the index gets you to
> the right manual or portal and the portal gets you the exact document for
> your catalog number. Publication revisions change continuously: every link
> was checked alive in July 2026, but treat the **publication ID** as the
> stable reference and re-search it at the vendor portal when a link moves.
> Inclusion is not endorsement — see the
> [directory notice]({{ '/tools/manufacturers/' | relative_url }}).

## How to find the exact document for your hardware

The manuals below are family-level. Exact terminal diagrams, connector pinouts,
and technical data normally depend on the **complete catalog or order number**,
so the reliable method is:

1. **Record the exact catalog/order number and series** from the nameplate or
   the order documentation (Siemens MLFB, Rockwell catalog number, Beckhoff
   order number).
2. **Search the vendor's own portal** with that number — not a web search.
3. **Open the current user/system manual, installation instructions, and
   technical data** for that exact article.
4. **Check firmware/software compatibility** between the hardware revision and
   your engineering-tool version.
5. **Archive the revision you designed against** — the portal will serve a
   newer revision next year, and your as-built documentation should name the
   one you actually used.

Where each vendor keeps the wiring-level detail:

- **Siemens** — search the MLFB/order number in SiePortal; the CPU and I/O
  *equipment manuals* carry terminal assignments and connection diagrams.
- **Allen-Bradley / Rockwell** — search the catalog number or publication ID in
  the Literature Library; *installation instructions* normally contain the
  wiring diagrams.
- **Beckhoff** — search the order number in the Download Finder or product
  page; the *Information System* carries model-specific connectors, pin
  assignments, and terminal wiring.

> **Safety documentation.** Do not design a safety function from a general
> product manual alone. Use the complete safety manual set for the exact
> certified hardware revision, validated safety libraries, and the applicable
> standards — see [safety application patterns]({{ '/fundamentals/plc-software/safety-application-patterns/' | relative_url }})
> and [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}).

## Master portals

Start here when you have an exact model number.

<div style="overflow-x:auto;">
<table>
  <thead>
    <tr><th>Brand</th><th>Portal</th><th>Best use</th></tr>
  </thead>
  <tbody>
    {% for p in site.data.manufacturers.vendor_doc_links.portals %}
    <tr>
      <td>{{ p.brand }}</td>
      <td><a href="{{ p.url }}" rel="noopener">{{ p.portal }}</a></td>
      <td>{{ p.use }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
</div>

## Siemens — SIMATIC controllers, I/O, and IPCs

LOGO!, S7-1200 and S7-1200 G2, S7-1500 (standard, safety, motion, redundant),
ET 200 distributed I/O, software controllers, and SIMATIC industrial PCs.

<div style="overflow-x:auto;">
<table>
  <thead>
    <tr><th>Family</th><th>Document</th><th>Type</th><th>Pub. / ID</th><th>Covers</th><th>Notes</th></tr>
  </thead>
  <tbody>
    {% for e in site.data.manufacturers.vendor_doc_links.siemens %}
    <tr>
      <td>{{ e.family }}</td>
      <td><a href="{{ e.url }}" rel="noopener">{{ e.title }}</a></td>
      <td>{{ e.doc_type }}</td>
      <td>{{ e.pub_id }}</td>
      <td>{{ e.coverage }}</td>
      <td>{{ e.notes }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
</div>

## Allen-Bradley / Rockwell — Logix controllers, I/O, and industrial computers

Micro800, CompactLogix and Compact GuardLogix, ControlLogix and GuardLogix,
distributed I/O, the Logix 5000 programming-manual set, and ASEM industrial
computers.

<div style="overflow-x:auto;">
<table>
  <thead>
    <tr><th>Family</th><th>Document</th><th>Type</th><th>Pub. / ID</th><th>Covers</th><th>Notes</th></tr>
  </thead>
  <tbody>
    {% for e in site.data.manufacturers.vendor_doc_links.allen_bradley %}
    <tr>
      <td>{{ e.family }}</td>
      <td><a href="{{ e.url }}" rel="noopener">{{ e.title }}</a></td>
      <td>{{ e.doc_type }}</td>
      <td>{{ e.pub_id }}</td>
      <td>{{ e.coverage }}</td>
      <td>{{ e.notes }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
</div>

## Beckhoff — TwinCAT, EtherCAT, embedded and industrial PCs

TwinCAT 3 programming and libraries, EtherCAT system documentation and
terminals, CX embedded PCs, and C-series / CP-series industrial and panel PCs.

<div style="overflow-x:auto;">
<table>
  <thead>
    <tr><th>Family</th><th>Document</th><th>Type</th><th>Pub. / ID</th><th>Covers</th><th>Notes</th></tr>
  </thead>
  <tbody>
    {% for e in site.data.manufacturers.vendor_doc_links.beckhoff %}
    <tr>
      <td>{{ e.family }}</td>
      <td><a href="{{ e.url }}" rel="noopener">{{ e.title }}</a></td>
      <td>{{ e.doc_type }}</td>
      <td>{{ e.pub_id }}</td>
      <td>{{ e.coverage }}</td>
      <td>{{ e.notes }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
</div>

## Related Pages

- [PLC &amp; IPC hardware families]({{ '/tools/manufacturers/plc-hardware-families/' | relative_url }}) — what these families are and how to choose between them
- [Vendor programming architectures]({{ '/fundamentals/plc-software/vendor-architectures/' | relative_url }}) — the software side of the same three ecosystems
- [PLC / PAC manufacturer directory]({{ '/tools/manufacturers/plc-pac/' | relative_url }}) — the broader vendor landscape
- [PLC wiring guide]({{ '/design/wiring/plc/' | relative_url }}) — the field practice these manuals inform
- [Manufacturer directory]({{ '/tools/manufacturers/' | relative_url }})
