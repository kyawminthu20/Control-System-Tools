# PLC Ladder Logic: Organization, Definition, and Execution Algorithm

## 1. Simplified explanation

PLC ladder logic is a graphical programming language used to control industrial machines.

It resembles an electrical relay diagram:

```text
|----[ Start Pushbutton ]----[/ Stop Pushbutton ]----( Motor )----|
```

The PLC repeatedly performs this process:

1. Read all physical inputs.
2. Evaluate the ladder program.
3. Calculate the required output states.
4. Update the physical outputs.
5. Perform communication and diagnostics.
6. Repeat.

This repeating process is called the **PLC scan cycle**.

A ladder program is normally evaluated:

* From the first rung to the last rung.
* From left to right within each rung.
* From top to bottom through the routine.

---

# 2. Basic ladder logic structure

A ladder diagram contains two vertical power rails and multiple horizontal rungs.

```text
 Left rail                                            Right rail
    |                                                     |
    |----[ Condition 1 ]----[ Condition 2 ]----( Output )-|
    |                                                     |
    |----[ Condition 3 ]----+------------------( Output )--|
    |                       |
    |----[ Condition 4 ]----+
    |                                                     |
```

Each horizontal line represents one control rule or logical expression.

For example:

```text
|----[ Start ]----[/ Stop ]----( Motor_Run )----|
```

Equivalent Boolean logic:

```text
Motor_Run = Start AND NOT Stop
```

---

# 3. Common ladder logic elements

## Normally open contact

```text
----[ Input ]----
```

The instruction is true when the referenced bit or Boolean tag is `1`.

Example:

```text
----[ Start_PB ]----
```

This becomes true when `Start_PB = TRUE`.

In Rockwell terminology, this is commonly called:

```text
XIC — Examine If Closed
```

It does not necessarily represent a physical normally open electrical contact. It simply checks whether the referenced bit is true.

---

## Normally closed contact

```text
----[/ Input ]----
```

The instruction is true when the referenced bit is `0`.

Example:

```text
----[/ Fault ]----
```

This is true while `Fault = FALSE`.

In Rockwell terminology:

```text
XIO — Examine If Open
```

---

## Output coil

```text
----( Output )----
```

The output instruction writes a Boolean result.

Example:

```text
----( Motor_Command )----
```

When the rung is true:

```text
Motor_Command = TRUE
```

When the rung is false:

```text
Motor_Command = FALSE
```

In Rockwell systems, this is commonly called:

```text
OTE — Output Energize
```

---

## Set and reset instructions

```text
----(S)----
----(R)----
```

Or, in Rockwell terminology:

```text
OTL — Output Latch
OTU — Output Unlatch
```

A set or latch instruction keeps a bit true after the original condition disappears.

Example:

```text
|----[ Start_PB ]----------------(S Motor_Request )----|

|----[ Stop_PB ]-----------------(R Motor_Request )----|
```

Use set/reset logic carefully. A latched bit can remain active until a specific reset instruction executes.

---

## Timer

A timer measures how long a condition remains true.

```text
|----[ Motor_Run ]----[ TON Motor_Start_Timer 5 s ]----|
```

Typical timer data includes:

* `PRE`: preset time
* `ACC`: accumulated time
* `EN`: timer enabled
* `TT`: timer timing
* `DN`: timer done

Example:

```text
Motor_Start_Timer.PRE = 5000 ms
```

After `Motor_Run` remains true for five seconds:

```text
Motor_Start_Timer.DN = TRUE
```

---

## Counter

A counter counts events or transitions.

```text
|----[ Part_Sensor_OneShot ]----[ CTU Part_Count ]----|
```

Typical counter fields:

* `PRE`: preset count
* `ACC`: accumulated count
* `DN`: count reached preset

A one-shot is usually required so the PLC counts one event rather than one count during every scan.

---

## Comparison instructions

Examples:

```text
EQU    Equal
NEQ    Not equal
GRT    Greater than
GEQ    Greater than or equal
LES    Less than
LEQ    Less than or equal
```

Example:

```text
|----[ Tank_Level >= 80.0 ]------------( High_Level )----|
```

---

## Mathematical instructions

Examples:

```text
ADD
SUB
MUL
DIV
CPT
MOV
```

Example:

```text
Scaled_Pressure = Raw_Input × Scale_Factor + Offset
```

---

# 4. How a ladder program is organized

The exact structure depends on the PLC manufacturer, but most modern PLC projects follow a hierarchy similar to this:

```text
Controller
├── Hardware configuration
├── Network configuration
├── Global variables or controller tags
├── Tasks
│   ├── Programs
│   │   ├── Local variables or program tags
│   │   ├── Main routine
│   │   ├── Equipment routines
│   │   ├── Alarm routines
│   │   └── Diagnostic routines
│   └── Additional programs
└── User-defined data types and function blocks
```

## Typical hierarchy

### Controller or CPU

The controller is the complete PLC processor.

It contains:

* Hardware configuration
* Communication configuration
* Tasks
* Programs
* Tags
* Diagnostics
* Security settings

---

### Task

A task determines **when and how often a program executes**.

Common task types include:

#### Continuous task

Runs repeatedly whenever processor time is available.

```text
Run program
Run program again
Run program again
...
```

#### Periodic task

Runs at a defined interval.

Example:

```text
Every 10 milliseconds
Every 100 milliseconds
Every 1 second
```

Periodic tasks are useful for:

* Motion control
* PID control
* Fast machine sequencing
* Data sampling
* Slow monitoring functions

#### Event task

Runs when a defined event occurs.

Examples:

* High-speed input event
* Motion event
* Communication event
* Hardware interrupt

---

### Program

A program normally represents a machine, process area, or major function.

Examples:

```text
Conveyor_Program
Pump_Station_Program
Tank_Control_Program
Safety_Interface_Program
Utility_Program
```

---

### Routine

A routine contains the actual control instructions.

A practical machine program may use routines such as:

```text
00_Main
10_IO_Mapping
20_Permissives
30_Interlocks
40_Sequence
50_Equipment_Control
60_Alarms
70_HMI_Interface
80_Diagnostics
90_Output_Mapping
```

The main routine calls the required routines in a controlled order.

Example:

```text
Main Routine
    JSR IO_Mapping
    JSR Permissives
    JSR Interlocks
    JSR Sequence
    JSR Equipment_Control
    JSR Alarms
    JSR HMI_Interface
    JSR Output_Mapping
```

`JSR` means jump to subroutine in Rockwell terminology.

---

# 5. How tags and variables are defined

Older PLCs often used fixed memory addresses:

```text
I:0/0
O:0/1
B3:0/0
N7:0
T4:0
C5:0
```

Modern PLCs commonly use descriptive tags:

```text
Start_PB
Stop_PB
Motor_101_RunCmd
Motor_101_Running
Tank_101_Level
Tank_101_HighHighAlarm
```

## Common data types

| Data type  | Description             | Example             |
| ---------- | ----------------------- | ------------------- |
| BOOL       | True or false value     | `Motor_RunCmd`      |
| INT        | 16-bit integer          | `Part_Count`        |
| DINT       | 32-bit integer          | `Production_Total`  |
| REAL       | Floating-point number   | `Tank_Level_Pct`    |
| TIMER      | Timer structure         | `Motor_Start_Timer` |
| COUNTER    | Counter structure       | `Part_Counter`      |
| STRING     | Text value              | `Batch_Name`        |
| ARRAY      | Multiple similar values | `Motor_Status[10]`  |
| STRUCT/UDT | Group of related values | `Motor_101`         |

---

## User-defined data type example

Instead of creating unrelated tags:

```text
Motor_101_StartCmd
Motor_101_StopCmd
Motor_101_Running
Motor_101_Faulted
Motor_101_Overload
Motor_101_Runtime
```

A structured motor tag can be created:

```text
Motor_101.StartCmd
Motor_101.StopCmd
Motor_101.Running
Motor_101.Faulted
Motor_101.Overload
Motor_101.Runtime
```

This improves organization and makes the program easier to reuse.

---

# 6. The PLC scan algorithm

A simplified PLC execution algorithm is:

```text
START SCAN

1. Read physical inputs
2. Copy input states into input memory
3. Execute scheduled tasks
4. Execute programs
5. Execute routines
6. Evaluate ladder rungs
7. Update output memory
8. Write output memory to physical outputs
9. Perform communications
10. Perform diagnostics

REPEAT
```

In pseudocode:

```text
while PLC_is_running:

    input_image = read_physical_inputs()

    execute_continuous_task()
    execute_due_periodic_tasks()
    execute_pending_event_tasks()

    update_output_image()

    write_physical_outputs(output_image)

    service_communications()
    perform_diagnostics()
```

Actual PLC processors may perform some of these operations differently, especially for remote I/O, immediate input/output instructions, motion systems, safety processors, or asynchronous communications.

---

# 7. How one rung is evaluated

Consider this rung:

```text
|----[ Auto_Mode ]----[/ Faulted ]----[ Start_Request ]----( Pump_RunCmd )----|
```

The PLC evaluates it as:

```text
Pump_RunCmd = Auto_Mode
              AND NOT Faulted
              AND Start_Request
```

Example input values:

```text
Auto_Mode      = TRUE
Faulted        = FALSE
Start_Request  = TRUE
```

Evaluation:

```text
TRUE AND NOT FALSE AND TRUE
TRUE AND TRUE AND TRUE
TRUE
```

Result:

```text
Pump_RunCmd = TRUE
```

If `Faulted` becomes true:

```text
TRUE AND NOT TRUE AND TRUE
TRUE AND FALSE AND TRUE
FALSE
```

Result:

```text
Pump_RunCmd = FALSE
```

---

# 8. Series and parallel logic

## Series contacts represent AND logic

```text
|----[ A ]----[ B ]----( Output )----|
```

Equivalent:

```text
Output = A AND B
```

Both conditions must be true.

---

## Parallel contacts represent OR logic

```text
|----+----[ A ]----+----( Output )----|
|    |             |                  |
|    +----[ B ]----+                  |
```

Equivalent:

```text
Output = A OR B
```

Either condition can make the rung true.

---

## Combined logic

```text
|----[ A ]----+----[ B ]----+----( Output )----|
|             |             |
|             +----[ C ]----+
```

Equivalent:

```text
Output = A AND (B OR C)
```

---

# 9. Start/stop seal-in circuit

A classic motor-control rung is:

```text
|----[/ Stop_PB ]----[/ Overload ]----+----[ Start_PB ]----+----( Motor_Run )----|
|                                     |                    |
|                                     +----[ Motor_Run ]----+
```

Boolean expression:

```text
Motor_Run =
NOT Stop_PB
AND NOT Overload
AND (Start_PB OR Motor_Run)
```

The `Motor_Run` contact is called a:

* Holding contact
* Seal-in contact
* Self-holding contact

When the start pushbutton is pressed, `Motor_Run` becomes true. The parallel `Motor_Run` contact then keeps the rung true after the start pushbutton is released.

Pressing the stop button or tripping the overload breaks the rung.

---

# 10. Physical input versus logical meaning

One of the most important ladder-logic concepts is that the ladder instruction symbol does not always describe the physical contact type.

Suppose a physical stop button is wired normally closed.

```text
Healthy state:
Input voltage present
Stop_Input = TRUE
```

When the button is pressed or the wire breaks:

```text
Stop_Input = FALSE
```

The ladder program may use:

```text
|----[ Stop_Input ]----( System_Permissive )----|
```

Although the physical button is normally closed, the program uses a true-check instruction because the input bit is true during the healthy condition.

Always distinguish between:

1. Physical device contact type
2. Electrical input state
3. PLC tag value
4. Ladder instruction type
5. Intended process meaning

---

# 11. Input and output mapping

A well-organized program should not use raw hardware addresses throughout the control logic.

## Raw input mapping

```text
|----[ Local:1:I.Data.0 ]------------( Start_PB )----|
|----[ Local:1:I.Data.1 ]------------( Stop_OK )-----|
|----[ Local:1:I.Data.2 ]------------( Motor_FB )----|
```

## Internal control logic

```text
|----[ Start_PB ]----[ Stop_OK ]----[/ Motor_Fault ]----( Motor_RunCmd )----|
```

## Output mapping

```text
|----[ Motor_RunCmd ]------------( Local:2:O.Data.0 )----|
```

This separates:

* Physical hardware addresses
* Control logic
* Equipment commands

It also makes simulation and hardware replacement easier.

---

# 12. Permissives, interlocks, and trips

These terms should be clearly separated.

## Permissive

A condition that must be true before equipment is allowed to start.

Examples:

```text
Power_Available
Air_Pressure_OK
Tank_Level_OK
Downstream_Ready
No_Active_Trip
```

Example:

```text
Pump_Start_Permissive =
Power_Available
AND Suction_Valve_Open
AND Tank_Level_OK
AND NOT Pump_Faulted
```

---

## Interlock

A condition that prevents or stops an action because another process condition conflicts with it.

Example:

```text
Valve_A_Open prevents Valve_B from opening
```

```text
|----[ Valve_A_Closed ]----[ Open_B_Request ]----( Valve_B_OpenCmd )----|
```

---

## Trip

A condition that requires immediate shutdown.

Examples:

```text
Motor_Overload
High_High_Pressure
Emergency_Stop
Low_Low_Lubrication_Pressure
Fire_Alarm
```

Example:

```text
Pump_Trip =
Motor_Overload
OR High_High_Pressure
OR Emergency_Stop
```

A trip may also require manual reset after the unsafe condition clears.

---

# 13. Command, status, and feedback

Do not treat a command as proof that equipment is running.

For a motor:

```text
Motor_RunCmd
```

means the PLC requested the motor to run.

```text
Motor_RunningFB
```

means the starter or drive reports that the motor is running.

```text
Motor_Current_OK
```

may provide additional confirmation that current is flowing.

A robust design compares command and feedback:

