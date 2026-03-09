<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC_60079
STANDARD_ID: IEC_60079-0
EDITION: 2017

IEC_HIERARCHY:
  part: "0"
  part_title: "Explosive Atmospheres — General Requirements"

INDEX_TAGS:
  topics: ["explosive_atmosphere", "equipment_marking", "EPL", "temperature_class", "gas_group", "certification", "ATEX", "IECEx"]
  systems: ["process_control", "oil_gas", "chemical", "hazardous_area"]
-->

# IEC 60079-0 — Explosive Atmospheres: General Requirements

## 0. Why this matters for control engineers

IEC 60079-0 establishes the foundational marking system and general requirements for ALL electrical equipment used in explosive atmospheres. Every piece of Ex-rated equipment carries markings defined in this part. Understanding the marking system allows engineers to select, install, and inspect equipment correctly without needing to read every protection-method standard individually.

## 1. Equipment marking system

All Ex equipment carries a marking string defined in IEC 60079-0. The format is:

```
Ex [protection method(s)] [gas group] T[temp class] [EPL]
```

**Example:** `Ex d IIB T4 Gb`
- `Ex` — certified for explosive atmospheres
- `d` — flameproof protection method (see IEC 60079-1)
- `IIB` — gas group (ethylene and similar)
- `T4` — maximum surface temperature 135°C
- `Gb` — Equipment Protection Level for Zone 1

Multiple protection methods may appear: `Ex de IIC T5 Gc`

## 2. Equipment Protection Levels (EPL)

EPL is the fundamental safety indicator — it replaces older category systems for most purposes:

| EPL | Zone | Protection Level |
|-----|------|-----------------|
| Ga  | Zone 0 | Very high — two independent faults required to cause ignition |
| Gb  | Zone 1 | High — suitable for normal operation and some abnormal conditions |
| Gc  | Zone 2 | Enhanced — suitable for normal operation |
| Da  | Zone 20 | Very high (dust) |
| Db  | Zone 21 | High (dust) |
| Dc  | Zone 22 | Enhanced (dust) |

## 3. Gas groups

Gas groups classify flammable gases by their ignition energy and quenching gap:

| Group | Hazard Level | Typical Gases |
|-------|-------------|--------------|
| IIA   | Lowest | Propane, methane, acetone |
| IIB   | Intermediate | Ethylene, hydrogen sulfide |
| IIC   | Highest | Hydrogen, acetylene |

Equipment marked IIC is suitable for all gas groups. Equipment marked IIA is only suitable for Group IIA gases and must not be used in IIB or IIC atmospheres.

## 4. Temperature classes (T-codes)

The T-code specifies the maximum surface temperature the equipment can reach under worst-case conditions:

| T-code | Max Surface Temp | Typical Use |
|--------|-----------------|-------------|
| T1 | 450°C | Very high autoignition gases |
| T2 | 300°C | |
| T3 | 200°C | Kerosene, fuel oil |
| T4 | 135°C | Most common for process industry |
| T5 | 100°C | Carbon disulfide (rare) |
| T6 | 85°C | Diethyl ether |

**Engineering rule:** Select equipment whose T-code maximum surface temperature is below the autoignition temperature of the hazardous substance at the installation. A margin of at least 50°C below autoignition is recommended by most best-practice guides.

## 5. Protection methods summary

| Code | Method | Standard | Typical Application |
|------|--------|----------|-------------------|
| d | Flameproof enclosure | IEC 60079-1 | Motors, junction boxes |
| e | Increased safety | IEC 60079-7 | Terminal boxes, luminaires |
| i | Intrinsic safety | IEC 60079-11 | Instrumentation, sensors |
| m | Encapsulation | IEC 60079-18 | Small components |
| n | Non-sparking | IEC 60079-15 | Zone 2 only |
| p | Purged/pressurized | IEC 60079-2 | Control panels, analyzers |
| q | Powder/sand filling | IEC 60079-5 | Transformers |
| o | Oil immersion | IEC 60079-6 | Switchgear |

## 6. Certification schemes

| Scheme | Scope | Recognition |
|--------|-------|-------------|
| ATEX | European Union | Mandatory for EU market |
| IECEx | International | Accepted in 55+ countries |
| UL (US) | United States | Required by NEC for listed equipment |
| CSA | Canada | Canadian market |

ATEX and IECEx certificates are mutually recognized in many countries. US installations using NEC Article 505 (Zone classification) can generally accept ATEX/IECEx certified equipment — verify with local AHJ.

## 7. Change log

- 2026-03-08 — Initial draft; marking system, EPL, gas groups, T-codes, protection methods overview.
