Implementing **Safety Integrity Level (SIL)** or **Performance Level (PL)** in a machine is not a single decision. It is a structured engineering process that flows through four layers:

1. **Risk Assessment**
2. **Safety Function Definition**
3. **Hardware Architecture Selection**
4. **Validation (hardware + software)**

These concepts come primarily from:

- IEC 61508
- IEC 62061
- ISO 13849-1
- NFPA 79

For a **machine builder**, the practical workflow looks like this.

---

# 1. Step 1 — Perform a Risk Assessment

Before choosing hardware, determine the **required safety level**.

Two common methods:

| Standard  | Result                               |
| --------- | ------------------------------------ |
| ISO 13849 | **PLr (Performance Level required)** |
| IEC 62061 | **SILCL (SIL claim limit)**          |

### Typical Risk Factors

ISO 13849 risk graph uses:

| Parameter | Meaning                        |
| --------- | ------------------------------ |
| **S**     | Severity of injury             |
| **F**     | Frequency of exposure          |
| **P**     | Possibility of avoiding hazard |

Example:

| Hazard          | Result            |
| --------------- | ----------------- |
| Crushing hazard | **PL d required** |

Equivalent SIL:

| PL       | SIL       |
| -------- | --------- |
| PL a     | SIL 1     |
| PL b     | SIL 1     |
| PL c     | SIL 1     |
| **PL d** | **SIL 2** |
| **PL e** | **SIL 3** |

---

# 2. Step 2 — Define Safety Functions

A **Safety Function** is the behavior the system must perform when danger occurs.

Example machine safety functions:

| Safety Function         | Description               |
| ----------------------- | ------------------------- |
| Emergency Stop          | Stop machine immediately  |
| Guard Door Interlock    | Stop if guard opened      |
| Safe Torque Off         | Disable motor torque      |
| Hydraulic Pressure Dump | Remove hydraulic pressure |
| Chemical Pump Shutoff   | Close dosing valve        |

Each function must include:

```
Input device → Safety logic → Output device
```

Example:

```
E-Stop Button
   ↓
Safety PLC
   ↓
Safety Contactor → Motor power removed
```

---

# 3. Step 3 — Choose Safety Hardware Architecture

Architecture determines the **Category (ISO 13849)**.

| Category | Description                    |
| -------- | ------------------------------ |
| B        | Basic single channel           |
| 1        | Reliable components            |
| 2        | Periodic test                  |
| **3**    | Dual channel with monitoring   |
| **4**    | Dual channel + fault tolerance |

Most industrial machines require:

**Category 3 or 4**

---

# 4. Safety Hardware Architecture Example

Typical **Category 3 architecture**

```
Channel A:  E-stop → Safety PLC input A
Channel B:  E-stop → Safety PLC input B

Safety PLC logic

Output A → Contactor A
Output B → Contactor B

Feedback → PLC safety monitoring
```

Key features:

- Dual channel wiring
- Cross monitoring
- Feedback loop

---

# 5. How to Choose Safety Devices

Only use **certified safety devices**.

Example device types:

| Device               | Certification                |
| -------------------- | ---------------------------- |
| Safety PLC           | SIL2 / SIL3                  |
| Safety Relay         | SIL3                         |
| Safety Contactor     | mechanically linked contacts |
| Safety Light Curtain | PL e                         |
| Safety Interlock     | PL d/e                       |

Typical vendors:

- Pilz
- SICK
- Rockwell Automation
- Siemens

Example safety PLC:

- GuardLogix
- Siemens F-CPU
- Pilz PNOZmulti

---

# 6. Safety Wiring Principles

Safety circuits follow strict wiring rules.

### Dual channel input wiring

```
E-STOP

Contact 1 → Safety input CH1
Contact 2 → Safety input CH2
```

Never connect both channels together.

---

### Contactor feedback loop

Purpose: detect welded contacts.

```
Safety PLC output → Contactor coil

Auxiliary contact (NC)
     ↓
Safety PLC feedback input
```

If contactor welds → feedback fails → machine cannot restart.

---

### Safe motor shutdown

Common methods:

| Method | Description     |
| ------ | --------------- |
| STO    | Safe Torque Off |
| SS1    | Safe Stop 1     |
| SS2    | Safe Stop 2     |

Example:

Servo drive with STO:

```
Safety PLC → STO channel 1
Safety PLC → STO channel 2
```

---

# 7. Programming Safety Logic

Safety PLC programming must follow **certified blocks**.

Typical safety logic:

```
IF
  EStop_OK
AND
  GuardDoorClosed
AND
  LightCurtainClear
THEN
  SafetyEnable = TRUE
ELSE
  SafetyEnable = FALSE
```

Safety rules:

- no bypass
- no unsafe resets
- reset must be manual

Example reset logic:

```
IF
  SafetyClear
AND
  ResetButtonPressed
THEN
  SafetyOutputEnable
```

---

# 8. Validation

Final step required by standards.

Verify:

- wiring correctness
- failure simulation
- safety response time
- documentation

Tools used:

- **SISTEMA** for PL calculation
- **Safety Evaluation Tool**

---

# 9. Example Machine Safety Stack

For a **hydraulic + chemical dosing machine** like you described earlier:

| Safety Function           | Hardware                 |
| ------------------------- | ------------------------ |
| E-Stop                    | dual channel push button |
| Guard Interlock           | coded safety switch      |
| Hydraulic pressure relief | safety valve             |
| Pump shutdown             | safety contactor         |
| Servo STO                 | drive STO input          |

Safety PLC handles the logic.

---

# 10. Example Minimal Architecture

```
E-STOP
Guard Door
Light Curtain
        ↓
     Safety PLC
        ↓
Contactor A
Contactor B
Servo STO
Hydraulic dump valve
```

Target safety level:

**PL d / SIL 2**

---

# What experienced machine builders actually do

In semiconductor / robotics equipment (similar to systems you work on):

- Architecture almost always **Category 3 or 4**
- Safety PLC with distributed safety IO
- Safety network (PROFIsafe / CIP Safety)
- STO used instead of cutting motor power

---

Yes. The **voltage level of a safety circuit does matter**, but not because SIL/PL calculations directly depend on voltage. The standards focus on **probability of failure and architecture**, not voltage. However, voltage affects **reliability, safety, wiring practices, and compliance with machine standards**.

In practice, voltage choice determines whether your design is **acceptable under machine safety standards** such as:

- NFPA 79
- IEC 60204-1
- ISO 13849-1

---

# 1. What Safety Standards Actually Require

Safety standards care about:

- **Architecture (Category 3 / 4)**
- **Diagnostics**
- **Redundancy**
- **Component certification**
- **Probability of dangerous failure**

They **do not require a specific voltage** for safety circuits.

However:

> Most machine safety systems use **24 VDC control circuits** because the supporting ecosystem is designed for it.

---

# 2. Industry Practice

Typical voltages used in safety circuits:

| Voltage    | Typical Use                          | Comments                |
| ---------- | ------------------------------------ | ----------------------- |
| **24 VDC** | Machine safety control               | Industry standard       |
| 48 VDC     | Robotics / telecom / battery systems | Rare for safety I/O     |
| 120 VAC    | Legacy machinery                     | Avoid in modern designs |

For modern machines:

**99% of safety circuits are 24 VDC.**

---

# 3. Why 24 VDC Became the Standard

### 1. Touch Safety

24 VDC is considered **SELV (Safety Extra Low Voltage)**.

Meaning:

- Low shock hazard
- Safer wiring in panels
- Safer field devices

Defined in:

- IEC 61140

---

### 2. Device Ecosystem

Most safety devices only support **24 VDC inputs**:

Examples:

| Device            | Typical Input |
| ----------------- | ------------- |
| E-stop buttons    | 24VDC         |
| Safety PLC        | 24VDC         |
| Light curtains    | 24VDC         |
| Safety interlocks | 24VDC         |

If you choose another voltage, you lose compatibility.

---

### 3. Diagnostics

Safety PLC inputs use **test pulses** to detect faults.

Example diagnostics:

- short circuit detection
- cross channel fault
- wire break detection

These diagnostics rely on **low-voltage DC signaling**.

---

# 4. Problems with 120VAC Safety Circuits

Older machines used 120VAC relay safety circuits.

Problems:

| Issue            | Reason                        |
| ---------------- | ----------------------------- |
| Shock hazard     | higher voltage                |
| Poor diagnostics | AC circuits harder to monitor |
| Noise issues     | AC interference               |
| Contact arcing   | larger electrical stress      |

Modern standards discourage this approach.

---

# 5. 48VDC Safety Circuits

48VDC sometimes appears in:

- robotics battery systems
- telecom equipment
- mobile robots

But safety IO modules are rarely designed for it.

Example:

A safety PLC input typically expects:

```
ON state: 15–30 VDC
OFF state: <5 VDC
```

48VDC would damage the input.

---

# 6. Where Higher Voltage IS Used

Higher voltages are used in **power circuits**, not **safety logic circuits**.

Example architecture:

```
Safety logic: 24VDC

Motor power: 480VAC

Safety PLC → STO → Servo drive
```

The safety logic **controls power isolation devices**, not the power itself.

---

# 7. Example Industrial Safety Architecture

Typical modern machine:

```
24VDC Power Supply
        │
        ▼
Safety Devices
(E-stop, guard switch)
        │
        ▼
Safety PLC
        │
        ▼
Contactor / STO / Valve
        │
        ▼
Power Circuit
(480VAC motor)
```

---

# 8. When Voltage DOES Affect SIL / PL

Voltage can indirectly affect safety level through **component reliability**.

Example factors:

| Factor           | Impact                    |
| ---------------- | ------------------------- |
| Contact wear     | affects MTTFd             |
| Arc energy       | affects relay reliability |
| Cable insulation | affects failure rate      |

These factors influence **PFHd calculations** in:

- IEC 62061

---

# 9. Best Practice for Machine Builders

Use this rule:

| Circuit Type | Voltage    |
| ------------ | ---------- |
| Safety logic | **24VDC**  |
| PLC IO       | 24VDC      |
| Sensors      | 24VDC      |
| Drives STO   | 24VDC      |
| Motor power  | 208/480VAC |

---

# 10. Practical Example (Hydraulic + Chemical Machine)

Safety circuit:

```
24VDC supply
      │
      ├─ E-Stop (dual channel)
      ├─ Guard switch
      ├─ Light curtain
      │
      ▼
Safety PLC
      │
      ├─ Servo STO
      ├─ Hydraulic dump valve
      └─ Pump contactor
```

---

# Key Takeaway

Voltage **does not define SIL or PL**, but:

- **24 VDC is the industry standard**
- higher voltages reduce safety and diagnostics capability
- most certified safety components require **24 VDC**

---

If you'd like, I can also explain something extremely useful for a controls engineer:

**The 6 fundamental safety wiring patterns used in almost every industrial machine.**

Once you understand those patterns, you can read **any machine safety circuit instantly.**
Yes, all of that matters.

For a **dual-channel safety input**, you do **not** just pick “two wires and any terminal.” The safety function depends on:

- conductor separation and fault avoidance,
- correct conductor type and ampacity,
- correct color identification,
- proper terminations,
- compatible input filtering / discrepancy timing,
- and correct device type.

Also, one correction:

## First correction: most hardwired safety inputs are **NC, held closed**, not NO

For classic hardwired safety devices like:

- E-stop pushbuttons
- gate interlock safety contacts
- rope pull switches
- limit switches used in a safety function

the usual design is:

- **2 NC channels**
- both channels **closed in the safe state**
- opening either channel causes a trip

That is done for **fail-safe behavior**: a broken wire looks like a demand to stop.

What you may be thinking of is:

- **OSSD outputs** from light curtains / safety sensors, which are electronic and sit high in the healthy state, or
- “held closed” as a behavior rather than NO contact form.

If the device is a mechanical contact safety input, the normal pattern is:

```text
24VDC test source → NC contact CH1 → Safety input I1
24VDC test source → NC contact CH2 → Safety input I2
```

A **dual-channel NO contact** is generally **not** the default choice for emergency stop style functions.

---

# What to do in practice

## 1. Use 2 separate conductors for the 2 channels

For dual-channel monitoring, use:

- **one conductor pair for Channel 1**
- **one conductor pair for Channel 2**
- do not parallel them
- do not common them in the field unless the safety device manual explicitly allows it

Minimum practical rule:

- treat **CH1** and **CH2** as independent circuits all the way back to the safety controller
- land them on separate safety input terminals
- use the controller’s pulse-tested outputs correctly if the module requires them

Why:

A Category 3 / 4 or PL d / e design is trying to detect faults like:

- short between channels
- short to 24V
- short to 0V
- wire break
- welded contact

That only works when the two channels are genuinely separate.

Rockwell safety hardware documentation explicitly uses pulsed inputs and monitors channel discrepancy; for some Guardmaster interfaces, the pulses are **1 ms** wide, offset between channels, and repeated periodically. That is part of how cross-faults are detected. ([Rockwell Automation][1])