```text
|----[ Motor_RunCmd ]----[/ Motor_RunningFB ]----[ TON StartFail 5 s ]----|
```

```text
|----[ StartFail.DN ]----------------( Motor_Failed_To_Start )----|
```

This detects a motor that was commanded to run but did not actually start.

---

# 14. Ladder logic for a simple motor

## Input definitions

```text
Start_PB
Stop_OK
Emergency_Stop_OK
Overload_OK
Auto_Mode
Process_Start_Request
Motor_RunningFB
```

## Output definitions

```text
Motor_RunCmd
Motor_Start_Failure
```

## Permissive logic

```text
|----[ Stop_OK ]----[ Emergency_Stop_OK ]----[ Overload_OK ]----( Motor_Permissive )----|
```

## Manual start request

```text
|----[ Start_PB ]----------------( Manual_Start_Request )----|
```

## Final run request

```text
|----+----[ Manual_Mode ]----[ Manual_Start_Request ]----------+----( Motor_Request )----|
|    |                                                         |
|    +----[ Auto_Mode ]------[ Process_Start_Request ]----------+
```

## Run command

```text
|----[ Motor_Request ]----[ Motor_Permissive ]----( Motor_RunCmd )----|
```

## Failed-to-start detection

```text
|----[ Motor_RunCmd ]----[/ Motor_RunningFB ]----[ TON Start_Timer 5 s ]----|
```

```text
|----[ Start_Timer.DN ]----------------( Motor_Start_Failure )----|
```

---

# 15. Sequence control algorithm

For simple controls, individual rungs may be sufficient. For larger machines, use a sequence or state-machine structure.

## Example sequence

```text
State 0   Stopped
State 10  Check permissives
State 20  Open inlet valve
State 30  Start pump
State 40  Running
State 50  Normal shutdown
State 900 Faulted
```

## State transition logic

```text
IF State = 0 AND Start_Request:
    State = 10

IF State = 10 AND All_Permissives_OK:
    State = 20

IF State = 20 AND Inlet_Valve_Open:
    State = 30

IF State = 30 AND Pump_Running:
    State = 40

IF State = 40 AND Stop_Request:
    State = 50

IF Any_Trip:
    State = 900
```

## Ladder-style implementation

```text
|----[ State = 0 ]----[ Start_Request ]----------------[ MOV 10 State ]----|

|----[ State = 10 ]----[ All_Permissives_OK ]-----------[ MOV 20 State ]----|

|----[ State = 20 ]----[ Inlet_Valve_Open ]-------------[ MOV 30 State ]----|

|----[ State = 30 ]----[ Pump_RunningFB ]---------------[ MOV 40 State ]----|

|----[ Any_Trip ]---------------------------------------[ MOV 900 State ]----|
```

## State output logic

```text
|----[ State = 20 ]----------------( Inlet_Valve_OpenCmd )----|

|----+----[ State = 30 ]----+------( Pump_RunCmd )-------------|
|    |                      |
|    +----[ State = 40 ]----+
```

This method makes sequence behavior easier to understand and diagnose.

---

# 16. Scan-order effects

PLC logic is not evaluated simultaneously. Instruction order can affect the result.

Consider:

```text
Rung 1:
|----[ Start ]----------------( Run_Request )----|

Rung 2:
|----[ Run_Request ]----------( Motor_Output )----|
```

If rung 1 executes before rung 2, the new value of `Run_Request` can be used immediately by rung 2 in the same scan.

If the order is reversed:

```text
Rung 1:
|----[ Run_Request ]----------( Motor_Output )----|

Rung 2:
|----[ Start ]----------------( Run_Request )----|
```

`Motor_Output` may not see the updated `Run_Request` value until the next scan.

This is why routine and rung ordering matters.

---

# 17. Multiple writes to the same output

Avoid controlling the same coil from multiple rungs.

Problematic example:

```text
Rung 1:
|----[ Auto_Start ]------------( Motor_RunCmd )----|

Rung 2:
|----[ Manual_Start ]----------( Motor_RunCmd )----|
```

The second rung can overwrite the result of the first rung.

This is often called:

```text
Last rung wins
```

Better design:

```text
|----+----[ Auto_Start ]------+----( Motor_Request )----|
|    |                        |
|    +----[ Manual_Start ]----+
```

Then use one final command rung:

```text
|----[ Motor_Request ]----[ Motor_Permissive ]----( Motor_RunCmd )----|
```

Each command output should preferably have one primary write location.

---

# 18. One-shot operation

Suppose a sensor remains true for 500 milliseconds while the PLC scans every 10 milliseconds.

Without a one-shot, a counter may count approximately:

```text
500 ms / 10 ms = 50 counts
```

A one-shot produces a true result for only one scan when the input changes from false to true.

```text
Sensor:
FALSE → TRUE

One-shot output:
TRUE for one scan only
```

Example:

```text
|----[ Part_Sensor ]----[ ONS Part_Sensor_OS ]----[ CTU Part_Count ]----|
```

Use one-shots for:

* Part counting
* Button actions
* State transitions
* Alarm acknowledgment
* Data logging triggers

---

# 19. Retentive and non-retentive values

## Non-retentive value

Returns to its default state after:

* Power cycle
* Program restart
* Controller mode change

depending on controller configuration.

## Retentive value

Keeps its value through a power cycle or program transition.

Examples:

* Total production count
* Runtime hours
* Recipe number
* Last sequence state
* Calibration values

Use retentive data carefully. A machine restarting from an old retained state can create hazardous or unexpected operation.

A startup routine should validate retained values before using them.

---

# 20. Recommended control-program organization

For a machine or process area:

```text
Program: P101_Pump_System

Routines:
00_Main
10_Input_Mapping
20_Mode_Control
30_Permissives
40_Interlocks
50_Sequence
60_Device_Control
70_Alarms
80_HMI
90_Output_Mapping
```

## 00_Main

Calls routines in the required execution order.

## 10_Input_Mapping

Converts hardware inputs into descriptive process tags.

## 20_Mode_Control

Controls modes such as:

```text
Off
Manual
Auto
Maintenance
Simulation
```

## 30_Permissives

Calculates conditions required before starting.

## 40_Interlocks

Calculates operating restrictions and shutdown conditions.

## 50_Sequence

Controls process states and transitions.

## 60_Device_Control

Controls motors, valves, heaters, drives, and actuators.

## 70_Alarms

Generates alarms, delays, acknowledgment, and reset logic.

## 80_HMI

Processes operator commands and sends status information to the HMI.

## 90_Output_Mapping

Maps internal commands to physical output modules.

---

# 21. Recommended rung structure

A good rung should normally have one clear purpose.

Weak design:

```text
One large rung controlling modes, alarms, timers, valves, motors,
HMI commands, and sequence transitions.
```

Better design:

```text
Rung 1: Calculate permissive
Rung 2: Calculate trip
Rung 3: Calculate start request
Rung 4: Calculate run command
Rung 5: Detect failed start
Rung 6: Generate alarm
```

This makes troubleshooting easier.

---

# 22. Naming convention example

Use a consistent format.

```text
<Area>_<Equipment>_<Signal>
```

Examples:

```text
UTIL_P101_RunCmd
UTIL_P101_RunningFB
UTIL_P101_Faulted
UTIL_P101_StartPermissive
UTIL_P101_FailedToStart
UTIL_P101_RuntimeHr
```

For instruments:

```text
TK101_LT_LevelPct
TK101_LSH_HighLevel
TK101_LSHH_HighHighLevel
TK101_LSL_LowLevel
TK101_LSLL_LowLowLevel
```

Common suffixes:

| Suffix  | Meaning        |
| ------- | -------------- |
| `Cmd`   | Command        |
| `Req`   | Request        |
| `FB`    | Feedback       |
| `Perm`  | Permissive     |
| `Intlk` | Interlock      |
| `Trip`  | Trip condition |
| `Alm`   | Alarm          |
| `SP`    | Setpoint       |
| `PV`    | Process value  |
| `Mode`  | Operating mode |
| `Sts`   | Status         |

---

# 23. Alarm algorithm

A complete alarm usually requires more than a single comparison.

Example high-temperature alarm:

```text
Alarm condition:
Temperature > 80°C
```

Improved design:

```text
1. Detect high temperature
2. Apply an ON delay
3. Set the alarm
4. Record alarm time
5. Display it on the HMI
6. Require acknowledgment
7. Clear it only when the process returns below the reset value
```

Using hysteresis:

```text
Alarm activates above: 80°C
Alarm clears below:    77°C
```

This prevents the alarm from rapidly turning on and off near the threshold.

---

# 24. Analog scaling algorithm

An analog input module may provide a raw value such as:

```text
0 to 32767
```

The transmitter may represent:

```text
4 to 20 mA = 0 to 100 psi
```

Linear scaling formula:

```text
EngineeringValue =
(RawValue - RawMin)
× (EngineeringMax - EngineeringMin)
÷ (RawMax - RawMin)
+ EngineeringMin
```

Example:

```text
Pressure =
(RawInput - 6553)
× (100 - 0)
÷ (32767 - 6553)
```

The exact raw values depend on the PLC and analog module configuration.

The program should also detect:

```text
Under-range
Over-range
Open circuit
Short circuit
Bad channel status
```

---

# 25. Safety-related ladder logic

Standard PLC logic should not be treated as the only protection for hazardous machinery.

Safety functions may require:

* Safety PLC
* Safety-rated I/O
* Safety relays
* Dual-channel devices
* Redundant feedback
* Discrepancy monitoring
* Manual reset
* Safe torque off
* Defined safety integrity or performance level

Examples include:

```text
Emergency stop
Guard door monitoring
Light curtains
Burner management
High-pressure shutdown
Personnel protection
```

The normal PLC may monitor safety status, but it should not bypass or replace the required safety-rated system.

---

# 26. Common ladder-logic design mistakes

## Using the HMI as the only interlock

The PLC must enforce the interlock. Hiding or disabling an HMI button is not sufficient.

## Writing the same coil in multiple locations

This creates scan-order-dependent behavior.

## Confusing command and feedback

`Motor_RunCmd` does not prove the motor is running.

## Counting without a one-shot

The counter increments during every scan.

## Using latch instructions without a clear reset

The machine may remain latched in an unexpected state.

## Ignoring startup conditions

Tags, timers, outputs, and sequence states may behave differently after a power cycle.

## Using very large rungs

Large rungs are difficult to test and diagnose.

## Mixing raw I/O with process logic

Use dedicated input and output mapping.

## Failing to document abnormal behavior

Define what happens during:

* Communication failure
* Sensor failure
* Power loss
* Emergency stop
* Controller restart
* Remote I/O failure
* VFD fault
* Unexpected feedback

---

# 27. Recommended PLC control algorithm

A robust equipment control algorithm can be organized as:

```text
1. Read and validate inputs
2. Scale analog signals
3. Determine equipment availability
4. Determine operating mode
5. Calculate permissives
6. Calculate interlocks and trips
7. Process operator and automatic requests
8. Execute sequence transitions
9. Generate equipment commands
10. Compare commands with feedback
11. Generate alarms and diagnostics
12. Update HMI status
13. Write physical outputs
```

Conceptually:

```text
Validated Inputs
       ↓
Modes and Requests
       ↓
Permissives and Interlocks
       ↓
Sequence Logic
       ↓
Equipment Commands
       ↓
Physical Outputs
       ↓
Feedback Verification
       ↓
Alarms and Diagnostics
```

---

# 28. Final design principle

A good ladder-logic program should make the following questions easy to answer:

1. What is the PLC being asked to do?
2. What conditions allow it to operate?
3. What conditions prevent it from operating?
4. What conditions immediately stop it?
5. What command is being sent?
6. What feedback confirms the command worked?
7. What happens when feedback does not match the command?
8. What happens after power loss or communication failure?
9. How can a technician identify the problem quickly?
10. How does the equipment return to a safe state?

The main purpose of ladder logic is not merely to turn outputs on and off. It is to create a deterministic, diagnosable, and safe control algorithm for the complete operating life of the machine.


=================

# PLC Program Organization, PackML, ISA-88, and Structured Text

A professional PLC project is organized at **three separate levels**:

1. **Execution structure** — when the code runs.
2. **Software structure** — how the code is divided into reusable modules.
3. **Industry architecture** — how equipment states, recipes, alarms, safety, and communications are standardized.

PackML, ISA-88, and ISA-95 are not programming languages. They define **how the control system behaves and how information is organized**. Ladder Diagram, Structured Text, Function Block Diagram, and Sequential Function Chart are methods used to implement that architecture.

---

# 1. IEC 61131-3: the PLC programming foundation

IEC 61131-3 is the main international standard for PLC programming languages. The current edition, IEC 61131-3:2025, defines:

* Structured Text — ST
* Ladder Diagram — LD
* Function Block Diagram — FBD
* Sequential Function Chart — SFC elements for structuring programs and function blocks

It also defines configuration elements used to install and organize programs in a controller. ([IEC Webstore][1])

A simplified hierarchy is:

```text
PLC Configuration
│
├── Controller or CPU
│
├── Tasks
│   ├── Fast task
│   ├── Main machine task
│   ├── Process-control task
│   └── Communication task
│
├── Programs
│   ├── Machine program
│   ├── Utilities program
│   └── Communication program
│
├── Program Organization Units — POUs
│   ├── Programs
│   ├── Function Blocks
│   └── Functions
│
├── Data types
│   ├── Structures
│   ├── Enumerations
│   └── Arrays
│
└── Global and local variables
```

Under IEC 61131-3 terminology, a POU can be a **program, function block, or function**. A function block has internal memory and is instantiated as an object, while a function is normally used for a calculation that does not require retained internal state. ([HelpMe CODESYS][2])

---

# 2. Vendor implementations

The names differ between PLC manufacturers.

## Rockwell ControlLogix

```text
Controller
└── Task
    └── Program
        └── Routine
            └── Instructions and Add-On Instructions
```

