---
layout: default
title: "Distribution SCADA and Telemetry"
description: "SCADA architecture for municipal water distribution systems — RTU telemetry, IEC 62443 security zones, historian logging, and communication failure fallback."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Water/Wastewater"
    url: "/industries/water-wastewater/"
  - name: "Distribution SCADA"
related_standards:
  - name: "IEC 62443"
    url: "/standards/cybersecurity/iec-62443/"
---

<div class="page-header">
  <span class="page-header__label">Water/Wastewater — System Reference</span>
  <h1>Distribution SCADA and Telemetry</h1>
</div>

<blockquote>
<strong>Scope:</strong> SCADA system architecture for municipal water distribution — central SCADA server, RTUs at remote pump stations and reservoirs, historian, HMI, and IEC 62443 security zone design. Covers communication failure fallback and regulatory logging requirements.
</blockquote>

## Standards Applicability

| Standard | Role in this system |
|---|---|
| IEC 62443 | SCADA security zones, conduit design, remote access controls |
| ISA-18.2 | Alarm management for communication loss, site offline |
| EPA SDWA | Continuous logging of Cl₂ residual and turbidity (4-hour rolling average) |
| NIST CSF | Cybersecurity framework — identify, protect, detect, respond, recover |

## SCADA Zone Architecture

```mermaid
flowchart TD
    subgraph Field["Field Layer"]
        A[Sensors & Actuators\n4-20mA / Hardwired]
        B[RTUs at remote sites\nDNP3 / cellular WAN]
    end
    subgraph Control["Site Control Layer"]
        C[Process PLCs\nEtherNet/IP or Modbus TCP]
        D[Local HMI panels]
    end
    subgraph Supervisory["Supervisory Layer"]
        E[SCADA Server]
        F[Historian]
        G[Engineering Workstation]
    end
    subgraph Enterprise["Enterprise Layer"]
        H[IT Network\nOffice / Billing]
        I[Regulatory Reporting Portal]
    end
    Field --> Control
    Control -->|Firewall| Supervisory
    Supervisory -->|DMZ / Data Diode| Enterprise
    B -->|Encrypted WAN| E
```

## IEC 62443 Security Zone Map

```mermaid
flowchart TD
    subgraph Z0["Zone 0 — Field SL1"]
        A[Sensors\nActuators\nLocal RTU I/O]
    end
    subgraph Z1["Zone 1 — Control SL2"]
        B[Process PLCs]
        C[Safety PLCs\nHardwired only — not network-reachable]
        D[RTUs at pump stations]
    end
    subgraph Z2["Zone 2 — Supervisory SL2"]
        E[SCADA Server]
        F[Historian]
        G[Engineering Workstation]
    end
    subgraph Z3["Zone 3 — Enterprise SL1"]
        H[IT Network]
        I[Reporting Systems]
    end
    subgraph Remote["Remote Access — Conduit"]
        J[VPN Gateway\nMFA required\nSession logging]
    end
    Z0 -->|Conduit: hardwired or serial| Z1
    Z1 -->|Conduit: firewall whitelist| Z2
    Z2 -->|DMZ: unidirectional data diode| Z3
    J -->|Encrypted tunnel| Z2
```

## Communication Failure Fallback Logic

```mermaid
flowchart TD
    A[RTU Heartbeat Register\nUpdated every 30s] --> B{Heartbeat received\nby SCADA within 60s?}
    B -->|Yes| C[Normal SCADA Operation\nAll values current]
    B -->|No| D[Alarm: Communication Loss\nSite RTU-XXX]
    D --> E{Duration > 5 minutes?}
    E -->|No| F[SCADA displays last-known values\nStale data indicator on HMI]
    E -->|Yes| G[Status: Site Offline\nLocal Control Active]
    G --> H[RTU falls back to local mode\nRuns on last setpoints and local alarms]
    H --> I{Comms restored?}
    I -->|Yes| J[RTU syncs time\nUploads buffered log\nReturns to SCADA control]
    I -->|No| K[Operator dispatched\nto site for manual operation]
```

## Historian Retention Requirements

| Data Type | Resolution | Retention | Driver |
|---|---|---|---|
| All analog values | 1-minute | 2 years | Good practice |
| Turbidity (post-filter) | 15-second | 2 years | EPA SWTR — 4-hr rolling avg |
| Cl₂ residual | 1-minute | 2 years | EPA SWTR — continuous record |
| Alarm events | Event-driven | 5 years | Regulatory audit readiness |
| Operator actions | Event-driven | 5 years | Audit trail |
| System start/stop | Event-driven | 5 years | Maintenance record |

## Key Engineering Decisions

**Why DNP3 for remote RTUs?** DNP3 handles communication gaps gracefully — RTUs buffer data locally and upload on reconnect. It also supports unsolicited reporting (RTU pushes alarms to SCADA immediately rather than waiting for a poll).

**Data diode for enterprise export:** A unidirectional security gateway allows historian data to flow to IT/reporting systems without allowing any inbound access to the OT network. This is the IEC 62443 conduit between Zone 2 and Zone 3.

**Safety PLCs are hardwired only:** The IEC 61511 safety logic (OT shutdown, overflow prevention) is hardwired, not networked. Even if the SCADA network is compromised, safety trips remain functional.

## Cross-Links

- [IEC 62443 — Cybersecurity](/standards/cybersecurity/iec-62443/)
- [Chemical Dosing](../chemical-dosing/) — OT trip wired to safety layer, not SCADA
- [Lifecycle Stage 4 — Detailed Design](/lifecycle/stage-04/)