---

## 2. Wire size: use machine-control wire, not “whatever fits”

For most panel and field safety input circuits, the practical default is:

- **18 AWG stranded copper** for most machine control wiring
- **16 AWG** if runs are longer, the environment is harsher, or the device terminal set favors it
- **20 AWG** can be acceptable on some compact devices or pre-made cordsets, but I would not make that your default for field hardwiring unless the manufacturer terminal range and code basis clearly support it

For safety inputs, current is usually tiny. The wire size is rarely driven by load current. It is driven by:

- mechanical robustness
- terminal compatibility
- voltage drop margin
- survivability during maintenance
- compliance with machine wiring rules

For a controls engineer, **18 AWG stranded MTW / TEW / machine-tool wire** is the normal conservative choice inside the panel.

For field wiring:

- use cable suitable for motion / flex / oil / coolant / tray / washdown as needed
- match insulation and jacket to the environment, not just the voltage

---

## 3. Voltage rating: use insulation appropriate for the machine environment

Even if the safety circuit is only **24 VDC**, the wire insulation rating still matters.

A practical default:

- **600 V rated machine wire** is common and conservative in industrial panels
- use cable listed for the installation method and environment
- if the machine has VFDs, servos, hydraulic oil mist, washdown, or tray routing, choose cable that is rated for those conditions

The conductor insulation rating is not chosen just by signal voltage. It is chosen by:

- panel practice
- routing alongside other conductors
- mechanical durability
- chemical exposure
- code / listing requirements

---

## 4. Color: follow machine wiring identification consistently

A very common North American machine convention aligned with NFPA 79 / UL 508A practice is:

- **Blue**: ungrounded **DC control conductors**
- **Red**: ungrounded **AC control conductors**
- **Green or green/yellow**: protective earth
- **Orange**: conductors that remain energized when the main disconnect is off
- **Orange with blue stripe**: DC conductors that remain energized when the main disconnect is off
- **White with blue stripe** or other standard identified grounded DC return, depending on the adopted convention and jurisdiction

UL’s published guidance on machine supply and conductor identification lists **blue for ungrounded DC control conductors**, **red for ungrounded AC control conductors**, and **orange** for excepted circuits that remain energized. NFPA 79 committee material also reflects **orange with blue stripe** for DC conductors remaining energized with the disconnect off. ([UL Solutions][2])

### Practical recommendation for your safety circuits

For a 24 VDC safety input loop:

- use **blue** for the ungrounded 24 VDC safety feed / channel conductors
- use your standard DC common identification consistently
- clearly label **CH1** and **CH2**
- if the circuit remains live when the main disconnect is off, identify it with the proper “always energized” color convention

Do not invent your own color code if the machine will be maintained by other people.

---

## 5. Termination: yes, vibration resistance matters

Yes, this matters a lot.

For machines with:

- vibration,
- repetitive shock,
- moving cable tracks,
- hydraulic power units,
- conveyors,
- fans,
- pumps,

you should treat termination quality as part of safety reliability.

Best practice:

- use **stranded wire**
- use **properly crimped ferrules** where the terminal system and manufacturer allow / recommend them
- use **spring-clamp** or vibration-resistant terminal technology where practical
- if using screw terminals, torque them correctly and follow terminal manufacturer requirements
- use terminals with proven vibration resistance for machine wiring

Phoenix Contact literature explicitly states spring and certain screw terminal systems are **vibration-resistant** and **maintenance-free**, and their ferrule guidance notes ferrules improve conductor stability and mechanical reliability. ([assets.phoenixcontact.com][3])

### My blunt recommendation

For machine safety I/O:

- **panel side**: spring terminals or high-quality screw terminals with ferrules
- **device side**: ferrules where accepted, otherwise the exact termination type the device manufacturer specifies
- avoid loose fine-strand wire under clamp plates with no ferrule unless the terminal is specifically designed for that conductor form

---

# Simultaneous actuation: how close do both channels need to switch?

They do **not** need to switch at the exact same microsecond.

Safety controllers expect a small timing difference between Channel 1 and Channel 2. That is handled with:

- **input filter time**
- **discrepancy time**

This is the key setting for dual-channel inputs.

## Discrepancy time

Discrepancy time is the maximum allowed delay between the two channels changing state.

Examples from vendor documentation:

- Rockwell POINT Guard I/O documentation shows **100 ms** discrepancy time as an application-dependent value for dual-channel safety inputs. ([Rockwell Automation][4])
- Siemens safety documentation states discrepancy time must be set less than the shortest expected time between switching events, and the F-DI input filter / discrepancy monitoring are configurable. ([Siemens Support][5])
- Newer Rockwell Guardmaster interface documentation flags **Input Channel Discrepancy >30 ms** as a diagnostic event on some devices. ([Rockwell Automation][6])

## What that means practically

For **mechanical NC contacts** operated by one actuator:

- a few milliseconds difference is normal
- tens of milliseconds can still be acceptable if the input configuration is set correctly
- if the channels separate too far apart in time, the controller may fault on discrepancy

### Good starting rule

For a hardwired mechanical dual-channel device:

- start with **20–100 ms discrepancy**, depending on the controller and device
- then set it based on the actual hardware behavior and the manufacturer instructions
- do **not** make it huge unless justified, because you reduce diagnostic sharpness

### Important point

You do **not** solve timing issues by trying to “match wire lengths perfectly.”
You solve them by:

- using the right device type,
- using the right safety input configuration,
- and setting the correct discrepancy / debounce parameters.

Wire length mismatch at normal machine scales is usually not the real issue. Mechanical contact travel and controller filtering are the real issue.

---

# Recommended hardwired pattern for dual-channel contact inputs

For a standard mechanical safety device:

## Preferred pattern

- 24 VDC safety-rated source or test pulse output
- **Channel 1 through NC contact 1**
- **Channel 2 through NC contact 2**
- each channel to its own safety input
- use separate return / diagnostic structure per module manual
- configure:
  - dual-channel equivalent
  - pulse test / cross-short detection
  - discrepancy time
  - manual reset if required by the safety function

### Example

```text
T0 (test pulse 1) → E-stop NC contact 1 → SI0
T1 (test pulse 2) → E-stop NC contact 2 → SI1
```

Not this:

```text
24V → jumper → both contacts → tied together → one input pair
```

That defeats diagnostics.

---

# How to choose wire and termination for a real machine

## Inside the panel

Use:

- **18 AWG stranded copper**
- **600 V machine wire**
- ferrules
- blue for 24 VDC ungrounded control
- labeled wire markers
- spring or torque-controlled screw terminals

## Field device wiring

Use cable with:

- suitable flex rating if moving
- oil / coolant resistance if near hydraulics
- shield only when needed by the device or EMI environment
- twisted pair can help with noise immunity in bad EMI areas
- separate routing from VFD motor leads and high-energy conductors

## For vibration

Use:

- ferrules
- strain relief
- clamp the cable jacket, not just the conductors
- no unsupported conductor hanging into a terminal
- no wirenuts
- no untinned fine strands under a screw unless the terminal permits it

---

# On contact type and device choice

For **E-stops and gate switches**, use devices with:

- safety-rated positive-opening contacts
- manufacturer data for PL / SIL use
- guidance on maximum bounce / switching characteristics
- compatibility with pulsed safety inputs

Do not assume any industrial pushbutton is suitable for a safety function.

---

# My practical recommendation for your baseline spec

For a 24 VDC dual-channel hardwired safety input on an industrial machine:

## Baseline specification

- **Voltage**: 24 VDC
- **Device type**: dual NC, positive-opening safety contacts
- **Wiring**: separate CH1 and CH2 conductors back to the safety input
- **Wire**: 18 AWG stranded copper minimum typical default
- **Insulation**: 600 V machine-control rated wire/cable suitable for environment
- **Color**:
  - blue = ungrounded DC control
  - proper identified DC common per plant/machine convention
  - orange / orange-blue stripe where always energized applies

- **Termination**:
  - ferrules where permitted
  - spring-clamp or vibration-resistant terminal system preferred
  - proper strain relief

- **Programming/config**:
  - dual-channel monitoring
  - pulse-test / cross-short detection enabled where supported
  - discrepancy time set per actual device behavior, often starting in the **20–100 ms** range unless the vendor requires something else
  - manual reset where required by the risk assessment

---

# The part you should be careful about

Your statement that:

> “All safety inputs are Normally Open Held Close type of contacts…”

is where a lot of bad safety designs start.

For **hardwired contact-based safety**, your default mental model should be:

- **NC, held closed, fail-safe, dual channel**

For **electronic safety sensors** like light curtains and OSSDs:

- outputs are electronic and behave differently
- the wiring and diagnostics are not the same as a dry contact loop

Do not mix those two models.

---

# Bottom line

Yes, all of this matters.

The correct answer is not:

- “just use two wires,” or
- “any 18 AWG is fine,” or
- “termination doesn’t matter.”

The correct answer is:

1. use **two truly separate channels**,
2. use **fail-safe contact logic** for hardwired devices,
3. use **machine-rated wire and correct identification**,
4. use **vibration-resistant terminations**,
5. and set the **discrepancy time** in the safety controller based on the actual device and manufacturer guidance.

If you want, next I’ll lay out the **6 standard safety wiring patterns** you will keep seeing in real machines: E-stop, guard door, OSSD sensor, EDM feedback, reset circuit, and STO.

[1]: https://literature.rockwellautomation.com/idc/groups/literature/documents/um/440r-um015_-en-p.pdf?utm_source=chatgpt.com "Guardmaster DG Safety Relay and GuardLink System"
[2]: https://www.ul.com/resources/machine-supply-circuit-and-disconnecting-means?utm_source=chatgpt.com "Machine Supply Circuit and Disconnecting Means"
[3]: https://assets.phoenixcontact.com/file/257a95b8-0ae0-4b65-8476-514c169bc2ba/media/original?1540293_EN_Aderendhuelsen_LoRes.pdf=&utm_source=chatgpt.com "What you should know about ferrules"
[4]: https://literature.rockwellautomation.com/idc/groups/literature/documents/um/1734-um013_-en-p.pdf?utm_source=chatgpt.com "POINT Guard I/O Safety Modules User Manual, 1734-UM013R ..."
[5]: https://support.industry.siemens.com/cs/attachments/109782490/G120_Safety_fct_man_0920_en-US.pdf?utm_source=chatgpt.com "Safety Integrated - SINAMICS G110M, G115D, G120, ..."
[6]: https://literature.rockwellautomation.com/idc/groups/literature/documents/um/440r-um009_-en-p.pdf?utm_source=chatgpt.com "Guardmaster EtherNet/IP Network Interface - Literature Library"

Below are the **six wiring patterns that appear repeatedly in industrial machine safety systems**.
These patterns form the backbone of **Category 3 / Category 4 (PL d–e) architectures** under standards such as:

- ISO 13849-1
- IEC 62061
- NFPA 79

Regardless of industry, most machines are composed of combinations of these patterns.

---

# The 6 Fundamental Safety Wiring Patterns

| Pattern | Purpose                  | Typical Devices            |
| ------- | ------------------------ | -------------------------- |
| 1       | Emergency Stop loop      | E-stop pushbuttons         |
| 2       | Guard interlock circuit  | Door switches              |
| 3       | OSSD sensor safety input | Light curtains / scanners  |
| 4       | EDM feedback monitoring  | Contactors / safety relays |
| 5       | Manual reset circuit     | Reset pushbutton           |
| 6       | Safe Torque Off (STO)    | Servo drives / VFDs        |

These patterns connect into the **core safety architecture**:

```
Safety Inputs
(E-stop, guard, sensors)
        ↓
Safety Controller
        ↓
Safety Outputs
(STO, contactor, valves)
```

---

# 1. Emergency Stop (Dual Channel NC)

This is the most universal safety circuit.

### Wiring pattern

```
24V test output A → E-stop NC contact 1 → Safety Input CH1
24V test output B → E-stop NC contact 2 → Safety Input CH2
```

Characteristics:

- **NC positive-opening contacts**
- **dual channel**
- controller checks discrepancy timing

Why NC?

A broken wire opens the circuit → machine stops.

### Typical architecture

```
E-STOP
  CH1 ───────► Safety Input 1
  CH2 ───────► Safety Input 2
```

Used in:

- almost every machine in every industry.

---

# 2. Guard Door Interlock

Used when a **physical hazard zone must be isolated**.

Two main types:

- mechanical tongue switch
- coded magnetic / RFID safety switch

### Wiring pattern

```
24V → Guard switch channel 1 → Safety input CH1
24V → Guard switch channel 2 → Safety input CH2
```

Safety PLC monitors both channels.

Some systems also include **guard locking solenoids**.

Example architecture:

```
Guard Door
   ↓
Safety PLC
   ↓
Unlock guard only when machine safe
```

---

# 3. OSSD Sensor Inputs (Electronic Safety Outputs)

Used by:

- light curtains
- safety laser scanners
- safety vision systems

Instead of dry contacts, these use **electronic outputs** called **OSSD**.