Rockwell supports continuous, periodic, and event tasks. Tasks schedule programs, and programs contain routines written in Ladder, Structured Text, Function Block, or SFC. ([Rockwell Automation][3])

Example:

```text
Controller: Packaging_Line_01

ContinuousTask
├── Program_System
├── Program_Conveyor
├── Program_Filler
└── Program_PackML

MotionTask_2ms
└── Program_ServoAxes

CommunicationTask_100ms
├── Program_OPCUA
└── Program_MES
```

## Siemens S7-1200/S7-1500

```text
PLC
├── Organization Blocks — OB
├── Function Blocks — FB
├── Functions — FC
└── Data Blocks — DB
```

Organization blocks connect the operating system to the user program. Function blocks have instance data, functions normally do not maintain instance memory, and data blocks store structured information. ([Siemens Industry Support][4])

Example:

```text
OB1     Main cyclic program
OB30    10 ms process task
OB100   Startup routine

FB100   Motor
FB110   Valve
FB200   PackML state manager
FB300   Unit sequence

DB100   Motor instances
DB200   PackML data
DB300   Recipe data
```

---

# 3. Recommended functional organization

Regardless of PLC manufacturer, the application should be divided into clear functional layers.

```text
Application
│
├── 00_System
│   ├── Startup
│   ├── First scan
│   ├── Controller status
│   └── Watchdogs
│
├── 10_IO_Mapping
│   ├── Digital inputs
│   ├── Analog inputs
│   ├── Network inputs
│   └── Signal validation
│
├── 20_Control_Modules
│   ├── Motors
│   ├── Valves
│   ├── Heaters
│   ├── Instruments
│   └── Drives
│
├── 30_Equipment_Modules
│   ├── Conveyor
│   ├── Pump station
│   ├── Robot station
│   └── Heating system
│
├── 40_Modes_And_States
│   ├── Manual
│   ├── Automatic
│   ├── Maintenance
│   ├── Simulation
│   └── PackML state manager
│
├── 50_Sequence
│   ├── Startup sequence
│   ├── Production sequence
│   ├── Shutdown sequence
│   └── Recovery sequence
│
├── 60_Interlocks
│   ├── Start permissives
│   ├── Operating interlocks
│   ├── Trips
│   └── Command-feedback monitoring
│
├── 70_Alarms
│   ├── Detection
│   ├── Delay and deadband
│   ├── Acknowledgment
│   └── Alarm history
│
├── 80_HMI_And_Integration
│   ├── HMI commands
│   ├── Recipes
│   ├── Production data
│   ├── OPC UA
│   └── MES interface
│
└── 90_Output_Mapping
    ├── Physical outputs
    ├── Network outputs
    └── Safe-state enforcement
```

This structure separates:

```text
Hardware signals
      ↓
Reusable devices
      ↓
Equipment functions
      ↓
Machine or process sequence
      ↓
Line and plant integration
```

---

# 4. Control modules and equipment modules

A good PLC program should follow the physical equipment.

## Control module

A control module represents the lowest practical controllable device.

Examples:

```text
Motor
Valve
VFD
Servo axis
Heater
Analog transmitter
Solenoid
Cylinder
```

Example motor object:

```text
Motor_101
├── CmdStart
├── CmdStop
├── Permissive
├── Interlock
├── RunningFB
├── Faulted
├── FailedToStart
├── Runtime
└── Alarm
```

The motor function block should handle the common behavior of every motor.

## Equipment module

An equipment module coordinates multiple control modules.

Example:

```text
Equipment Module: Feed Conveyor

Devices
├── Conveyor motor
├── Entry photoeye
├── Exit photoeye
├── Jam sensor
└── Guard status

Functions
├── Start conveyor
├── Stop conveyor
├── Clear product
├── Detect jam
└── Report status
```

The main machine sequence should command the equipment module. It should not directly manipulate every motor, valve, and sensor.

---

# 5. PackML organization

PackML was developed by OMAC and adopted by ISA as ISA-TR88.00.02. The current ISA technical report is ISA-TR88.00.02-2022, **Machine and Unit States: An Implementation Example of ISA-88.00.01**. ([OMAC][5])

PackML defines three main elements:

1. **Unit modes**
2. **Machine or unit state models**
3. **PackTags**

PackTags provide standardized command, status, and administrative data. PackML is intended to give machines from different vendors a consistent operational interface and common behavior. ([OPC UA Online Reference][6])

## Simplified PackML architecture

```text
Operator / Line Controller / MES
               │
               ▼
         PackML Interface
     ├── Commands
     ├── Status
     └── Administrative data
               │
               ▼
          Mode Manager
     ├── Production
     ├── Manual
     ├── Maintenance
     ├── Cleaning
     └── Calibration
               │
               ▼
          State Manager
     ├── Stopped
     ├── Starting
     ├── Idle
     ├── Execute
     ├── Holding / Held
     ├── Suspending / Suspended
     ├── Completing / Complete
     └── Aborting / Aborted
               │
               ▼
       Machine Procedures
     ├── Start procedure
     ├── Execute procedure
     ├── Hold procedure
     ├── Stop procedure
     └── Abort procedure
               │
               ▼
       Equipment Modules
               │
               ▼
        Control Modules
```

## Example PackML PLC organization

```text
Program_PackML
├── Main
├── ModeManager
├── StateManager
├── CommandProcessor
├── State_Stopped
├── State_Starting
├── State_Idle
├── State_Execute
├── State_Holding
├── State_Held
├── State_Stopping
├── State_Aborting
├── PackTags
└── Diagnostics
```

The **state manager** decides the current machine state. The individual state procedures perform the required actions.

---

# 6. PackML does not replace the machine sequence

PackML controls the machine’s overall operating condition.

For example:

```text
PackML state = EXECUTE
```

does not itself specify:

```text
1. Clamp the product
2. Move the servo
3. Start dispensing
4. Verify pressure
5. Retract the cylinder
6. Release the product
```

That detailed sequence belongs inside the machine’s execute procedure.

```text
PackML EXECUTE state
          │
          ▼
Production sequence
├── Step 10: Wait for product
├── Step 20: Clamp product
├── Step 30: Process product
├── Step 40: Inspect product
├── Step 50: Release product
└── Step 60: Increment production count
```

PackML answers:

> What overall condition is the machine in?

The machine sequence answers:

> What exact operation is the machine performing?

---

# 7. PackML implemented with Structured Text

Structured Text is commonly suitable for the PackML state manager because state transitions are naturally represented using `CASE` logic.

Conceptual example:

```iecst
CASE UnitState OF

    State_Stopped:
        MachineRunning := FALSE;

        IF CmdReset AND ResetPermissive THEN
            UnitState := State_Resetting;
        END_IF;

        IF CmdAbort THEN
            UnitState := State_Aborting;
        END_IF;


    State_Resetting:
        ResetDevices := TRUE;

        IF ResetComplete THEN
            ResetDevices := FALSE;
            UnitState := State_Idle;
        END_IF;

        IF CmdAbort THEN
            UnitState := State_Aborting;
        END_IF;


    State_Idle:
        MachineReady := TRUE;

        IF CmdStart AND StartPermissive THEN
            UnitState := State_Starting;
        END_IF;

        IF CmdStop THEN
            UnitState := State_Stopping;
        END_IF;


    State_Execute:
        MachineRunning := TRUE;

        IF HoldRequired THEN
            UnitState := State_Holding;

        ELSIF UpstreamBlocked THEN
            UnitState := State_Suspending;

        ELSIF ProductionComplete THEN
            UnitState := State_Completing;

        ELSIF CmdStop THEN
            UnitState := State_Stopping;

        ELSIF CmdAbort THEN
            UnitState := State_Aborting;
        END_IF;


    State_Aborted:
        MachineRunning := FALSE;
        MachineFaulted := TRUE;

        IF CmdClear AND AbortConditionCleared THEN
            UnitState := State_Clearing;
        END_IF;

END_CASE;
```

This is only the state-dispatch layer. Each state should call a separate function block or routine.

```iecst
CASE UnitState OF
    State_Resetting:
        ResetProcedure();

    State_Starting:
        StartProcedure();

    State_Execute:
        ProductionSequence();

    State_Holding:
        HoldProcedure();

    State_Stopping:
        StopProcedure();

    State_Aborting:
        AbortProcedure();
END_CASE;
```

---

# 8. ISA-88 organization

ISA-88 was originally developed for batch control, particularly for pharmaceuticals, food and beverage, chemicals, and other batch-processing applications. It separates the **physical equipment** from the **procedural recipe**. ([isa.org][7])

## Physical model

```text
Enterprise
└── Site
    └── Area
        └── Process Cell
            └── Unit
                └── Equipment Module
                    └── Control Module
```

Example:

```text
Enterprise: Pharmaceutical Company
└── Site: California Plant
    └── Area: Liquid Processing
        └── Process Cell: Mixing
            └── Unit: Mixer 101
                ├── Equipment Module: Ingredient Addition
                ├── Equipment Module: Mixing
                ├── Equipment Module: Heating
                └── Equipment Module: Transfer
```

## Procedural model

```text
Procedure
└── Unit Procedure
    └── Operation
        └── Phase
```

Example:

```text
Procedure: Produce Product A

Unit Procedure: Prepare Mixer
├── Operation: Charge ingredients
│   ├── Phase: Add water
│   ├── Phase: Add chemical A
│   └── Phase: Add chemical B
│
├── Operation: Mix product
│   ├── Phase: Start agitator
│   ├── Phase: Heat product
│   └── Phase: Hold temperature
│
└── Operation: Transfer product
    ├── Phase: Open transfer path
    ├── Phase: Start transfer pump
    └── Phase: Complete transfer
```

ISA-88’s procedural and physical models make it possible to reuse equipment logic with different recipes. ([Automation.com][8])

---

# 9. ISA-88 versus PackML

| Characteristic         | PackML                                 | ISA-88                                       |
| ---------------------- | -------------------------------------- | -------------------------------------------- |
| Primary application    | Machines and production units          | Batch and procedural processes               |
| Main focus             | Modes, states and machine interface    | Equipment hierarchy, procedures and recipes  |
| Typical industries     | Packaging, assembly, material handling | Pharmaceutical, food, chemical, biotech      |
| Main execution concept | Machine state model                    | Procedure → operation → phase                |
| Production recipes     | Basic recipe interface possible        | Comprehensive recipe model                   |
| Equipment structure    | Unit and machine modules               | Units, equipment modules and control modules |
| PLC language           | Any IEC 61131-3 language               | Any IEC 61131-3 language                     |

PackML is an implementation example based on ISA-88 concepts. It applies ISA-88-style state and equipment organization to automated machines. ([isa.org][7])

---

# 10. ISA-95 organization

ISA-95, also published internationally as IEC 62264, addresses integration between manufacturing control and enterprise systems. It defines equipment and activity models and helps define the boundary between plant-floor control, MES, and ERP systems. ([isa.org][9])

```text
Level 4
ERP and business planning
        │
        ▼
Level 3
MES / manufacturing operations management
        │
        ▼
Level 2
SCADA, supervisory control and PLC coordination
        │
        ▼
Level 1
Sensors, actuators and basic control
        │
        ▼
Level 0
Physical process
```

ISA-95 does not tell you how to program a motor rung. It organizes:

* Production scheduling
* Production performance
* Material information
* Equipment capability
* Personnel capability
* Quality information
* Maintenance information
* MES-to-control-system interfaces

ISA-88 and PackML structure the lower-level equipment behavior. ISA-95 structures integration above the equipment level. ISA publishes specific guidance for using ISA-88 and ISA-95 together. ([isa.org][10])

---

# 11. Industry standards and typical PLC languages

| Industry                   | Main architecture or standards                                   | Typical language use                                                           |
| -------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Packaging machinery        | PackML, IEC 61131-3, PLCopen Motion                              | ST for state management; LD for devices and interlocks; SFC/ST for sequence    |
| Food and beverage          | ISA-88 for batching, PackML for packaging, ISA-95                | ST/SFC for recipes; FBD for process control; LD for equipment                  |
| Pharmaceutical and biotech | ISA-88, ISA-95, GAMP 5, FDA 21 CFR Part 11                       | ST/SFC for phase logic; FBD for PID; LD for interlocks                         |
| Chemical and oil/gas       | ISA-88 where batch applies, ISA-18.2, ISA-101, IEC 61511         | FBD for continuous control; ST for calculations; LD for shutdown logic         |
| Automotive manufacturing   | IEC 61131-3, PLCopen Motion, PackML or OEM-specific state models | LD for station logic; ST for sequences and data; motion function blocks        |
| Robotics and motion        | PLCopen Motion, IEC 61131-3, machine-safety standards            | ST for axis coordination; LD for commands; SFC for cell sequence               |
| Semiconductor              | SEMI SECS/GEM, GEM300 and EDA for equipment-host integration     | ST for equipment state/data handling; LD for I/O; vendor-specific architecture |
| Building automation        | ASHRAE 135 BACnet                                                | ST/FBD for HVAC algorithms; LD for simple interlocks                           |
| Power utilities            | IEC 61850 for utility automation interoperability                | ST/FBD/LD depending controller and function                                    |
| Water/wastewater           | IEC 61131-3, ISA-18.2, ISA-101, ISA-95 where applicable          | FBD for PID; ST for sequencing; LD for pumps and permissives                   |

Some of these standards do not define internal PLC code organization. For example, BACnet defines communication and object representation for building systems; IEC 61850 addresses interoperability in power utility automation; and SEMI SECS/GEM/GEM300 defines semiconductor equipment-to-host automation interfaces. The internal PLC program can still use an ISA-88, PackML-like, or owner-specific architecture. ([SEMI][11])

---

# 12. Pharmaceutical controls

Pharmaceutical systems commonly combine several requirements:

```text
ISA-88
    Equipment and recipe organization

GAMP 5
    Computerized-system lifecycle and validation approach

21 CFR Part 11
    Electronic records and electronic signatures

ISA-18.2
    Alarm management

ISA-101
    HMI design

ISA-95
    MES and ERP integration
```

GAMP 5 provides a risk-based good-practice framework for effective, high-quality computerized systems. FDA Part 11 applies when required records are created, maintained, archived, retrieved, transmitted, or submitted electronically under applicable FDA regulations. ([U.S. Food and Drug Administration][12])

A pharmaceutical PLC project might be organized as:

```text
Unit_Mixer101
├── EquipmentModules
│   ├── MaterialCharge
│   ├── Agitation
│   ├── TemperatureControl
│   └── Transfer
│
├── Phases
│   ├── AddMaterial
│   ├── Mix
│   ├── Heat
│   ├── Hold
│   ├── Cool
│   └── Transfer
│
├── RecipeParameters
├── BatchReporting
├── Alarms
└── AuditInterface
```

---

# 13. Semiconductor controls

Semiconductor equipment normally needs two different software organizations.

## Internal equipment control

```text
Machine state
├── Load wafer
├── Align wafer
├── Process wafer
├── Inspect wafer
├── Unload wafer
└── Recover from fault
```

This may be implemented with:

* PLC state machines
* Structured Text
* SFC
* Robot controllers
* PC-based equipment-control software

## Factory host interface

```text
Equipment
   │
   ├── SECS-II messages
   ├── GEM state and events
   ├── Alarms
   ├── Collection events
   ├── Recipe management
   └── Remote commands
   │
   ▼
Factory host / EAP / MES
```

SEMI describes SECS/GEM and GEM300 as standards supporting automated equipment operation and factory-system integration. GEM300 is a family of standards used for 300 mm semiconductor manufacturing equipment. ([SEMI][11])

SECS/GEM does not replace the PLC sequence. It standardizes how the equipment communicates its state, data, events, alarms, and commands to the factory.

---

# 14. Choosing the programming language

## Ladder Diagram

Use Ladder for:

* Start/stop logic
* Permissives
* Interlocks
* Motor control
* Valve control
* Safety-status monitoring
* Simple Boolean troubleshooting
* Command and feedback comparison

Example:

```text
|----[ AutoMode ]----[ StartReq ]----[ AllPermissives ]----[/ Trip ]----( RunCmd )----|
```

Ladder is useful where electricians and maintenance technicians need to trace Boolean conditions online.

## Structured Text

Use Structured Text for:

* State machines
* Sequences
* Arrays
* Loops
* Recipe handling
* Data structures
* Mathematical calculations
* Communication parsing
* Alarm list processing
* Production data
* String processing
* Complex decision logic

Example:

```iecst
FOR Index := 1 TO NumberOfMotors DO
    IF Motors[Index].Faulted THEN
        FaultCount := FaultCount + 1;
    END_IF;
END_FOR;
```

## Function Block Diagram

Use FBD for:

* PID loops
* Analog conditioning
* Signal selection
* Filtering
* Ramp functions
* Process control
* Mathematical signal flow

```text
PressurePV → Scaling → Filtering → PID → OutputLimit → ValveCommand
```

## Sequential Function Chart

Use SFC for:

* Batch phases
* Machine cycles
* Startup procedures
* Shutdown procedures
* Cleaning sequences
* Process transitions

IEC 61131-3 defines SFC elements specifically for structuring the internal organization of programs and function blocks. ([IEC Webstore][1])

---

# 15. Recommended mixed-language design

A strong design does not force the entire PLC into one language.

```text
Main execution and routine calls        Ladder or ST
PackML mode and state manager           Structured Text
Machine production sequence             SFC or Structured Text
Motor and valve control                 Ladder or Function Blocks
Analog signal processing                FBD or Structured Text
PID control                             FBD
Alarm processing                        Ladder + Structured Text
Recipe and data processing              Structured Text
Motion commands                         PLCopen function blocks in ST or LD
Safety logic                            Certified safety language/environment
```

PLCopen Motion defines a common state machine and function blocks for single-axis and multi-axis motion within the IEC 61131-3 framework. ([PLCopen][13])

A useful pattern is to write complex internal logic in Structured Text but expose it to the main program through a simple function-block interface:

```text
Ladder main routine
        │
        ▼
FB_PackMLMachine
        │
        ├── Structured Text state manager
        ├── Structured Text sequence
        ├── Alarm handler
        └── PackTag interface
```

The Ladder programmer sees:

```text
Machine.Enable
Machine.StartCmd
Machine.StopCmd
Machine.State
Machine.Ready
Machine.Running
Machine.Faulted
```

The internal state-machine complexity remains encapsulated.

---

# 16. Safety must remain separate

PackML states such as `STOPPED` or `ABORTED` do not, by themselves, constitute a safety function.

Machine safety may require:

* Safety PLC or safety relay
* Dual-channel emergency stops
* Guard monitoring
* Safe Torque Off
* Feedback monitoring
* Manual safety reset
* Performance Level or SIL verification

ISO 13849-1 defines requirements for safety-related control-system parts, including software. IEC 62061 specifies requirements for the design, integration, and validation of safety-related machine-control systems. IEC 61511 applies to safety instrumented systems in process industries. ([ISO][14])

A proper architecture is:

```text
Safety system
      │
      ├── Removes hazardous energy
      ├── Controls STO
      └── Reports safety status
              │
              ▼
Standard PLC / PackML
      ├── Detects safety unavailable
      ├── transitions to Aborting or Aborted
      └── displays diagnostic information
```

The safety system causes the safe action. PackML reports and coordinates the resulting machine state.

---

# 17. Overall recommended architecture

```text
Enterprise / ERP
        │
        │ ISA-95
        ▼
MES / Manufacturing Operations
        │
        │ OPC UA, SECS/GEM or industry interface
        ▼
Line Control
        │
        │ PackML commands and status
        ▼
Machine / Unit Controller
        │
        ├── Mode manager
        ├── State manager
        ├── Recipe or procedure manager
        ├── Production sequence
        ├── Alarm manager
        └── Diagnostics
        │
        ▼
Equipment Modules
        │
        ▼
Control Modules
        │
        ▼
I/O, drives, instruments and actuators
```

The cleanest general rule is:

```text
IEC 61131-3
Defines the programming languages and basic software elements.

PackML
Defines standardized machine modes, states and interface data.

ISA-88
Defines equipment modules, procedures, phases and recipes.

ISA-95
Defines manufacturing-to-enterprise integration.

ISA-18.2
Defines the alarm-management lifecycle.

ISA-101
Defines HMI design and lifecycle practices.

ISO 13849 / IEC 62061
Define machinery safety-control requirements.

IEC 61511
Defines process safety-instrumented-system requirements.

ISA/IEC 62443
Defines industrial-control-system cybersecurity requirements.
```

ISA-18.2 addresses alarm-system management in process industries, ISA-101 provides a lifecycle framework for industrial HMI design, and ISA/IEC 62443 establishes cybersecurity requirements and processes for industrial automation and control systems. ([isa.org][15])

[1]: https://webstore.iec.ch/en/publication/68533 "IEC 61131-3:2025 | IEC"
[2]: https://content.helpme-codesys.com/en/CODESYS%20Development%20System/_cds_obj_function_block.html "Object: Function Block"
[3]: https://literature.rockwellautomation.com/idc/groups/literature/documents/pm/1756-pm005_-en-p.pdf "Logix 5000 Controllers Tasks, Programs, and Routines"
[4]: https://support.industry.siemens.com/cs/attachments/90885040/81318674_Programming_guideline_DOC_v16_en.pdf "Programming Guideline for S7-1200/1500 - Support"
[5]: https://www.omac.org/packml "PackML | OMAC"
[6]: https://reference.opcfoundation.org/specs/OPC-30050/4 "Concept – OPC UA for PackML - Common Object Model: PackML"
[7]: https://www.isa.org/standards-and-publications/isa-standards/isa-88-standards "ISA-88 Series of Standards - Batch Process Control"
[8]: https://blog.isa.org/modular-systems-speed-simplify-new-industrial-plant-programming "Modular Systems Speed and Simplify New Plant ..."
[9]: https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard "ISA-95 Standard: Enterprise-Control System Integration"
[10]: https://www.isa.org/products/isa-tr88-95-01-2008-using-isa-88-and-isa-95-togeth "ISA-TR88.95.01-2008 Using ISA-88 and ISA-95 Together"
[11]: https://www.semi.org/en/standards-watch-2022-Sept/intro-to-semi-communication-standards "Introduction to SEMI's Communication Standards: SECS ..."
[12]: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application "Part 11, Electronic Records; Electronic Signatures - Scope ..."
[13]: https://www.plcopen.org/standards/motion-control/ "PLCopen Motion Control Standard"
[14]: https://www.iso.org/standard/73481.html "ISO 13849-1:2023 - Safety of machinery"
[15]: https://www.isa.org/standards-and-publications/isa-standards/isa-18-series-of-standards "ISA-18 Series of Standards"


=====================

Yes. PLC programs use many standard **control algorithms and data-handling patterns**. They can be written in Ladder Logic, but some algorithms are easier in Structured Text.

The important distinction is:

* **Ladder instruction**: a vendor-provided operation such as FIFO load, compare, move, timer, or counter.
* **Algorithm**: a collection of instructions organized to solve a problem such as queuing products, sorting motors by runtime, or selecting the next pump.

# Common PLC algorithms

| Algorithm              | Typical purpose                            | Best language      |
| ---------------------- | ------------------------------------------ | ------------------ |
| FIFO queue             | Product tracking, job queues, alarm queues | Ladder or ST       |
| LIFO stack             | Undo/recovery, temporary storage           | Ladder or ST       |
| Circular buffer        | Historical samples, event logs             | ST                 |
| Sorting                | Rank motors, jobs, measurements            | ST preferred       |
| Runtime staging        | Lead/lag pumps, compressors, fans          | Ladder + ST        |
| Round-robin            | Alternate equipment equally                | Ladder             |
| Priority queue         | Select highest-priority request            | ST preferred       |
| Shift register         | Track products along conveyor              | Ladder             |
| State machine          | Machine sequence                           | ST, SFC, or Ladder |
| Debounce/filter        | Stabilize sensor signals                   | Ladder/FBD         |
| First-in-zone tracking | Conveyor product tracking                  | Ladder             |
| Alarm queue            | Record active alarms by time or priority   | ST                 |
| Load shedding          | Disconnect loads by priority               | Ladder/ST          |

---

# 1. FIFO algorithm

FIFO means:

> First In, First Out

The first value placed into the queue is the first value removed.

Example:

```text
Queue before:
[Job 101] [Job 102] [Job 103]

Add Job 104:
[Job 101] [Job 102] [Job 103] [Job 104]

Remove one:
Job 101 leaves first
```

## Common applications

* Conveyor product tracking
* Recipe request queue
* Machine job queue
* Pallet tracking
* Alarm history
* Barcode tracking
* Production order processing
* Warehouse routing

## Rockwell FIFO instructions

Rockwell PLCs commonly use:

```text
FFL — FIFO Load
FFU — FIFO Unload
```

The structure typically includes:

```text
FIFO_Array[0..19]
FIFO_Control.POS
FIFO_Control.LEN
FIFO_Control.EN
FIFO_Control.DN
```

Conceptual Ladder:

```text
|----[ New_Product ]----[ OneShot ]----[ FFL Product_ID FIFO_Array Control 20 ]----|

|----[ Product_Exit ]---[ OneShot ]----[ FFU FIFO_Array Exit_Product_ID Control 20 ]----|
```

Operation:

```text
New product enters:
Product_ID → FIFO queue

Product reaches exit:
Oldest Product_ID → Exit_Product_ID
```

## Generic FIFO pseudocode

```iecst
IF LoadRequest AND QueueCount < QueueSize THEN
    Queue[WriteIndex] := NewValue;
    WriteIndex := WriteIndex + 1;
    QueueCount := QueueCount + 1;
END_IF;

IF UnloadRequest AND QueueCount > 0 THEN
    RemovedValue := Queue[ReadIndex];
    ReadIndex := ReadIndex + 1;
    QueueCount := QueueCount - 1;
END_IF;
```

Usually the indexes wrap around:

```iecst
IF WriteIndex >= QueueSize THEN
    WriteIndex := 0;
END_IF;
```

This creates a **circular FIFO buffer**.

---

# 2. Conveyor shift-register algorithm

For conveyors, a shift register is often easier than a general FIFO.

Imagine ten conveyor positions:

```text
Position:
  0    1    2    3    4    5    6    7    8    9

Data:
[101][---][102][---][---][103][---][---][---][---]
```

Every encoder pulse shifts the data:

```text
Before pulse:
[101][---][102][---][---]

After pulse:
[---][101][---][102][---]
```

Ladder concept:

```text
|----[ Encoder_Pulse ]----[ OneShot ]----[ BSL Tracking_Array ]----|
```

Common Rockwell instructions include:

```text
BSL — Bit Shift Left
BSR — Bit Shift Right
```

For integer product IDs, programmers may use:

* Array copying
* COP instructions
* FIFO instructions
* Structured Text loops

Example:

```iecst
FOR Index := 9 TO 1 BY -1 DO
    ConveyorPosition[Index] := ConveyorPosition[Index - 1];
END_FOR;

ConveyorPosition[0] := NewProductID;
```

Structured Text is usually clearer when each product contains more than one value:

```text
Product record
├── ProductID
├── Recipe
├── Barcode
├── RejectRequired
├── InspectionResult
└── Destination
```

---

# 3. Queue algorithm

A queue is a broader concept than FIFO. A queue may be processed by:

* Arrival order
* Priority
* Machine availability
* Recipe type
* Due date
* Destination
* Production order

Example machine job queue:

```text
Job queue
├── Job 301: Priority 2
├── Job 302: Priority 1
├── Job 303: Priority 3
└── Job 304: Priority 1
```

