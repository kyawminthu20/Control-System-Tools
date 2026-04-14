---
layout: default
title: "Gas Cabinet Control and Safety Reference"
description: "Semiconductor gas cabinet architecture, purge sequencing, interlocks, trips, tool handshakes, and a full Mermaid visual set for GitHub Pages."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Semiconductor"
    url: "/industries/semiconductor/"
  - name: "Facility Reference"
    url: "/industries/semiconductor/facility/"
  - name: "Gas Cabinet"
repo_path: "control-standards/rag/design_framework/semiconductor_facility/gas_cabinet_control_safety_and_interlocks.md"
related_standards:
  - name: "SEMI S2/S8/S14"
    url: "/standards/semiconductor/semi/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
---

<div class="page-header">
  <span class="page-header__label">Semiconductor Facility — Gas Systems</span>
  <h1>Gas Cabinet Control, Safety, and Interlock Architecture</h1>
  <span class="badge badge--new">Phase 24</span>
</div>

This page is the cabinet-level companion to the broader [Bulk Specialty Gas Systems](/industries/semiconductor/facility/bulk-specialty-gas/) reference. It focuses on the local package where hazardous gas, purge sequencing, exhaust proof, valve proving, shutdown logic, and tool handshake all converge.

The diagrams below are conceptual engineering aids, not vendor-specific P&IDs. They use the site’s existing Mermaid integration and are wired in the GitHub Pages-safe wrapper pattern already used elsewhere on the site.

---

## Scope

- Gas cylinder or gas source interface
- Cabinet isolation valves and regulator train
- Purge and vent routing
- Exhaust dependency and proof
- Gas detection and door interlocks
- Valve proving and flow enable logic
- Tool permit and shutdown handshake
- Fault, trip, and reset behavior

---

## Why gas cabinets deserve a dedicated page

Gas cabinets are one of the densest control packages in the facility layer because they combine:

- hazardous gas containment
- sequencing and state logic
- local hazardous shutdown action
- strong dependency on exhaust and detection
- direct interaction with the process tool

If these topics stay buried inside a generic gas-systems page, the most important cabinet behavior becomes too easy to miss during design review and commissioning.

---

## Functional overview

| Block | Main role | Main design concern |
|-------|-----------|--------------------|
| Source connection | Bring gas into the cabinet boundary | wrong gas, wrong hookup, manual isolation discipline |
| Shutoff valves | Isolate the hazardous path | fail position, proof of closure and opening |
| Regulation train | Control source pressure | overpressure, drift, contamination |
| Purge path | Clear gas before or after operation | purge availability, pressure proof, timing |
| Vent and exhaust path | Route gas safely away from the cabinet | prove capture, not just fan status |
| Detection and interlocks | Identify unsafe condition | sensor placement, nuisance trip management, proof testing |
| Tool handshake | Coordinate delivery with the process tool | ownership of permit, stop, and reset |

---

## Overall gas cabinet architecture

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
    A[Gas Cylinder or Source] --> B[Cylinder Valve]
    B --> C[Regulator or Pressure Control]
    C --> D[Valve Manifold]
    D --> E[Mass Flow Controller]
    E --> F[Process Tool]

    G[N2 Purge Supply] --> D
    G --> E

    H[Vent or Exhaust Line] --> I[Scrubber or House Exhaust]

    D --> H
    E --> H

    J[Gas Detector] --> K[Safety PLC or Safety Relay]
    L[Exhaust Flow Switch] --> K
    M[Door Switch] --> K
    N[Pressure Sensors] --> O[PLC]

    O --> P[HMI or SCADA]
    K --> Q[Shutoff Valves]
    K --> R[Horn or Beacon]
    K --> S[Tool Permit Signal]
</pre>
</div>

This is the minimum architecture most readers need before any sequence discussion starts.

---

