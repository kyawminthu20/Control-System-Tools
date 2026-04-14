<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: LEGACY_CAPTURED_NOTE
CATEGORY: SEMI_FACILITY_DRAFT_NOTE
-->

You won’t get good gas cabinet drawings by “Googling PDFs.” Most of the useful material comes from **three sources**: vendors, standards, and engineering repositories. If you want something usable for PLC/SCADA or design work, you need to pull from all three.

---

# 1. OEM / Vendor drawings (most practical)

These are the **closest to real-world designs** (P&ID, GA, wiring, interlocks).

## Major gas cabinet vendors

- Applied Energy Systems
- Entegris
- Ultra Clean Technology
- Air Liquide Advanced Materials
- Linde

### What you can get

- General Arrangement (GA) drawings
- P&ID (gas panel + cabinet)
- Pneumatic diagrams
- Electrical schematics (sometimes)
- Installation manuals

### How to actually get them

- Request **“typical gas cabinet P&ID / GA / control schematic”** from sales or applications engineering
- Ask specifically for:
  - _toxic gas cabinet with purge panel_
  - _VMB (Valve Manifold Box) integration_
  - _fully automatic cabinet sequence_

👉 Reality: Full drawings are usually **NDA-controlled**, but “typical” or “reference” drawings are often shared.

---

# 2. Standards (architecture backbone — not drawings)

These won’t give you exact wiring diagrams, but they define the **correct architecture**.

## Critical semiconductor standards

- SEMI
  - **SEMI F14** → gas enclosure design
  - **SEMI S2** → EHS baseline
  - **SEMI S6** → exhaust requirements
  - **SEMI S18** → toxic gas monitoring

- NFPA
  - **NFPA 318** → semiconductor facilities
  - **NFPA 55** → compressed gases

### What you extract

- Required interlocks
- Exhaust philosophy
- Gas classification rules
- Safety shutdown logic

👉 Use this to **validate your design**, not to copy drawings.

---

# 3. Engineering drawings (best learning source)

These are harder to find but extremely valuable.

## Where to look

- University cleanroom design docs (search: _“semiconductor gas cabinet P&ID pdf”_)
- Government labs (DOE, national labs)
- EPC companies (Jacobs, Fluor, Exyte) — sometimes publish snippets

## Example search strategy

Use targeted queries like:

- “toxic gas cabinet P&ID semiconductor pdf”
- “VMB gas panel schematic semiconductor”
- “gas cabinet purge sequence diagram”

---

# 4. What a real gas cabinet architecture looks like

Here is the **actual structure you should expect** (this matters more than drawings):

## Mechanical / process layer

- Cylinder → CGA connection
- Manual shutoff valve
- Pressure regulator (single or dual stage)
- Pneumatic diaphragm valves (fail-close)
- Purge line (N₂)
- Vent line to exhaust
- Check valves / restrictors

## Control layer

- Cabinet controller (PLC or embedded)
- Solenoid manifold (air-operated valves)
- Pressure transmitters / switches
- Flow restrictors / MFC (optional)

## Safety layer (critical)

- Gas detector input (toxic/flammable)
- Exhaust flow proof (DP switch or airflow switch)
- Door interlock
- E-stop / facility EPO
- Fire alarm interface

## Integration layer

- PLC / SCADA
- Tool interlock (permit signal)
- Facility ESD network

---

# 5. If you want to build your own (recommended for you)

Given your background, don’t wait for perfect drawings. Build a **reference architecture yourself**.

Start with:

### Step 1 — P&ID (core)

- Cylinder → Regulator → Valve → Process
- Add purge + vent loop

### Step 2 — Interlock matrix

- Exhaust fail → close all valves
- Gas detect → isolate + alarm
- Door open → disable supply

### Step 3 — PLC I/O list

- Inputs: pressure, gas detect, exhaust, door
- Outputs: valves, alarms, permits

### Step 4 — State machine

- Idle → Purge → Ready → Supply → Alarm

---

# Direct advice (no fluff)

You’re aiming for **semiconductor facility control engineering**. Don’t rely on vendor drawings alone.

Do this instead:

- Get 1–2 vendor reference drawings
- Overlay SEMI + NFPA rules
- Build your own **standard gas cabinet template**

That becomes:

- reusable
- portfolio-grade
- aligned with your long-term goal (automation + industrial SaaS)

---

If you want, I can:

- Build a **full gas cabinet P&ID (engineering-grade)**
- Create **PLC I/O list + tag naming (Allen-Bradley style)**
- Define **alarm & interlock philosophy (SEMI-compliant)**

That would be more valuable than collecting random PDFs.
