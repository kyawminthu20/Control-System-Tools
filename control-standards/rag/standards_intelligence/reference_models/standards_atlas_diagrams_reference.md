# Standards Atlas — Diagram Reference Pack

**AI_READ_ACCESS: ALLOWED**

This file collects the core diagrams for the Control System Standards Atlas project.

Use these as source diagrams for the site, docs, or future SVG redraws.

---

## 1. Platform Information Architecture

```mermaid
graph TD
    A[Control System Standards Atlas] --> B[Standards Directory]
    A --> C[Lifecycle Guide]
    A --> D[Industry Matrix]
    A --> E[Scenario Explorer]
    A --> F[Software Stack]
    A --> G[Crosswalks]
    A --> H[Interview Guide]

    B --> B1[Machinery]
    B --> B2[Process Safety]
    B --> B3[Electrical]
    B --> B4[Cybersecurity]
    B --> B5[Software]
    B --> B6[Industry Specific]

    C --> C1[Concept]
    C --> C2[Standards Selection]
    C --> C3[Safety Architecture]
    C --> C4[Detailed Design]
    C --> C5[Build]
    C --> C6[Commissioning]
    C --> C7[Lifecycle Support]
```

---

## 2. Directory Navigation Model

```mermaid
graph LR
    A[Home] --> B["/standards"]
    A --> C["/lifecycle"]
    A --> D["/industries"]
    A --> E["/scenarios"]
    A --> F["/software-stack"]
    A --> G["/crosswalks"]

    B --> B1["/standards/machinery"]
    B --> B2["/standards/process-safety"]
    B --> B3["/standards/electrical"]
    B --> B4["/standards/cybersecurity"]
    B --> B5["/standards/software"]
    B --> B6["/standards/industry-specific"]

    D --> D1["/industries/semiconductor"]
    D --> D2["/industries/food-and-beverage"]
    D --> D3["/industries/oil-and-gas"]
    D --> D4["/industries/marine"]
    D --> D5["/industries/medical"]
    D --> D6["/industries/nuclear"]
```

---

## 3. Standards Relationship Graph

```mermaid
graph TD
    ISO12100[ISO 12100] --> ISO13849[ISO 13849-1]
    ISO12100 --> IEC62061[IEC 62061]
    ISO13849 --> IEC60204[IEC 60204-1]
    IEC62061 --> IEC61508[IEC 61508]
    IEC61511[IEC 61511] --> IEC61508
    NFPA79[NFPA 79] --> NEC[NEC]
    UL508A[UL 508A] --> NEC
    UL508A --> NFPA79
    IEC60204 --> NFPA79
    IEC62443[IEC 62443] --> IEC61508
    IEC62443 --> IEC61511
    IEC61131[IEC 61131-3] --> IEC62061
    IEC61131 --> IEC61508
    IEC60079[IEC 60079 Family] --> IEC61511
```

---

## 4. Machinery vs Process Safety Routing

```mermaid
flowchart TD
    A[Start: Define System] --> B{Primary risk context?}
    B -->|Machine motion / access / entrapment| C[Machinery route]
    B -->|Process containment / pressure / chemical shutdown| D[Process route]

    C --> E[ISO 12100 risk assessment]
    E --> F{Safety framework?}
    F -->|PL route| G[ISO 13849-1]
    F -->|Machinery SIL route| H[IEC 62061]
    G --> I[IEC 60204-1 / NFPA 79 / UL 508A]
    H --> I

    D --> J[IEC 61511]
    J --> K[IEC 61508 lifecycle foundation]
    K --> L[IEC 60079 if hazardous area]
    L --> M[NEC / local electrical code]
```

---

## 5. SIL vs PL Concept Map

```mermaid
graph LR
    A[Risk Assessment] --> B[Required Risk Reduction]
    B --> C{Application domain}
    C -->|Machinery| D[PL / Machinery SIL]
    C -->|Process Industry| E[SIL]

    D --> F[ISO 13849-1]
    D --> G[IEC 62061]
    E --> H[IEC 61511]
    H --> I[IEC 61508]
    G --> I

    F --> J[Category / architecture / diagnostics]
    G --> K[Safety function design / machinery SIL]
    H --> L[SIF allocation / lifecycle / proof test]
```

