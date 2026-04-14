Below is a **worked scenario** for a **UPW system** showing:

* what the **regular control system** does
* what the **SIS** does
* what a **SIF** looks like
* what **components and sensors** are used
* how the **logic works**
* how this sits **on top of normal machine safety**
* several **visual layers** to make it easier to understand

This is a **conceptual engineering example**, not a certified design package. Real SIL assignment, device selection, trip setpoints, proof test intervals, and architecture must come from **HAZOP/LOPA, site standards, utility process requirements, and OEM data**.

---

# 1. Scenario: UPW Distribution and Storage Skid

Assume a semiconductor facility has a **UPW polishing and distribution system** with:

* incoming RO/EDI treated water
* UPW storage tank
* recirculation loop
* distribution pumps
* UV / TOC reduction unit
* final filters
* heat exchanger
* branch supply to fab users
* return line back to tank / loop

The system’s normal purpose is to deliver:

* very high purity water
* stable pressure
* stable flow
* stable temperature
* continuous recirculation
* no particle contamination
* no stagnant zones

---

# 2. Why UPW needs both normal control and safety control

A UPW skid is not usually “high hazard” like toxic gas or flammable solvent, but it can still create serious problems:

## Process risks

* tank overflow causing water damage
* pump deadhead / overpressure
* loss of circulation causing temperature drift or quality degradation
* dry running pump damage
* cross-contamination event
* branch header pressure excursion damaging downstream equipment
* chemical cleaning skid interface causing accidental misrouting

## Machine risks

* rotating pump shafts
* motor starters / VFD cabinets
* moving valve actuators
* maintenance access doors
* electrical shock
* lockout/tagout hazards

So you end up with **two protection domains**:

## A. Regular machine safety

This protects people from machinery hazards:

* E-stops
* cabinet door interlocks
* motor safe stop / STO
* maintenance lockout
* guard switches

## B. Process safety / SIS

This protects the process and facility from hazardous process states:

* tank high-high level trip
* pump low suction trip
* discharge overpressure trip
* overflow containment response
* critical quality diversion / isolation

That distinction is the same point from IEC 61511: **process SIS is separate from normal control and separate from machine safety logic**.  

---

# 3. First define the three layers

## Layer 1 — Basic Process Control System (BPCS)

This is the normal PLC/HMI/SCADA control:

* start/stop pumps
* maintain loop pressure
* maintain tank level
* regulate temperature
* switch duty/standby pumps
* monitor conductivity/resistivity, TOC, flow, pressure
* run alarms and trends

## Layer 2 — Machine safety

This is the safety relay / safety PLC / STO / E-stop layer:

* local emergency stop
* cabinet safety interlock
* maintenance access interlock
* motor STO
* safe shutdown for personnel protection

## Layer 3 — SIS / SIF

This is the independent process protection layer:

* separate sensors where needed
* separate logic solver
* separate trip path to final elements
* drives process to safe state when a hazardous process condition occurs

---

# 4. Example hazardous scenario for UPW

We need one scenario to build the example around.

## Scenario

**UPW storage tank inlet control valve fails open while outlet demand is low.**
The tank continues filling. Normal level control fails to stop it. If not stopped:

* tank overflows
* water floods utility area
* electrical cabinets may be affected
* contamination and facility downtime occur
* floor drain capacity may be exceeded

This is a good process-safety-style scenario.

---

# 5. Define the SIS and SIF for this scenario

## SIS

The **Safety Instrumented System** is the whole dedicated protection system for process trips in the UPW skid.

Example SIS for this skid may include:

* independent level switches/transmitters
* safety logic solver
* hardwired trip outputs
* shutdown valve(s)
* pump trip command
* trip alarm annunciation
* reset / bypass control with management rules

## SIF-001

One individual function inside that SIS:

### SIF-001 — UPW Tank High-High Level Shutdown