A simple FIFO processes:

```text
301 → 302 → 303 → 304
```

A priority queue might process:

```text
302 → 304 → 301 → 303
```

assuming priority 1 is highest.

## Queue record

A queue normally stores a structure:

```iecst
TYPE JobRecord :
STRUCT
    JobID       : DINT;
    Priority    : INT;
    RecipeID    : INT;
    Destination : INT;
    Valid       : BOOL;
END_STRUCT;
END_TYPE
```

Then:

```iecst
JobQueue : ARRAY[0..49] OF JobRecord;
```

This is generally easier to manage in Structured Text than Ladder.

---

# 4. Sorting algorithms

Sorting means rearranging data according to a value.

Examples:

* Lowest runtime to highest runtime
* Highest priority to lowest priority
* Lowest temperature to highest temperature
* Earliest production order first
* Most available machine first

## Bubble sort

Bubble sort is easy to understand and implement in PLCs, although it is not efficient for large arrays.

Example values:

```text
Before:
[520, 110, 375, 240]

After:
[110, 240, 375, 520]
```

Structured Text example:

```iecst
FOR Pass := 0 TO EquipmentCount - 2 DO
    FOR Index := 0 TO EquipmentCount - 2 - Pass DO

        IF Runtime[Index] > Runtime[Index + 1] THEN
            Temp := Runtime[Index];
            Runtime[Index] := Runtime[Index + 1];
            Runtime[Index + 1] := Temp;
        END_IF;

    END_FOR;
END_FOR;
```

But this example only sorts runtime values. Usually you need to preserve the equipment identity.

Better:

```iecst
TYPE EquipmentRecord :
STRUCT
    EquipmentID : INT;
    RuntimeHr   : REAL;
    Available   : BOOL;
    Running     : BOOL;
    Faulted     : BOOL;
END_STRUCT;
END_TYPE
```

Then swap the complete records:

```iecst
IF Equipment[Index].RuntimeHr >
   Equipment[Index + 1].RuntimeHr THEN

    TempEquipment := Equipment[Index];
    Equipment[Index] := Equipment[Index + 1];
    Equipment[Index + 1] := TempEquipment;

END_IF;
```

## Sorting in Ladder

Sorting can be done in Ladder using:

* Compare instructions
* MOV instructions
* Temporary registers
* Counters
* Loop instructions
* Indirect addressing

However, the result is usually harder to read.

Conceptual Ladder:

```text
IF Runtime[0] > Runtime[1]:
    Temp       := Runtime[0]
    Runtime[0] := Runtime[1]
    Runtime[1] := Temp
```

A full multi-element sort may require many rungs or an iterative routine. Structured Text is normally the better choice.

---

# 5. Runtime-based staging

Runtime staging is common for:

* Pumps
* Chillers
* Compressors
* Cooling towers
* Boilers
* Exhaust fans
* Vacuum pumps
* Air handlers
* Generators

The main goals are:

1. Start enough equipment to satisfy demand.
2. Balance accumulated runtime.
3. avoid starting faulted or unavailable equipment.
4. Respect minimum run and stop times.
5. Prevent simultaneous starts.
6. Rotate lead and lag equipment.

---

# 6. Lead-lag staging

Consider three pumps:

```text
Pump 1 runtime: 1,250 hours
Pump 2 runtime:   980 hours
Pump 3 runtime: 1,480 hours
```

The lowest-runtime available pump is:

```text
Pump 2
```

It becomes the next lead pump.

The ranking would be:

```text
First choice:  Pump 2 — 980 hours
Second choice: Pump 1 — 1,250 hours
Third choice:  Pump 3 — 1,480 hours
```

## Basic selection algorithm

```text
For each pump:
    Check available
    Check not faulted
    Check not in maintenance
    Check minimum off-time complete

Among valid pumps:
    Select lowest runtime
```

Structured Text:

```iecst
SelectedPump := -1;
LowestRuntime := 3.4E38;

FOR Index := 0 TO NumberOfPumps - 1 DO

    IF Pump[Index].Available
       AND NOT Pump[Index].Faulted
       AND Pump[Index].MinOffTimerDone THEN

        IF Pump[Index].RuntimeHr < LowestRuntime THEN
            LowestRuntime := Pump[Index].RuntimeHr;
            SelectedPump := Index;
        END_IF;

    END_IF;

END_FOR;
```

The selected pump is then commanded in Ladder:

```text
|----[ Stage1Required ]----[ SelectedPump = 0 ]----( Pump1.StartRequest )----|

|----[ Stage1Required ]----[ SelectedPump = 1 ]----( Pump2.StartRequest )----|

|----[ Stage1Required ]----[ SelectedPump = 2 ]----( Pump3.StartRequest )----|
```

---

# 7. Demand-based staging

Suppose three pumps are available.

```text
Demand < 40%                  Run 1 pump
Demand > 70% for 30 seconds   Run 2 pumps
Demand > 90% for 30 seconds   Run 3 pumps
Demand < 75% for 60 seconds   Reduce to 2 pumps
Demand < 45% for 60 seconds   Reduce to 1 pump
```

This includes:

* Start thresholds
* Stop thresholds
* On-delay
* Off-delay
* Hysteresis
* Minimum runtime
* Minimum stop time

Example staging logic:

```text
Stage 1 Required:
SystemEnable

Stage 2 Required:
Demand > 70% for 30 seconds

Stage 3 Required:
Demand > 90% for 30 seconds
```

Ladder concept:

```text
|----[ System_Enable ]----------------------------------------( Stage1_Req )----|

|----[ Demand > 70% ]----[ TON Stage2OnDelay 30 s ]----------------------------|

|----[ Stage2OnDelay.DN ]------------------------------------( Stage2_Req )----|

|----[ Demand > 90% ]----[ TON Stage3OnDelay 30 s ]----------------------------|

|----[ Stage3OnDelay.DN ]------------------------------------( Stage3_Req )----|
```

Use lower stop thresholds:

```text
Stage 2 starts above 70%
Stage 2 stops below 45%

Stage 3 starts above 90%
Stage 3 stops below 75%
```

Without hysteresis, equipment may cycle rapidly.

---

# 8. Runtime accumulation

Runtime is commonly accumulated while confirmed running feedback is true.

Conceptual Ladder:

```text
|----[ Pump1_RunningFB ]----[ TON Pump1_RuntimeTimer 1 hour ]----|

|----[ Pump1_RuntimeTimer.DN ]----[ ADD 1 Pump1_RuntimeHours ]----|
|                                 [ RES Pump1_RuntimeTimer ]       |
```

A better implementation may accumulate seconds:

```iecst
IF Pump.RunningFeedback THEN
    Pump.RuntimeSeconds :=
        Pump.RuntimeSeconds + TaskPeriodSeconds;
END_IF;
```

Then calculate hours:

```iecst
Pump.RuntimeHours :=
    DINT_TO_REAL(Pump.RuntimeSeconds) / 3600.0;
```

Important design considerations:

* Use confirmed running feedback, not merely the start command.
* Make runtime retentive.
* Prevent overflow.
* Allow authorized maintenance correction.
* Store lifetime and resettable runtime separately.

Example:

```text
Pump.LifetimeRuntimeHr
Pump.MaintenanceRuntimeHr
Pump.CurrentRunTimeMin
Pump.StartsCount
```

---

# 9. Round-robin algorithm

Round-robin selects the next device in sequence rather than by runtime.

Example:

```text
Cycle 1 → Pump 1
Cycle 2 → Pump 2
Cycle 3 → Pump 3
Cycle 4 → Pump 1
```

Ladder concept:

```text
|----[ New_Run_Cycle ]----[ OneShot ]----[ ADD 1 Lead_Index ]----|

|----[ Lead_Index >= 3 ]-----------------[ MOV 0 Lead_Index ]-----|
```

Selection:

```text
Lead_Index = 0 → Pump 1
Lead_Index = 1 → Pump 2
Lead_Index = 2 → Pump 3
```

The algorithm must skip unavailable devices:

```iecst
FOR Attempts := 1 TO NumberOfPumps DO
    LeadIndex := LeadIndex + 1;

    IF LeadIndex >= NumberOfPumps THEN
        LeadIndex := 0;
    END_IF;

    IF Pump[LeadIndex].Available THEN
        EXIT;
    END_IF;
END_FOR;
```

Runtime ranking is generally better when equipment usage needs to remain balanced. Round-robin is simpler.

---

# 10. First-available algorithm

This selects the first equipment item that satisfies all conditions.

```iecst
SelectedPump := -1;

FOR Index := 0 TO NumberOfPumps - 1 DO
    IF Pump[Index].Available THEN
        SelectedPump := Index;
        EXIT;
    END_IF;
END_FOR;
```

This algorithm is easy but can cause Pump 1 to run much more often than Pump 2 or Pump 3.

---

# 11. Fixed lead-lag algorithm

A fixed configuration assigns permanent roles:

```text
Pump 1 = Lead
Pump 2 = Lag
Pump 3 = Standby
```

Sequence:

```text
Low demand:
Run Pump 1

Higher demand:
Run Pump 1 + Pump 2

Pump 1 fault:
Start Pump 3
```

This is simple but does not automatically balance equipment runtime.

---

# 12. Runtime equalization algorithm

A runtime equalization system can use two limits:

```text
Start lowest-runtime available equipment.

Stop highest-runtime running equipment.
```

Example:

```text
P1 runtime = 1,100 hours, running
P2 runtime =   900 hours, running
P3 runtime = 1,400 hours, stopped
```

When demand decreases, stop the running pump with the highest runtime:

```text
Stop P1, because 1,100 > 900
```

When demand later increases:

```text
Start P1, because P1 has less runtime than P3
```

However, this algorithm must also consider:

* Minimum run time
* Minimum stop time
* Start count
* Device capacity
* Maintenance status
* Process suitability
* VFD speed
* Fault status

---

# 13. Start-count balancing

Runtime alone may not be sufficient.

Example:

```text
Pump 1: 1,000 hours, 1,500 starts
Pump 2: 1,020 hours,   500 starts
```

Although the runtime is almost equal, Pump 1 has three times as many starts.

A weighted selection score can be used:

```text
SelectionScore =
RuntimeHours × RuntimeWeight
+
StartCount × StartWeight
```

Example:

```iecst
Pump[Index].SelectionScore :=
    Pump[Index].RuntimeHr * 1.0
    + DINT_TO_REAL(Pump[Index].StartCount) * 0.05;
```

Select the lowest score.

This needs engineering judgment because runtime and starts affect different equipment differently.

---

# 14. Priority-based equipment selection

Sometimes equipment should not be selected only by runtime.

Example priorities:

```text
Priority 1: Normal-duty equipment
Priority 2: Older equipment
Priority 3: Emergency standby equipment
Priority 4: Rental or backup equipment
```

The algorithm first considers priority, then runtime:

```text
1. Find available equipment with the highest operating priority.
2. Within that priority group, choose the lowest runtime.
```

Structured Text concept:

```iecst
Selected := -1;
BestPriority := 32767;
LowestRuntime := 3.4E38;

FOR Index := 0 TO NumberOfPumps - 1 DO

    IF Pump[Index].Available THEN

        IF Pump[Index].Priority < BestPriority THEN
            BestPriority := Pump[Index].Priority;
            LowestRuntime := Pump[Index].RuntimeHr;
            Selected := Index;

        ELSIF Pump[Index].Priority = BestPriority
              AND Pump[Index].RuntimeHr < LowestRuntime THEN

            LowestRuntime := Pump[Index].RuntimeHr;
            Selected := Index;

        END_IF;

    END_IF;

END_FOR;
```

---

# 15. Capacity-based staging

Not all equipment has the same capacity.

Example:

```text
Pump 1 = 100 GPM
Pump 2 = 100 GPM
Pump 3 = 200 GPM
```

For a demand of 180 GPM, selecting Pump 3 may be more efficient than running Pumps 1 and 2.

The algorithm may evaluate combinations:

```text
Combination A: P1 + P2 = 200 GPM
Combination B: P3      = 200 GPM
```

Selection may depend on:

* Energy efficiency
* Runtime
* Minimum flow
* Equipment availability
* Number of starts
* Maintenance priority

This type of optimization is normally implemented in Structured Text or a supervisory controller rather than pure Ladder.

---

# 16. Sorting without changing the original array

For runtime staging, it is often better not to rearrange the equipment objects.

Instead, generate a ranked index array:

```text
Original equipment:
Pump[0], Pump[1], Pump[2]

Ranked indexes:
Rank[0] = 1
Rank[1] = 0
Rank[2] = 2
```

This means:

```text
First choice  = Pump[1]
Second choice = Pump[0]
Third choice  = Pump[2]
```

The equipment data stays in its original location.

Example:

```iecst
Rank[0] := 0;
Rank[1] := 1;
Rank[2] := 2;
```

Then sort `Rank[]` using the runtime belonging to each index:

```iecst
IF Pump[Rank[Index]].RuntimeHr >
   Pump[Rank[Index + 1]].RuntimeHr THEN

    TempIndex := Rank[Index];
    Rank[Index] := Rank[Index + 1];
    Rank[Index + 1] := TempIndex;

END_IF;
```

This is a useful industrial programming pattern.

---

# 17. Equipment staging state machine

A robust staging controller should use states rather than turning equipment on and off directly from demand comparisons.

Example states:

```text
0   Disabled
10  Determine required capacity
20  Select next equipment
30  Issue start command
40  Wait for running feedback
50  Running
60  Select equipment to stop
70  Issue stop command
80  Wait for stopped feedback
900 Fault handling
```

Example sequence:

```text
Demand increases
      ↓
Calculate required number of units
      ↓
Select lowest-runtime available unit
      ↓
Check minimum off-time
      ↓
Issue start request
      ↓
Wait for running feedback
      ↓
Confirm stage active
```

This prevents several pumps from starting during the same scan.

---

# 18. Start-delay sequencing