---

## 6. Control System Lifecycle with Standards Overlay

```mermaid
flowchart LR
    A[Concept] --> B[Standards Selection]
    B --> C[Risk Assessment]
    C --> D[Safety Architecture]
    D --> E[Detailed Design and Part Sizing]
    E --> F[Draft Design and Documentation]
    F --> G[Build and Software Implementation]
    G --> H[Installation]
    H --> I[Pre-commissioning and Calibration]
    I --> J[Commissioning and Validation]
    J --> K[Maintenance and Lifecycle Support]

    A -.-> A1[ISO 12100 / project boundary]
    B -.-> B1[NFPA 79 / IEC 60204 / IEC 61511]
    C -.-> C1[ISO 12100 / IEC 61511]
    D -.-> D1[ISO 13849 / IEC 62061 / IEC 61511]
    E -.-> E1[UL 508A / NEC / design assumptions]
    G -.-> G1[IEC 61131-3 / IEC 62443]
    J -.-> J1[FAT / SAT / safety validation]
    K -.-> K1[Proof test / calibration / MOC]
```

---

## 7. Lifecycle Deliverables Map

```mermaid
graph TD
    A[Concept] --> A1[System description]
    A --> A2[Operating assumptions]
    A --> A3[Boundary definition]

    B[Risk Assessment] --> B1[Hazard list]
    B --> B2[Risk evaluation]
    B --> B3[Safe state definition]

    C[Safety Architecture] --> C1[Safety function register]
    C --> C2[PLr or SIL target]
    C --> C3[Architecture concept]

    D[Detailed Design] --> D1[Device list]
    D --> D2[I/O list]
    D --> D3[Panel BOM]
    D --> D4[Cable and network architecture]

    E[Drafting] --> E1[Schematics]
    E --> E2[P&ID]
    E --> E3[Cause and effect]
    E --> E4[Loop drawings]

    F[Commissioning] --> F1[Loop checks]
    F --> F2[Calibration sheets]
    F --> F3[FAT / SAT]
    F --> F4[Validation report]

    G[Lifecycle Support] --> G1[Proof-test procedures]
    G --> G2[PM checklists]
    G --> G3[MOC records]
    G --> G4[Revision history]
```

---

## 8. 7-Layer Industrial Machine Architecture

```mermaid
graph TD
    L1[Layer 1: Process / Machine Function] --> L2[Layer 2: Actuators and Power Conversion]
    L2 --> L3[Layer 3: Sensors and Feedback]
    L3 --> L4[Layer 4: Standard Control]
    L4 --> L5[Layer 5: Safety Control]
    L5 --> L6[Layer 6: HMI / SCADA / Logging]
    L6 --> L7[Layer 7: Site / Enterprise / Historian]

    L4 -. standards .-> S1[IEC 61131-3]
    L5 -. standards .-> S2[ISO 13849 / IEC 62061 / IEC 61511]
    L2 -. standards .-> S3[IEC 60204-1 / NFPA 79 / UL 508A]
    L6 -. standards .-> S4[IEC 62443]
```

---

## 9. Standard Control vs Safety Control Separation

```mermaid
graph LR
    A[HMI / Operator Commands] --> B[Standard PLC]
    B --> C[Normal Sequence Control]
    C --> D[Drives / Valves / Outputs]

    E[Safety Inputs<br/>E-Stop / Guard / Pressure / Interlocks] --> F[Safety PLC / Safety Relay]
    F --> G[Safety Outputs<br/>STO / Safe Valve / Contactor Dropout]
    G --> D

    B -. monitored by .-> F
    F -. independent safety action .-> D
```

---

## 10. Safety Function Chain