**Cause:** tank reaches dangerous high-high level
**Action:** close feed isolation valve and stop transfer pump
**Safe state:** no further water enters tank

That is one SIF.

---

# 6. Typical system architecture

## 6.1 Normal control architecture

```mermaid
flowchart LR
    A[Level Transmitter LT-101] --> B[Main PLC]
    C[Pressure Transmitter PT-201] --> B
    D[Flow Transmitter FT-301] --> B
    E[Temperature Transmitter TT-401] --> B
    F[Resistivity Analyzer AIT-501] --> B

    B --> G[VFD Pump P-101A]
    B --> H[VFD Pump P-101B]
    B --> I[Control Valve LCV-101]
    B --> J[Bypass Valve XV-102]
    B --> K[HMI/SCADA]
```

This is the **BPCS**.

---

## 6.2 Process safety architecture with SIS

```mermaid
flowchart LR
    A1[Independent High-High Level Switch LSHH-101A] --> S[Safety PLC / SIS Solver]
    A2[Independent High-High Level Switch LSHH-101B] --> S

    S --> V1[Shutdown Valve SDV-101 Feed Isolation]
    S --> M1[Trip Transfer Pump P-001]
    S --> AL[Hardwired Trip Alarm]
    S --> PLCI[Trip Status to Main PLC]

    PLCI --> HMI[HMI/SCADA Display]
```

This is the **SIS path**, separate from the normal control path.

---

## 6.3 Machine safety architecture

```mermaid
flowchart LR
    ES1[E-Stop PB] --> SR[Safety Relay / Safety PLC]
    GD1[Guard Door Interlock] --> SR
    MS1[Maintenance Access Switch] --> SR

    SR --> STO1[VFD STO - Pump A]
    SR --> STO2[VFD STO - Pump B]
    SR --> MCC[Motor Contactor Safe Drop]
```

This is **personnel/machine protection**, not the process SIS.

---

# 7. Components and sensors

Now make it concrete.

## 7.1 For normal process control

### Tank and level control

* **LT-101**: continuous radar or guided-wave level transmitter
* **LCV-101**: modulating inlet control valve
* **LSL-101**: low-level switch for pump protection
* **LSH-101**: high-level alarm switch

### Pump skid

* **P-101A / P-101B**: duty/standby recirculation pumps
* **VFD-A / VFD-B**: variable speed drives
* **PT-201**: suction pressure transmitter
* **PT-202**: discharge pressure transmitter
* **FT-301**: recirculation flow transmitter
* **TSH-401**: motor bearing or winding high temp switch
* **Vibration switch** if required

### Water quality

* **AIT-501**: resistivity/conductivity analyzer
* **AIT-502**: TOC analyzer
* **AIT-503**: dissolved oxygen or silica analyzer if used
* **DPIT-601**: differential pressure across final filter
* **TT-402**: loop temperature transmitter

### Valves

* modulating diaphragm valves
* pneumatically actuated isolation valves
* fail-closed or fail-last depending on design intent
* feedback limit switches: open/closed proof

---

## 7.2 For the SIS / SIF path

For **SIF-001 Tank High-High Level Shutdown**, use dedicated protective devices:

* **LSHH-101A**: independent high-high level switch
* **LSHH-101B**: second independent high-high level switch
* **SIS logic solver**: safety PLC or dedicated logic solver
* **SDV-101**: fail-closed feed shutdown valve
* **P-001 trip output**: de-energize transfer pump starter / VFD run permit
* **trip annunciator**
* **manual reset station**
* **bypass key switch** with strict procedural control if allowed

Possible architecture:

* **1oo2 sensing** for high-high trip voting
* **1oo1 final element** for shutdown valve
* pump trip in parallel for extra protection

---

## 7.3 For machine safety

* E-stop pushbuttons
* safety relay or machine safety PLC
* safety-rated door switches
* VFD STO channels
* lockable disconnect switches
* motor contactor feedback
* safety status indicators