### Wiring pattern

```
Sensor OSSD1 → Safety input CH1
Sensor OSSD2 → Safety input CH2
```

Sensor performs self-diagnostics:

- short detection
- cross-channel fault detection
- internal monitoring

Controller just reads the channels.

Example:

```
Light Curtain
   OSSD1 ─► Safety PLC input 1
   OSSD2 ─► Safety PLC input 2
```

---

# 4. EDM Feedback (External Device Monitoring)

Ensures **output contactors actually opened**.

Without this, a welded contactor could leave power on.

### Wiring pattern

```
Safety PLC Output → Contactor coil

Contactor auxiliary NC
        ↓
Safety PLC feedback input
```

Architecture:

```
Safety PLC
   ↓
Contactor
   ↓
Aux feedback → Safety PLC
```

If contactor welds:

Machine **cannot reset**.

---

# 5. Manual Reset Circuit

Prevents automatic restart after a hazard clears.

Required in many standards.

### Wiring pattern

```
Reset button NO → Safety PLC reset input
```

Logic example:

```
IF
   safety conditions OK
AND
   reset pressed
THEN
   enable outputs
```

Key rule:

Reset must be **manual** and **outside the hazard zone**.

---

# 6. Safe Torque Off (STO)

Modern machines stop motion **inside the drive**, not by cutting power.

Used with:

- servo drives
- VFDs
- robotic axes

### Wiring pattern

```
Safety PLC output 1 → STO channel 1
Safety PLC output 2 → STO channel 2
```

Inside the drive:

- torque generation disabled
- motor power stage disabled

Architecture:

```
Safety PLC
   ↓
STO inputs
   ↓
Servo drive
```

No contactors needed for motion stopping.

---

# Comparison Across Industries

The **same patterns exist everywhere**, but the implementation changes depending on risk and environment.

| Industry        | Typical Safety Level | Special Requirements |
| --------------- | -------------------- | -------------------- |
| Semiconductor   | PL d–e               | high-speed robotics  |
| Marine          | SIL2                 | corrosion protection |
| Offshore oil    | SIL2–3               | explosion proof      |
| Nuclear         | SIL3                 | redundancy           |
| Medical devices | SIL2–3               | traceability         |
| Food industry   | PL d                 | washdown             |
| Agriculture     | PL c–d               | rugged sensors       |
| Hospitals       | SIL2                 | patient safety       |

---

# Industry Differences

## Semiconductor / Robotics

Typical architecture:

```
Light curtain
Robot safety fence
E-stop
       ↓
Safety PLC
       ↓
Robot STO
Servo STO
Vacuum valve shutoff
```

Focus:

- fast stop times
- robotic motion safety
- interlocked access zones.

---

## Marine Systems

Additional constraints:

- corrosion resistant wiring
- shielded cables
- vibration protection

Example:

```
Bridge E-stop
Engine guard
Hydraulic interlock
       ↓
Safety PLC
       ↓
Hydraulic dump valve
Engine shutdown
```

Standards emphasize **environmental durability**.

---

## Offshore / Petroleum

Explosion risk dominates design.

Safety outputs often drive:

```
ESD valves
Fire shutdown systems
Blowout preventer controls
```

Architecture:

```
Sensors
   ↓
SIL3 safety system
   ↓
Emergency shutdown valves
```

Devices must be **ATEX / hazardous area rated**.

---

## Nuclear Industry

Safety architecture is much more complex.

Typical characteristics:

- triple redundancy
- diverse control systems
- independent power supplies

Example architecture:

```
Sensor A
Sensor B
Sensor C
     ↓
Safety logic voting
(2oo3 voting)
     ↓
Reactor trip system
```

This goes beyond typical machine safety.

---

## Medical / Hospital Systems

Examples:

- radiation therapy machines
- surgical robotics

Safety functions include:

```
Emergency stop
Collision detection
Radiation shielding interlock
```

Architectures often include:

- redundant processors
- traceable event logging.

---

## Food and Beverage Industry

Main differences:

- washdown environments
- corrosion resistant materials

Typical pattern:

```
Guard door
Light curtain
E-stop
       ↓
Safety PLC
       ↓
Motor STO
Conveyor stop
```

All hardware must be:

- stainless
- IP67 or higher.

---

## Agricultural Machinery

Often uses simpler safety architecture.

Example:

```
Seat switch
Guard switch
PTO safety
```

Usually:

```
PL c or PL d
```

Focus is durability.

---

# Key Insight

Across industries:

**The six wiring patterns remain the same.**

What changes is:

- redundancy level
- environmental protection
- certification requirements
- documentation rigor.

---

# Practical Summary

The **core building blocks of machine safety wiring** are:

1. Dual-channel E-stop
2. Dual-channel guard interlock
3. OSSD safety sensors
4. Contactor feedback monitoring
5. Manual reset circuit
6. Safe torque off outputs

Combine these patterns and you can design **almost any industrial machine safety system**.

---

If you want, I can also show you something useful for your control-systems work:

**The “Universal Machine Safety Architecture” used by companies like ASML, Tesla, and AMAT — a layered model that integrates these six patterns into a full machine safety system.**
Below is the **Universal Machine Safety Architecture** used in modern industrial equipment.
This model is not a single standard but a **practical architecture derived from multiple safety frameworks**, including:

- IEC 61508
- ISO 13849-1
- IEC 62061
- NFPA 79

This architecture is widely used in high-end industrial systems such as semiconductor equipment, robotics, automated warehouses, and process plants.

---

# Universal Machine Safety Architecture

A modern machine safety system can be understood as **7 layers**.

```text
Layer 1  Hazard Source
Layer 2  Energy Isolation
Layer 3  Safety Actuators
Layer 4  Safety Control System
Layer 5  Safety Sensors
Layer 6  Human Interface
Layer 7  Risk Management / Procedures
```

Think of it as **defense in depth**.
If one layer fails, another layer still protects the operator.

---

# Layer 1 — Hazard Source

This is the **physical energy** that can cause harm.

Examples:

| Hazard             | Source            |
| ------------------ | ----------------- |
| Mechanical motion  | motors, robots    |
| Hydraulic pressure | cylinders         |
| Pneumatic pressure | actuators         |
| Electrical power   | drives, heaters   |
| Chemical energy    | dosing systems    |
| Radiation          | medical / nuclear |

Example machine:

```text
Servo motor → gearbox → hydraulic piston
```

This is where the hazard originates.

---

# Layer 2 — Energy Isolation

These devices **physically disconnect energy**.

Typical devices:

| Device                  | Purpose              |
| ----------------------- | -------------------- |
| main disconnect switch  | electrical isolation |
| lockout breaker         | maintenance safety   |
| hydraulic dump valve    | remove pressure      |
| pneumatic exhaust valve | depressurize system  |

Example architecture:

```text
Power supply
     ↓
Main disconnect
     ↓
Motor drive
```

This layer supports **lockout/tagout procedures**.

---

# Layer 3 — Safety Actuators

These are **devices that remove hazardous motion automatically**.

Typical components:

| Device               | Function            |
| -------------------- | ------------------- |
| safety contactor     | cut motor power     |
| STO input on drive   | disable torque      |
| hydraulic dump valve | release pressure    |
| pneumatic vent valve | remove air pressure |

Example:

```text
Safety PLC
     ↓
STO
     ↓
Servo drive stops torque
```

This layer is responsible for **actually stopping the machine**.

---

# Layer 4 — Safety Control System

This is the **logic layer**.

Typical implementations:

| Device            | Example                    |
| ----------------- | -------------------------- |
| Safety PLC        | GuardLogix / Siemens F-CPU |
| Safety relay      | Pilz PNOZ                  |
| Safety controller | distributed safety IO      |

The controller evaluates:

```text
E-stop
Guard door
Light curtain
Robot zone
```

Then determines if outputs are allowed.

Typical logic:

```text
IF
  guard_closed
AND
  estop_ok
AND
  sensor_clear
THEN
  enable_motion
```

---

# Layer 5 — Safety Sensors

These detect hazards or unsafe access.

Examples:

| Device          | Application           |
| --------------- | --------------------- |
| E-stop button   | manual emergency stop |
| light curtain   | human detection       |
| safety scanner  | robot zone monitoring |
| guard interlock | door safety           |
| pressure sensor | hydraulic safety      |

Architecture:

```text
Sensors → Safety PLC
```

Many sensors use **dual channel signals**.

---

# Layer 6 — Human Interface

Operators must interact safely with the machine.

Examples:

| Device          | Purpose            |
| --------------- | ------------------ |
| reset button    | controlled restart |
| HMI             | status display     |
| key switch      | maintenance mode   |
| enabling switch | robot teaching     |

Typical requirement:

- reset must be **outside the hazard zone**
- operator must **see the hazard area before restart**

---

# Layer 7 — Risk Management / Procedures

Even perfect hardware cannot prevent all hazards.

Operational safety includes:

| Procedure          | Example       |
| ------------------ | ------------- |
| lockout tagout     | maintenance   |
| safety training    | operators     |
| hazard analysis    | design phase  |
| validation testing | commissioning |

This layer ensures **the safety system is used correctly**.

---

# Example: Full Machine Safety Stack

Example system:

**Hydraulic + servo machine with chemical pumps**

Architecture:

```text
Layer 5
E-stop
Guard door
Light curtain
Pressure sensor
        ↓

Layer 4
Safety PLC
        ↓

Layer 3
STO
Hydraulic dump valve
Pump contactor
        ↓

Layer 2
Main disconnect
Lockout valve
        ↓

Layer 1
Servo motor
Hydraulic piston
Chemical pump
```

Operator interface:

```text
Reset button
HMI
Maintenance key
```

---

# What High-End Machines Add

Advanced equipment adds more layers.

Example semiconductor machine:

```text
Robot zone scanners
Access interlocks
Dual safety PLCs
Redundant STO channels
Vacuum system safety
Gas monitoring
```

These machines often reach:

```text
PL e / SIL 3
```

---

# Safety System Example (Robot Cell)

Architecture:

```text
Light curtain
Safety scanner
Fence interlock
E-stop
        ↓
Safety PLC
        ↓
Robot STO
Servo STO
Conveyor stop
Hydraulic dump valve
```

Reset required before restart.

---

# Architecture Differences by Industry

| Industry      | Safety Characteristics        |
| ------------- | ----------------------------- |
| Semiconductor | fast robotics, complex zoning |
| Oil & gas     | emergency shutdown systems    |
| Nuclear       | triple redundancy             |
| Medical       | strict traceability           |
| Food          | washdown hardware             |
| Marine        | corrosion protection          |
| Agriculture   | rugged sensors                |

But the **layered model remains the same**.

---

# Important Engineering Insight

A safe machine is **not just a safety PLC**.

Safety requires **multiple independent protection layers**.

Typical design principle:

```text
Hazard
 ↓
Prevent access
 ↓
Detect access
 ↓
Stop motion
 ↓
Remove energy
```

---

# Practical Design Rule

When designing a machine:

1. Identify hazards
2. Define safety functions
3. select architecture (PL/SIL)
4. implement layered safety
5. validate system

---

# How Advanced Automation Companies Design Safety

Companies like semiconductor or robotics manufacturers often use:

```text
Safety sensors
      ↓
Distributed safety IO
      ↓
Safety PLC
      ↓
STO / safety valves
      ↓
Energy isolation
```

Often integrated with **safe industrial networks**.

---

If you want, the next useful step is something many controls engineers never see clearly documented:

**The “15-standard minimum compliance stack” used when designing industrial machines (semiconductor / robotics / automation equipment).**

That stack explains **exactly which safety standards must be satisfied simultaneously when building a real machine.**

Choosing **process-based safety interlocks** (pressure, temperature, current, flow, etc.) is different from choosing **machine access safety devices** like E-stops or light curtains.

These interlocks protect the machine from **dangerous operating conditions**, not from **human access hazards**.

They are implemented under functional safety frameworks such as:

- IEC 61508
- IEC 62061
- ISO 13849-1

Process industries (oil, nuclear, chemical) use similar concepts in:

- IEC 61511

The key idea is a **Safety Instrumented Function (SIF)**.

---

# 1. Define the Safety Function First

Before choosing the sensor, define the **interlock function**.

Example:

| Hazard                  | Safety Function |
| ----------------------- | --------------- |
| hydraulic over-pressure | stop pump       |
| motor overheating       | stop drive      |
| high current            | trip system     |
| chemical tank overflow  | close valve     |

Each function must specify:

```
Process sensor → safety logic → shutdown actuator
```

Example:

```
Pressure switch → Safety PLC → pump contactor
```

---

# 2. Decide the Required Safety Level

Perform a **risk assessment** to determine the required safety level.

Possible targets:

| Level       | Typical Application       |
| ----------- | ------------------------- |
| PL c / SIL1 | simple machine protection |
| PL d / SIL2 | hazardous machinery       |
| PL e / SIL3 | critical safety systems   |

Higher levels require:

- redundancy
- diagnostics
- certified devices

