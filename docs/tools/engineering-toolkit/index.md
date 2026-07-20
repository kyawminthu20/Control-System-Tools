---
layout: default
title: "Python Engineering Toolkit (cst)"
description: "The open-source cst toolkit behind this site: standards-cited calculators, panel design pipeline, commissioning generators, PLC utilities, and diagnostics."
breadcrumb:
  - name: "Tools"
    url: "/tools/"
  - name: "Python Toolkit"
related_standards:
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
  - name: "UL 508A"
    url: "/standards/us-electrical/ul-508a/"
---

<div class="page-header">
  <span class="page-header__label">Engineering Tools</span>
  <h1>Python Engineering Toolkit — <code>cst</code></h1>
  <p>The open-source package that powers this project's templates: standards-cited calculators, a panel design pipeline, commissioning generators, PLC utilities, and diagnostics.</p>
</div>

The toolkit lives in the same repository as this site:
[github.com/kyawminthu20/Control-System-Tools](https://github.com/kyawminthu20/Control-System-Tools)
(`src/cst/`). Python 3.12+, standard library only at its core, 145 tests.

```bash
git clone https://github.com/kyawminthu20/Control-System-Tools.git
cd Control-System-Tools
uv sync            # installs the cst CLI (or: pip install -e .)
uv run cst --help
```

## Design Principles

1. **Every result carries its citations.** Calculators return the value plus
   the standard clauses, formulas, and assumptions behind it — ready to paste
   into design notes.
2. **Licensed table values are never distributed.** Rule *logic* is open;
   bulk table values (NEC ampacity, motor FLC, Bussmann C-values) load from
   files you transcribe from your own licensed copies. Clearly-marked sample
   data lets everything run out of the box — and warns you it's sample data.
3. **One I/O list drives everything.** The panel and commissioning generators
   all consume the same CSV, so the BOM, wire schedule, loop sheets, and FAT
   protocol stay consistent with each other.

## What It Does

| Command | What it produces | Basis |
|---|---|---|
| `cst voltage-drop` / `wire-size` | Conductor voltage drop; minimum AWG for a drop target | NEC K-factor method; 210.19(A)/215.2(A) recommendations |
| `cst ampacity` | Allowable ampacity with ambient correction and bundle adjustment | NEC 310.15(B) equation, Table 310.15(C)(1) |
| `cst motor-branch` | Conductor, OCPD, and overload sizing for one motor | NEC Art. 430 chain (430.22, Table 430.52(C)(1), 240.6(A), 430.32) |
| `cst transformer` | Transformer FLA and OCPD limits | NEC Table 450.3(B) |
| `cst sccr` | Panel SCCR weakest-link assessment | UL 508A Supplement SB4; NEC 409.22 check |
| `cst fault-current` | Infinite-bus fault current + point-to-point attenuation | Bussmann method |
| `cst enclosure` / `fan` | Sealed-enclosure temperature rise; filter-fan airflow | IEC/TR 60890-style effective-surface method |
| `cst encoder` | Encoder scaling: counts ↔ units ↔ RPM ↔ linear speed | Kinematics |
| `cst io-check` | I/O list validation (duplicate tags, address conflicts) | — |
| `cst bom` / `wire-schedule` / `legend` | Panel design documents from the I/O list | NFPA 79 Ch. 16/19 conventions |
| `cst loop-sheets` / `fat` | Per-point loop test sheets; FAT/SAT protocol skeleton | ISA-style loop-check practice |
| `cst tags-from-io` / `modbus-map` | PLC tag database; Modbus register map | IEC 61131-3 identifier rules; Modbus data model |
| `cst saleae` | Pulse stats, glitch finder, quadrature decode from Logic 2 exports | — |
| `cst modbus-decode` | Offline Modbus TCP capture analysis: exception responses, unanswered requests, response latency, polled register spans | Modbus Application Protocol Specification V1.1b3 |
| `cst sbm` | Similarity-based anomaly scores for sensor data | SBM-family kernel autoassociative model |
| `cst twin-validate` | Digital-twin payload against the data contract: required fields, requested authority vs the register ceiling, freshness | Corpus `digital_twin.md` §5; NIST SP 800-82r3 |
| `cst twin-sync` | Synchronization health of twin telemetry: gaps, out-of-order arrivals, staleness, clock skew and drift | Corpus `digital_twin.md` §3 steps 2 and 4 |
| `cst design-package` | One markdown design document stitching the above together | — |

Example — the classic Article 430 chain for a 10 hp, 460 V motor:

```text
$ cst motor-branch --hp 10 --volts 460 --nameplate-fla 13.2
Motor branch circuit — 10 hp, 460 V, 3-phase: 17.5 A (min conductor ampacity)
  ocpd_rating_a: 35
  overload_max_a: 16.5
  References:
    - NEC 2023 Table 430.250 — table FLC 14 A
    - NEC 2023 430.22 — branch conductors >= 125 % of table FLC
    - NEC 2023 Table 430.52(C)(1) + Exc. 1 — inverse time breaker max 250 %
    - NEC 2023 240.6(A) — standard rating selected: 35 A
    - NEC 2023 430.32(A)(1) — overload at 125 % of nameplate FLA
```

Example — reading a Modbus TCP capture taken during an intermittent-dropout
investigation:

```text
$ cst modbus-decode capture.pcap --exceptions --unanswered
frames        : 13  (7 req / 6 resp)
unit ids      : 1
capture span  : 0.600 s
  Read Holding Registers            13
response time : mean 8.33 ms, max 10.00 ms
exceptions    : 1
unanswered    : 1

exception responses:
  t=1000.510000 unit=1 txn=6 Read Holding Registers: Illegal Data Address

unanswered requests: 1
  t=1000.600000 unit=1 txn=7 Read Holding Registers start=200 qty=2
```

`--addresses` lists the register spans the client actually polls, which you can
diff against the design-time map from `cst modbus-map`.

Example — checking a digital-twin proposal before a gate would see it, and the
synchronization health of the telemetry feeding it:

```text
$ cst twin-validate payload.json --register methods.yml --method-id digital_twin_state_sync
3 problem(s):
  - missing required contract field "calibration_version" — which calibration the value rests on
  - requested_authority 3 exceeds the register ceiling 2 for this method
  - payload is stale: valid_until 1752960302.000 passed at 1752960500.000 (198 s late) — a gate must reject it

$ cst twin-sync telemetry.csv --max-age 5
Twin synchronization health: 60 samples over 70 s
  median interval: 1 s
  max gap: 12 s (1 gap(s) detected)
  out-of-order samples: 0
  stale samples: 0 (0.0%)
  mean skew: 0.1922 s (max |skew| 0.204 s)
  skew drift: 0.000309 s/s
  Warnings:
    ! 1 telemetry gap(s); longest 12 s at 1752960030.000 — twin state was unsynchronized across it
```

The authority ceiling comes from the [AI method register]({{ '/design/ai-integration/' | relative_url }}),
never from the payload's own claim. See [The Digital Twin]({{ '/design/ai-integration/digital-twin/' | relative_url }})
for the contract and the maturity ladder these checks implement.

## Limits

- Screening and design-assist calculations — final designs need the official
  standards, project-specific data, and engineering review.
- `cst twin-validate` and `cst twin-sync` **report and never act.** A clean
  result means a proposal is well-formed enough for a non-learned gate to judge,
  or that telemetry has the synchronization properties it claims — never that
  anything is safe or authorized. The gate that clamps or vetoes a proposal is
  plant-side engineering with its own integrity requirements, not a Python
  library.
- `cst modbus-decode` reads capture files offline and never opens a network
  interface. Taking the capture is a separate step: on a live OT segment use a
  passive method (a TAP or a switch mirror port) — active scanning or injected
  traffic can disturb a process that is controlling plant.
- Sample table data is for demonstration; transcribe licensed values before
  design use (the tool warns you until you do).
- Live PLC helpers (`pycomm3` extra) read and verify only — they never write
  to a running controller.

See the [templates page]({{ '/tools/templates/' | relative_url }}) for
documents generated by the toolkit that you can download directly.