---

# 8. Separation of duties: what each system is allowed to do

This is where many designs become messy.

## Main PLC/BPCS responsibilities

* maintain tank at normal operating level
* modulate LCV-101
* start/stop duty pump based on schedule and demand
* switch lead/lag pumps
* alarm on high level, low flow, low resistivity, high DP, etc.
* trend and log all data
* perform non-safety permissives

## SIS responsibilities

* monitor independent trip condition
* ignore normal control objectives
* execute trip to safe state
* latch trip
* require controlled reset
* provide trip status only, not depend on BPCS for action

## Machine safety responsibilities

* protect personnel from hazardous motion/energy
* force safe torque off or safe motor shutdown
* operate independently of operator software controls
* not be replaced by normal PLC logic

---

# 9. Control philosophy: normal operation vs abnormal protection

## 9.1 Normal operation

The PLC runs the UPW skid like this:

1. Tank level LT-101 reads current level
2. PLC modulates inlet valve LCV-101
3. Pumps maintain header pressure
4. Quality analyzers verify resistivity / TOC / temp
5. If one pump fails, standby pump starts
6. SCADA trends all process values

### Simple normal logic

* maintain tank level at 60%
* high alarm at 80%
* high-high trip setpoint at 92%
* low alarm at 25%
* low-low permissive stop at 10%

The key point: **normal level control uses LT-101 and LCV-101**.
The **trip function should not depend only on that same chain**.

---

## 9.2 Abnormal but non-SIS condition

Suppose level rises above normal high alarm but not yet dangerous.

BPCS actions:

* alarm operator
* command inlet valve closed
* maybe stop feed pump by normal PLC command
* log event

This is still **control/alarm layer**, not SIS.

---

## 9.3 Dangerous condition requiring SIF

Suppose:

* inlet control valve failed open
* PLC output failed
* operator did not respond
* level continues rising

At high-high level, **independent level switches** activate.

### SIF-001 action

When trip condition is satisfied:

* safety PLC trips
* SDV-101 de-energizes and closes
* transfer feed pump trips
* trip is latched
* alarm horn / beacon activates
* main PLC receives trip status
* operator sees “SIS TRIP: TANK HIGH-HIGH LEVEL”

This is the process safety layer.

---

# 10. Detailed SIF design example

## SIF-001 — UPW Tank High-High Level Shutdown

### Hazard

Overflow of UPW storage tank due to failure of normal level control

### Initiating causes

* inlet control valve fails open
* PLC analog output fails high
* wrong setpoint or software bug
* operator leaves manual mode open
* instrument drift / false low reading on normal LT

### SIF purpose

Prevent overflow by stopping further inflow

### Inputs

* LSHH-101A
* LSHH-101B

### Voting

* either 1oo2 or 2oo2 depending risk/availability philosophy

#### Option A: 1oo2

* trip if either switch trips
* safer against dangerous non-trip
* more nuisance trips

#### Option B: 2oo2

* both switches must agree
* fewer nuisance trips
* weaker fault tolerance for hidden failure

For water utility systems, many teams may choose **1oo2 or 1oo1D style thinking** if overflow consequence is mainly property/process damage, but final choice must come from risk study.

### Logic solver

* safety PLC with dedicated inputs/outputs
* separate power and I/O segmentation preferred

### Final elements

* SDV-101 fail-close feed isolation valve
* feed pump trip relay / VFD run permit removal

### Safe state

* inflow isolated
* pump stopped
* no restart until reset and condition normal

### Reset rule

Reset allowed only when:

* both level switches are normal
* operator performs reset locally or from secure HMI role
* cause reviewed
* bypass removed

---

# 11. Truth table for the SIF

Assume 1oo2 trip voting.