## Gas flow path and isolation points

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
    A[Gas Cylinder] --> B[Manual Cylinder Valve]
    B --> C[Automatic Shutoff Valve A]
    C --> D[Pressure Regulator]
    D --> E[Pressure Transmitter PT-1]
    E --> F[Automatic Shutoff Valve B]
    F --> G[Mass Flow Controller MFC-1]
    G --> H[Downstream Pressure PT-2]
    H --> I[Tool Isolation Valve]
    I --> J[Process Tool]

    K[N2 Purge Valve] --> L[Purge Check Valve]
    L --> F

    M[Vent Valve] --> N[Exhaust Header]
    F --> M
    G --> M
</pre>
</div>

Use this diagram to review where isolation actually occurs and where purge or vent paths can bypass assumptions about the main flow path.

---

## Instrumentation layout

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
    A[Gas Cabinet]

    A --> B[Pressure Transmitter PT-1]
    A --> C[Pressure Switch PSH]
    A --> D[Mass Flow Controller MFC]
    A --> E[Gas Leak Detector GD]
    A --> F[Exhaust Flow Prove FS]
    A --> G[Door Interlock Switch]
    A --> H[Valve Position Feedback ZSO or ZSC]
    A --> I[Emergency Stop Input]
    A --> J[Purge Pressure Monitor]
    A --> K[Cabinet Temperature Sensor]

    B --> L[PLC]
    C --> M[Safety PLC]
    D --> L
    E --> M
    F --> M
    G --> M
    H --> L
    I --> M
    J --> L
    K --> L

    L --> N[HMI or SCADA]
    M --> O[ESD Outputs]
</pre>
</div>

This makes the cabinet’s logic burden visible: some signals support normal sequencing, while others exist primarily to block or trip the cabinet.

---

## Gas cabinet control state machine

<div class="mermaid-wrap">
<pre class="mermaid">
stateDiagram-v2
    [*] --> Idle

    Idle --> Precheck : Operator Enable
    Precheck --> Ready : All Permissives True
    Precheck --> Fault : Any Permissive Failed

    Ready --> Purge : Start Sequence
    Purge --> ValveProve : Purge Complete
    ValveProve --> GasReady : Valve Positions Confirmed
    GasReady --> Flowing : Tool Demand Active

    Flowing --> Flowing : Normal Delivery
    Flowing --> PurgeShutdown : Stop Command
    PurgeShutdown --> Idle : Safe Complete

    Idle --> EmergencyShutdown : ESD
    Precheck --> EmergencyShutdown : Gas Leak or Exhaust Fail
    Ready --> EmergencyShutdown : Gas Leak or Exhaust Fail
    Purge --> EmergencyShutdown : Gas Leak or Exhaust Fail
    GasReady --> EmergencyShutdown : Gas Leak or Exhaust Fail
    Flowing --> EmergencyShutdown : Gas Leak or Exhaust Fail

    EmergencyShutdown --> Fault
    Fault --> Idle : Reset and Safe Conditions Restored
</pre>
</div>

This is the core behavioral map for the page. If a real package cannot explain its logic in roughly this structure, its sequence is probably too implicit.

---

## Start permissive logic

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
    A[Start Request] --> B{Cabinet Door Closed}
    B -- No --> X1[Start Blocked]
    B -- Yes --> C{Exhaust Flow Proven}

    C -- No --> X2[Start Blocked]
    C -- Yes --> D{Gas Detector Healthy and Safe}

    D -- No --> X3[Start Blocked]
    D -- Yes --> E{E-Stop Healthy}

    E -- No --> X4[Start Blocked]
    E -- Yes --> F{Cylinder Pressure OK}

    F -- No --> X5[Start Blocked]
    F -- Yes --> G{Purge N2 Available}

    G -- No --> X6[Start Blocked]
    G -- Yes --> H{No Active Faults}

    H -- No --> X7[Start Blocked]
    H -- Yes --> I[Permit Purge and Start Sequence]
</pre>
</div>

Use this to separate pre-start proof from true trip logic. A permissive should answer "may I start?" not "what do I trip on now?"

---

## Purge sequence logic