---

# 3. Choose Sensor Type

Process safety sensors come in **two categories**.

## Mechanical Safety Switches

Examples:

| Device             | Example        |
| ------------------ | -------------- |
| pressure switch    | diaphragm type |
| temperature switch | bimetal        |
| flow switch        | paddle         |

Advantages:

- simple
- fail-safe
- deterministic

Disadvantages:

- less precise
- limited diagnostics

These are common in **machine safety interlocks**.

---

## Electronic Sensors

Examples:

| Sensor                  | Output         |
| ----------------------- | -------------- |
| pressure transmitter    | 4–20 mA        |
| temperature transmitter | 4–20 mA        |
| current transducer      | analog         |
| flow meter              | analog/digital |

Advantages:

- precise
- programmable thresholds
- diagnostics

Disadvantages:

- requires logic controller

Common in **process safety systems**.

---

# 4. Select the Trip Method

There are two ways to implement shutdown.

## Direct Hardware Interlock

Sensor directly breaks the safety circuit.

Example:

```
Pressure switch (NC) → safety relay
```

Used for:

- compressors
- pumps
- hydraulic systems

---

## PLC / Safety PLC Interlock

Sensor feeds a controller which decides.

Example:

```
Pressure transmitter → Safety PLC → trip output
```

Used when:

- thresholds are dynamic
- multiple sensors involved
- diagnostics needed.

---

# 5. Choose Fail-Safe Behavior

Safety sensors must fail **toward the safe state**.

Typical practice:

| Signal Type        | Fail Safe                    |
| ------------------ | ---------------------------- |
| contact switch     | NC contact                   |
| analog transmitter | low signal indicates failure |

Example:

```
4 mA = sensor fault
20 mA = maximum range
```

This allows detection of wiring failure.

---

# 6. Use Redundancy When Needed

Higher safety levels require multiple sensors.

Typical architectures:

### 1oo1

One sensor trips system.

```
Sensor → shutdown
```

Lowest reliability.

---

### 1oo2

Either sensor trips system.

```
Sensor A
        → shutdown
Sensor B
```

Higher safety.

---

### 2oo3 Voting

Two of three sensors must agree.

```
Sensor A
Sensor B → voting logic → shutdown
Sensor C
```

Common in nuclear and oil systems.

---

# 7. Example: Hydraulic Over-Pressure Protection

System:

```
Hydraulic pump
Cylinder
Pressure sensor
```

Safety design:

```
Pressure switch (NC)
      ↓
Safety PLC
      ↓
Hydraulic dump valve
Pump shutdown
```

Trigger:

```
Pressure > limit
```

Shutdown sequence:

1. stop pump
2. open pressure relief valve

---

# 8. Example: Motor Overcurrent Protection

Protection layers:

```
Motor current sensor
        ↓
Safety PLC
        ↓
Drive STO
```

Trip condition:

```
Current > threshold for defined time
```

This prevents:

- motor damage
- mechanical overload

---

# 9. Example: Temperature Interlock

Example machine:

```
heater
temperature sensor
```

Interlock logic:

```
Temperature > 120°C
        ↓
Shutdown heater
```

Often implemented with:

- dual temperature switches
- or transmitter + PLC.

---

# 10. Typical Safety Interlock Architecture

A robust design:

```
Process Sensor
       ↓
Safety PLC
       ↓
Shutdown device
       ↓
Energy isolation
```

Example shutdown devices:

| Device    | Action               |
| --------- | -------------------- |
| contactor | remove power         |
| STO       | disable motor torque |
| valve     | release pressure     |
| pump stop | stop fluid flow      |

---

# 11. Key Sensor Selection Criteria

When choosing sensors for safety interlocks evaluate:

| Factor               | Why                    |
| -------------------- | ---------------------- |
| safety certification | required for SIL       |
| fail-safe output     | detect faults          |
| response time        | trip speed             |
| environmental rating | temperature, vibration |
| accuracy             | avoid nuisance trips   |
| diagnostics          | fault detection        |

---

# 12. Typical Industrial Interlock Sensors

Common manufacturers:

| Device Type        | Example       |
| ------------------ | ------------- |
| pressure switch    | WIKA, Danfoss |
| temperature switch | Honeywell     |
| flow switch        | Gems          |
| current sensor     | LEM           |

Select models rated for:

- vibration
- temperature
- pressure range
- electrical environment.

---

# 13. Multi-Sensor Safety Logic Example

Example chemical dosing system:

```
Tank level high
Pump current high
Pressure high
Temperature high
```

Logic:

```
IF any condition unsafe
THEN shutdown system
```

Architecture:

```
Sensors → Safety PLC → pump shutdown + valve close
```

---

# 14. Process vs Machine Safety

Important distinction:

| Machine Safety | Process Safety    |
| -------------- | ----------------- |
| protect people | protect system    |
| E-stop         | pressure trip     |
| light curtain  | temperature limit |
| guard switch   | flow limit        |

Both must work together.

---

# Practical Rule

When designing safety interlocks:

1. identify hazard
2. define safety function
3. determine required PL/SIL
4. choose fail-safe sensors
5. implement shutdown path
6. validate response time.

---

If you'd like, I can also show a **very useful engineering tool**:

A **universal process-interlock design template** that lists about **25 common industrial safety interlocks (pressure, flow, level, vibration, temperature, current, etc.) used in real machines**. This is what many equipment manufacturers use during design reviews.

Below is a **practical engineering template of common industrial process-safety interlocks**.
This is similar to the checklist used during **machine design reviews, HAZOP, or safety validation** in industries like automation, semiconductor equipment, oil & gas, robotics, and process plants.

The safety logic normally feeds a **Safety PLC or safety relay** which then triggers shutdown actions.

---

# Universal Process-Safety Interlock Template

Each safety function follows the same structure:

```
Process Variable → Sensor → Safety Logic → Shutdown Action
```

Example:

```
Pressure → Pressure switch → Safety PLC → Pump shutdown
```

---

# 1. Pressure Safety Interlocks

Used in hydraulic, pneumatic, and fluid systems.

| Interlock          | Sensor              | Action              |
| ------------------ | ------------------- | ------------------- |
| High pressure      | pressure switch     | stop pump           |
| Very high pressure | redundant switch    | open relief valve   |
| Low pressure       | pressure switch     | stop system         |
| pressure spike     | transmitter + logic | controlled shutdown |

Example architecture:

```
Hydraulic pressure switch
        ↓
Safety PLC
        ↓
Stop pump + open dump valve
```

Typical applications:

- hydraulic presses
- chemical dosing systems
- compressors
- steam systems

---

# 2. Temperature Safety Interlocks

Used when overheating can cause fire or equipment damage.

| Interlock           | Sensor           | Action             |
| ------------------- | ---------------- | ------------------ |
| high temperature    | thermostat       | stop heater        |
| extreme temperature | redundant switch | emergency shutdown |
| coolant temperature | RTD              | stop motor         |
| cabinet temperature | thermal switch   | stop electronics   |

Example:

```
Motor temperature sensor
       ↓
Safety PLC
       ↓
Disable drive STO
```

Typical use:

- motors
- furnaces
- power electronics
- battery systems.

---

# 3. Current / Electrical Load Interlocks

Protect motors and electrical systems.

| Interlock    | Sensor           | Action          |
| ------------ | ---------------- | --------------- |
| overcurrent  | current relay    | stop motor      |
| phase loss   | phase monitor    | shutdown system |
| ground fault | protection relay | isolate power   |
| overvoltage  | voltage monitor  | trip supply     |

Example:

```
Current monitor
      ↓
Safety PLC
      ↓
Drive shutdown
```

Used in:

- conveyor systems
- pumps
- compressors
- robotics.

---

# 4. Flow Safety Interlocks

Used in cooling and fluid systems.

| Interlock    | Sensor      | Action       |
| ------------ | ----------- | ------------ |
| no flow      | flow switch | stop pump    |
| low flow     | transmitter | reduce power |
| reverse flow | flow meter  | close valve  |

Example:

```
Cooling water flow switch
       ↓
Safety PLC
       ↓
Stop heater
```

Applications:

- heat exchangers
- cooling loops
- lubrication systems.

---

# 5. Level Safety Interlocks

Prevent tank overflow or pump damage.

| Interlock       | Sensor           | Action             |
| --------------- | ---------------- | ------------------ |
| high level      | level switch     | stop pump          |
| high-high level | redundant switch | emergency shutdown |
| low level       | level switch     | stop pump          |
| dry run         | level sensor     | stop pump          |

Example:

```
Tank high-level switch
      ↓
Safety PLC
      ↓
Stop fill valve
```

Used in:

- chemical tanks
- water systems
- oil tanks.

---

# 6. Mechanical Motion Interlocks

Protect mechanical systems.

| Interlock           | Sensor           | Action          |
| ------------------- | ---------------- | --------------- |
| overspeed           | speed sensor     | stop drive      |
| jam detection       | torque/current   | stop motor      |
| excessive vibration | vibration switch | shutdown system |
| position limit      | limit switch     | stop motion     |

Example:

```
Overspeed sensor
      ↓
Safety PLC
      ↓
Drive STO
```

Common in:

- turbines
- conveyors
- centrifuges.

---

# 7. Environmental Safety Interlocks

Used in hazardous environments.

| Interlock       | Sensor           | Action               |
| --------------- | ---------------- | -------------------- |
| gas detection   | gas sensor       | shutdown ventilation |
| fire detection  | smoke detector   | system shutdown      |
| oxygen level    | O₂ sensor        | alarm + stop process |
| radiation level | radiation sensor | emergency stop       |

Example:

```
Gas detector
      ↓
Safety PLC
      ↓
Close gas valve
```

Used in:

- offshore oil
- chemical plants
- laboratories.

---

# 8. Cooling System Interlocks

Protect electronics and drives.

| Interlock        | Sensor          | Action         |
| ---------------- | --------------- | -------------- |
| fan failure      | tach signal     | stop system    |
| coolant flow     | flow switch     | stop heater    |
| coolant pressure | pressure switch | shutdown drive |

Example:

```
Fan speed sensor
       ↓
Safety PLC
       ↓
Disable power electronics
```

---

# 9. Utility Supply Interlocks

Protect system when utilities fail.

| Interlock            | Sensor          | Action                |
| -------------------- | --------------- | --------------------- |
| air supply failure   | pressure switch | stop pneumatic system |
| water supply failure | flow sensor     | shutdown system       |
| vacuum loss          | vacuum switch   | stop process          |

Example:

```
Air pressure switch
      ↓
Safety PLC
      ↓
Disable actuators
```

---

# 10. Chemical Process Interlocks

Used in dosing and mixing systems.

| Interlock            | Sensor        | Action         |
| -------------------- | ------------- | -------------- |
| pH out of range      | pH sensor     | stop dosing    |
| chemical leak        | leak detector | shutdown pump  |
| reaction temperature | RTD           | emergency stop |

Example:

```
Leak detector
      ↓
Safety PLC
      ↓
Stop pump + close valve
```

---

# Typical Interlock Shutdown Hierarchy

Most machines implement **multiple layers of shutdown**.

Example:

```
Sensor detects hazard
        ↓
Safety PLC logic
        ↓
Shutdown outputs
```

Shutdown actions may include:

| Action           | Device     |
| ---------------- | ---------- |
| stop motor       | STO        |
| isolate power    | contactor  |
| release pressure | dump valve |
| stop pump        | VFD stop   |
| close valve      | actuator   |

---

# Example: Full Interlock System

Example hydraulic + chemical machine.

```
Pressure high
Temperature high
Tank level high
Pump current high
Cooling flow low
```

Architecture:

```
Sensors
   ↓
Safety PLC
   ↓
STO + pump shutdown + valve close
```

---

# Good Engineering Practice

When implementing interlocks:

1. identify hazard
2. define safe operating range
3. select fail-safe sensor
4. verify response time
5. implement shutdown path
6. validate during testing.

---

# Typical Interlock Levels

| Level             | Purpose        |
| ----------------- | -------------- |
| alarm             | warn operator  |
| control interlock | automatic stop |
| safety shutdown   | emergency stop |

Example:

```
Temperature > 80°C → alarm
Temperature > 100°C → shutdown
Temperature > 120°C → emergency trip
```

---

# Engineering Insight

In many real machines:

- **30–50 interlocks** exist
- only **5–10 are safety critical**

The rest are **equipment protection interlocks**.

Distinguishing these is crucial during design.

---

If you'd like, I can also show something extremely useful for a controls engineer:

**The standard “Industrial Shutdown Hierarchy” (Alarm → Interlock → Trip → Emergency Shutdown) used in oil & gas, robotics, semiconductor tools, and chemical plants.**

Understanding this hierarchy helps design **safe and stable machines without nuisance trips.**
The **Industrial Shutdown Hierarchy** organizes how machines respond when process conditions move outside safe limits. It prevents nuisance trips while ensuring that **dangerous conditions reliably stop the system**.

This concept is widely used in industrial automation and process industries under standards such as:

- IEC 61508
- IEC 61511
- ISO 13849-1

The hierarchy separates responses into **four levels**.

---

# Industrial Shutdown Hierarchy

```text
Level 1  Alarm
Level 2  Control Interlock
Level 3  Safety Trip
Level 4  Emergency Shutdown (ESD)
```

Each level becomes progressively more serious.

---

# Level 1 — Alarm

Purpose: **Warn the operator before a dangerous condition occurs.**

Typical actions:

- HMI warning
- annunciator light
- audible alarm
- operator message

Example:

```text
Temperature > 80°C → Alarm
```

Operator intervention is expected.

Typical sensors:

| Variable    | Sensor         |
| ----------- | -------------- |
| temperature | RTD            |
| pressure    | transmitter    |
| current     | current sensor |
| flow        | flow meter     |

Common environments:

- manufacturing machines
- semiconductor tools
- HVAC systems.

---

# Level 2 — Control Interlock

Purpose: **Automatically prevent unsafe operation but without a full shutdown.**

Example logic:

```text
Cooling flow low → reduce heater power
```

Typical actions:

- reduce speed
- disable certain functions
- stop a subsystem

Example architecture:

```text
Sensor
   ↓
PLC control logic
   ↓
Controlled system adjustment
```

Example:

```text
Low hydraulic pressure → stop motion commands
```

This level helps maintain **stable operation**.

---

# Level 3 — Safety Trip

Purpose: **Stop the machine safely when hazardous conditions occur.**

Typical shutdown actions:

- disable drives
- stop pumps
- close valves
- vent pressure

Example:

```text
Hydraulic pressure > limit → trip pump
```

Architecture:

```text
Sensor
   ↓
Safety PLC
   ↓
Trip outputs
```

Trip devices may include:

| Device     | Action               |
| ---------- | -------------------- |
| STO        | disable motor torque |
| contactor  | remove power         |
| valve      | stop fluid           |
| dump valve | release pressure     |

This level is usually designed for **PL d / SIL2** systems.

---

# Level 4 — Emergency Shutdown (ESD)

Purpose: **Protect life or prevent catastrophic failure.**

Triggered by:

- extreme conditions
- multiple failures
- manual emergency stop

Typical actions:

- isolate all power
- close emergency valves
- depressurize systems
- activate fire protection

Example:

```text
Pressure > critical limit → emergency shutdown
```

Architecture:

```text
Critical sensor
      ↓
ESD system
      ↓
Full system shutdown
```

This layer is common in:

- oil & gas plants
- nuclear facilities
- chemical plants
- large robotics cells.

---

# Example Shutdown Ladder

Example temperature protection:

```text
Temperature > 80°C → Alarm
Temperature > 95°C → Control interlock
Temperature > 110°C → Safety trip
Temperature > 130°C → Emergency shutdown
```

This prevents unnecessary shutdown while still ensuring safety.

---

# Example Machine Implementation

Hydraulic + servo machine:

### Alarm level

```text
Temperature > 70°C → HMI warning
```

### Interlock

```text
Cooling flow low → disable high-speed operation
```

### Trip

```text
Hydraulic pressure high → stop pump
```

### Emergency shutdown

```text
Pressure extreme → dump hydraulic pressure
```

---

# Example Architecture

```text
Sensors
  ↓
PLC (alarm/interlock)
  ↓
Safety PLC (trip logic)
  ↓
Shutdown devices
```

Shutdown devices include:

- STO inputs
- contactors
- valves
- dump valves.

---

# Example: Industrial Robot Cell

Possible shutdown hierarchy:

```text
Robot zone scanner warning → Alarm
Robot zone intrusion → Stop robot motion
Robot collision detection → Safety trip
E-stop → Emergency shutdown
```

---

# Example: Chemical Process System

```text
Tank level high → Alarm
Tank level very high → Close inlet valve
Tank overflow risk → Stop pump
Tank rupture risk → Emergency shutdown
```

---

# Why This Hierarchy Is Important

Without this hierarchy:

- machines **trip too often**
- production becomes unstable
- operators bypass safety systems.

Proper shutdown hierarchy ensures:

1. early warning
2. controlled correction
3. safe stopping
4. emergency protection.

---

# How Engineers Design It

Typical steps:

1. hazard analysis
2. define operating limits
3. define alarm limits
4. define trip limits
5. design shutdown actions
6. validate response time.

---

# Typical Number of Protection Layers

In real industrial machines:

| Type                        | Count |
| --------------------------- | ----- |
| alarms                      | 10–30 |
| control interlocks          | 10–20 |
| safety trips                | 5–10  |
| emergency shutdown triggers | 2–5   |

---

# Practical Insight for Controls Engineers

The shutdown hierarchy also separates **two types of protection**:

| Type                 | Purpose        |
| -------------------- | -------------- |
| equipment protection | prevent damage |
| functional safety    | protect people |

Both must work together.

---

If you'd like, the next step is something many engineers struggle with:

**How to calculate SIL / PL requirements for a real machine safety function (including MTTFd, DC, PFHd, and SISTEMA calculations).**

That is the part where safety design becomes mathematically validated rather than just conceptual.

## How to calculate SIL / PL for a real machine safety function

For machinery, the usual path is:

- **Use ISO 13849-1 / SISTEMA** to determine the **required PLr** and the **achieved PL / PFHd** of the safety-related control function.
- Use **IEC 62061** when you want a machinery SIL workflow; it uses **SILCL** and **PFHd**.
- In both approaches, the core output is still the **probability of dangerous failure per hour** of the safety function. ([dguv.de][1])

The clean engineering workflow is:

1. define the **safety function**
2. determine the **required level**: **PLr** or **SILCL**
3. design the architecture
4. calculate reliability inputs: **MTTFd**, **DCavg**, **CCF**, Category
5. calculate **PFHd**
6. verify the achieved **PL / SIL** meets the requirement
7. validate on the real machine. ([dguv.de][1])

---

## 1) Start with one specific safety function

Do not calculate the whole machine at once. Calculate **one safety function at a time**.

A safety function is normally expressed as:

```text
Input(s) → Logic solver → Output(s)
```

Typical example:

```text
Guard door opened → safety PLC detects it → STO removes torque to servo
```

Rockwell’s machine safety documentation uses this same decomposition: **input device, logic device, output device** together make one safety function. ([Rockwell Automation][2])

### Example safety functions

- E-stop stops hazardous motion
- Guard door opening removes torque
- Overpressure opens dump valve and stops pump
- Overspeed triggers STO
- Light curtain intrusion stops conveyor/robot motion

---

## 2) Determine the required level first: PLr or SILCL

### ISO 13849 path

You determine **PLr** from the risk assessment using severity, exposure, and possibility of avoidance. The IFA report on applying ISO 13849 explicitly supports selecting the required **PLr** from the risk graph. ([dguv.de][3])

Typical result:

- lower risk → PL c
- medium/high machinery risk → PL d
- severe/high-exposure risk → PL e

### IEC 62061 path

You determine a **required SIL claim limit / SIL target** and then verify the design PFHd fits that requirement. PFHd is central to both 62061 and 13849 workflows. ([dguv.de][4])

### Practical rule

For most industrial machines, especially the kinds you work around—motion, hydraulics, conveyors, robots—the first pass usually lands around:

- **PL d / Cat. 3** for many serious machine hazards
- **PL e / Cat. 4** for higher-risk access/motion functions

That is a design tendency, not a shortcut. The formal answer still comes from the risk assessment. ([dguv.de][3])

---

## 3) Choose the architecture before you calculate

Under ISO 13849, the simplified method assumes the control system matches one of the designated **Categories**. If it does not, the simplified method is not valid and a more involved method may be needed. ([dguv.de][5])

Typical categories:

- **B / 1**: basic or single-channel with limited fault tolerance
- **2**: tested channel
- **3**: dual-channel with monitoring; single fault should not lead to loss of safety
- **4**: dual-channel with higher fault tolerance and monitoring

For real machines, the common practical targets are:

- **Cat. 3** for PL d
- **Cat. 4** for PL e

Again, this is typical practice, not an automatic rule. ([dguv.de][1])

### Example architecture

For a guard door stop function:

```text
Input: dual-channel coded interlock
Logic: safety PLC
Output: dual-channel STO or monitored contactors
Architecture: Category 3
```

---

## 4) The core terms: MTTFd, DCavg, PFHd, CCF

### MTTFd

**MTTFd** is the **mean time to dangerous failure** of a channel or subsystem. SISTEMA calculates it for you when you provide the right component data, often from **B10d** and frequency of operation for electromechanical devices. ([dguv.de][4])

### DCavg

**DCavg** is the **average diagnostic coverage**: how much of the dangerous failures are detected by monitoring and diagnostics. SISTEMA supports estimation/calculation of **DCavg** as part of the subsystem evaluation. ([dguv.de][4])

### PFHd

**PFHd** is the **probability of dangerous failure per hour**. Under ISO 13849, PFHd is what is finally used to determine the achieved PL of the safety function. ([dguv.de][1])

### CCF

**CCF** is **common cause failure**. ISO 13849 requires a CCF evaluation, and SISTEMA includes CCF analysis. ([dguv.de][6])

---

## 5) Where the numbers come from

For each safety function, split the design into three blocks:

- **Input subsystem**
- **Logic subsystem**
- **Output subsystem**

Then gather:

- component type and part number
- safety data sheet / manufacturer reliability data
- B10d or MTTFd
- diagnostic method and DC claim
- proof of Category / architecture
- proof of CCF measures
- expected operating frequency / cycles per year
- mission time / useful life if applicable. ([Rockwell Automation][2])

### Typical data sources

- Manufacturer safety manuals
- SISTEMA libraries from component vendors
- official reliability data sheets

Rockwell explicitly publishes safety-function examples using B10d data for contactors and estimated operation frequency as part of the SISTEMA calculation flow. ([Rockwell Automation][7])

---

## 6) Practical calculation logic

### Step A — define the safety function

Example:

**SF-01 Guard Door Stop**

> If the guard door opens during automatic mode, hazardous motion shall be removed within the required stopping time by STO.

### Step B — determine PLr

Use the risk graph and document the result.

Example:

- Severity: serious injury
- Exposure: frequent
- Avoidance: difficult

Possible result:

- **PLr = d**

The exact result depends on the formal risk assessment. ([dguv.de][3])

### Step C — choose structure

Example:

- Dual-channel guard switch
- Safety PLC
- Dual-channel STO
- Manual reset
- EDM if contactors used

This would usually be designed toward **Cat. 3** or **Cat. 4** depending on the devices and diagnostic strategy. ([dguv.de][1])

### Step D — calculate subsystem data

#### Input subsystem

Example:

- coded interlock switch
- dual channel
- manufacturer MTTFd / PFHd data or SISTEMA library
- diagnostics from pulsed inputs and discrepancy monitoring

#### Logic subsystem

Example:

- safety PLC
- manufacturer PFHd value from certified data

#### Output subsystem

Example:

- STO on drive, or two monitored contactors
- contactors require B10d/frequency inputs if using electromechanical outputs

SISTEMA then combines subsystem information and produces:

- subsystem MTTFd
- DCavg
- PFHd
- achieved PL. ([dguv.de][4])

---

## 7) Electromechanical outputs: where many calculations go wrong

For contactors, relays, and mechanically actuated switches, the dangerous failure calculation depends heavily on:

- **B10d**
- the **number of operations per year**
- whether they are **effectively monitored**
- whether they are correctly specified and installed. ([Rockwell Automation][7])

That matters a lot for machine builders because the same contactor can look acceptable or unacceptable depending on the switching frequency.

### Example

A contactor used only for safety trips a few times per day has a very different life profile than a contactor switching every machine cycle.

That is why your templates must always include:

- cycles per hour
- hours per day
- days per year
- expected trips/tests per year

---

## 8) DCavg: how to think about it practically

You do not invent DCavg out of thin air. DCavg comes from the diagnostics you actually implement, such as:

- dual-channel monitoring
- discrepancy monitoring
- pulse testing
- EDM feedback
- line fault detection
- drive internal STO diagnostics
- periodic self-tests. ([dguv.de][4])

### Practical interpretation

- poor diagnostics → lower DCavg
- good channel monitoring + fault detection → higher DCavg

The exact accepted value should come from the standard tables, component data, or vendor SISTEMA library, not from guessing.

---

## 9) PFHd bands and achieved PL

Under ISO 13849, the achieved PL is tied to the resulting **PFHd** of the safety function. SISTEMA automates that mapping. ([dguv.de][1])

You do not need to manually re-derive the standard every time. In practice:

- gather correct subsystem data
- build the safety function in SISTEMA
- verify the achieved PFHd / PL result

That is exactly what SISTEMA is for. The IFA describes it as a tool that automates MTTFd, DCavg, PFH and PL tasks. ([dguv.de][4])

---

## 10) When SISTEMA is the right tool

