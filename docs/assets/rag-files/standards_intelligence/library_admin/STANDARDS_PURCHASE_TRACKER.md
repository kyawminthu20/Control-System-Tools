<!--
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Standards Purchase Tracker
**AI_READ_ACCESS: ALLOWED**
**CONTENT_CLASS: RAG_APPROVED**
**Status:** Working Reference
**Last Updated:** 2026-03-05

## Purpose

This file tracks which standards are already represented in `control-standards/rag/standards_intelligence/` and which official standards should be purchased or downloaded to improve local standards insight for machinery, hydraulic systems, chemical handling, OT cybersecurity, HMI/alarm design, and the multi-industry machine scenario packages.

## How To Read This File

- `Have locally` means there is a substantive local RAG module or scenario support content.
- `Planned locally` means the standard appears in local routing or index content but does not yet have usable clause-level coverage.
- `Missing locally` means there is no dedicated local module in `standards_intelligence/`.
- `Buy now` means the standard closes an active gap in the current scenario packages.
- Prices are the public prices visible on official vendor pages on **2026-03-05**.
- If a vendor page did not expose a current public list price, the price cell is marked `Not publicly listed`.
- Local paraphrased content does **not** replace an official licensed standard.

## Already In Local Corpus

| Priority | Standard | Local status | Local evidence | Official link | Public price | Notes |
|---|---|---|---|---|---|---|
| Keep official copy | NFPA 70 / NEC 2023 | Have locally | `us/nec/` and `_index.yaml` shows `NEC_2023` as `complete` | [NFPA LiNK](https://products.nfpa.org/view/126122027/) | Not publicly listed | Local module exists, but official NFPA access is still needed for authoritative installation code decisions and edition control. |
| Keep official copy | NFPA 79:2024 | Have locally | `us/nfpa79/` and `_index.yaml` shows `NFPA_79_2024` as `complete` | [NFPA LiNK](https://products.nfpa.org/view/126122027/) | Not publicly listed | Local module exists, but official NFPA access is still needed for machine electrical design decisions. |
| Keep official copy | UL 508A | Have locally | `us/ul_508a/` and `_index.yaml` shows `UL_508A_Ed3` as `complete` | [UL 508A](https://www.shopulstandards.com/ProductDetail.aspx?productId=UL508A_3_S_20180424) | USD 350.00 online / USD 698.00 print | Displayed provenance normalized 2026-07-13 to Edition 3 published 2018 and revised 2025; legacy filenames remain for link stability. |
| Keep official copy | IEC 60204-1 | Have locally | `international/machinery/iec_60204_1/` and `_index.yaml` shows `IEC_60204_1_2016A1` as `complete` | [IEC 60204-1:2016+AMD1:2021 CSV](https://webstore.iec.ch/en/publication/71256) | CHF 790 | Local corpus currently labels this as `2018`; IEC webstore currently presents the consolidated `2016+AMD1:2021` version, so edition normalization is needed. |

## High-Priority Purchases For Current Gaps

| Priority | Standard | Local status | Local evidence | Official link | Public price | Notes |
|---|---|---|---|---|---|---|
| Buy now | ISO 12100:2010 | Planned locally | `_index.yaml` lists `ISO_12100_2010` under `international/functional_safety` with status `planned`; also repeatedly cited as `[TO VERIFY: ISO 12100]` in `scenario/mini_machine_safety_design_v2/` | [ISO 12100:2010](https://www.iso.org/standard/51528.html) | CHF 225 | Highest-value gap for machinery risk assessment and risk reduction framing. |
| Buy now | ISO 13849-1:2023 | Planned locally | `_index.yaml` lists `ISO_13849_1_2023` with status `planned`; local folder only contains `international/functional_safety/iso_13849_1/file_structure.md` | [ISO 13849-1:2023](https://www.iso.org/standard/73481.html) | CHF 227 | Best first buy if your machinery work will use the PL method rather than IEC 62061. |
| Buy now | ISO 13849-2:2012 | Missing locally | Not present as a dedicated module; safety validation gap is visible in the scenario package | [ISO 13849-2:2012](https://www.iso.org/standard/53640.html) | CHF 225 | Complements ISO 13849-1 with validation methods; buy with Part 1, not later. |
| Buy now | IEC 62061:2021 | Planned locally | `_index.yaml` lists `IEC_62061_2021` with status `planned`; scenario package repeatedly marks `[TO VERIFY: IEC 62061]` | [IEC 62061:2021](https://webstore.iec.ch/en/publication/59927) | CHF 430 | Buy if you want the machinery SIL path or if customers prefer SIL vocabulary over PL. |
| Buy now | IEC 62061:2021/AMD1:2024 | Missing locally | No dedicated local module | [IEC 62061:2021/AMD1:2024](https://webstore.iec.ch/en/publication/71331) | CHF 40 | Cheap add-on; buy with the base publication. |
| Buy now | ISO 4413:2010 | Missing locally | Scenario package repeatedly marks `[TO VERIFY: ISO 4413]` in hydraulic and isolation sections | [ISO 4413:2010](https://www.iso.org/standard/44781.html) | CHF 181 | Most important hydraulic safety gap for the mini machine concept. |
| Buy now | IEC 61511-1:2016 | Planned locally | `_index.yaml` lists `IEC_61511_2016` with status `planned`; scenario package repeatedly marks `[TO VERIFY: IEC 61511]` | [IEC 61511-1:2016](https://webstore.iec.ch/en/publication/24241) | CHF 380 | Required if you want a defensible process-industry SIS path for chemical dosing or petroleum/energy overlays. |
| Buy now | IEC 61511-2:2016 | Missing locally | No dedicated local module | [IEC 61511-2:2016](https://webstore.iec.ch/en/publication/25510) | CHF 475 | Needed with Part 1 for application guidance. |
| Buy now | IEC 61511-3:2016 | Missing locally | No dedicated local module | [IEC 61511-3:2016](https://webstore.iec.ch/en/publication/25480) | CHF 405 | Needed with Parts 1 and 2 for SIL determination and lifecycle guidance. |
| Buy now | IEC 62443-2-1:2024 | Missing locally | Scenario package repeatedly marks `[TO VERIFY: IEC 62443]`; no dedicated `iec_62443` module exists | [IEC 62443-2-1:2024](https://webstore.iec.ch/en/publication/62883) | CHF 405 | Best starting point for OT cybersecurity program/process requirements. |
| Buy now | IEC 62443-3-3:2013 | Missing locally | No dedicated local module | [IEC 62443-3-3:2013](https://webstore.iec.ch/en/publication/7033) | CHF 380 | Use for system security requirements and security levels. |
| Buy now | IEC 62443-4-2:2019 | Missing locally | No dedicated local module | [IEC 62443-4-2:2019](https://webstore.iec.ch/en/publication/34421) | CHF 405 | Use for component-level technical security requirements. |
| Buy now | NFPA 70E | Missing locally | Scenario package marks `[TO VERIFY: NFPA 70E]`; no dedicated `nfpa70e` module exists | [NFPA LiNK](https://products.nfpa.org/view/126122027/) | Not publicly listed | Needed if you want stronger arc-flash and electrical safe work coverage in US projects. |
| Free download | NIST SP 800-82 Rev. 3 | Missing locally | Scenario package repeatedly marks `[TO VERIFY: NIST SP 800-82]` | [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | USD 0 | Download immediately; this is a no-cost OT security baseline. |

## Supporting Purchases

| Priority | Standard | Local status | Local evidence | Official link | Public price | Notes |
|---|---|---|---|---|---|---|
| Buy next | IEC 61508-1:2010 | Planned locally | `_index.yaml` lists `IEC_61508_2010` with status `planned`; scenario package repeatedly marks `[TO VERIFY: IEC 61508]` | [IEC 61508-1:2010](https://webstore.iec.ch/en/publication/5515) | CHF 380 | Foundation standard; buy after IEC 61511 unless you need the generic SIL lifecycle first. |
| Buy next | ISO 13850:2015 | Missing locally | No dedicated module; scenario uses E-stop examples without a direct local source | [ISO 13850:2015](https://www.iso.org/standard/59970.html) | CHF 100 | Focused E-stop design reference for machinery. |
| Buy next | ISO 14118:2017 | Missing locally | No dedicated module; scenario covers LOTO and stored-energy discharge but lacks this source | [ISO 14118:2017](https://www.iso.org/standard/66460.html) | CHF 67 | Good value for unexpected startup and intervention safety. |
| Buy next | ISO 14120:2015 | Missing locally | No dedicated module | [ISO 14120:2015](https://www.iso.org/standard/59545.html) | CHF 159 | Guard design and construction reference. |
| Buy next | ISO 14119:2024 | Missing locally | No dedicated module | [ISO 14119:2024](https://www.iso.org/standard/75942.html) | CHF 227 | Guard interlock design and selection reference. |
| Buy next | IEC 62682:2022 | Missing locally | No dedicated module; scenario currently points to ISA-18.2 as a gap | [IEC 62682:2022](https://webstore.iec.ch/en/publication/65543) | CHF 380 | Good official-priced alarm-management path if you want an IEC source alongside or instead of ISA-18.2. |
| Buy next | ANSI/ISA-18.2-2016 | Missing locally | Scenario package repeatedly marks `[TO VERIFY: ISA-18.2]` | [ANSI/ISA-18.2-2016](https://www.isa.org/products/ansi-isa-18-2-2016-management-of-alarm-systems-for) | Not publicly listed | Official ISA product page was accessible, but current public list price was not exposed on the accessible page. |
| Buy next | ANSI/ISA-101.01-2015 | Missing locally | Scenario package repeatedly marks `[TO VERIFY: ISA-101]` | [ANSI/ISA-101.01-2015](https://www.isa.org/products/ansi-isa-101-01-2015-human-machine-interfaces-for) | Not publicly listed | Official ISA product page was accessible, but current public list price was not exposed on the accessible page. |
| Free download | 21 CFR Part 11 | Missing locally | Scenario package repeatedly marks `[TO VERIFY: 21 CFR Part 11]` | [21 CFR Part 11 PDF](https://www.govinfo.gov/content/pkg/CFR-2023-title21-vol1/pdf/CFR-2023-title21-vol1-part11.pdf) | USD 0 | Free federal regulation; useful for regulated logging, audit trail, and electronic records. |
| Free download | FDA Part 11 scope and application guidance | Missing locally | No dedicated module | [FDA guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application) | USD 0 | Useful companion to Part 11 if you want a medical/pharma overlay. |

## Software, Redundancy, and Intrinsic Safety Purchases

| Priority | Standard | Local status | Local evidence | Official link | Public price | Notes |
|---|---|---|---|---|---|---|
| Buy now | IEC 61508-3:2010 | Planned locally | `_index.yaml` lists `IEC_61508_2010` as `planned`; see `reference_models/software_safety_and_intrinsic_safety_standards.md` | [IEC 61508-3:2010](https://webstore.iec.ch/en/publication/5517) | CHF 405 | Core software lifecycle standard for safety-related systems. |
| Buy now | IEC 61508-2:2010 | Missing locally | No dedicated module; see `reference_models/software_safety_and_intrinsic_safety_standards.md` | [IEC 61508-2:2010](https://webstore.iec.ch/en/publication/5516) | CHF 405 | Needed when software questions turn into redundancy, diagnostics, hardware architecture, or voting. |
| Buy next | IEC 61508-6:2010 | Missing locally | No dedicated module; see `reference_models/software_safety_and_intrinsic_safety_standards.md` | [IEC 61508-6:2010](https://webstore.iec.ch/en/publication/5520) | CHF 405 | Guidance companion for architecture and application interpretation. |
| Buy now | IEC 61131-3:2025 | Missing locally | No dedicated module; see `reference_models/software_safety_and_intrinsic_safety_standards.md` | [IEC 61131-3:2025](https://webstore.iec.ch/en/publication/68533) | CHF 475 | Use for PLC language and implementation structure; not enough alone for SIL or PL claims. |
| Buy now | IEC 62443-4-1:2018 | Missing locally | No dedicated module; see `reference_models/software_safety_and_intrinsic_safety_standards.md` | [IEC 62443-4-1:2018](https://webstore.iec.ch/en/publication/33615) | CHF 335 | Secure development lifecycle for IACS products and software-enabled components. |
| Buy if hazardous area work is real | IEC 60079-11:2023 | Missing locally | No dedicated module; see `reference_models/software_safety_and_intrinsic_safety_standards.md` | [IEC 60079-11:2023](https://webstore.iec.ch/en/publication/60654) | CHF 475 | Apparatus requirements for intrinsic safety. |
| Buy if hazardous area work is real | IEC 60079-14:2024 | Missing locally | No dedicated module; see `reference_models/software_safety_and_intrinsic_safety_standards.md` | [IEC 60079-14:2024](https://webstore.iec.ch/en/publication/66049) | CHF 430 | Design, selection, erection, and segregation rules for hazardous-area installations. |
| Buy if hazardous area work is real | IEC 60079-25:2020 | Missing locally | No dedicated module; see `reference_models/software_safety_and_intrinsic_safety_standards.md` | [IEC 60079-25:2020](https://webstore.iec.ch/en/publication/60679) | CHF 335 | System-level intrinsic-safety requirements for loops and associated apparatus. |
| Buy if hazardous area work is real | UL 60079-11 | Missing locally | No dedicated module | [UL 60079-11](https://www.shopulstandards.com/ProductDetail.aspx?productId=UL60079-11_1_S_20260130) | USD 846.00 online / USD 2116.00 print | US listing path for intrinsically safe apparatus and associated apparatus. |
| Buy if hazardous area work is real | UL 698A | Missing locally | No dedicated module | [UL 698A](https://www.shopulstandards.com/ProductDetail.aspx?productId=UL698a) | USD 402.00 online / USD 998.00 print | US panel route to verify when hazardous-location control panels or associated apparatus are in scope. |

## Semiconductor Overlay Purchases

| Priority | Standard | Local status | Local evidence | Official link | Public price | Notes |
|---|---|---|---|---|---|---|
| Buy if semiconductor work is real | SEMI S2 | Missing locally | `scenario/mini_machine_safety_design_v2/industry_overlays/semiconductor.md` marks `[TO VERIFY: SEMI S2]` | [SEMI S2](https://store-us.semi.org/products/s00200-semi-s2-environmental-health-and-safety-guideline-for-semiconductor-manufacturing-equipment) | USD 380.00 | Highest-priority semiconductor equipment safety buy. |
| Buy if semiconductor work is real | SEMI S8 | Missing locally | Same overlay marks `[TO VERIFY: SEMI S8]` | [SEMI S8](https://store-us.semi.org/products/s00800-semi-s8-safety-guideline-for-ergonomics-engineering-of-semiconductor-manufacturing-equipment) | USD 380.00 | Ergonomics overlay for semiconductor equipment. |
| Buy if semiconductor work is real | SEMI S10 | Missing locally | Same overlay references risk assessment and evaluation gaps | [SEMI S10](https://store-us.semi.org/products/s01000-semi-s10-safety-guideline-for-risk-assessment-and-risk-evaluation-process) | USD 380.00 | Semiconductor-specific risk-assessment process. |
| Buy if semiconductor work is real | SEMI S22 | Missing locally | Same overlay notes electrical design gaps | [SEMI S22](https://store-us.semi.org/products/s02200-semi-s22-safety-guideline-for-the-electrical-design-of-semiconductor-manufacturing-equipment) | USD 380.00 | Electrical design overlay for semiconductor equipment. |
| Buy if semiconductor work is real | SEMI S13 | Missing locally | Same overlay notes documentation expectations | [SEMI S13](https://store-us.semi.org/products/s01300-semi-s13-environmental-health-and-safety-guideline-for-documents-provided-to-the-equipment-user-for-use-with-manufacturing-equipment) | USD 193.00 | Documentation and user-package support standard. |

## Standards Not Yet Scoped To A Single Concrete Buy

| Industry area | Why it is not in the main buy list yet | What to decide first |
|---|---|---|
| Petroleum and offshore hazardous locations | The current scenario package only says `NEC hazardous location articles`, `offshore standard`, and `marine classification standard`; that is too generic for a clean purchase list. | Decide whether the project basis is NEC hazloc, IEC 60079/ATEX, or an owner/class-society rule set. |
| Marine and offshore | The exact required rulebook depends on class and flag basis. | Decide class society first, for example ABS, DNV, Lloyd's Register, or equivalent. |
| Nuclear | The current scenario package only says `nuclear standard`, `nuclear safety standard`, and `nuclear QA standard`; that is too generic for a defensible procurement list. | Decide whether the target basis is commercial nuclear QA, software V&V, safety system design, or plant-specific procurement rules. |
| Food and beverage hygienic design | The scenario package only says `food equipment hygienic standard`. | Decide whether the governing basis is 3-A, NSF/ANSI, EHEDG, or customer plant specifications. |
| Medical device overlays | The free Part 11 and FDA guidance are broadly useful, but true medical-device compliance can point to very different paid standards. | Decide whether the machine is only supporting regulated manufacturing, or is itself part of a medical-device product system. |

## Recommended Buy Order

1. Buy or renew official access for `NFPA 70`, `NFPA 79`, `UL 508A`, and `IEC 60204-1`.
2. Buy `ISO 12100`, `ISO 13849-1`, `ISO 13849-2`, and `ISO 4413`.
3. Choose one machinery integrity path to deepen first:
   - `ISO 13849` path for PL-heavy machinery work
   - `IEC 62061` path for machinery SIL work
4. Buy `IEC 61511 Parts 1-3` if chemical dosing, petroleum, energy, or process-style interlocks matter.
5. Download `NIST SP 800-82`, `21 CFR Part 11`, and the FDA Part 11 guidance immediately because they are free.
6. Add `IEC 61508-3`, `IEC 61131-3`, and `IEC 62443-4-1` for software lifecycle, PLC language, and secure-development coverage.
7. Add `IEC 62443-2-1`, `IEC 62443-3-3`, and `IEC 62443-4-2` for OT security coverage.
8. Add `IEC 60079-11`, `IEC 60079-14`, `IEC 60079-25`, and the US UL or NEC path only if intrinsically safe or classified-area I/O is in scope.
9. Add `ISA-18.2` or `IEC 62682`, plus `ISA-101`, if alarm philosophy, event logging, and HMI governance are important.
10. Add `SEMI S2/S8/S10/S22/S13` only if semiconductor work is active.
