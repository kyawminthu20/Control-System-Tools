<!--
CONTENT_CLASS: DERIVED_REFERENCE
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Chemical Dosing Systems

## 0. Purpose

Control narrative for chemical dosing systems in water and wastewater treatment: chlorination (disinfection), coagulation/flocculation (solids removal), and pH adjustment. Covers flow-paced dosing with feedback trim, over-treatment (OT) shutdown logic, and chemical feed interlock chain.

## 1. Chlorination — Flow-Paced Dosing with Residual Feedback

Chlorine dosing uses a two-component control strategy:

**Base rate (feedforward):** Dosing pump rate is proportional to the plant flow rate measured by FT-301. This ensures the dose ratio (mg/L) stays approximately constant regardless of flow.

```
Base dose rate (mg/L) = Operator setpoint (typically 1.5–3.0 mg/L free Cl₂)
Pump rate (mL/min) = Base dose rate × Flow (m³/h) × [chemical concentration factor]
```

**Feedback trim (PID):** Chlorine residual analyzer AT-301 (amperometric or colorimetric, post-contact time) measures actual free Cl₂. A PID controller trims the pump rate up or down from the base rate to maintain residual at setpoint (typically 0.5–1.0 mg/L at the sample point).

The trim is limited to ±30% of base rate to prevent the feedback loop from fighting large disturbances (changes in chlorine demand from raw water quality changes).

## 2. Over-Treatment (OT) Shutdown

If the chlorine residual analyzer detects residual above the maximum allowed concentration (typically 4 mg/L for free chlorine under EPA rules), the system must take protective action:

1. **Alarm:** AT-301 > 3.5 mg/L → Alarm "High Cl₂ Residual" (early warning)
2. **Trip:** AT-301 > 4.0 mg/L for > 5 minutes → Close distribution isolation valve XV-301 (hardwired, SIL-rated)
3. **Latch:** XV-301 stays closed — requires operator manual reset
4. **Log:** SCADA records timestamp, residual value, operator ID for regulatory record

The 5-minute delay prevents nuisance trips from analyzer measurement lag. The latching requirement ensures an operator physically acknowledges the condition.

## 3. Coagulant Dosing (Alum / PAC)

Coagulant dose is flow-paced only (no feedback because the quality response is too slow and too noisy for real-time trim):

```
Alum dose (mg/L) = f(raw water turbidity, jar test results)
Pump rate = Dose × Flow × [concentration factor]
```

Dose ratio is set by the operator based on daily jar test results. SCADA provides a trend of raw turbidity vs. dose ratio vs. filtered turbidity to assist optimization.

## 4. pH Correction

pH adjustment is done with lime (Ca(OH)₂ slurry) or soda ash (Na₂CO₃) to raise pH, or CO₂ or H₂SO₄ to lower it. A PID controller with pH analyzer AT-302 at the contact basin outlet:

- **Setpoint:** 7.2–7.8 pH (within EPA secondary MCL range)
- **PV:** AT-302 (glass electrode pH sensor)
- **MV:** Lime slurry pump speed (0–100%)
- **Integral windup protection:** Required — pH is slow to respond (3–5 minute lag from dosing point to analyzer)

## 5. Chemical Feed Interlock Chain

Before any chemical metering pump can run, all interlocks must be clear:

| Interlock | Condition | Action |
|---|---|---|
| Secondary containment OK | Float switch in containment sump | High level — lockout all chemical pumps, alarm |
| Tank level > Low-Low | LT-TANK > 5% | Low-Low — stop pump, alarm "Chemical Supply Low" |
| Flow > minimum | FT-301 > 20 m³/h | No flow — stop dosing (no feed to dilute into) |
| Injection point pressure OK | PT-INJECT > 50 kPa | Low pressure — pump against closed valve — stop pump |

## 6. Instrumentation List

| Tag | Type | Range | Output | Purpose |
|---|---|---|---|---|
| AT-301 | Amperometric Cl₂ analyzer | 0–5 mg/L | 4-20mA | Free chlorine residual (dosing feedback) |
| AT-302 | pH transmitter | 0–14 pH | 4-20mA | pH at contact basin |
| FT-301 | Mag flowmeter | 0–1000 m³/h | 4-20mA + pulse | Plant flow (dosing feedforward) |
| LT-TANK | Float or guided wave radar | 0–100% | 4-20mA | Chemical tank level |
| FT-302 | Variable area or mag | 0–10 L/min | 4-20mA | Chemical feed flow confirmation |
| XV-301 | Motor-operated valve | Open/close | DO + DI feedback | Distribution isolation (SIL-rated trip) |