<div class="mermaid-wrap">
<pre class="mermaid">
sequenceDiagram
    participant OP as Operator or Tool
    participant PLC as PLC
    participant SV as Shutoff Valves
    participant PV as Purge Valve
    participant EX as Exhaust
    participant GD as Gas Detector

    OP->>PLC: Start Request
    PLC->>EX: Verify Exhaust Flow
    EX-->>PLC: Exhaust Proven

    PLC->>GD: Verify Safe Gas Reading
    GD-->>PLC: Safe

    PLC->>PV: Open N2 Purge Valve
    PLC->>SV: Keep Gas Valves Closed
    PLC->>PLC: Start Purge Timer

    PLC->>PLC: Verify Purge Pressure or Flow
    PLC->>PV: Maintain Purge for Set Duration

    PLC->>PV: Close Purge Valve
    PLC->>SV: Open Gas Path in Sequence
    PLC->>OP: Gas Delivery Ready
</pre>
</div>

This is where most cabinet pages become vague. Purge should have explicit entry, proof, duration, and exit behavior.

---

## Valve actuation sequence

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
    A[Sequence Start] --> B[Confirm Gas Valves Closed]
    B --> C[Open N2 Purge Valve]
    C --> D[Run Purge Timer]
    D --> E[Close Purge Valve]
    E --> F[Open Upstream Shutoff Valve]
    F --> G[Verify Open Feedback]
    G --> H[Open Downstream Shutoff Valve]
    H --> I[Verify Open Feedback]
    I --> J[Enable MFC]
    J --> K[Send Tool Permit]
</pre>
</div>

This visual is especially useful when reviewing valve proof, timeout behavior, and tool-permit release conditions.

---

## Emergency shutdown logic

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
    A[Emergency Condition] --> B{Source}

    B -->|Gas Leak| C[Close Automatic Shutoff Valves]
    B -->|Exhaust Failure| C
    B -->|E-Stop| C
    B -->|Door Open During Hazardous Mode| C
    B -->|Pressure High-High| C

    C --> D[Disable MFC]
    D --> E[Remove Tool Permit]
    E --> F[Open Safe Vent or Purge Path if Designed]
    F --> G[Activate Horn or Beacon]
    G --> H[Latch Fault]
    H --> I[Require Manual Reset]
</pre>
</div>

The cabinet’s hazardous shutdown should be obvious enough that operators, integrators, and commissioning teams all predict the same response before testing.

---

## Safety layer architecture

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
    subgraph Basic_Control
        A1[PLC]
        A2[HMI or SCADA]
        A3[MFC Control]
        A4[Valve Sequencing]
    end

    subgraph Safety_Layer
        B1[Gas Detector]
        B2[Exhaust Flow Prove]
        B3[E-Stop Loop]
        B4[Safety PLC or Safety Relay]
        B5[ESD Shutoff Valves]
    end

    B1 --> B4
    B2 --> B4
    B3 --> B4
    B4 --> B5

    A1 --> A3
    A1 --> A4
    B4 --> A1
    A2 --> A1
</pre>
</div>

This diagram separates basic sequence control from the layer that actually owns hazardous isolation.

---

## Tool interface and handshake

<div class="mermaid-wrap">
<pre class="mermaid">
sequenceDiagram
    participant Tool
    participant PLC as Gas Cabinet PLC
    participant Safety as Safety Layer
    participant Valves as Gas Valves and MFC

    Tool->>PLC: Request Gas
    PLC->>Safety: Check Safety Healthy
    Safety-->>PLC: Safe or Not Safe

    PLC->>Valves: Run Purge and Open Sequence
    Valves-->>PLC: Valve Status Confirmed

    PLC-->>Tool: Gas Ready Permit
    Tool->>PLC: Process Start
    PLC->>Valves: Enable Flow

    Tool->>PLC: Process Stop
    PLC->>Valves: Stop Flow
    PLC->>Valves: Shutdown and Purge
    PLC-->>Tool: Safe Complete
</pre>
</div>

This is the boundary where facility and tool assumptions often conflict. The cabinet page should make the ownership explicit.