SISTEMA is the standard practical tool for ISO 13849 calculations. The IFA states that SISTEMA is intended for the implementation/evaluation of safety-related control systems to EN ISO 13849-1 and automates the calculation work. Recent version-history notes show the tool has been updated to reflect amendments to ISO 13849-1:2015, including items such as MTTFd capping behavior and DC/CCF updates. ([dguv.de][1])

### Important limit

If your design does **not** fit a designated architecture, the simplified ISO 13849 route may not be valid. IFA’s cookbook explicitly warns about this. ([dguv.de][5])

---

# A real example workflow

## Example safety function

**SF-02: Hydraulic overpressure shutdown**

### Functional requirement

If hydraulic pressure exceeds 210 bar, the system shall:

- stop the pump drive
- open the dump valve
- prevent restart until manual reset

### Target

Assume risk assessment gives:

- **PLr = d**

### Proposed architecture

- Pressure switch A
- Pressure switch B
- Safety PLC
- Pump STO
- Dump valve safety output
- reset circuit

### What you need to collect

- Safety data for the 2 pressure switches
- PFHd or MTTFd for the safety PLC
- PFHd or B10d/MTTFd for the output devices
- diagnostic strategy:
  - dual input comparison
  - output monitoring
  - valve feedback if present

- operation/test frequency
- proof of CCF measures

Then enter those as:

- input subsystem
- logic subsystem
- output subsystem
  in SISTEMA. ([Rockwell Automation][2])

---

# Copy-paste templates

## Template 1 — Safety Function Specification Sheet

```markdown
# Safety Function Specification

## General

- Safety Function ID:
- Machine / System:
- Revision:
- Owner:
- Date:

## Function Name

- Example: Guard Door Open -> Remove Servo Torque

## Hazard Addressed

- Hazard description:
- Hazardous energy involved:
- Possible harm:

## Functional Requirement

- Trigger condition:
- Safe state:
- Required action:
- Maximum response time:
- Reset behavior:
- Restart permitted automatically? (Yes/No)

## Safety Chain

- Input device(s):
- Logic solver:
- Output device(s):
- Feedback / monitoring:
- Related modes (Auto/Manual/Teach/Maintenance):

## Risk Assessment

- Standard used:
- Severity:
- Frequency / exposure:
- Possibility of avoidance:
- Required Performance Level (PLr):
- Required SIL / SILCL:
- Assumptions / notes:

## Architecture

- Category target:
- Channel structure:
- Fault tolerance concept:
- Common cause reduction measures:
- Diagnostic measures:

## Validation Requirements

- Test method:
- Fault insertion tests:
- Proof of stop time:
- Proof of manual reset:
- Required documents:
```

---

## Template 2 — Device Data Collection Sheet

```markdown
# Safety Device Data Collection

## Device Identification

- Safety Function ID:
- Subsystem: Input / Logic / Output
- Device tag:
- Manufacturer:
- Part number:
- Description:

## Reliability Data

- Certified standard / certificate:
- Manufacturer PFHd:
- Manufacturer MTTFd:
- B10d:
- Useful life / mission time:
- Source document:

## Application Data

- Operating mode:
- Expected operations per hour:
- Hours per day:
- Days per year:
- Annual operations:
- Proof-test interval / test frequency:

## Diagnostics

- Diagnostic method:
- Claimed DC / DCavg:
- External monitoring used:
- EDM used:
- Cross-fault detection:
- Pulse testing:
- Discrepancy monitoring:

## Installation / Notes

- Channel:
- Wiring notes:
- Environmental conditions:
- Assumptions:
```

---

## Template 3 — PL Calculation Summary

```markdown
# PL Calculation Summary

## Safety Function

- ID:
- Name:
- PLr:

## Subsystem Breakdown

### Input subsystem

- Devices:
- Category:
- MTTFd:
- DCavg:
- PFHd:
- Notes:

### Logic subsystem

- Devices:
- Category:
- MTTFd or PFHd:
- DCavg:
- PFHd:
- Notes:

### Output subsystem

- Devices:
- Category:
- MTTFd:
- DCavg:
- PFHd:
- Notes:

## Function-Level Evaluation

- CCF score:
- Achieved category:
- Overall PFHd:
- Achieved PL:
- Meets PLr? (Yes/No)

## Review

- Reviewer:
- Date:
- Open issues:
```

---

## Template 4 — SIL / PFHd Verification Sheet

```markdown
# SIL / PFHd Verification

## Safety Function

- ID:
- Name:
- Required SIL / SILCL:
- Required PFHd target:

## Elements in Loop

- Sensor(s):
- Logic solver:
- Final element(s):

## Reliability Inputs

- Sensor PFHd:
- Logic solver PFHd:
- Final element PFHd:
- Common cause considerations:
- Test interval assumptions:
- Diagnostic assumptions:

## Total

- Combined PFHd:
- Achieved SIL / SILCL:
- Meets requirement? (Yes/No)

## Notes

- Source documents:
- Assumptions:
- Validation required:
```

---

## Template 5 — SISTEMA Project Planning Sheet

```markdown
# SISTEMA Build Sheet

## Project

- Machine:
- Revision:
- Analyst:
- Date:

## Safety Function

- Safety function name:
- Required PLr:
- Notes:

## SISTEMA Structure

### Subsystem 1 - Input

- Devices:
- Library file available? (Yes/No)
- MTTFd/B10d source:
- DCavg basis:
- Category:

### Subsystem 2 - Logic

- Devices:
- Library file available? (Yes/No)
- PFHd source:
- Category:

### Subsystem 3 - Output

- Devices:
- Library file available? (Yes/No)
- MTTFd/B10d source:
- DCavg basis:
- Category:

## Global Checks

- CCF evaluation completed? (Yes/No)
- Mission time entered? (Yes/No)
- Operating frequency entered? (Yes/No)
- Validation plan linked? (Yes/No)

## Result

- Achieved PL:
- PFHd:
- Pass / Fail:
```

---

## Template 6 — Validation Test Template

```markdown
# Safety Function Validation Test

## General

- Safety Function ID:
- Machine:
- Test date:
- Tester:

## Preconditions

- Machine state:
- Tools required:
- Instrumentation required:
- Risk controls during test:

## Test Cases

### Test 1 - Normal operation

- Expected result:
- Actual result:
- Pass/Fail:

### Test 2 - Trigger safety input

- Trigger:
- Expected safe state:
- Actual:
- Pass/Fail:

### Test 3 - Single fault simulation

- Fault inserted:
- Expected result:
- Actual:
- Pass/Fail:

### Test 4 - Reset behavior

- Expected result:
- Actual:
- Pass/Fail:

### Test 5 - Restart prevention

- Expected result:
- Actual:
- Pass/Fail:

## Timing

- Measured response time:
- Allowed response time:
- Pass/Fail:

## Final

- Overall result:
- Issues found:
- Corrective actions:
```

---

# How to use SISTEMA in practice

## Recommended workflow

1. Create one project per machine or machine family.
2. Create one safety function at a time.
3. Split each safety function into:
   - input subsystem
   - logic subsystem
   - output subsystem

4. Import vendor libraries where available.
5. Enter manual data only when vendor library data is missing.
6. Run CCF evaluation.
7. Review achieved PFHd and PL.
8. Attach the report to the machine technical file. ([dguv.de][8])

## Good engineering discipline

Do not treat SISTEMA as a magic pass/fail button. The result is only as good as:

- the actual architecture,
- the device data,
- the operating frequency assumptions,
- and the diagnostics you truly implemented. ([dguv.de][5])

---

# Common mistakes

## 1. Calculating before defining the safety function

That produces meaningless numbers.

## 2. Using ordinary PLC I/O as if it were safety-rated

The logic subsystem must have appropriate safety data/certification. ([Rockwell Automation][2])

## 3. Ignoring operation frequency

This is a major error for contactors and switches. B10d-based results depend on usage assumptions. ([Rockwell Automation][7])

## 4. Guessing DCavg

Only claim diagnostics you actually have and can defend. ([dguv.de][4])

## 5. Forgetting CCF

Dual-channel design still needs documented CCF measures. ([dguv.de][6])

## 6. No validation

A passing calculation is not enough. Real-machine validation is still required. Rockwell’s safety-function documentation includes verification and validation planning alongside the PL calculation. ([Rockwell Automation][2])

---

# What I recommend for your kind of work

For the kinds of systems you deal with—motion, hydraulics, pumps, process interlocks—build a reusable library of safety functions like:

- SF-01 E-stop hazardous motion stop
- SF-02 Guard door STO
- SF-03 Hydraulic overpressure trip
- SF-04 Cooling-flow-loss shutdown
- SF-05 High current / jam trip
- SF-06 Chemical leak shutdown

Then keep for each one:

- the functional spec
- the SISTEMA worksheet
- the validation procedure
- the wiring pattern
- the reset / restart philosophy

That gives you a repeatable engineering package instead of recalculating from scratch every time.

If you want, I can turn these templates into a **ready-to-use spreadsheet workbook** with tabs for PLr, device data, PFHd rollup, and validation records.

[1]: https://www.dguv.de/medien/ifa/en/pra/softwa/sistema/kochbuch/sistema_cookbook1_end.pdf?utm_source=chatgpt.com "SISTEMA Cookbook 1, Version 1.0 (EN)"
[2]: https://literature.rockwellautomation.com/idc/groups/literature/documents/rm/safebk-rm002_-en-p.pdf?utm_source=chatgpt.com "M ACHINERY SAFEBOOK 5 - Literature Library"
[3]: https://www.dguv.de/medien/ifa/en/pub/rep/pdf/reports-2019/report0217e/rep0217e.pdf?utm_source=chatgpt.com "Application of EN ISO 13849 – (IFA Report 2/2017e)"
[4]: https://www.dguv.de/medien/ifa/en/pra/softwa/sistema/erlauet_e.pdf?utm_source=chatgpt.com "SISTEMA – the software utility for evaluation of safety- ..."
[5]: https://www.dguv.de/medien/ifa/en/pra/softwa/sistema/kochbuch/sistema_cookbook4_v2_en.pdf?utm_source=chatgpt.com "SISTEMA-Cookbook 4: When the designated architectures ..."
[6]: https://www.dguv.de/medien/ifa/en/pra/softwa/sistema/kochbuch/sistema_cookbook5_en.pdf?utm_source=chatgpt.com "The SISTEMA Cookbook 5"
[7]: https://literature.rockwellautomation.com/idc/groups/literature/documents/at/safety-at069_-en-e.pdf?utm_source=chatgpt.com "Safety Function: Door Monitoring"
[8]: https://www.dguv.de/medien/ifa/en/pra/softwa/sistema/paper_e.pdf?utm_source=chatgpt.com "SISTEMA: a Tool for the Easy Application of the Control ..."

You covered a **large safety engineering domain** in this thread. If you keep it as a flat document, it will become unusable quickly. The right approach is to organize it as a **structured safety engineering knowledge system** that mirrors how real machines are designed and validated.

Below is the structure I recommend. It matches the **actual lifecycle of machine safety engineering** and also works well for your GitHub documentation project.

---

# 1. Top-Level Structure

Organize the repository or documentation into **six primary domains**.

```
machine-safety-architecture/
│
├── 01_safety_fundamentals
├── 02_safety_architecture_patterns
├── 03_process_safety_interlocks
├── 04_safety_hardware_design
├── 05_safety_calculations
├── 06_validation_and_lifecycle
```

This mirrors how engineers actually design machines:

1. understand safety theory
2. choose architecture
3. design interlocks
4. implement hardware
5. calculate safety levels
6. validate and maintain

---

# 2. Domain 1 — Safety Fundamentals

This explains the **conceptual layer**.

```
01_safety_fundamentals
│
├── safety_standards_overview.md
├── sil_vs_pl.md
├── safety_integrity_levels.md
├── risk_assessment_methods.md
├── shutdown_hierarchy.md
```

Topics covered from this thread:

- SIL vs PL
- shutdown hierarchy (Alarm → Interlock → Trip → ESD)
- safety layers
- machine hazard classification

This section answers:

**“Why does this safety system exist?”**

---

# 3. Domain 2 — Safety Architecture Patterns

This contains the **core wiring and logic patterns**.

```
02_safety_architecture_patterns
│
├── universal_machine_safety_architecture.md
├── six_safety_wiring_patterns.md
│
├── pattern_estop.md
├── pattern_guard_interlock.md
├── pattern_ossd_sensor.md
├── pattern_edm_feedback.md
├── pattern_manual_reset.md
├── pattern_sto_drive.md
```

These patterns are **the foundation of nearly every machine**.

Example patterns:

```
E-stop dual channel
Guard door interlock
Light curtain OSSD
External device monitoring
Manual reset
Safe torque off
```

This section answers:

**“How are safety systems architected?”**

---

# 4. Domain 3 — Process Safety Interlocks

This section focuses on **process monitoring shutdown logic**.

```
03_process_safety_interlocks
│
├── interlock_design_principles.md
├── process_interlock_template.md
│
├── pressure_interlocks.md
├── temperature_interlocks.md
├── current_interlocks.md
├── flow_interlocks.md
├── level_interlocks.md
├── vibration_interlocks.md
├── environmental_interlocks.md
```