```mermaid
flowchart LR
    A[Hazard] --> B[Sensor / Detection]
    B --> C[Logic Solver]
    C --> D[Final Element]
    D --> E[Safe State]

    B -. examples .-> B1[Guard switch / pressure transmitter / light curtain / gas detector]
    C -. examples .-> C1[Safety relay / safety PLC / SIS logic solver]
    D -. examples .-> D1[STO / contactor / shutdown valve / motor trip]
```

---

## 11. Machinery Safety Function Example

```mermaid
flowchart TD
    A[Guard door opens] --> B[Dual channel guard switch]
    B --> C[Safety PLC]
    C --> D[Dual STO channels]
    D --> E[Servo torque removed]
    E --> F[Machine safe stop]
```

---

## 12. Process Shutdown Function Example

```mermaid
flowchart TD
    A[High reactor pressure] --> B[Pressure transmitters]
    B --> C[Safety logic solver]
    C --> D[Shutdown valve / vent valve]
    D --> E[Pressure reduced / process safe state]
```

---

## 13. 1oo1, 1oo2, and 2oo3 Architecture Comparison

```mermaid
graph TD
    A[1oo1] --> A1[Single sensor]
    A --> A2[Simple architecture]
    A --> A3[Lower fault tolerance]

    B[1oo2] --> B1[Two sensors]
    B --> B2[Redundancy]
    B --> B3[Improved tolerance / possible nuisance trips]

    C[2oo3] --> C1[Three sensors]
    C --> C2[Voting logic]
    C --> C3[Higher integrity and availability]
```

---

## 14. Detailed Design and Part Sizing Logic

```mermaid
flowchart TD
    A[Safety concept approved] --> B[Determine architecture]
    B --> C[Select sensors]
    B --> D[Select logic solver]
    B --> E[Select final elements]
    C --> F[Check response time / environment / diagnostics]
    D --> G[Check safety rating / separation / libraries]
    E --> H[Check fail-safe state / shutdown time / power isolation]
    F --> I[Electrical sizing]
    G --> I
    H --> I
    I --> J[Create BOM and schematics]
```

---

## 15. Electrical Design Standards Route

```mermaid
flowchart LR
    A[Control system power design] --> B[Conductor sizing]
    A --> C[OCPD selection]
    A --> D[Disconnecting means]
    A --> E[SCCR path]
    A --> F[Wiring segregation / bonding]

    B -.-> S1[NEC]
    C -.-> S2[NFPA 79]
    D -.-> S3[IEC 60204-1]
    E -.-> S4[UL 508A]
    F -.-> S5[NFPA 79 / IEC 60204-1]
```

---

## 16. Draft Design Documentation Stack

```mermaid
graph TD
    A[Draft Design Package] --> B[System description]
    A --> C[Risk assessment]
    A --> D[Safety function register]
    A --> E[P&ID / process diagram]
    A --> F[Electrical schematics]
    A --> G[Panel layout]
    A --> H[I/O list]
    A --> I[Cause and effect matrix]
    A --> J[Alarm list]
    A --> K[Network architecture]
    A --> L[Test procedures]
```

---

## 17. Software Stack Architecture

```mermaid
graph TD
    A[Operator / Engineering User] --> B[HMI / Dashboard / SCADA]
    B --> C[PLC / Safety PLC]
    C --> D[Drives / Remote I/O / Field Devices]

    C --> E[OPC UA / MQTT / Edge Services]
    E --> F[Historian / Database / Logging]
    E --> G[Analytics / Reporting]

    H[Version Control / CI / Testing] --> E
    H --> C

    I[Cybersecurity Controls] --> B
    I --> C
    I --> E
```

---

## 18. Cybersecurity Overlay for Controls

```mermaid
graph LR
    A[Enterprise Zone] --> B[Site Operations Zone]
    B --> C[Supervisory Zone]
    C --> D[Control Zone]
    D --> E[Safety Zone]
    D --> F[Field Devices]

    G[IEC 62443 Policies] --> A
    G --> B
    G --> C
    G --> D
    G --> E
```

---

## 19. Installation and Pre-Commissioning Workflow