Large motors should often not start simultaneously.

Example:

```text
Pump 1 starts
Wait 10 seconds
Pump 2 starts
Wait 10 seconds
Pump 3 starts
```

Ladder:

```text
|----[ Pump1_RunningFB ]----[ TON Pump2_StartDelay 10 s ]----|

|----[ Stage2_Req ]----[ Pump2_StartDelay.DN ]----( Pump2_StartReq )----|
```

The staging manager should also check whether the previous unit successfully started.

```text
Start Pump 1
    ↓
Did Pump 1 provide running feedback?
    ├── Yes → continue staging
    └── No  → alarm and choose another pump
```

---

# 19. Failed-to-start replacement

Example:

```text
Selected pump = Pump 2

Pump 2 commanded to start
No running feedback after 10 seconds
```

The algorithm should:

```text
1. Remove Pump 2 from the available list.
2. Set Pump 2 failed-to-start alarm.
3. Select the next available pump.
4. Start the replacement pump.
```

Conceptual logic:

```iecst
IF StartFailure THEN
    Pump[SelectedPump].StartFailed := TRUE;
    Pump[SelectedPump].Available := FALSE;
    SelectionRequired := TRUE;
END_IF;
```

Do not repeatedly attempt to start the same failed equipment without a controlled retry policy.

---

# 20. Load-shedding queue

Queuing also applies when electrical loads must be removed.

Example priority list:

```text
Priority 1: Nonessential HVAC
Priority 2: Process heaters
Priority 3: Secondary pumps
Priority 4: Critical process equipment
```

When power demand exceeds a limit:

```text
Shed Priority 1
Wait and reevaluate
Shed Priority 2 if still required
```

Restoration should normally occur in reverse order with delays:

```text
Restore Priority 2
Wait
Restore Priority 1
```

This is essentially a priority queue combined with a state machine.

---

# 21. Alarm queue

An alarm queue may store:

```text
Alarm ID
Timestamp
Priority
State
Acknowledged status
Source
Message index
```

Example:

```iecst
TYPE AlarmEvent :
STRUCT
    AlarmID     : DINT;
    Timestamp   : LINT;
    Priority    : INT;
    Active      : BOOL;
    Acknowledged: BOOL;
END_STRUCT;
END_TYPE
```

For high-volume alarms, queue management is usually better handled in:

* SCADA
* HMI
* Historian
* Alarm server

The PLC should detect and report alarms, but it should not necessarily maintain a large historical database.

---

# 22. Where Ladder is suitable

Ladder is good for:

```text
Queue load trigger
Queue unload trigger
One-shots
Full and empty detection
Runtime timers
Start permissives
Lead/lag command selection
Staging delays
Failed-start detection
Equipment interlocks
```

Example:

```text
|----[ NewJob ]----[ OneShot ]----[/ QueueFull ]----( LoadQueue )----|

|----[ MachineReady ]----[ QueueNotEmpty ]------------( UnloadQueue )--|
```

---

# 23. Where Structured Text is better

Structured Text is better for:

```text
Sorting arrays
Searching arrays
Priority calculations
Circular buffers
Queue record management
Nested loops
Equipment ranking
Weighted selection
Capacity optimization
String and barcode handling
Dynamic recipe queues
```

A common mixed implementation is:

```text
Ladder
├── Device interlocks
├── Start/stop commands
├── Timers
├── Operator commands
└── Equipment feedback

Structured Text
├── FIFO manager
├── Equipment ranking
├── Runtime sorting
├── Job scheduler
└── State manager
```

---

# 24. Recommended staging function block

A reusable staging block could contain:

```text
FB_EquipmentStaging
│
├── Inputs
│   ├── Enable
│   ├── RequiredUnits
│   ├── RequiredCapacity
│   ├── EquipmentAvailable[]
│   ├── EquipmentRunning[]
│   ├── EquipmentFaulted[]
│   ├── RuntimeHours[]
│   ├── StartCount[]
│   └── Priority[]
│
├── Outputs
│   ├── StartRequest[]
│   ├── StopRequest[]
│   ├── SelectedLead
│   ├── ActiveUnitCount
│   ├── AvailableUnitCount
│   └── CapacityUnavailable
│
└── Internal logic
    ├── Availability filtering
    ├── Ranking
    ├── Start sequencing
    ├── Stop sequencing
    ├── Delay handling
    └── Failed-start recovery
```

---

# 25. Practical design rule

Use this structure:

```text
Demand calculation
        ↓
Required equipment count or capacity
        ↓
Availability filtering
        ↓
Equipment ranking
        ↓
Start/stop selection
        ↓
Sequenced commands
        ↓
Feedback verification
        ↓
Alarm and fallback handling
```

Do not combine everything into one large Ladder rung.

For FIFO, sorting, queuing, and staging, the best industrial pattern is usually:

* **Ladder** for physical commands, permissives, timers, and troubleshooting.
* **Structured Text** for arrays, sorting, ranking, queue management, and calculations.
* **State machines** for coordinating starts, stops, retries, and recovery.


----------------------

# Siemens vs Allen-Bradley vs Beckhoff PLC Architecture

The three platforms solve the same control problems, but their internal philosophies are different:

| Platform                | Simplified philosophy                                                                                                                         |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Siemens SIMATIC**     | **Block-and-data architecture**: equipment behavior is placed in FBs, while state is stored in instance DBs                                   |
| **Allen-Bradley Logix** | **Tag-and-instruction architecture**: named tags are operated on directly by Ladder instructions, routines, and AOIs                          |
| **Beckhoff TwinCAT**    | **Software-library-and-task architecture**: IEC software objects execute in configurable real-time tasks and connect symbolically to hardware |

All three can use Ladder and Structured Text. The main difference is **how they schedule code, store state, expose hardware, and package reusable logic**.

---

# 1. High-level comparison

| Feature                   | Siemens S7-1200/1500                                      | Allen-Bradley Logix 5000                | Beckhoff TwinCAT 3                                      |
| ------------------------- | --------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------- |
| Engineering software      | TIA Portal                                                | Studio 5000 Logix Designer              | TwinCAT XAE                                             |
| Runtime hardware          | Dedicated SIMATIC CPU                                     | Dedicated CompactLogix/ControlLogix CPU | Industrial PC, embedded PC, or compatible PC runtime    |
| Main execution container  | Organization Block, OB                                    | Task                                    | Real-time task                                          |
| Main software modules     | FB, FC, DB, OB                                            | Program, Routine, AOI                   | Program, FB, Function, Method                           |
| Shared data               | Global DB                                                 | Controller-scoped tags                  | Global Variable Lists                                   |
| Local/module data         | Instance DB and block interface                           | Program-scoped and AOI instance tags    | FB instance variables                                   |
| Reusable object           | FB with instance DB                                       | Add-On Instruction                      | Function Block or class-like FB                         |
| Hardware I/O data         | Process image and hardware tags                           | Module-defined tags                     | Task/process-image variables linked to I/O              |
| Main fieldbus philosophy  | PROFINET / PROFIBUS                                       | EtherNet/IP / CIP                       | EtherCAT                                                |
| Typical dominant language | LAD/FBD/SCL                                               | Ladder                                  | Structured Text/FBD                                     |
| Advanced software design  | FBs, UDTs, libraries, technology objects                  | AOIs, UDTs, program parameters          | FBs, methods, interfaces, inheritance, libraries        |
| I/O update model          | Process image synchronized with PLC cycle or OB partition | Asynchronous at configured RPI          | Normally synchronized to the responsible real-time task |

Siemens recommends symbolic, optimized data blocks for S7-1200/1500. Rockwell organizes applications as tasks containing programs and routines, with tag-based memory. TwinCAT separates its engineering environment, XAE, from its real-time runtime, XAR, and can execute PLC, motion, C++, and other runtime modules on PC-based controllers. ([Siemens Support][1])

---

# 2. Overall architecture flow

```text
                    ENGINEERING PROJECT
                           │
             ┌─────────────┼─────────────┐
             │             │             │
          Siemens       Rockwell      Beckhoff
             │             │             │
       Device config   I/O tree      System Manager
       OB/FB/FC/DB     Tasks         Real-time tasks
       Libraries       Programs      PLC projects
       Technology Obj. Routines      Libraries
             │             │             │
             └─────────────┼─────────────┘
                           │
                    Compile / Download
                           │
                    Controller runtime
                           │
                Read → Execute → Command
                           │
               I/O, motion, drives, HMI
```

The important design principle is:

```text
Hardware configuration
        ↓
I/O data representation
        ↓
Reusable device objects
        ↓
Equipment modules
        ↓
Sequence or state manager
        ↓
Machine/line interface
```

The vendor-specific differences are mainly in the first three layers.

---

# 3. Siemens programming philosophy

## 3.1 Program hierarchy

A typical Siemens S7-1500 project is organized as:

```text
PLC
├── Device configuration
├── PLC data types
├── PLC tags
├── Technology objects
├── Program blocks
│   ├── OBs
│   ├── FBs
│   ├── FCs
│   └── DBs
└── Project/global libraries
```

### Siemens block types

| Block                       | Purpose                                    |             Maintains internal state? |
| --------------------------- | ------------------------------------------ | ------------------------------------: |
| **OB — Organization Block** | Entry point called by the operating system |             Depends on implementation |
| **FB — Function Block**     | Reusable stateful equipment or algorithm   |           Yes, through an instance DB |
| **FC — Function**           | Calculation or stateless operation         | Normally no persistent instance state |
| **DB — Data Block**         | Stores shared data or FB instance data     |                                   Yes |
| **UDT / PLC data type**     | Defines a reusable data structure          |                  Type definition only |

## 3.2 Execution model

The CPU operating system calls different OBs for different events:

```text
CPU Operating System
│
├── Startup event ───────────────► Startup OB
├── Normal cyclic execution ─────► Main OB1
├── Periodic time event ─────────► Cyclic interrupt OB
├── Hardware event ──────────────► Hardware interrupt OB
├── Diagnostic event ────────────► Diagnostic OB
└── Programming/runtime fault ───► Error-handling OB
```

Example project:

```text
OB100  Startup
OB1    Main cyclic program
OB30   10 ms control loop
OB31   100 ms process loop
OB82   Diagnostic handling

OB1
├── FB_IO_Manager
├── FB_ModeManager
├── FB_Equipment
├── FB_Sequence
└── FB_AlarmManager
```

The Siemens CPU controls when the OBs run. The programmer places the required application code inside those operating-system entry points.

## 3.3 Siemens FB and instance DB concept

Suppose a reusable pump block is created:

```text
FB_Pump
├── Inputs
│   ├── StartRequest
│   ├── StopRequest
│   ├── RunningFeedback
│   └── FaultFeedback
├── Outputs
│   ├── RunCommand
│   ├── Available
│   └── FailedToStart
└── Static internal data
    ├── StartTimer
    ├── Runtime
    ├── State
    └── StartCount
```

Each pump requires its own instance DB:

```text
FB_Pump + DB_Pump101
FB_Pump + DB_Pump102
FB_Pump + DB_Pump103
```

Conceptually:

```text
             Shared algorithm
                  FB_Pump
                     │
       ┌─────────────┼─────────────┐
       │             │             │
 DB_Pump101     DB_Pump102     DB_Pump103
 State of P101  State of P102  State of P103
```

This separation exists because Siemens treats the block algorithm and block memory as related but distinct entities.

### Why Siemens uses this model

It provides:

* Explicit control over shared versus instance data
* Multiple instances of one equipment block
* Predictable block interfaces
* Clear storage for timers, counters, states, and configuration
* Strong symbolic data organization
* Ability to inspect an equipment instance through its DB

For S7-1200/1500, optimized blocks use symbolic access and may organize memory differently from declaration order for processor efficiency. Siemens recommends optimized blocks and notes that instance DB optimization follows the associated FB. ([Siemens Support][1])

## 3.4 Siemens data organization

```text
PLC Data
│
├── Process image
│   ├── Inputs
│   └── Outputs
│
├── Global DBs
│   ├── Machine configuration
│   ├── HMI interface
│   ├── Recipe data
│   └── Production data
│
├── Instance DBs
│   ├── Pump instances
│   ├── Valve instances
│   └── Sequence instances
│
├── PLC tags
│   ├── Hardware symbols
│   └── Memory symbols
│
└── Technology-object DBs
    ├── Motion axes
    └── PID controllers
```

Example:

```text
DB_Machine
├── Commands
├── Status
├── Alarms
├── Production
└── Configuration

DB_Pump101
├── State
├── StartTimer
├── RuntimeHours
├── Starts
└── Diagnostics
```

A strong Siemens design commonly passes structured data through FB interfaces rather than allowing every block to read and write arbitrary global DB members.

## 3.5 Siemens I/O flow

A simplified S7-1500 cyclic flow is:

```text
Beginning of cycle
        │
        ▼
Previous process-image outputs
transferred to output modules
        │
        ▼
Physical input values transferred
into process-image inputs
        │
        ▼
OB1 and called blocks execute
        │
        ▼
Program writes new values into
process-image outputs
        │
        ▼
Next cycle
```

Siemens documents the process image as the memory area between physical modules and the user program. Direct peripheral access is possible, but the process image gives one consistent value during the relevant cycle or process-image partition. ([Siemens Support][2])

---

# 4. Siemens instructions and libraries

Siemens functionality is divided into several groups:

```text
TIA Portal
├── Basic CPU instructions
├── Extended instructions
├── Technology instructions
├── Communication instructions
├── User-created FBs and FCs
├── Project libraries
└── Global libraries
```

## 4.1 Common Siemens instructions

