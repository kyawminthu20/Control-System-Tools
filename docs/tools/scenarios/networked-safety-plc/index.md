---
layout: default
title: "Scenario 04 — Networked Safety PLC Architecture"
description: "Standards routing for a safety PLC with network connectivity: ISO 13849-1 or IEC 62061 + IEC 62443."
breadcrumb:
  - name: "Scenarios"
    url: "/tools/scenarios/"
  - name: "Networked Safety PLC"
repo_path: "control-standards/rag/standards_intelligence/reference_models/"
related_standards:
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 62443 (Cybersecurity)"
    url: "/standards/cybersecurity/iec-62443/"
  - name: "Software Stack"
    url: "/design/software-stack/"
redirect_from:
  - /implementation/scenarios/networked-safety-plc/
  - /scenarios/networked-safety-plc/
  - /scenarios/networked-safety-plc/index.html
---

<div class="page-header">
  <span class="page-header__label">Scenario 04</span>
  <h1>Networked Safety PLC Architecture</h1>
</div>

## Project Summary

| Field | Detail |
|-------|--------|
| **Application** | Safety PLC with Ethernet/network connectivity |
| **Safety standard** | ISO 13849-1 (PL) or IEC 62061 (SIL) for safety functions |
| **Cybersecurity standard** | IEC 62443 for network and system security |
| **Software standard** | IEC 61131-3 for PLC programming |

## Starting Standards

| Standard | Role | Status |
|----------|------|--------|
| **ISO 13849-1 2023** | PL design for safety functions | Planned <span class="badge badge--verify">Review pending</span> |
| **IEC 62061 2021** | SIL design for safety functions (alternative) | Planned <span class="badge badge--verify">Review pending</span> |
| **IEC 62443** | Industrial cybersecurity | <span class="badge badge--pending">Review pending</span> — [detail page]({{ '/standards/cybersecurity/iec-62443/' | relative_url }}) |
| **IEC 61131-3** | PLC programming | Routing reference |

## Two-Layer Architecture

Networked safety systems require addressing two separate concerns:

| Layer | Standard | Concern |
|-------|----------|---------|
| **Safety layer** | ISO 13849-1 or IEC 62061 | Safety function reliability (PL/SIL) |
| **Security layer** | IEC 62443 | Cybersecurity of the control system |

**These are independent but related:** A safety PLC may achieve PLd, but if the network it sits on is compromised, the safety function may not operate correctly. IEC 62443 addresses the security of the system as a whole.

## Mermaid: Standard Control vs Safety Control Separation

<div class="mermaid-wrap">
<pre class="mermaid">
graph LR
    A[HMI / Operator Commands] --> B[Standard PLC]
    B --> C[Normal Sequence Control]
    C --> D[Drives / Valves / Outputs]

    E[Safety Inputs<br/>E-Stop / Guard / Pressure] --> F[Safety PLC / Safety Relay]
    F --> G[Safety Outputs<br/>STO / Safe Valve / Contactor]
    G --> D

    B -. monitored by .-> F
    F -. independent safety action .-> D
</pre>
</div>

## Safety Function Design (choose one path)

**PL Path (ISO 13849-1):**
- Use for most industrial machinery applications
- Category 3 or 4 with appropriate MTTFd and DC
- Simpler methodology; well-accepted for typical machine safety

**SIL Path (IEC 62061):**
- Use when SIL > PLd equivalent is required
- PFHD-based calculation
- More flexible for complex safety functions

## IEC 62443 Cybersecurity Routing

IEC 62443 is a series of standards for industrial automation and control system security:

| Standard | Scope |
|----------|-------|
| IEC 62443-2-1 | Security management system requirements |
| IEC 62443-3-3 | System security requirements and SL levels |
| IEC 62443-4-1 | Secure product development lifecycle |
| IEC 62443-4-2 | Technical security requirements for IACS components |

See the [IEC 62443 detail page]({{ '/standards/cybersecurity/iec-62443/' | relative_url }}) for Zone/Conduit design, Security Level table, Foundational Requirements, and safety system checklist. See [Software Stack]({{ '/design/software-stack/' | relative_url }}) for routing guidance on IEC 61131-3 and related topics.

## Repository Paths

| Reference | Path |
|-----------|------|
| Software safety routing | `rag/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md` |
| Safety architecture reference | `rag/reference_models/Universal Machine Safety Architecture.md` |
| 7-layer architecture | `rag/reference_models/7-Layer Industrial Machine Architecture Model.md` |

<a href="{{ '/design/software-stack/' | relative_url }}" class="card__link">Software Stack page — IEC 61131-3, IEC 62443, and more &rarr;</a>