```mermaid
flowchart TD
    A[Installation complete] --> B[Mechanical inspection]
    B --> C[Wiring verification]
    C --> D[Continuity / insulation checks]
    D --> E[Loop checks]
    E --> F[Calibration]
    F --> G[Device configuration check]
    G --> H[Interlock verification]
    H --> I[Ready for commissioning]
```

---

## 20. Calibration Workflow

```mermaid
flowchart LR
    A[Identify calibrated devices] --> B[Verify range and units]
    B --> C[Apply reference input]
    C --> D[Adjust / trim]
    D --> E[Record as-found / as-left]
    E --> F[Update calibration sheet]
    F --> G[Release for commissioning]
```

---

## 21. Commissioning and Validation Workflow

```mermaid
flowchart TD
    A[Pre-commissioning complete] --> B[Power-up checks]
    B --> C[Functional sequence checks]
    C --> D[Alarm verification]
    D --> E[Safety interlock tests]
    E --> F[Stop time / shutdown tests]
    F --> G[FAT / SAT closeout]
    G --> H[Validation report]
    H --> I[Operational handover]
```

---

## 22. Maintenance and Lifecycle Support Loop

```mermaid
flowchart LR
    A[Operate system] --> B[Preventive maintenance]
    B --> C[Proof testing]
    C --> D[Recalibration]
    D --> E[Review diagnostics / alarms]
    E --> F[Manage changes / MOC]
    F --> G[Update drawings / software revisions]
    G --> H[Spare parts / obsolescence review]
    H --> A
```

---

## 23. Industry Standards Matrix Navigator

```mermaid
graph TD
    A[Industry Matrix] --> B[Semiconductor]
    A --> C[Food and Beverage]
    A --> D[Warehouse Automation]
    A --> E[Medical]
    A --> F[Energy and Power]
    A --> G[Oil and Gas]
    A --> H[Marine]
    A --> I[Nuclear]
    A --> J[Agriculture]

    B --> B1[ISO 12100 / ISO 13849 / IEC 60204 / SEMI]
    C --> C1[ISO 12100 / ISO 13849 / IEC 60204 / hygiene constraints]
    D --> D1[ISO 12100 / ISO 13849 / NFPA 79]
    E --> E1[Medical-specific frameworks]
    F --> F1[IEC 61508 / IEC 62443]
    G --> G1[IEC 61511 / IEC 61508 / IEC 60079]
    H --> H1[Marine electrical and safety frameworks]
    I --> I1[Nuclear-specific frameworks]
    J --> J1[ISO 12100 / agriculture-specific safety frameworks]
```

---

## 24. Semiconductor Standards Route Example

```mermaid
flowchart TD
    A[Semiconductor equipment concept] --> B[ISO 12100]
    B --> C[ISO 13849-1]
    C --> D[IEC 60204-1]
    D --> E[SEMI S2 / related SEMI requirements]
    E --> F[IEC 62443]
    F --> G[Scenario and validation documents]
```

---

## 25. US Industrial Control Panel Route Example

```mermaid
flowchart TD
    A[US industrial control panel] --> B[NEC]
    A --> C[NFPA 79]
    A --> D[UL 508A]
    C --> E[Machine electrical requirements]
    D --> F[Panel construction / SCCR]
    B --> G[Installation code path]
    E --> H[Panel documentation and testing]
    F --> H
    G --> H
```

---

## 26. Global Machine Route Example (US + EU)

```mermaid
flowchart TD
    A[Global machine project] --> B[ISO 12100]
    B --> C{Safety route}
    C --> D[ISO 13849-1]
    C --> E[IEC 62061]
    D --> F[IEC 60204-1]
    E --> F
    F --> G[US adaptation: NFPA 79 / UL 508A / NEC]
    G --> H[Common design core + regional compliance overlays]
```

---

## 27. Chemical / Process Skid Route Example

```mermaid
flowchart TD
    A[Chemical dosing or process skid] --> B[Hazard and risk review]
    B --> C[IEC 61511]
    C --> D[IEC 61508]
    D --> E{Hazardous area?}
    E -->|Yes| F[IEC 60079 family]
    E -->|No| G[Standard industrial installation]
    F --> H[Shutdown logic / SIS / loop design]
    G --> H
    H --> I[Proof test and lifecycle support]
```