| Function              | Siemens example                            |
| --------------------- | ------------------------------------------ |
| Boolean logic         | Contacts, coils, AND, OR                   |
| Timers                | TON, TOF, TP                               |
| Counters              | CTU, CTD, CTUD                             |
| Copy value            | MOVE                                       |
| Copy array range      | MOVE_BLK                                   |
| Fill array            | FILL_BLK                                   |
| Scaling               | NORM_X, SCALE_X                            |
| Edge detection        | R_TRIG, F_TRIG                             |
| Structured conversion | Serialize, Deserialize                     |
| PID                   | PID_Compact technology object              |
| Motion                | MC_Power, MC_MoveAbsolute, MC_MoveVelocity |
| Queue                 | FIFO example or `LGF_FIFO` library block   |
| Stack                 | `LGF_LIFO` library block                   |

Siemens supplies a Library of General Functions containing blocks such as `LGF_FIFO` and `LGF_LIFO`. It also provides examples for implementing FIFO ring buffers with arrays. ([Siemens Support][3])

## 4.2 Siemens library model

TIA Portal has two important reusable-object forms:

| Library item     | Behavior                                                      |
| ---------------- | ------------------------------------------------------------- |
| **Master copy**  | Creates an independent copy in the project                    |
| **Library type** | Creates version-controlled instances linked to a defined type |

```text
Global Library
├── Types
│   ├── FB_Motor
│   ├── FB_Valve
│   └── UDT_Equipment
└── Master Copies
    ├── Example station
    ├── Hardware configuration
    └── Template program
```

Use **types** when many projects or objects must remain standardized. Use **master copies** when the copied object will be independently modified. ([Siemens Support][4])

## 4.3 Siemens hardware philosophy

Siemens is relatively **controller-centric and hardware-integrated**:

```text
Selected CPU
    ↓
Available memory and execution resources
    ↓
Available technology objects
    ↓
Configured PROFINET devices
    ↓
Hardware identifiers and process image
    ↓
User blocks
```

The project is strongly anchored to the selected CPU and configured station. Motion and PID are often represented as technology objects rather than only ordinary user-written code. Motion instructions command the technology object, while dedicated motion OBs and the CPU firmware perform the underlying control work. ([Siemens Support][5])

This is useful when the goal is:

* Strong integration between PLC, drives, HMI, safety, and distributed I/O
* Standardized industrial diagnostics
* Clearly defined controller resource limits
* Consistent plant-wide engineering

---

# 5. Allen-Bradley programming philosophy

## 5.1 Program hierarchy

A Logix 5000 project normally follows:

```text
Controller
├── Controller tags
├── I/O configuration
├── Add-On Instructions
├── User-defined data types
└── Tasks
    ├── Task
    │   ├── Program
    │   │   ├── Program tags
    │   │   ├── Main routine
    │   │   ├── Other routines
    │   │   └── Fault routine
    │   └── Additional programs
    └── Additional tasks
```

Example:

```text
MainContinuousTask
├── Program_IO
├── Program_Conveyors
├── Program_Stations
└── Program_LineSequence

FastPeriodicTask_5ms
├── Program_FastControl
└── Program_PositionTracking

ProcessTask_100ms
├── Program_PID
└── Program_AnalogProcessing
```

Rockwell tasks may be continuous, periodic, or event-driven. A task schedules one or more programs, and each program contains routines and program-scoped tags. ([Rockwell Automation][6])

## 5.2 Rockwell tag-centric memory model

Logix does not normally require separate DB objects like Siemens.

You define tags directly:

```text
Controller Tags
├── Line01
├── Pump101
├── RecipeData
├── ProductionData
└── Local_2_I / Local_3_O

Program Tags
├── StartRequest
├── CurrentStep
├── SequenceTimer
└── LocalInterlocks
```

A pump UDT might be:

```text
Pump101
├── Cmd
│   ├── Start
│   ├── Stop
│   └── Reset
├── Sts
│   ├── Running
│   ├── Available
│   └── Faulted
├── Alm
│   ├── FailedToStart
│   └── UnexpectedStop
└── Data
    ├── RuntimeHours
    └── StartCount
```

There is no need to create a separate general-purpose DB. `Pump101` itself is a named memory object.

### Scope

| Scope                 | Accessible from                  |
| --------------------- | -------------------------------- |
| Controller-scoped tag | Entire controller                |
| Program-scoped tag    | Its program                      |
| AOI local tag         | Only inside the AOI instance     |
| Program parameter     | Through the program interface    |
| Module-defined tag    | Generated from I/O configuration |

## 5.3 Add-On Instructions

An AOI is Rockwell’s main reusable logic object.

```text
AOI_Pump
├── Input parameters
├── Output parameters
├── InOut parameters
├── Local tags
├── Main logic
├── Prescan logic
├── Postscan logic
└── Enable-in-false logic
```

When instantiated:

```text
P101_Control : AOI_Pump
P102_Control : AOI_Pump
P103_Control : AOI_Pump
```

Each AOI instance tag contains the instruction’s internal state.

Conceptually:

```text
AOI definition
    │
    ├── P101_Control instance data
    ├── P102_Control instance data
    └── P103_Control instance data
```

AOIs package parameters, local tags, and logic into a custom instruction that can appear directly in Ladder or another supported language. ([Rockwell Automation][7])

### Why Rockwell uses this model

Rockwell emphasizes:

* Readable online Ladder troubleshooting
* Direct named access to data
* Custom instructions that look like native instructions
* Strong integration with EtherNet/IP devices
* Easy mapping between equipment objects, tags, HMI objects, and alarms
* Modular controller and I/O replacement

The result is usually easier for plant maintenance personnel, but large projects can become heavily dependent on disciplined tag naming and UDT/AOI standards.

---

# 6. Rockwell I/O and hardware philosophy

When an I/O module is added, Studio 5000 generates module-defined tags.

Example:

```text
Local:2:I
├── Data
├── Fault
└── Status

Local:3:O
├── Data
└── Command
```

More complex modules may create:

```text
ModuleName:I
ModuleName:O
ModuleName:C
ModuleName:Event
```

The exact structure depends on the module profile and selected connection definition. ([Rockwell Automation][8])

## 6.1 Rockwell I/O flow

Rockwell I/O does **not** normally wait for the Ladder scan.

```text
I/O module
    │
    │ Data transfer at configured RPI
    ▼
Module-defined controller tag
    │
    │ May update at any point
    ▼
Continuous / periodic / event task
    │
    ▼
Application logic
```

An I/O tag can change while a routine is executing. Rockwell therefore recommends buffering I/O when the application requires a consistent snapshot. For larger data, the `CPS` synchronous copy instruction can prevent other tasks or I/O updates from changing the data during the copy. ([Rockwell Automation][9])

Recommended pattern:

```text
Raw module input tags
        │
        ▼
CPS/COP/MOV or program input parameters
        │
        ▼
Buffered application input structure
        │
        ▼
Machine logic
        │
        ▼
Buffered output structure
        │
        ▼
Module output tags
```

## 6.2 Rockwell hardware philosophy

Rockwell is relatively **connection-oriented and modular**:

```text
Controller
    │
    ├── Local chassis modules
    ├── Remote EtherNet/IP adapters
    ├── Drives
    ├── HMIs
    ├── Remote controllers
    └── Produced/consumed tags
```

Each connection has communication properties such as an RPI. Devices are integrated using module profiles, and their data structures become part of the controller project.

This design is particularly strong where:

* The plant standard is EtherNet/IP
* Equipment is represented by UDT/AOI objects
* Technicians troubleshoot primarily in Ladder
* Multiple modular skids or machines exchange produced/consumed tags
* I/O and drive profiles are central to engineering

---

# 7. Rockwell instructions and reusable code

Rockwell provides many specialized Ladder instructions that directly implement common industrial algorithms.

| Function                | Rockwell instruction |
| ----------------------- | -------------------- |
| Timer                   | TON, TOF, RTO        |
| Counter                 | CTU, CTD             |
| One-shot                | ONS                  |
| Copy                    | MOV, COP, CPS        |
| FIFO                    | FFL and FFU          |
| Bit tracking            | BSL and BSR          |
| Array expression        | FAL                  |
| Array search            | FSC                  |
| Sequencer               | SQO, SQI, SQL        |
| PID                     | PID or PIDE          |
| Messaging               | MSG                  |
| Custom reusable control | AOI                  |

For example, `FFL` and `FFU` form a native FIFO queue. `FAL` applies an arithmetic or logical expression across array elements, although the current instruction is Ladder-only rather than a Structured Text instruction. ([Rockwell Automation][10])

This produces a distinctive Rockwell pattern:

```text
Rung condition
      ↓
Specialized instruction
      ↓
CONTROL structure
├── .EN
├── .DN
├── .ER
├── .POS
└── .LEN
```

That design is convenient for online Ladder diagnostics because the instruction exposes its progress and state in a standard control structure.

---

# 8. Beckhoff programming philosophy

## 8.1 System hierarchy

A TwinCAT solution can contain several engineering domains:

```text
TwinCAT Solution
├── System
│   ├── Real-time settings
│   ├── CPU-core assignments
│   └── Tasks
├── I/O
│   ├── EtherCAT master
│   └── Terminals and devices
├── PLC
│   ├── PLC project
│   └── PLC task
├── Motion
├── Safety
├── HMI
├── C++ modules
└── Other TwinCAT functions
```

Inside a PLC project:

```text
PLC Project
├── POUs
│   ├── Programs
│   ├── Function Blocks
│   └── Functions
├── DUTs
│   ├── Structures
│   ├── Enumerations
│   └── Aliases
├── GVLs
├── Libraries
├── Tasks
└── Visualization or other objects
```

TwinCAT supports ST and graphical IEC editors, including Ladder, FBD, SFC, and CFC. ([infosys.beckhoff.com][11])

## 8.2 POU and object-oriented model

TwinCAT function blocks are stateful instances, like Siemens FBs, but they can also use software-oriented features such as:

* Methods
* Properties
* Interfaces
* Function-block extension
* Encapsulation
* Inheritance-style design

Beckhoff documents these as extensions beyond the basic IEC function-block model. ([infosys.beckhoff.com][12])

Example:

```iecst
FUNCTION_BLOCK FB_Pump IMPLEMENTS I_Equipment
VAR
    eState       : E_PumpState;
    tonStart     : TON;
    nStartCount  : UDINT;
    fRuntimeHr   : LREAL;
END_VAR

METHOD PUBLIC Start
METHOD PUBLIC Stop
METHOD PUBLIC Reset
METHOD PRIVATE CheckFeedback
PROPERTY Available : BOOL
PROPERTY Running   : BOOL
```

Instances:

```iecst
fbPump101 : FB_Pump;
fbPump102 : FB_Pump;
fbPump103 : FB_Pump;
```

This is closer to conventional software engineering than the typical plant-level Rockwell approach.

## 8.3 TwinCAT task execution

A TwinCAT task has:

* Cycle time
* Priority
* CPU-core assignment
* Process image
* Runtime modules registered to it

```text
TwinCAT real-time scheduler
│
├── Task 1: 1 ms, high priority
│   ├── EtherCAT update
│   ├── Motion
│   └── Fast PLC program
│
├── Task 2: 10 ms
│   └── Machine control
│
└── Task 3: 100 ms
    ├── Temperature control
    ├── Logging
    └── Communications
```

Beckhoff defines a task as a schedulable runtime object with a cycle time and priority. ([infosys.beckhoff.com][13])

## 8.4 TwinCAT I/O flow

TwinCAT commonly links PLC variables directly to EtherCAT process data:

```text
EtherCAT input
      │
      │ Symbolic process-image link
      ▼
PLC input variable
      │
      ▼
Task input update
      │
      ▼
PLC program and other runtime modules
      │
      ▼
Task output update
      │
      ▼
EtherCAT output
```

For a task-synchronized process image:

```text
Task starts
    ↓
Input process images update
    ↓
Runtime modules execute
    ↓
Output process images update
    ↓
Task waits for next scheduled cycle
```

Beckhoff documents that task-triggered input updates occur around the start of task processing and output updates around the end. Variables can be linked between PLC, EtherCAT, motion, and other process images. ([infosys.beckhoff.com][14])

## 8.5 TwinCAT data organization

```text
PLC Data
├── Global Variable Lists
├── Program-local variables
├── FB instance variables
├── Function temporary variables
├── DUT structures
├── Process-image variables
├── RETAIN variables
└── PERSISTENT variables
```

Beckhoff distinguishes temporary function data from stateful FB instance data. It also supports `RETAIN` and `PERSISTENT` storage, although reliable power-loss retention depends on the target hardware and retention mechanism. ([infosys.beckhoff.com][15])

---

# 9. Beckhoff libraries and instructions

Beckhoff handles advanced functionality primarily through libraries.

```text
TwinCAT PLC
├── IEC operators
├── Tc2_Standard
├── Tc2_System
├── Tc2_Utilities
├── Tc2_MC2
├── Tc3 libraries
├── Industry-specific libraries
└── User/company libraries
```

Examples:

| Function               | Beckhoff approach                             |
| ---------------------- | --------------------------------------------- |
| Timers and counters    | IEC function blocks such as TON, TOF, CTU     |
| FIFO                   | `FB_MemRingBuffer`, `FB_FileRingBuffer`       |
| String FIFO            | `FB_StringRingBuffer`                         |
| Linked list            | Utility library block                         |
| Hash table             | Utility library block                         |
| Motion                 | `Tc2_MC2` PLCopen function blocks             |
| PID/process algorithms | Controller or process libraries               |
| Communications         | Protocol-specific TwinCAT libraries/functions |
| Reusable equipment     | Custom FB with methods/interfaces             |

`FB_MemRingBuffer` stores data records and retrieves them according to the FIFO principle. The utilities library also includes examples for file ring buffers, linked lists, hash tables, and CSV operations. ([infosys.beckhoff.com][16])

The Beckhoff philosophy is less:

```text
Select one special native Ladder instruction
```

and more:

```text
Reference a library
        ↓
Declare a function-block instance
        ↓
Call its methods or execute it cyclically
        ↓
Read status and error outputs
```

---

# 10. Direct instruction comparison

## 10.1 General operations

