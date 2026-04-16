---
layout: default
title: "Cybersecurity Standards"
description: "Industrial cybersecurity standards family: IEC 62443 for IACS security, Security Levels, Zone/Conduit model, and integration with functional safety."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Cybersecurity"
repo_path: "control-standards/rag/standards_intelligence/international/cybersecurity/"
related_standards:
  - name: "Functional Safety"
    url: "/standards/functional-safety/"
  - name: "Networked Safety PLC"
    url: "/implementation/scenarios/networked-safety-plc/"
  - name: "Software Stack"
    url: "/design/software-stack/"
---

<div class="page-header">
  <span class="page-header__label">Standards Explorer · Cybersecurity</span>
  <h1>Industrial Cybersecurity Standards</h1>
  <p>IACS security standards for networked industrial automation and control systems. IEC 62443 is the primary international series.</p>
</div>

## Quick Routing

```
Networked PLC or controller?            → IEC 62443-3-3 (Zone/Conduit + SL design)
Asset Owner — need a security program?  → IEC 62443-2-1 (CSMS)
Buying or certifying a product?         → IEC 62443-4-2 (component requirements)
Developing safety PLC software?         → IEC 62443-4-1 (secure development lifecycle)
Safety system with network interface?   → IEC 62443 + IEC 61511 (or IEC 62061)
```

---

## IEC 62443 Series

| Standard | Scope | Status |
|----------|-------|--------|
| [IEC 62443 (full page)]({{ '/standards/cybersecurity/iec-62443/' | relative_url }}) | IACS security — Zone/Conduit, Security Levels, FRs, lifecycle | <span class="badge badge--complete">Phase 5 Complete</span> |
| IEC 62443-2-1 | Security management system (CSMS) | Covered in IEC 62443 page |
| IEC 62443-3-3 | System security requirements and SL levels | Covered in IEC 62443 page |
| IEC 62443-4-1 | Secure product development lifecycle | Covered in IEC 62443 page |
| IEC 62443-4-2 | Component security requirements | Covered in IEC 62443 page |

<p><a href="{{ '/standards/cybersecurity/iec-62443/' | relative_url }}">View IEC 62443 detail page &rarr;</a></p>

---

## Relationship to Functional Safety

Cybersecurity and functional safety are separate but interdependent disciplines for networked safety systems:

- **IEC 61511:2016** requires a cybersecurity risk assessment for safety instrumented systems.
- **IEC 62061** does not explicitly mandate a cybersecurity assessment but the principle that a safety function must not be defeated by a foreseeable means applies.
- A successful cyberattack on a safety system is a safety hazard — the cybersecurity Zone/Conduit design must protect the safety function as well as the system.

| See also | Link |
|----------|------|
| Networked Safety PLC scenario | [Scenario 04]({{ '/implementation/scenarios/networked-safety-plc/' | relative_url }}) |
| Software Stack and routing guide | [Software Stack]({{ '/design/software-stack/' | relative_url }}) |
| Functional safety family | [Functional Safety]({{ '/standards/functional-safety/' | relative_url }}) |

---

## Out-of-Scope for This Corpus

| Topic | Status |
|-------|--------|
| IEC 60079 (hazardous area) | <span class="badge badge--gap">NOT CONFIRMED IN CORPUS</span> |
| NIST SP 800-82 (US OT security guide) | <span class="badge badge--gap">NOT IN CORPUS</span> |
| NERC CIP (electric utility cybersecurity) | <span class="badge badge--gap">NOT IN CORPUS</span> |
| ISA/IEC 62443 certification schemes | <span class="badge badge--gap">NOT IN CORPUS</span> — verify against ISASecure and TÜV certification bodies |
