---
layout: default
title: "Semiconductor Industry Standards Overlay"
description: "Standards path for semiconductor fab equipment: SEMI S2/S8/S14, IEC 60204-1, ISO 12100, NFPA 79, IEC 62443."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Semiconductor"
related_standards:
  - name: "SEMI S2/S8/S14"
    url: "/standards/semiconductor/semi/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
  - name: "IEC 62443"
    url: "/standards/cybersecurity/iec-62443/"
---

<div class="page-header">
  <span class="page-header__label">Industry Overlay — Semiconductor</span>
  <h1>Semiconductor Equipment Standards</h1>
  <span class="badge badge--complete">Phase 11 — SEMI Corpus Complete</span>
</div>

## Industry Profile

| Field | Value |
|-------|-------|
| **Industry** | Semiconductor fab equipment (process tools, metrology, handlers) |
| **Typical tools** | Etch, CVD, PVD, CMP, diffusion, implant, metrology, wafer handlers |
| **Markets** | US fabs + EU fabs + Asian fabs (global installation) |
| **Special concerns** | Flammable/toxic process gases, cleanroom EMC, SEMI qualification requirements, automated host interface |

---

## Standards Applicability by Project Phase

| Phase | Standards | Purpose |
|-------|-----------|---------|
| **Tool Design** | ISO 12100, SEMI S2 §4–6, SEMI S14 | Risk assessment, interlock architecture, fire risk evaluation |
| **Electrical Build** | IEC 60204-1, NFPA 79, UL 508A | Machine electrical design, US electrical compliance, panel listing |
| **Ergonomics Review** | SEMI S8 | Control placement, force limits, maintenance access |
| **Fab Qualification** | SEMI S2 (full), SEMI S8, SEMI S14 | EH&S review, SEMI compliance checklist |
| **Installation** | NEC, IEC 60204-1 §8 | Facility connection, equipotential bonding |
| **Networked Operation** | IEC 62443 | Cybersecurity for fab host interface and remote diagnostics |
| **Periodic Inspection** | SEMI S2 §15 | Interlock function verification, LOTO procedure audit |

---

## Standards Selection Flow

```
Is the tool for a US fab?
  YES → NFPA 79 (machine electrical) + NEC (installation) + UL 508A (panel listing)
  NO  → IEC 60204-1 (machine electrical)
  BOTH → Apply NFPA 79 and IEC 60204-1 in parallel (most global tools)

Does the tool use flammable or toxic process gases?
  YES → SEMI S14 fire risk assessment required
       → NC shutoff valves on all gas lines
       → Exhaust flow monitoring interlock
       → Gas detector integration with automatic shutoff

Does the tool have high-voltage circuits (>50 V AC or >120 V DC)?
  YES → SEMI S2: interlocks must de-energize before panel access
       → Stored energy: capacitors must discharge to <50 V within 5 s of isolation
       → All energy isolation points must accept a padlock (LOTO)

Is the tool connected to fab host or remote network?
  YES → IEC 62443: apply appropriate Security Level (SL-T) based on risk
       → Segment tool network from process control network (conduit model)
```

---

## Standards Path Summary

| Category | Standards | Corpus Status |
|----------|-----------|---------------|
| Risk assessment | ISO 12100 | <span class="badge badge--complete">Complete</span> |
| Safety functions | ISO 13849-1 (PLd typical for tools) | <span class="badge badge--complete">Complete</span> |
| Machine electrical (international) | IEC 60204-1 | <span class="badge badge--complete">Complete</span> |
| US electrical | NEC, NFPA 79, UL 508A | <span class="badge badge--complete">Complete</span> |
| Semiconductor-specific | SEMI S2, S8, S14 | <span class="badge badge--complete">Complete</span> |
| Cybersecurity | IEC 62443 | <span class="badge badge--complete">Complete</span> |
| Fab fire code | NFPA 318 | Not in corpus |

---

## Key Engineering Decisions for Semiconductor Tools

**Capacitor discharge interlock design (SEMI S2):**
High-voltage power supplies (RF generators, ion implant supplies) store significant energy. The interlock must either: (a) discharge capacitors to <50 V within 5 seconds of isolation, OR (b) provide a discharge indicator visible at the access point AND an access interlock that prevents opening until discharge is confirmed. Option (b) is safer and easier to verify during qualification.