| Application       | Siemens                                 | Allen-Bradley                   | Beckhoff                                   |
| ----------------- | --------------------------------------- | ------------------------------- | ------------------------------------------ |
| Rising edge       | `R_TRIG`                                | `ONS`                           | `R_TRIG`                                   |
| On-delay timer    | `TON`                                   | `TON`                           | `TON`                                      |
| Retentive timer   | Custom/IEC implementation depending CPU | `RTO`                           | Retentive logic around timer               |
| Counter           | `CTU/CTD/CTUD`                          | `CTU/CTD`                       | `CTU/CTD/CTUD`                             |
| Copy scalar       | `MOVE`                                  | `MOV`                           | Assignment                                 |
| Copy array        | `MOVE_BLK`                              | `COP/CPS`                       | Array assignment, loops, utility functions |
| Fill array        | `FILL_BLK`                              | `FLL` or `FAL` depending need   | Loop or library function                   |
| FIFO              | `LGF_FIFO` or array ring buffer         | `FFL/FFU`                       | `FB_MemRingBuffer`                         |
| Shift tracking    | Shift instructions or array logic       | `BSL/BSR`                       | Array/bit-shift code                       |
| Array calculation | SCL loop                                | `FAL` or ST loop                | ST loop                                    |
| Array search      | SCL algorithm                           | `FSC` or ST                     | ST/library algorithm                       |
| Sorting           | SCL algorithm/library                   | ST, Ladder/FAL algorithm        | ST algorithm/library                       |
| Device object     | FB + instance DB                        | AOI + UDT                       | FB/class-like object                       |
| Motion            | Technology object + `MC_*`              | Axis tags + motion instructions | PLCopen `MC_*` library                     |
| PID               | PID technology object                   | `PIDE`/PID                      | Control library FB                         |
| Communications    | Instructions and Siemens libraries      | `MSG`, module profiles, AOIs    | Protocol libraries and ADS                 |

## 10.2 Practical interpretation

### Siemens

```text
Native instruction
      +
Reusable FB/FC
      +
Explicit DB storage
      +
Technology object
```

### Allen-Bradley

```text
Native Ladder instruction
      +
Named tags
      +
CONTROL structures
      +
AOI for custom behavior
```

### Beckhoff

```text
IEC language
      +
Function-block library
      +
Task scheduler
      +
Symbolic process-image mapping
```

---

# 11. FIFO example across the three platforms

## Siemens

```text
Enqueue request
      ↓
LGF_FIFO or custom FB
      ↓
ARRAY in instance/global DB
      ↓
Read/write index and count
      ↓
Oldest element returned
```

Typical data:

```text
DB_Queue
├── Buffer[0..49]
├── ReadIndex
├── WriteIndex
├── ElementCount
├── Empty
└── Full
```

## Allen-Bradley

```text
New item pulse
      ↓
FFL instruction
      ↓
FIFO_Array[]
      +
CONTROL tag
      ↓
FFU on dequeue
```

Typical data:

```text
JobFIFO[50]
JobFIFO_Control
├── .POS
├── .LEN
├── .EN
├── .DN
└── .EM
```

## Beckhoff

```text
Add request
      ↓
FB_MemRingBuffer.A_AddTail()
      ↓
User-supplied buffer memory
      ↓
A_GetHead / A_RemoveHead
```

Typical data:

```iecst
fbQueue    : FB_MemRingBuffer;
aBuffer    : ARRAY[0..4095] OF BYTE;
stNewJob   : ST_Job;
stNextJob  : ST_Job;
```

---

# 12. Runtime staging example across platforms

Suppose the application must select the available pump with the lowest runtime.

## Siemens implementation

```text
OB1 or periodic OB
      ↓
FB_Staging
      ↓
Pump array passed as InOut
      ↓
SCL FOR loop ranks pumps
      ↓
Selected index stored in instance DB
      ↓
Individual FB_Pump instances receive requests
```

```scl
FOR #i := 0 TO #PumpCount - 1 DO
    IF #Pump[#i].Available
       AND #Pump[#i].RuntimeHours < #LowestRuntime THEN

        #LowestRuntime := #Pump[#i].RuntimeHours;
        #SelectedPump := #i;
    END_IF;
END_FOR;
```

## Allen-Bradley implementation

```text
Periodic task
      ↓
Staging program
      ↓
UDT array of pump data
      ↓
ST routine, FAL/FSC logic, or AOI
      ↓
SelectedPump tag
      ↓
Ladder output-command routines
```

A practical Rockwell project often uses Structured Text for ranking, then Ladder for commands and interlocks.

## Beckhoff implementation

```text
Machine-control task
      ↓
FB_Staging.Execute()
      ↓
ARRAY OF FB_Pump references/data
      ↓
Structured Text ranking algorithm
      ↓
Method call on selected pump object
```

Beckhoff naturally supports placing the entire selector inside a reusable object with methods and interfaces.

---

# 13. Programming philosophy comparison

| Question                           | Siemens                                 | Allen-Bradley                         | Beckhoff                                       |
| ---------------------------------- | --------------------------------------- | ------------------------------------- | ---------------------------------------------- |
| Where is state stored?             | Instance DB                             | Tag/AOI instance tag                  | FB instance variables                          |
| What is the primary reusable unit? | FB                                      | AOI                                   | FB/library object                              |
| What drives execution?             | CPU calls OBs                           | Tasks schedule programs               | Real-time scheduler runs tasks                 |
| How visible is memory structure?   | DB-centered and explicit                | Tag-centered                          | Variable/object-centered                       |
| How is hardware exposed?           | Process image, tags, technology objects | Module-defined tags                   | Symbolic process-image links                   |
| What is emphasized?                | Structured modular automation           | Online plant troubleshooting          | Software flexibility and real-time integration |
| Typical sequence style             | GRAPH/SCL/FBs                           | Ladder/SFC/ST                         | ST/SFC/state objects                           |
| Typical maintenance style          | Navigate OB → FB → DB                   | Trace tags and Ladder rungs           | Trace task → FB instance → I/O mapping         |
| Reuse distribution                 | TIA libraries                           | AOI/UDT exports and project templates | Versioned PLC libraries/packages               |
| Best natural fit                   | Integrated plant/process systems        | North American discrete manufacturing | High-performance machinery and motion          |

---

# 14. Hardware philosophy comparison

## Siemens: automation appliance

```text
Dedicated CPU
    +
Integrated PROFINET
    +
Technology firmware
    +
Distributed I/O
    +
TIA-integrated diagnostics
```

The software is designed around a known industrial controller family. CPU capability determines memory, task resources, technology-object capacity, and performance.

## Allen-Bradley: modular connected controller

```text
Controller
    +
Chassis or distributed I/O
    +
CIP connections
    +
Module profiles
    +
Tag-based data
```

The software treats modules and networked devices as configured objects with generated data structures and update rates.

## Beckhoff: real-time software platform

```text
Industrial PC
    +
Real-time runtime
    +
EtherCAT
    +
Modular software functions
    +
PLC/motion/robotics/vision integration
```

TwinCAT turns PC-based hardware into a real-time controller and can combine PLC, NC/CNC, robotics, vision, HMI, and custom software on one platform. ([Beckhoff Automation][17])

---

# 15. Recommended cross-platform program organization

The same application structure can be used on all three vendors:

```text
01_System
├── Startup
├── Watchdogs
├── Time synchronization
└── Controller diagnostics

02_IO
├── Raw input mapping
├── Raw output mapping
├── Signal validation
└── Communication status

03_ControlModules
├── Motors
├── Valves
├── Instruments
├── Drives
└── Servo axes

04_EquipmentModules
├── Pump groups
├── Conveyors
├── Robot stations
└── Process skids

05_ModesAndStates
├── Manual
├── Automatic
├── Maintenance
├── PackML
└── Safe-state coordination

06_Sequences
├── Startup
├── Production
├── Shutdown
└── Recovery

07_StagingAndScheduling
├── FIFO
├── Job queue
├── Runtime staging
├── Lead/lag selection
└── Capacity management

08_Alarms
├── Detection
├── Delay
├── Acknowledgment
└── Diagnostics

09_Integration
├── HMI
├── SCADA
├── MES
├── OPC UA
└── Line interface
```

Vendor mapping:

| Architecture layer   | Siemens                | Allen-Bradley         | Beckhoff             |
| -------------------- | ---------------------- | --------------------- | -------------------- |
| System execution     | OBs                    | Tasks/programs        | Real-time tasks      |
| Device objects       | FB + instance DB       | AOI + UDT             | FB instances/classes |
| Shared machine data  | Global DB              | Controller tags       | GVL                  |
| Equipment-local data | Instance DB            | Program tags/AOI tags | FB variables         |
| Complex algorithms   | SCL                    | ST routine/AOI        | ST method/FB         |
| Boolean interlocks   | LAD/FBD                | Ladder                | LD/FBD/ST            |
| Hardware mapping     | I/O tags/process image | Module tags           | Symbol links         |
| Reuse                | TIA type library       | AOI/UDT export        | PLC library/package  |

---

# 16. Which platform is strongest for which style?

## Siemens is strongest when

* The project needs formal block and data separation.
* The plant uses PROFINET, Siemens drives, Siemens HMI, and Siemens safety.
* Equipment modules must have clearly defined instance DBs.
* Process control and machine control coexist.
* Standardized plant engineering is more important than software openness.

## Allen-Bradley is strongest when

* Maintenance personnel primarily troubleshoot Ladder.
* EtherNet/IP and Rockwell drives/I/O dominate the facility.
* Native instructions such as FIFO, file operations, sequencers, and messaging are useful.
* Equipment is represented using UDTs and AOIs.
* Online modification and direct tag visibility are operational priorities.

## Beckhoff is strongest when

* The application has high-speed motion or many synchronized axes.
* Structured Text and software-oriented design are preferred.
* PLC, motion, vision, HMI, analytics, and custom PC software must coexist.
* EtherCAT cycle synchronization is important.
* Libraries, interfaces, methods, version control, and modular packages are central to development.

---

# 17. Main conclusion

The platforms are not simply different versions of Ladder Logic.

```text
Siemens
Algorithm separated from state:
FB + instance DB

Allen-Bradley
Algorithm operates directly on named data:
Instruction/AOI + tag

Beckhoff
Algorithm packaged as software object:
Function block/library + real-time task
```

For queueing, sorting, runtime staging, PackML, and equipment management:

* **Siemens:** place the algorithm in an FB written primarily in SCL, store its state in an instance DB, and expose clean inputs and outputs.
* **Allen-Bradley:** use native Ladder instructions where appropriate, but use UDTs, AOIs, and Structured Text for complicated ranking or scheduling.
* **Beckhoff:** implement the algorithm as a reusable Structured Text function block or library object and execute it in a defined real-time task.

The best cross-vendor philosophy is:

```text
Ladder
    → physical commands, permissives and diagnostics

Structured Text
    → arrays, sorting, queues, scheduling and state machines

Function blocks/AOIs
    → reusable equipment behavior

Tasks/OBs
    → deterministic execution timing

UDTs/DBs/GVLs
    → organized and controlled data ownership
```

[1]: https://support.industry.siemens.com/cs/attachments/90885040/81318674_Programming_guideline_DOC_v16_en.pdf "Programming Guideline for  S7-1200/1500   "
[2]: https://support.industry.siemens.com/cs/attachments/59193558/s71500_cycle_and_reaction_times_function_manual_en-US_en-US.pdf "Cycle and response times - Support"
[3]: https://support.industry.siemens.com/cs/mdm/109742272?c=86842143115&lc=el-GR "Programming queues (FIFO) (S7-1200, S7-1500) - STEP 7 ..."
[4]: https://support.industry.siemens.com/cs/mdm/109011420?c=69219625867&lc=en-id "Master copies and types - STEP 7 Professional V13.1 - Support"
[5]: https://support.industry.siemens.com/cs/attachments/109812056/s71500_s71500t_motion_control_overview_function_manual_en-US_en-US.pdf "S7-1500/S7-1500T Motion Control Overview V7.0 as of STEP ..."
[6]: https://literature.rockwellautomation.com/idc/groups/literature/documents/pm/1756-pm006_-en-p.pdf "Logix 5000 Controllers Sequential Function Charts"
[7]: https://literature.rockwellautomation.com/idc/groups/literature/documents/pm/1756-pm010_-en-p.pdf "Logix 5000 Controllers Add-On Instructions - Literature Library"
[8]: https://literature.rockwellautomation.com/idc/groups/literature/documents/pm/1756-pm002_-en-d.pdf "Logix 5000 Controllers EDS AOP Guidelines for Logix Designer"
[9]: https://literature.rockwellautomation.com/idc/groups/literature/documents/pm/1756-pm004_-en-p.pdf "Logix 5000 Controllers I/O and Tag Data - Literature Library"
[10]: https://www.rockwellautomation.com/en-us/docs/studio-5000-logix-designer/38-01/contents-ditamap/instruction-set/array--file--shift-instructions/fifo-load--ffl-.html "FIFO Load (FFL)"
[11]: https://infosys.beckhoff.com/content/1033/tc3_plc_intro/2525041803.html "Your first TwinCAT 3 PLC project"
[12]: https://infosys.beckhoff.com/content/1033/tc3_plc_intro/2530279563.html "Object Function block"
[13]: https://infosys.beckhoff.com/content/1033/tc3_grundlagen/17677068555.html "Tasks"
[14]: https://infosys.beckhoff.com/content/1033/tc3_grundlagen/6828869003.html "TwinCAT real-time"
[15]: https://infosys.beckhoff.com/content/1033/tc3_plc_intro/2530284939.html "Object Function"
[16]: https://infosys.beckhoff.com/content/1033/tcplclib_tc2_utilities/35010187.html "FB_MemRingBuffer"
[17]: https://www.beckhoff.com/en-us/products/automation/twincat/ "TwinCAT | Automation software | Beckhoff USA"


-================