| LSHH-101A | LSHH-101B | SIS Action |
| --------- | --------: | ---------- |
| Normal    |    Normal | No trip    |
| Trip      |    Normal | Trip       |
| Normal    |      Trip | Trip       |
| Trip      |      Trip | Trip       |

If 2oo2 were used:

| LSHH-101A | LSHH-101B | SIS Action                 |
| --------- | --------: | -------------------------- |
| Normal    |    Normal | No trip                    |
| Trip      |    Normal | No trip, discrepancy alarm |
| Normal    |      Trip | No trip, discrepancy alarm |
| Trip      |      Trip | Trip                       |

---

# 12. Example pseudo-logic

## 12.1 BPCS normal level control

```text
IF AUTO_MODE = TRUE THEN
    LEVEL_PID controls LCV-101 to maintain Tank Level SP
END_IF

IF LT-101 >= HIGH_ALARM THEN
    Raise Alarm "Tank Level High"
END_IF

IF LT-101 >= HIGH_HIGH_WARN THEN
    Command LCV-101 = 0%
    Stop Feed Pump by normal control command
END_IF
```

This is **not the SIS**. This is normal control with alarm response.

---

## 12.2 SIS trip logic

```text
TRIP_CONDITION =
    (LSHH-101A = TRIPPED) OR (LSHH-101B = TRIPPED)

IF TRIP_CONDITION THEN
    DE_ENERGIZE SDV-101
    REMOVE RUN PERMIT TO FEED PUMP
    LATCH SIF-001_TRIP
    ACTIVATE HARDWIRED ALARM
END_IF

RESET_ALLOWED =
    (LSHH-101A = NORMAL) AND
    (LSHH-101B = NORMAL) AND
    (OPERATOR_RESET = TRUE) AND
    (NO_BYPASS_ACTIVE)

IF RESET_ALLOWED THEN
    CLEAR SIF-001_TRIP
END_IF
```

---

# 13. Add another SIF to show the system concept

One SIF is not enough to see the structure clearly. Here is a second realistic one.

## SIF-002 — Pump Low Suction / Dry Run Protection

### Hazard

Recirculation pump runs without adequate suction, causing:

* seal failure
* overheating
* cavitation
* loss of water quality / process interruption

### Inputs

* PSL-201A suction low pressure switch
* FSL-301A low flow switch
* LSL-101 tank low-low level switch

### Action

* stop pump
* close discharge valve if needed
* generate trip
* prevent auto-restart until reset

### Logic philosophy

Pump trip if:

* suction pressure too low for X seconds, or
* suction flow lost, or
* tank low-low level reached

This may be process protection but not always a formal SIS depending on consequence. Still, it shows how SIF thinking scales.

---

# 14. Visualization by layers

## Layered view 1 — Physical process layer

```mermaid
flowchart LR
    IN[UPW Feed Inlet] --> SDV[SDV-101 Shutdown Valve]
    SDV --> TANK[UPW Tank]
    TANK --> PUMP[Recirculation Pump]
    PUMP --> UV[UV / TOC Unit]
    UV --> FILTER[Final Filter]
    FILTER --> HDR[UPW Distribution Header]
    HDR --> FAB[Fab Users]
    FAB --> RET[Return Line]
    RET --> TANK
```

---

## Layered view 2 — Instrumentation layer

```mermaid
flowchart TB
    TANK[UPW Tank]
    LT[LT-101 Continuous Level]
    LSH[LSH-101 High Alarm]
    LSHH1[LSHH-101A Safety Level Switch]
    LSHH2[LSHH-101B Safety Level Switch]
    LSL[LSL-101 Low Level]

    PUMP[Pump Skid]
    PTS[PT-201 Suction Pressure]
    PTD[PT-202 Discharge Pressure]
    FT[FT-301 Recirc Flow]
    TT[TT-401 Temperature]

    QUAL[Quality Monitoring]
    RES[AIT-501 Resistivity]
    TOC[AIT-502 TOC]
    DP[DPIT-601 Filter DP]
```

