<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: DERIVED_REFERENCE
CATEGORY: SEMI_FACILITY
STATUS: DRAFT
-->

# Semiconductor Gas Cabinet — Control, Safety, and Interlock Architecture

## Purpose

This note is the cabinet-level reference for semiconductor specialty-gas delivery.

It sits below the broad facility gas-system view and focuses on the local package that typically includes:

- gas source isolation
- pressure control
- purge routing
- vent and exhaust dependency
- gas detection
- cabinet-door and maintenance interlocks
- tool permit and shutdown exchange

This is an engineering pattern reference, not a vendor P&ID, not a substitute for the governing standards, and not a final SIL claim.

## Why gas cabinets need their own reference

Gas cabinets are not just a smaller version of the bulk specialty-gas page.

They combine:

- hazardous gas containment
- local sequence control
- exhaust-dependent safety behavior
- cabinet-specific detection and shutdown logic
- a direct interface to the process tool

That combination makes them one of the most interlock-heavy packages in a semiconductor facility.

## Scope and boundary

This note covers the cabinet package from the gas source connection to the tool-facing permit and gas-delivery boundary.

It usually includes:

- cylinder or source connection
- automatic shutoff valves
- regulator and pressure measurement
- purge and vent path
- MFC or local flow-control hardware where applicable
- gas detector and exhaust proof inputs
- door interlock and E-stop integration
- local PLC and safety-layer responsibilities

It usually excludes:

- bulk pad and gas-room design
- facility distribution upstream of the cabinet boundary
- tool-internal process-gas box design
- vendor-specific wiring details

## Functional block summary

| Block | Primary role | Typical engineering concern |
| --- | --- | --- |
| Source connection | bring gas into the cabinet boundary | wrong gas, wrong hookup, manual isolation discipline |
| Automatic shutoff valves | isolate hazardous gas rapidly | fail position, valve proof, cycle life |
| Regulation train | reduce and stabilize pressure | overpressure, contamination, drift |
| Purge path | clear hazardous gas before or after flow | proof of purge availability, timing, pressure confirmation |
| Vent and exhaust path | remove released or purged gas safely | prove capture, not just fan running |
| Detection and interlocks | identify unsafe condition | detector placement, nuisance trip management, proof testing |
| Local control and safety layers | run sequence and hazardous shutdown | ownership split between PLC, safety logic, and tool handshake |

## Core design rules

- Gas enable should depend on cabinet health, exhaust proof, and no active hazard alarm.
- Hazardous shutdown should isolate gas first, then remove tool permit, then drive the cabinet toward its defined safe state.
- Purge should be treated as a defined sequence with entry, proof, timing, and exit criteria.
- Manual mode should not bypass leak, gas-detection, exhaust-loss, or emergency-stop shutdown paths.
- A cabinet page should separate `PERMISSIVE`, `INTERLOCK`, `TRIP`, and `ALARM` behavior clearly.

## Overall gas cabinet architecture

```mermaid
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
```

This diagram shows the minimum architectural layers that make the cabinet work as a controlled hazardous-gas package instead of a simple valve panel.

## Gas flow path and isolation points

```mermaid
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
```

The exact hardware varies by gas and vendor, but the engineering pattern stays stable: two fast isolation points, pressure observation, purge injection, controlled venting, and a defined tool boundary.

## Instrumentation layout

```mermaid
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
```

The instrumentation burden is one reason gas cabinets deserve a dedicated note. Several signals are not there to optimize flow; they exist to block unsafe operation or trigger immediate isolation.

## Control state model

```mermaid
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
```

Not every cabinet uses every state name, but the behavioral stages should still be explicit and testable.

## Start permissive logic

```mermaid
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
```

These permissives answer one question only: may the cabinet begin the sequence. They should not be mixed with hazardous trip logic.

## Purge sequence logic

```mermaid
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
```

The purge path should be proven, timed, and closed deliberately. It is not just a convenience feature.

## Valve actuation sequence

```mermaid
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
```

Valve proving belongs in the sequence, not just in maintenance notes. The cabinet should know whether the commanded path is actually established.

## Emergency shutdown logic

```mermaid
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
```

This is the local hazardous shutdown layer for the cabinet. It should remain active regardless of the current operating mode.

## Safety layer architecture

```mermaid
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
```

The separation matters because operator displays and normal sequence control are not sufficient protection against a gas release scenario.

## Tool interface and handshake

```mermaid
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
```

The cabinet-to-tool handshake should define both permission and shutdown behavior. A "permit" signal without ownership rules is not enough.

## Alarm philosophy

```mermaid
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
```

This keeps the cabinet readable: not every abnormal signal should trip, and every trip-capable signal should be obvious.

## Failure mode flow

```mermaid
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
```

The cabinet is a good example of why failure-mode visualization matters. Several failures are not process upsets first; they are state-machine or hazardous-shutdown problems first.

## Operating modes

```mermaid
flowchart LR
    A[Maintenance Mode] --> B[Manual Access Restricted]
    C[Standby Mode] --> D[Safe and No Gas Flow]
    E[Auto Mode] --> F[Tool-Driven Operation]
    G[Emergency Mode] --> H[Shutdown Latched]

    B --> I[No Automatic Gas Delivery]
    D --> I
    F --> J[Purge plus Valve Sequence plus Delivery]
    H --> K[Manual Reset Required]
```

Mode naming can vary by site, but the restrictions should stay explicit.

## Representative signal set

Example tag stems for one cabinet:

- `GCAB_GD_ALM`
- `GCAB_EXH_PROOF`
- `GCAB_DOOR_CLS`
- `GCAB_PSHH`
- `GCAB_N2_AVAIL`
- `GCAB_SOV_A_CMD`
- `GCAB_SOV_A_ZSO`
- `GCAB_SOV_B_CMD`
- `GCAB_SOV_B_ZSO`
- `GCAB_MFC_EN`
- `GCAB_TOOL_PERMIT`
- `GCAB_FAULT_LATCH`

These are placeholders for engineering discussion, not a required naming standard.

## Standards routes

Use these standards families to route detailed questions:

- `SEMI F13` and `SEMI F14` for gas source control equipment and enclosure guidance
- `SEMI F6` and `SEMI S6` for containment and exhaust-related design context
- `SEMI S2` and `SEMI S14` for equipment safety and fire-risk framing
- `NFPA 55` and `NFPA 318` for facility gas and fab fire-life-safety context
- `IEC 61511` when cabinet shutdown logic becomes part of a formal safety lifecycle

Confirm current edition and project applicability before turning any one of these routes into a requirement claim.

## Related files

- [Bulk Specialty Gas Systems](./bulk_specialty_gas.md)
- [Common Control Philosophy](./common_control_philosophy.md)
- [Safety and Shutdown Architecture](./safety_and_shutdown.md)
- [Tool-Facility Interface](./tool_facility_interface.md)
- [Instrumentation Use Matrix](./instrumentation_use_matrix.md)

## Scope caution

This note is intentionally cabinet-level and vendor-neutral.

It is meant to answer:

- what the cabinet must prove before enabling gas
- what should happen when the cabinet loses a critical protection input
- how purge, valve proving, and tool permit fit together
- how to separate operator information from hazardous shutdown logic

Final valve selection, detector technology, integrity assignment, hazardous-area detail, and code compliance remain project-specific.