---

## Alarm philosophy

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
    A[Detected Condition] --> B{Severity Classification}

    B -->|Critical| C[Trip Cabinet Immediately]
    B -->|Warning| D[Alarm Only]
    B -->|Maintenance| E[Log Event or Service Required]

    C --> F[Close Gas Valves]
    C --> G[Remove Tool Permit]
    C --> H[Horn or Beacon]
    C --> I[Operator Reset Required]

    D --> J[Display on HMI]
    D --> K[SCADA Alarm History]

    E --> L[Maintenance Notification]
</pre>
</div>

This keeps the page from collapsing all bad states into one bucket. Alarm philosophy is part of the engineering model, not a cosmetic add-on.

---

## Failure mode flow

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
    A[Exhaust Fan Failure] --> B[Loss of Cabinet Extraction]
    B --> C[Exhaust Flow Switch Drops]
    C --> D[Safety Logic Trips]
    D --> E[Gas Valves Close]
    E --> F[Tool Permit Removed]
    F --> G[Alarm Latched]

    H[Gas Line Leak] --> I[Gas Detector Alarm]
    I --> D

    J[Valve Fails to Open] --> K[Valve Prove Timeout]
    K --> L[Start Sequence Fault]

    M[Purge Pressure Low] --> N[Incomplete Purge Risk]
    N --> O[Block Gas Enable]
</pre>
</div>

This is one of the best training and troubleshooting visuals because it shows how different failures collapse into a few repeatable cabinet responses.

---

## Operating modes

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
    A[Maintenance Mode] --> B[Manual Access Restricted]
    C[Standby Mode] --> D[Safe and No Gas Flow]
    E[Auto Mode] --> F[Tool-Driven Operation]
    G[Emergency Mode] --> H[Shutdown Latched]

    B --> I[No Automatic Gas Delivery]
    D --> I
    F --> J[Purge plus Valve Sequence plus Delivery]
    H --> K[Manual Reset Required]
</pre>
</div>

Mode naming can vary by vendor or site, but the restriction set should remain explicit.

---

## Key design rules

- Gas flow should not enable without exhaust proof, detector health, and cabinet health.
- Hazardous shutdown should isolate gas before trying to recover process behavior.
- Purge, valve proving, and permit-to-run should be sequenced explicitly, not implied.
- Manual mode should not bypass leak, gas-detection, exhaust-loss, or E-stop shutdown logic.
- Reset authority should be documented before commissioning, not negotiated during a trip event.

---

## Standards anchors

| Standard | Role |
|----------|------|
| SEMI F13 | Gas source control equipment routing |
| SEMI F14 | Gas source enclosure routing and cabinet context |
| SEMI F6 | Secondary containment context for hazardous gas paths |
| SEMI S6 | Exhaust ventilation guidance |
| SEMI S2 / S14 | Equipment safety and fire-risk framing |
| NFPA 55 | Compressed gas code context |
| NFPA 318 | Semiconductor-fab fire and life-safety context |
| IEC 61511 | Formal safety lifecycle when cabinet shutdown logic enters SIS territory |

Confirm current edition and project applicability before converting any routing anchor into a requirement claim.

---

## See also

- [Bulk Specialty Gas Systems](/industries/semiconductor/facility/bulk-specialty-gas/) — broader facility gas context
- [Safety and Shutdown Architecture](/industries/semiconductor/facility/safety-shutdown/) — shutdown-layer model used by this page
- [Common Control Philosophy](/industries/semiconductor/facility/control-philosophy/) — modes, states, permissives, interlocks, and trips
- [Tool-Facility Interface](/industries/semiconductor/facility/tool-facility-interface/) — handshake and ownership at the tool boundary
- [SEMI S2/S8/S14](/standards/semiconductor/semi/) — semiconductor equipment safety context
- [IEC 61511 — Functional Safety: SIS](/standards/functional-safety/iec-61511/) — lifecycle structure when shutdown logic becomes formal SIS work