---

## Layered view 3 — Functional layer

```mermaid
flowchart LR
    subgraph BPCS[Basic Process Control System]
        LT1[LT-101]
        PT1[PT-201/PT-202]
        FT1[FT-301]
        AIT1[AIT-501/AIT-502]
        PLC[Main PLC]
        HMI[SCADA/HMI]
        LT1 --> PLC
        PT1 --> PLC
        FT1 --> PLC
        AIT1 --> PLC
        PLC --> HMI
    end

    subgraph SIS[Safety Instrumented System]
        LSHH1[LSHH-101A]
        LSHH2[LSHH-101B]
        SPLC[Safety PLC]
        SDV[SDV-101]
        PTRIP[Feed Pump Trip]
        LSHH1 --> SPLC
        LSHH2 --> SPLC
        SPLC --> SDV
        SPLC --> PTRIP
    end

    subgraph MS[Machine Safety]
        ESTOP[E-Stop]
        GD[Guard Switch]
        SR[Safety Relay]
        STO[Drive STO]
        ESTOP --> SR
        GD --> SR
        SR --> STO
    end
```

---

## Layered view 4 — Cause and effect

```mermaid
flowchart TD
    A[Normal level control fails] --> B[Tank level rises]
    B --> C[High alarm]
    C --> D[Operator may respond]
    B --> E[High-high level switch trips]
    E --> F[SIS solver trips]
    F --> G[Feed shutdown valve closes]
    F --> H[Feed pump stops]
    G --> I[Overflow prevented]
    H --> I
```

---

# 15. How SIS sits on top of regular machine safety

This is a critical concept.

## Machine safety answers:

“How do I stop hazardous energy so a person is protected?”

Examples:

* E-stop pressed
* guard door opened
* maintenance mode entered

Typical action:

* VFD STO
* motor contactor drop
* actuator power removed

## SIS answers:

“How do I stop the process from entering a hazardous state?”

Examples:

* tank high-high
* pump low suction
* discharge overpressure
* quality diversion failure during contamination scenario

Typical action:

* shut isolation valve
* trip pump
* isolate branch
* divert to drain / reject loop if designed

## They can interact, but one should not casually replace the other

For example:

* Opening a maintenance guard door may stop the pump via machine safety.
* But machine safety alone does **not** replace a process overfill SIF.
* Likewise, a process high-high level trip does **not** automatically satisfy personnel safety requirements.

---

# 16. Recommended control-system structure

For a clean engineering design, structure it like this.

## Level 0 — Field devices

* transmitters
* switches
* analyzers
* valves
* motors
* VFDs

## Level 1 — Controllers

* main PLC for BPCS
* safety PLC / SIS solver
* machine safety relay / safety PLC

## Level 2 — Operations

* HMI
* SCADA
* historian
* alarm management
* maintenance diagnostics

## Level 3 — Engineering / reporting

* trends
* proof test records
* batch/event logs
* MOC records
* maintenance CMMS interface

---

# 17. Suggested sensor list for a robust UPW skid

## Tank

* 1 continuous level transmitter for control
* 1 high alarm switch
* 2 independent high-high switches for SIF
* 1 low-low level switch for pump protection
* optional leak detection in bund / containment

## Pumps

* suction pressure transmitter
* discharge pressure transmitter
* flow transmitter
* motor current / drive feedback
* winding temp or bearing temp switch
* vibration monitor if critical

## Water quality

* resistivity analyzer
* conductivity analyzer if on less pure side
* TOC analyzer
* temperature transmitter
* filter differential pressure
* optional particle counter in critical applications

## Valves

* valve position feedback
* solenoid healthy feedback if used
* air pressure low switch for pneumatic actuators

## Facility protection

* skid leak detector
* sump high level
* panel moisture detector if needed
* floor drain overflow monitoring in sensitive utility area

---

# 18. Example cause-and-effect matrix