This covers sensors like:

- pressure switches
- temperature switches
- current monitors
- flow sensors
- level sensors

Example template:

```
Process variable
      ↓
Sensor
      ↓
Safety logic
      ↓
Shutdown actuator
```

This section answers:

**“How do process conditions trigger safe shutdown?”**

---

# 5. Domain 4 — Safety Hardware Design

This is the **practical electrical design layer**.

```
04_safety_hardware_design
│
├── safety_wiring_rules.md
├── dual_channel_design.md
├── safety_input_design.md
├── safety_output_design.md
├── termination_practices.md
├── cable_selection.md
├── device_selection.md
```

Topics include:

- dual-channel wiring
- wire sizing
- conductor color coding
- terminal reliability
- vibration resistance
- discrepancy timing
- device selection

Example subsection:

```
dual_channel_wiring.md
```

Contents:

```
CH1 wire
CH2 wire
separate routing
diagnostics
pulse testing
```

This section answers:

**“How do we physically implement the safety system?”**

---

# 6. Domain 5 — Safety Calculations

This is where **engineering math and reliability calculations** live.

```
05_safety_calculations
│
├── pl_calculation_method.md
├── sil_calculation_method.md
├── mttfd_calculation.md
├── dcavg_explanation.md
├── pfhd_calculation.md
├── sistema_workflow.md
```

Templates included:

```
safety_function_spec_template.md
device_data_template.md
pl_calculation_template.md
sistema_project_template.md
validation_template.md
```

These are used during:

- design review
- certification
- compliance documentation

This section answers:

**“How do we prove the system is safe?”**

---

# 7. Domain 6 — Validation and Lifecycle

Safety does not end at design.

```
06_validation_and_lifecycle
│
├── safety_validation_procedure.md
├── commissioning_tests.md
├── fault_injection_tests.md
├── safety_maintenance.md
├── change_management.md
```

Topics include:

- validation testing
- fault simulation
- commissioning checks
- lifecycle maintenance

This section answers:

**“How do we ensure safety continues during operation?”**

---

# 8. Cross-Industry Section

Add an industry comparison section.

```
07_industry_profiles
│
├── semiconductor_safety.md
├── offshore_safety.md
├── nuclear_safety.md
├── marine_safety.md
├── medical_device_safety.md
├── food_industry_safety.md
├── agriculture_safety.md
```

These explain how the same patterns adapt to:

- offshore oil
- nuclear plants
- semiconductor tools
- robotics
- food processing

---

# 9. Example Machine Safety Case Study

Include full examples.

```
08_case_studies
│
├── hydraulic_machine_safety.md
├── robot_cell_safety.md
├── chemical_dosing_system_safety.md
```

Each case study includes:

```
hazard analysis
safety functions
architecture
wiring
SIL/PL calculation
validation tests
```

---

# 10. Diagram Library

Create reusable diagrams.

```
09_diagrams
│
├── safety_architecture.mmd
├── estop_circuit.mmd
├── interlock_flow.mmd
├── shutdown_hierarchy.mmd
```

Use **Mermaid diagrams** so your site can render them.

---

# 11. Knowledge Graph Structure

Your documentation naturally forms a **knowledge graph**:

```
Hazard
  ↓
Safety Function
  ↓
Architecture Pattern
  ↓
Hardware Implementation
  ↓
Reliability Calculation
  ↓
Validation
```

Each concept should link to the others.

---

# 12. How This Helps Your Control-System Tools Project

This structure is ideal for your **Control System Tools website**.

It lets you build navigation like:

```
Safety Standards
Safety Architecture
Safety Hardware
Safety Calculations
Safety Validation
Industry Applications
```

Users can move from:

```
hazard → safety function → wiring → calculation → validation
```

Which mirrors real engineering workflow.

---

# 13. Recommended Implementation Format

Use **Markdown + diagrams + templates**.

Example page structure:

```
---
title: Guard Door Safety Function
category: safety_functions
standard: ISO 13849
target_PL: d
---

# Description
# Architecture
# Wiring Pattern
# Calculation Example
# Validation Tests
```

This makes it searchable and reusable.

---

# 14. Most Important Organizational Principle

Everything should be structured around **Safety Functions**.

Each safety function contains:

```
hazard
trigger condition
input device
logic solver
output device
PL/SIL calculation
validation tests
```

This matches how real safety certification works.

---

💡 **My honest advice:**
What you just developed in this conversation is essentially the **skeleton of a complete machine safety engineering handbook**. If organized correctly, it can become:

- a **professional reference system**
- a **training guide for engineers**
- a **design framework for real machines**

—and it fits perfectly into the **Control-System-Tools project** you're building.

---

If you want, I can also show you something extremely useful for your project:

**The “Control System Safety Design Workflow” used by companies like ASML, Tesla, and AMAT — a step-by-step design process from hazard identification all the way to certification.**

That workflow ties together **everything we discussed in this thread.**

Below is the **same 14-topic structure**, but now with the **applicable standards mapped to each section**.
This makes the knowledge base **engineering-grade** because every concept is traceable to a safety standard.

I grouped standards into four classes:

- **Functional Safety**
- **Machine Electrical Safety**
- **Process Safety**
- **Industry-specific standards**

The most central standards referenced are:

- ISO 13849-1
- IEC 62061
- IEC 61508
- NFPA 79
- IEC 60204-1

These five form the **core compliance backbone** for most machines.

---

# 1. Safety Fundamentals

Folder:

```text
01_safety_fundamentals
```

### Applicable standards

Primary standards:

- ISO 12100
- IEC 61508
- ISO 13849-1
- IEC 62061

Supporting standards:

- IEC 61511
- ISO 14121

Topics covered

- risk assessment
- hazard classification
- SIL vs PL
- functional safety lifecycle.

---

# 2. Safety Architecture Patterns

Folder:

```text
02_safety_architecture_patterns
```

### Applicable standards

Primary:

- ISO 13849-1
- IEC 62061

Supporting:

- ISO 13849-2
- IEC 62046

Patterns governed by these standards:

- dual-channel circuits
- safety logic architectures
- Category B / 1 / 2 / 3 / 4 structures
- redundant shutdown paths.

---

# 3. Process Safety Interlocks

Folder:

```text
03_process_safety_interlocks
```

### Applicable standards

Primary:

- IEC 61511
- IEC 61508

Supporting:

- API 14C
- API 521
- ISO 4126

Typical applications:

- pressure trip
- temperature shutdown
- flow interlocks
- level protection.

---

# 4. Safety Hardware Design

Folder:

```text
04_safety_hardware_design
```

### Applicable standards

Primary:

- NFPA 79
- IEC 60204-1

Supporting:

- UL 508A
- IEC 60947-5-1
- IEC 60947-5-5

These govern:

- wire sizes
- color codes
- emergency stop design
- contactor requirements
- safety switch construction.

---

# 5. Safety Calculations

Folder:

```text
05_safety_calculations
```

### Applicable standards

Primary:

- ISO 13849-1
- IEC 62061

Supporting:

- IEC 61508

Calculation concepts:

- MTTFd
- DCavg
- PFHd
- Category
- CCF

Tools referenced:

- SISTEMA.

---

# 6. Validation and Lifecycle

Folder:

```text
06_validation_and_lifecycle
```

### Applicable standards

Primary:

- ISO 13849-2
- IEC 62061

Supporting:

- IEC 61508

Lifecycle phases:

- verification
- validation
- proof testing
- maintenance.

---

# 7. Industry Profiles

Folder:

```text
07_industry_profiles
```

### Semiconductor / robotics

Standards:

- SEMI S2
- ISO 10218
- ANSI R15.06

---

### Offshore oil & gas

Standards:

- API 14C
- IEC 61511
- IEC 60079

---

### Nuclear

Standards:

- IEC 61513
- IEEE 603

---

### Marine

Standards:

- IEC 60092
- IMO SOLAS

---

### Medical devices

Standards:

- IEC 60601
- ISO 14971

---

### Food industry

Standards:

- ISO 14159
- 3-A Sanitary Standards

---

# 8. Case Studies

Folder:

```text
08_case_studies
```

Applicable standards depend on machine type but usually include:

- ISO 12100
- ISO 13849-1
- IEC 62061
- NFPA 79

Case studies demonstrate:

- hazard analysis
- safety function definition
- architecture
- validation.

---

# 9. Diagram Library

This section references standards indirectly but supports documentation.

Common standards referenced in diagrams:

- ISO 14617
- IEC 60617

---

# 10. Knowledge Graph Model

Standards that define the relationships:

- IEC 61508
- ISO 12100

Concept chain:

```text
Hazard
↓
Safety Function
↓
Architecture
↓
Hardware
↓
Reliability Calculation
↓
Validation
```

---

# 11. Control System Tools Integration

Your project should reference:

- ISO 13849-1
- IEC 62061
- NFPA 79
- IEC 60204-1

These form the **minimum compliance stack** for machine safety.

---

# 12. Documentation Format

Relevant documentation standards:

- IEC 82079
- ISO 20607

These govern:

- technical files
- safety documentation.

---

# 13. Safety Function Structure

Standards defining safety functions:

- ISO 13849-1
- IEC 62061

Safety function structure:

```text
hazard
trigger
sensor
logic
actuator
verification
```

---

# 14. Engineering Lifecycle

Standards governing the lifecycle:

- IEC 61508
- IEC 61511
- ISO 13849-2

Lifecycle phases:

```text
concept
risk assessment
design
implementation
verification
validation
operation
maintenance
decommissioning
```

---

# Recommended Minimum Standards Stack

For most industrial machines:

```text
ISO 12100   Risk assessment
ISO 13849   Machine safety control
IEC 62061   Functional safety for machinery
NFPA 79     Electrical machine design
IEC 60204   Machine electrical equipment
UL 508A     Control panel construction
```

This stack covers **~90% of machine safety compliance needs**.

---

If you want, I can also build something extremely useful for your **Control-System-Tools site**:

**A complete “Industrial Safety Standards Map” (around 40–60 standards) organized by machine layer — mechanical, electrical, functional safety, robotics, process, hazardous areas, and industry-specific.**

That diagram is what **system architects at companies like ASML, Tesla, and AMAT actually use to plan compliance for a new machine platform.**

Below is a **comprehensive Industrial Safety Standards Map** organized by **machine layers**.
This is the way large engineering organizations structure compliance when designing new equipment platforms.

The map integrates **40+ standards** grouped into functional domains.
The layers move from **physical hazards → control systems → software → lifecycle → industry-specific requirements**.

---

# Industrial Safety Standards Map

```text
Layer 1  Hazard & Risk Assessment
Layer 2  Mechanical Safety
Layer 3  Electrical Safety
Layer 4  Functional Safety Control Systems
Layer 5  Sensors & Protective Devices
Layer 6  Robotics & Motion Safety
Layer 7  Process Safety
Layer 8  Hazardous Environment Safety
Layer 9  Industry-Specific Standards
Layer 10 Lifecycle, Documentation & Validation
```

---

# Layer 1 — Hazard and Risk Assessment

These standards define **how hazards are identified and evaluated**.

Primary standards:

- ISO 12100
- ISO 14121

Supporting standards:

- IEC 61508
- ISO 31000

Purpose:

```text
identify hazards
evaluate risk
define safety functions
```

These standards guide **the entire safety design process**.

---

# Layer 2 — Mechanical Safety

These standards govern **physical hazards**.

Primary:

- ISO 13857
- ISO 14120
- ISO 14119

Supporting:

- ISO 14118
- ISO 13850

Typical applications:

- machine guarding
- fence design
- interlocked doors
- emergency stop placement.

---

# Layer 3 — Electrical Safety

These standards govern **machine electrical systems**.

Primary:

- NFPA 79
- IEC 60204-1

Supporting:

- UL 508A
- IEC 60947-5-1
- IEC 60947-5-5

They regulate:

```text
wiring
control circuits
disconnect devices
control panels
```

---

# Layer 4 — Functional Safety Control Systems

These standards govern **safety-related control systems**.

Primary:

- ISO 13849-1
- IEC 62061

Supporting:

- IEC 61508

These define:

```text
SIL
PL
PFHd
MTTFd
DCavg
```

Used with tools such as **SISTEMA**.

---

# Layer 5 — Sensors and Protective Devices

These standards define **protective equipment**.

Primary:

- IEC 61496
- IEC 62046

Supporting:

- IEC 60947-5-3
- ISO 13855

Typical devices:

```text
light curtains
laser scanners
safety mats
interlock switches
```

---

# Layer 6 — Robotics and Motion Safety

These standards apply to **robotic and automated motion systems**.

Primary:

- ISO 10218
- ANSI R15.06

Collaborative robots:

- ISO TS 15066

Applications:

```text
robot cells
collaborative robots
automated assembly
material handling
```

---

# Layer 7 — Process Safety

These standards govern **process shutdown systems**.

Primary:

- IEC 61511
- IEC 61508

Supporting:

- API 14C
- API 521

Typical safety functions:

```text
pressure trip
temperature shutdown
flow interlock
level protection
```

---

# Layer 8 — Hazardous Environment Safety

These standards govern **explosive environments**.

Primary:

- IEC 60079
- ATEX Directive

Supporting:

- NFPA 70
- NFPA 497

Applications:

```text
oil refineries
gas plants
chemical plants
offshore platforms
```

---

# Layer 9 — Industry-Specific Standards

These standards apply to specific industries.

### Semiconductor manufacturing

- SEMI S2
- SEMI S8

### Nuclear

- IEC 61513
- IEEE 603

### Marine

- IEC 60092
- IMO SOLAS

### Medical devices

- IEC 60601
- ISO 14971

### Food industry

- ISO 14159
- 3-A Sanitary Standards

---

# Layer 10 — Lifecycle, Documentation, and Validation

These standards govern **safety lifecycle management**.

Primary:

- IEC 61508
- ISO 13849-2

Supporting:

- IEC 82079
- ISO 20607

Lifecycle phases:

```text
concept
design
verification
validation
operation
maintenance
decommissioning
```

---

# Minimum Compliance Stack for Most Industrial Machines

For typical industrial automation systems:

```text
ISO 12100   Risk assessment
ISO 13849   Safety control system
IEC 62061   Functional safety
NFPA 79     Electrical machinery
IEC 60204   Machine electrical equipment
UL 508A     Control panels
```

This stack typically covers **most machine compliance requirements**.

---

# How These Standards Fit Together

```text
Hazard analysis
     ↓
ISO 12100
     ↓
Safety architecture
     ↓
ISO 13849 / IEC 62061
     ↓
Electrical design
     ↓
NFPA 79 / IEC 60204
     ↓
Protective devices
     ↓
IEC 61496 / ISO 14119
     ↓
Industry-specific standards
     ↓
Validation and lifecycle
```

This layered approach ensures **complete safety coverage**.

---

# How This Should Appear in Your Control-System-Tools Project

Your site navigation could look like:

```text
Safety Standards
Safety Architecture
Safety Hardware
Safety Calculations
Safety Validation
Industry Profiles
Case Studies
```

Each page references the applicable standards.

---

💡 **Important insight:**
Large automation companies often track **50–100 safety standards** for a single machine platform.
However, most projects rely heavily on **about 10 core standards**.

---

If you'd like, I can also show something extremely valuable for your project:

**A “Machine Safety Compliance Matrix” used in real design reviews — mapping each machine subsystem (robot, hydraulics, electrical panel, software, operator interface) to the exact standards that apply.**

That matrix becomes the **master compliance document** during machine certification.

## Machine Safety Compliance Matrix

This is the document that ties the whole project together. It maps each **machine subsystem** to the **standards that apply**, the **design outputs required**, and the **evidence needed for review**. It is useful because the core standards play different roles: **ISO 12100** covers risk assessment, **ISO 13849-1:2023** and **IEC 62061:2021/AMD1:2024** cover safety-related control systems, and **NFPA 79 (2024)** covers electrical equipment of industrial machinery. ([ISO][1])

### How to structure it

Use one row per subsystem or safety-relevant domain. Suggested columns:

- **Subsystem**
- **Hazards**
- **Applicable standards**
- **Key safety functions**
- **Required deliverables**
- **Verification / validation evidence**
- **Owner**
- **Status**
- **Notes / deviations**

---

## Recommended master matrix

| Subsystem                     | Main hazards                                     | Core standards                                                                                         | Typical safety functions                                       | Required deliverables                                              | Evidence                                                 |
| ----------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------- |
| Whole machine / concept       | all machine hazards                              | ISO 12100                                                                                              | hazard identification, risk reduction strategy                 | risk assessment, hazard log, safety requirements spec              | completed risk assessment, residual risk review          |
| Safety-related control system | failure of safety logic                          | ISO 13849-1:2023, IEC 62061:2021/AMD1:2024, IEC 61508 framework                                        | E-stop, guard stop, STO, interlocks                            | safety function list, architecture, PL/SIL calculations            | SISTEMA file, PFHd summary, validation tests             |
| Electrical panel              | shock, fire, incorrect wiring                    | NFPA 79, IEC 60204-1, UL 508A                                                                          | safe control power, disconnects, panel segregation             | schematics, panel layout, BOM, wire schedule                       | panel review, build inspection, labeling check           |
| Guards / doors / access       | entrapment, access to motion                     | ISO 14120, ISO 14119, ISO 13850, ISO 14118                                                             | interlocked access, prevention of unexpected start             | guard drawings, interlock selection sheet, reset philosophy        | guard inspection, defeat-resistance review, restart test |
| Protective devices            | intrusion into hazard zone                       | IEC 61496, IEC 62046, ISO 13855                                                                        | light curtain stop, scanner zone stop                          | protective device layout, minimum distance calc, zone map          | stop-time test, placement verification                   |
| Motion / servo / VFD          | hazardous motion                                 | ISO 13849-1, IEC 62061, robot standards if applicable                                                  | STO, SS1 if used, speed/position related interlocks            | motion safety architecture, drive safety manuals, stop-time budget | drive safety config review, measured stopping time       |
| Robots / robot cell           | collision, trapping                              | ISO 10218, ANSI/RIA R15.06, ISO/TS 15066 for cobots                                                    | robot stop, zone monitoring, enabling device                   | cell layout, safeguarded space definition, mode logic              | robot risk assessment, teach-mode validation             |
| Hydraulics / pneumatics       | stored energy, overpressure, unexpected movement | ISO 12100, ISO 13849, process/interlock standards as needed                                            | pressure trip, dump valve, safe depressurization               | P&ID, interlock list, valve action table                           | pressure trip test, energy isolation verification        |
| Process sensors / shutdowns   | pressure, temp, flow, level excursions           | IEC 61511 concepts for process interlocks, IEC 61508, IEC 62061/ISO 13849 for machinery implementation | alarm, interlock, trip, ESD-style shutdown                     | cause-and-effect matrix, setpoint list, trip narrative             | loop test, fault simulation, response-time test          |
| Hazardous area equipment      | ignition risk                                    | IEC 60079, ATEX where applicable, NEC/NFPA hazardous-location rules as applicable                      | safe shutdown in classified area                               | area classification, Ex device schedule, cable method review       | hazardous-area compliance review                         |
| HMI / operator interface      | unsafe reset, misleading status                  | NFPA 79, IEC 60204-1, ISO 13849 software aspects                                                       | manual reset, mode selection, alarm display                    | HMI safety state design, alarm philosophy, mode matrix             | reset validation, mode transition test                   |
| Software / safety application | systematic faults                                | ISO 13849-1 software requirements, IEC 62061, IEC 61508 principles                                     | validated safety logic, protected parameters                   | software design spec, versioning, change control                   | code review, test record, backup/archive proof           |
| Documentation / instructions  | misuse, maintenance errors                       | ISO 20607, IEC 82079                                                                                   | safe use, maintenance precautions, residual risk communication | manuals, labels, LOTO instructions                                 | document review, field-use review                        |
| Validation / lifecycle        | drift after commissioning                        | ISO 13849-2, IEC 62061 lifecycle expectations                                                          | periodic validation, modification control                      | validation plan, maintenance plan, change log                      | acceptance test, periodic proof/inspection records       |

The general principle behind this matrix is that **risk assessment drives the safety functions**, then the safety functions drive **architecture, electrical design, calculations, and validation**. That relationship is explicit in ISO 12100, ISO 13849, and IEC 62061. ([ISO][1])

---

## How to use it in design reviews

### 1. Concept review

Start with these rows:

- Whole machine / concept
- Guards / doors / access
- Motion / servo / VFD
- Hydraulics / pneumatics
- Process sensors / shutdowns

Goal: confirm you have identified the real hazards and defined the safety functions. ISO 12100 is the anchor here. ([ISO][1])

### 2. Detailed design review

Then expand:

- Safety-related control system
- Electrical panel
- Protective devices
- HMI / operator interface
- Software / safety application

Goal: confirm the implementation path can actually achieve the required PL or SIL and is electrically buildable under the machine electrical standard. ([ISO][2])

### 3. Validation review

Finish with:

- Validation / lifecycle
- Documentation / instructions

Goal: make sure the machine can be tested, handed over, modified safely, and maintained without breaking the safety case. ISO 13849-2 is the key reference for validating safety-related parts of control systems. ([ISO][2])

---

## Good row format for each subsystem

For each subsystem, attach a one-page detail sheet:

```text
Subsystem:
Applicable standards:
Hazards:
Safety functions:
Interfaces to other subsystems:
Key design decisions:
Open issues:
Required evidence:
Owner:
```

That keeps the matrix readable while the detail lives in linked sheets.

---

## Example filled rows

### Example 1 — Servo axis with guard door

| Field                | Entry                                                                     |
| -------------------- | ------------------------------------------------------------------------- |
| Subsystem            | Servo Axis A + access door                                                |
| Hazards              | crush, entanglement, unexpected restart                                   |
| Applicable standards | ISO 12100, ISO 13849-1:2023, IEC 62061:2021/AMD1:2024, NFPA 79            |
| Safety functions     | guard door open → STO; E-stop → STO; manual reset required                |
| Deliverables         | safety function spec, wiring diagram, stop-time measurement, SISTEMA calc |
| Evidence             | drive safety manual, STO proof test, reset validation, PFHd report        |

### Example 2 — Hydraulic power unit

| Field                | Entry                                                                                        |
| -------------------- | -------------------------------------------------------------------------------------------- |
| Subsystem            | HPU + cylinder circuit                                                                       |
| Hazards              | overpressure, stored energy, hose failure, unexpected motion                                 |
| Applicable standards | ISO 12100, ISO 13849-1:2023, IEC 62061, NFPA 79; process-style interlock practices as needed |
| Safety functions     | high pressure trip; E-stop stops pump; dump valve to safe state                              |
| Deliverables         | interlock list, cause/effect table, valve schedule, schematic                                |
| Evidence             | pressure trip test, dump valve fail-safe test, restart prevention test                       |

### Example 3 — Light curtain on loading station

| Field                | Entry                                                                          |
| -------------------- | ------------------------------------------------------------------------------ |
| Subsystem            | Infeed load zone                                                               |
| Hazards              | reach-in to moving conveyor/actuator                                           |
| Applicable standards | IEC 61496, IEC 62046, ISO 13855, ISO 13849-1                                   |
| Safety functions     | intrusion → stop hazardous motion                                              |
| Deliverables         | placement calc, protective distance calc, wiring pattern, validation procedure |
| Evidence             | measured stop time, installation distance check, fault test                    |

---

## Industry-specific add-on columns

For your project, add a **Profile** column so the same matrix can branch by industry.

| Profile                       | Add these standards / concerns                                    |
| ----------------------------- | ----------------------------------------------------------------- |
| Semiconductor                 | SEMI S2, robot and gas/tool-specific hazards                      |
| Marine                        | IEC 60092, corrosion, vibration, shipboard power constraints      |
| Offshore / petroleum          | IEC 61511 concepts, API 14C, IEC 60079 hazardous areas            |
| Nuclear                       | IEC 61513, IEEE 603, independent/diverse architectures            |
| Medical / hospital / research | IEC 60601, ISO 14971, traceability and patient/operator risk      |
| Food / beverage               | ISO 14159, hygienic design, washdown compatibility                |
| Agriculture                   | harsher environment, simpler but rugged guarding/interlock design |

Industry-specific standards sit on top of the core machine standards rather than replacing them in most cases. ([ISO][1])

---

## What belongs in the evidence pack

For each row, require links to:

- risk assessment reference
- safety function specification
- schematic / P&ID / layout
- component safety manuals or certificates
- calculation file, including SISTEMA where used
- validation test record
- open issue / deviation record

That gives you a real certification-style trail instead of just a checklist.

---

## Best repository structure for this matrix

For your Control-System-Tools project, I would store it like this:

```text
/compliance
  /master-compliance-matrix
    master_matrix.xlsx
    master_matrix.md
  /subsystem-sheets
    electrical_panel.md
    servo_motion.md
    hydraulics.md
    guarding.md
    process_interlocks.md
  /evidence
    /risk-assessments
    /safety-functions
    /calculations
    /validation
```

---

## Blunt recommendation

Do **not** organize compliance by standard number alone.
That is how teams create a reference library nobody can use.

Organize it by:

1. **subsystem**
2. **hazard**
3. **safety function**
4. **evidence**

Then tag each item with the standards that apply.

That is how a design review actually works.

If you want, I can turn this into a **ready-to-fill spreadsheet structure with tabs and column definitions**.

[1]: https://www.iso.org/standard/51528.html?utm_source=chatgpt.com "ISO 12100:2010 - Risk assessment and risk reduction"
[2]: https://www.iso.org/standard/73481.html?utm_source=chatgpt.com "ISO 13849-1:2023 - Safety of machinery"
