<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: troubleshooting — motor won't start (across-the-line / starter-driven)
SOURCE_BASIS: diagnostic reasoning + generally accepted field practice (flagged)
INDEX_TAGS:
  topics: [troubleshooting, motor, starter, contactor, overload, single-phasing]
  systems: [motion_drives, motors, motor_control]
-->

# Motor Won't Start — Diagnostic Reasoning (Starter-Driven)

Scope: a motor fed by an across-the-line or reduced-voltage starter — direct
contactor, star-delta, soft starter in bypass. Drive-fed motors have their
own failure modes; route those to the VFD-faults reasoning. This note reasons
from one branching question that splits the whole problem cleanly.

**The pivot: does the contactor pull in?** The contactor is the boundary
between the control circuit and the power circuit. If it does not energize,
the fault is upstream in the control side. If it pulls in but the motor does
nothing, the fault is downstream in the power side. Establish which, and
you have halved the search before measuring anything else.

## Contactor does NOT pull in — control circuit

The coil is not energizing. Trace the control circuit from control-power
source to coil.

- **E-stop or interlock open** — any series-connected stop, guard interlock,
  or safety relay contact breaks the string. What it looks like: nothing
  responds to start. Check: verify each interlock/e-stop is satisfied and its
  contact is actually closed, not just reset at the operator station.
- **Overload tripped (aux contact open)** — the overload relay's auxiliary
  contact sits in the control string; a tripped overload opens it. What it
  looks like: ran fine, tripped, won't restart until reset (and won't reset
  until cooled on a thermal element). Check: overload trip indicator and the
  state of its aux contact.
- **No start command** — the start pushbutton, PLC output, or run signal
  never reaches the coil circuit. Check: measure for the command at the
  control input, not at the HMI — an HMI "start" that never made it to a
  physical/logical output is a common trap.
- **Control power absent** — the control transformer (CPT), fuse, or control
  supply is dead. What it looks like: nothing in the control circuit works.
  Check: control voltage present downstream of the CPT and its fuses. Route
  to the control-power wiring guide.
- **Seal-in / holding circuit broken** — a start that "won't hold": the
  contactor chatters or drops out the instant the button is released because
  the seal-in (holding) auxiliary contact or its wiring is open. Route to
  the motor-starter wiring guide for the seal-in topology.

## Contactor pulls in but motor does NOT turn — power circuit

The coil energized and the main contacts closed, but no torque. The control
side is proven; the problem is in the power path or the machine.

- **Blown fuse / lost phase on one line** — one of L1/L2/L3 is missing
  downstream of the contactor. What it looks like: motor hums, may draw heavy
  current, will not accelerate, trips overload. Check: voltage on all three
  phases at the load side of the contacts.
- **Overload heater / element open** — an open thermal element or a burned
  heater breaks a power leg. Check: continuity/voltage across each overload
  pole with the contactor closed.
- **Motor connection wrong or open** — a wiring error in the motor terminal
  box (wrong star/delta arrangement) or an open winding lead. Check: motor
  terminal connections against the nameplate diagram; winding resistance
  balance across phases.
- **Mechanical seizure or brake still set** — the motor is fine but the load
  or a failed-closed brake holds the shaft. What it looks like: full current,
  overload trip, sometimes a hum. Check: try to rotate the shaft by hand
  under zero-power conditions; confirm any holding brake actually releases.

## Motor hums / single-phases

A specific, dangerous signature of the power branch: the motor buzzes, may
start if spun by hand, will not develop starting torque, and heats fast.

- **What it looks like** — loud hum, no rotation from rest, rapid heating,
  overload trip within seconds.
- **Cause** — a lost phase: one open fuse, one failed contact pole, one
  broken conductor or terminal. A three-phase motor cannot start on two
  phases.
- **Check** — measure all three phases at the motor terminals while the
  contactor is closed; the missing leg is the fault. De-energize before
  touching terminals.

## Trips overload on start (but does start to move)

The motor begins to turn, then the overload trips during acceleration or
shortly after.

- **What it looks like** — accelerates slowly or partially, then trips; may
  restart and trip repeatedly.
- **Causes** — load too high or jammed; overload set below the motor's actual
  FLA; excessive start frequency without cooling; or, on a reduced-voltage
  starter, a **star-delta transition** problem — a bad transition timer,
  open transition contact, or too-early switchover drops the motor off during
  acceleration.
- **Check** — confirm the overload setting against nameplate FLA; test the
  load free/unjammed; on star-delta, verify the transition sequence and
  timing. Route the transition wiring to the motor-starter guide.

## What to measure

- **Voltage present at each stage** — supply L1/L2/L3 at the disconnect, at
  the line side of the contactor, at the load side of the contactor, and at
  the motor terminals. Walking the voltage down these stages localizes an
  open to one segment.
- **Control voltage at the coil** — is the coil actually seeing pull-in
  voltage? This confirms whether the control string closed. No coil voltage
  sends you into the control-circuit branch; coil voltage present with no
  pull-in means a failed coil/contactor.
- **Overload state** — tripped or reset, and the aux-contact state; a tripped
  overload explains both a no-pull-in (aux open in control string) and a
  power-leg open (element open).

Every branch ends the same way: prove the control side or the power side
first with a voltage measurement, then localize. Generally accepted
practice — verify for your installation.