| Condition           | BPCS Action                | SIS Action                        | Machine Safety Action     |
| ------------------- | -------------------------- | --------------------------------- | ------------------------- |
| Tank high           | Alarm, close control valve | None                              | None                      |
| Tank high-high      | Normal PLC may also react  | Trip feed valve + stop feed pump  | None                      |
| Pump suction low    | Alarm, stop by permissive  | Optional SIF if risk warrants     | None                      |
| Motor overtemp      | Alarm / controlled stop    | Optional depending design         | None                      |
| E-stop pressed      | PLC sees status only       | None unless integrated by design  | STO / safe motor shutdown |
| Guard door opened   | PLC sees status only       | None                              | STO / safe shutdown       |
| Quality out of spec | Alarm, divert/recirc       | Possible process trip if critical | None                      |

---

# 19. What the operator sees on the HMI

Visualization matters. Separate the displays by intent.

## Screen 1 — Process overview

Show:

* tank level
* recirculation flow
* header pressure
* temperature
* resistivity / TOC
* pump status
* valve positions

## Screen 2 — Safety overview

Show:

* SIS healthy / fault
* each SIF status
* bypass active / inactive
* last trip cause
* reset permissive
* proof test mode status

## Screen 3 — Machine safety overview

Show:

* E-stop chain healthy
* guard circuit healthy
* STO active / inactive
* local disconnect status

## Screen 4 — Cause/effect page

Show:

* trip input
* voted result
* final outputs commanded
* final device feedback
* latch/reset state

That separation helps operators and maintenance avoid confusing:

* alarms
* trips
* safety trips
* machine interlocks

---

# 20. Example HMI safety visualization concept

```mermaid
flowchart TB
    A[SIF-001 Tank HH] --> B{Trip Active?}
    B -->|No| C[Green: Healthy]
    B -->|Yes| D[Red: Latched Trip]

    D --> E[Cause: LSHH-101A or LSHH-101B]
    D --> F[Action: SDV-101 Closed]
    D --> G[Action: Feed Pump Stopped]
    D --> H[Reset Permissive Check]
```

---

# 21. Proof test and maintenance visualization

Because IEC 61511 is lifecycle-driven, include maintenance visuals.

## Recommended maintenance dashboard

For each SIF show:

* SIF tag
* service description
* last proof test date
* next due date
* bypass status
* failed components
* trip history count
* valve stroke test status

Example:

| SIF     | Description             |  Last Test |   Next Due | Status  |
| ------- | ----------------------- | ---------: | ---------: | ------- |
| SIF-001 | Tank high-high shutdown | 2026-03-01 | 2026-09-01 | Healthy |
| SIF-002 | Pump low suction trip   | 2026-02-15 | 2026-08-15 | Healthy |

This is where the standard becomes operationally real, because overdue proof tests degrade the claimed protection performance. 

---

# 22. Practical implementation notes

## Device separation

Do not build a fake SIS by using:

* one normal PLC
* one normal level transmitter
* one shared power supply
* one shared network path
* then just adding a “trip bit”

That is not robust independence.

## Better practice

Use:

* independent high-high switches
* separate safety I/O or safety PLC
* hardwired trip path to final element where appropriate
* feedback confirmation from shutdown valve
* latched trip and controlled reset

## Final element design

For SIF-001, make the feed isolation valve:

* fail-close on loss of energy
* position monitored
* accessible for proof testing
* located where it truly isolates inflow

Because in many SIFs, the final element is the weak point.

---

# 23. Expanded scenario with three protection rings

A strong way to explain it is with concentric rings.

```mermaid
flowchart TD
    A[Ring 1: Normal Control]
    B[Ring 2: Alarm / Operator Response]
    C[Ring 3: SIS Automatic Trip]
    D[Ring 4: Secondary Physical Protection]

    A --> B --> C --> D
```

## Ring 1 — Normal control