---

## 28. Safety PLC Software + Networked Control + Cybersecurity Scenario

```mermaid
graph TD
    A[Safety PLC application] --> B[Safety inputs and interlocks]
    A --> C[Standard PLC and HMI]
    A --> D[Industrial network]
    D --> E[Remote I/O / drives]
    D --> F[Historian / edge services]

    G[IEC 61131-3] --> C
    H[IEC 62443] --> D
    I[ISO 13849 / IEC 62061 / IEC 61511] --> A
    J[Validation and change control] --> A
    J --> C
    J --> D
```

---

## 29. Scenario Explorer Model

```mermaid
graph TD
    A[Scenario Explorer] --> B[Robotic Cell]
    A --> C[Conveyor / Sorter]
    A --> D[Chemical Dosing Skid]
    A --> E[Hydraulic Machine]
    A --> F[Semiconductor Tool]
    A --> G[Food Processing Machine]
    A --> H[Offshore Process Skid]

    B --> X[Lifecycle + standards + software stack]
    C --> X
    D --> X
    E --> X
    F --> X
    G --> X
    H --> X
```

---

## 30. Interview Answer Logic: How I Choose Standards

```mermaid
flowchart TD
    A[Define machine or process boundary] --> B[Identify hazards and safe state]
    B --> C{Machinery or process?}
    C -->|Machinery| D[ISO 12100]
    C -->|Process| E[IEC 61511]
    D --> F{PL or machinery SIL route?}
    F --> G[ISO 13849-1]
    F --> H[IEC 62061]
    E --> I[IEC 61508 foundation]
    G --> J[Electrical implementation]
    H --> J
    I --> J
    J --> K[NEC / NFPA 79 / UL 508A / IEC 60204-1]
    K --> L[Software / cybersecurity / validation / lifecycle support]
```

---

## 31. Repository-to-Website Content Flow

```mermaid
graph LR
    A[Repository Source Docs] --> B[Standards Pages]
    A --> C[Lifecycle Pages]
    A --> D[Industry Pages]
    A --> E[Scenario Pages]
    A --> F[Crosswalk Pages]

    B --> G[Website Navigation]
    C --> G
    D --> G
    E --> G
    F --> G
```

---

## 32. Trust Boundary Diagram

```mermaid
graph TD
    A[Website Overview Layer] --> B[Paraphrased guidance]
    A --> C[Navigation and routing]
    A --> D[Scenario learning]

    E[Repository Detail Layer] --> F[Deeper technical source material]
    E --> G[Reference models]
    E --> H[Crosswalk notes]

    I[Purchased / official standards] --> J[Authoritative clause-level requirements]

    A -. does not replace .-> I
    E -. does not replace .-> I
```

---

## 33. MVP vs Phase 2 Expansion Map

```mermaid
graph TD
    A[MVP] --> B[Home]
    A --> C[Standards Directory]
    A --> D[Lifecycle Guide]
    A --> E[Industry Matrix]
    A --> F[Scenario Explorer]
    A --> G[Crosswalks]

    H[Phase 2] --> I[Interactive graph]
    H --> J[Search and filters]
    H --> K[Linked standards cards]
    H --> L[Printable diagrams]
    H --> M[Interview answer mode]
    H --> N[Scenario comparison mode]
```

---

## 34. Recommended Diagram Priority

```mermaid
graph TD
    A[Priority 1] --> A1[Lifecycle flow]
    A --> A2[Standards relationship graph]
    A --> A3[Machinery vs process routing]
    A --> A4[7-layer architecture]
    A --> A5[Control vs safety separation]

    B[Priority 2] --> B1[Industry matrix navigator]
    B --> B2[Scenario explorer]
    B --> B3[Software stack architecture]
    B --> B4[Commissioning workflow]
    B --> B5[Maintenance loop]
```