**Single-point ground vs. equipotential bonding:**
RF-intensive tools (etch, CVD) require single-point grounding to prevent RF ground loops. Equipotential bonding per IEC 60204-1 §8 must still be maintained for safety — achieve both by designing the safety ground and signal ground as a star topology meeting at one point.

**SEMI S2 interlock independence:**
S2 requires that safety interlocks be independent of the process control system where a single failure could cause injury. In practice: use a dedicated safety relay or safety PLC for personnel protection interlocks (door interlocks, E-stops, gas shutoffs), separate from the process recipe controller.

---

## SEMI S2 Compliance Flow

```
1. ISO 12100 risk assessment → identify all hazards
2. For each hazard: determine required risk reduction (PL per ISO 13849-1)
3. SEMI S2 electrical safety:
   - Ground all accessible conductive surfaces
   - Interlock all HV panels (de-energize before opening)
   - LOTO: one padlock per energy isolation point
   - Capacitor discharge: <50 V within 5 s
4. SEMI S14 fire risk assessment:
   - Identify all flammable/pyrophoric materials
   - Automatic shutoff on fire detection
   - Independent over-temperature cutout on all heater circuits
5. SEMI S8 ergonomics review:
   - E-stop: 600–1400 mm height, ≤40 N force
   - Maintenance access: 600 mm wide × 900 mm high minimum
6. Documentation package: interlock list, schematic, LOTO procedure, HazMat inventory
```

---

<a href="{{ '/scenarios/semiconductor-fab-tool/' | relative_url }}" class="card__link">See Semiconductor Fab Tool scenario &rarr;</a>

<a href="{{ '/scenarios/semiconductor-equipment/' | relative_url }}" class="card__link">See Semiconductor Equipment Compliance scenario &rarr;</a>

## Related References

- [15-Standard Minimum Compliance Stack]({{ '/reference/architecture/compliance-stack/' | relative_url }}) — full compliance baseline for semiconductor equipment

---

## Semiconductor Facility Reference

This page covers **equipment**-oriented standards (S2/S8/S14, IEC 60204-1). The companion Facility Reference section covers the building and utility layer that tools depend on:

| Section | Coverage |
|---------|----------|
| [Facility Overview]({{ '/industries/semiconductor/facility/' | relative_url }}) | Standards stack, cross-cutting design threads |
| [Bulk Specialty Gas]({{ '/industries/semiconductor/facility/bulk-specialty-gas/' | relative_url }}) | Gas storage, cabinets, VMBs, purge panels |
| [UPW and Wastewater]({{ '/industries/semiconductor/facility/upw-wastewater/' | relative_url }}) | UPW generation, distribution, reclaim, drain segregation |
| [Exhaust and Abatement]({{ '/industries/semiconductor/facility/exhaust-abatement/' | relative_url }}) | Process exhaust, abatement utilities, vacuum |
| [HVAC and Cleanroom]({{ '/industries/semiconductor/facility/hvac-cleanroom/' | relative_url }}) | Room pressure cascade, FFU systems, temperature/humidity, particle monitoring |
| [Bulk Chemical Distribution]({{ '/industries/semiconductor/facility/bulk-chemical/' | relative_url }}) | Bulk storage, transfer skids, blend systems, containment, drain segregation |
| [Safety and Shutdown Architecture]({{ '/industries/semiconductor/facility/safety-shutdown/' | relative_url }}) | Shutdown layers, gas/leak detection integration, cause-and-effect design |
| [Common Control Philosophy]({{ '/industries/semiconductor/facility/control-philosophy/' | relative_url }}) | Modes, states, permissives, interlocks, trips, and shutdown ownership |
| [Tool-Facility Interface]({{ '/industries/semiconductor/facility/tool-facility-interface/' | relative_url }}) | Handshake signals, permit-to-run, battery limit definitions |
| [Instrumentation]({{ '/industries/semiconductor/facility/instrumentation/' | relative_url }}) | Device selection matrix by system and compliance lens |

<a href="{{ '/industries/' | relative_url }}" class="card__link">&larr; Industry matrix</a>