* LT-101 controls inlet valve

## Ring 2 — Alarm / operator

* high level alarm
* operator intervention

## Ring 3 — SIS

* high-high independent switches
* safety trip valve closure and feed pump stop

## Ring 4 — passive backup

* overflow containment / bund
* floor drainage
* leak detection

This is classic layered protection thinking.

---

# 24. One complete narrative

Here is the scenario written as an engineering narrative.

## UPW Tank Overfill Protection Narrative

During normal operation, the UPW storage tank level is controlled by the main PLC using LT-101 and modulating control valve LCV-101 to maintain the tank at its normal operating setpoint. High level alarm LSH-101 warns the operator if the tank level rises above the normal operating range. The operator can view level trend, inlet valve command, and pump status on the HMI.

If the normal control loop fails due to inlet valve failure, PLC output failure, incorrect mode selection, or instrument error, the tank level may continue to rise. To prevent overflow, an independent SIS-based SIF is provided.

The SIF uses two independent high-high level switches, LSHH-101A and LSHH-101B, wired to a dedicated safety logic solver. Upon detection of the high-high level trip condition according to the selected voting logic, the safety logic solver shall de-energize shutdown valve SDV-101 causing it to fail closed, and shall simultaneously remove the run permit to the feed pump. The trip shall be latched. A hardwired trip alarm and HMI annunciation shall indicate the cause of trip. Restart shall not occur automatically. Manual reset shall only be permitted after the trip condition clears and the operator performs a controlled reset.

Machine safety functions such as emergency stop pushbuttons, guard interlocks, and VFD STO shall remain separate and shall protect personnel from hazardous energy during maintenance or emergency personnel conditions. These machine safety functions do not replace the process overfill SIF.

That is how the story should read.

---

# 25. Bottom line

For a UPW system, the clean design approach is:

## Normal control

Use the main PLC for:

* level control
* pressure control
* pump sequencing
* quality monitoring
* alarms and trends

## SIS

Use a separate protective layer for credible hazardous process scenarios such as:

* tank high-high overflow
* critical overpressure
* low suction / dry run where risk justifies it
* contamination isolation if the consequence is serious enough

## Machine safety

Use safety relays / safety PLC / STO for:

* E-stops
* access doors
* maintenance hazard protection

## Visualization

Present the system in four views:

* physical process flow
* instrumentation layer
* functional control layer
* cause/effect safety layer

That separation is what keeps the design understandable, maintainable, and defensible.

---

# 26. Starter tag list example

Here is a simple tag naming starter set.

## BPCS tags

* LT-101 Tank Level Transmitter
* LCV-101 Tank Inlet Control Valve
* PT-201 Pump Suction Pressure
* PT-202 Pump Discharge Pressure
* FT-301 Recirculation Flow
* AIT-501 Resistivity Analyzer
* AIT-502 TOC Analyzer
* P-101A Duty Pump
* P-101B Standby Pump

## SIS tags

* LSHH-101A Tank High-High Level Switch A
* LSHH-101B Tank High-High Level Switch B
* SDV-101 Feed Shutdown Valve
* SIF-001 Tank Overfill Shutdown
* SIF-002 Pump Dry Run Trip
* SIS-PLC-01 Safety Logic Solver

## Machine safety tags

* ES-001 Emergency Stop
* GS-001 Guard Switch
* STO-101A Pump A Safe Torque Off
* STO-101B Pump B Safe Torque Off

---

# 27. Recommended next step

The strongest next deliverable would be one of these:

1. a **formal SRS-style document** for the UPW SIFs
2. a **cause-and-effect matrix** for the entire UPW skid
3. a **PLC + SIS + machine safety architecture drawing** in panel/I/O style
4. a **semiconductor facility version** with bulk chemical distribution, reclaim, and drain interfaces

I recommend doing **#2 and #3 next**, because that turns this from concept into controls-engineering structure.
