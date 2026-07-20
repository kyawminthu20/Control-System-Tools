# Phase 49d — Digital-Twin Evidence Closure (maturity vocabulary + ISO 23247 currency)

**Generated:** 2026-07-19 · **Status:** Work tier — non-authoritative research capture. Not site or
corpus content, and **no register row is changed by this document.**
**Inputs:** three publisher-verification targets (ISO 23247-5:2026 currency; re-check of the NIST
digital-twin publication; a sweep for any published digital-twin maturity model).
**Predecessors:** `digital-twin-integration.md` (the Phase 49a research note), `research-map.md`
(open TODO at line 144), `source-register.md`, `49a-findings.md`, `49c-findings.md`.
**Consumer:** the maturity-ladder content slice. §5 carries the verdict that slice must apply.

---

## 1. Headline

**The maturity vocabulary is PARTIALLY GROUNDED — better than the slice assumed.** The NIST digital-twin
publication already in `sources.yml` contains a **published five-category twin ladder** (Figure 1) that
was not previously extracted into the corpus note. The project's five proposed names are *not* the same
axis, but they map onto it cleanly, so the content slice can cite a real anchor for the ladder's shape
and reserve the "project working vocabulary" label for the synchronization axis alone.

Two results matter most:

- **NIST publishes the functional ladder.** Descriptive → Diagnostic → Predictive → Prescriptive →
  Intelligent, captioned *"Increasing complexity, more decision support, and greater value."* This is a
  primary, publisher-verified source for a five-rung twin progression.
- **NIST's top rung is explicitly aspirational, in NIST's own words.** *"Intelligent Digital Twins are
  **envisaged to** control their physical counterparts…"* — future tense, in the source. This
  independently corroborates the planned **M4 = described, not authorized** framing. The top of the
  published ladder is not a deployed state in the source either.

---

## 2. What closed, and what did not

**Verification key** as in `evidence-table.md` / `49c-findings.md`.

| Item | Prior status | 49d status | Basis |
|---|---|---|---|
| ISO 23247-5:2026 exists; title and scope | cited via NIST pub only | **VERIFIED_AT_PUBLISHER (catalogue metadata)** | iso.org catalogue entry, std. 87425 — see §3 caveat |
| ISO 23247 four-domain reference model | asserted in corpus note | **VERIFIED_AT_PUBLISHER** | NIST pub §4 + Figure 2, read directly |
| ISO 23247 twin definition ("fit for purpose… with synchronization") | verified via NIST | **VERIFIED_AT_PUBLISHER (re-confirmed)** | NIST pub §4, quoted verbatim below |
| One-way vs two-way synchronization (jet-engine case) | verified via NIST | **VERIFIED_AT_PUBLISHER (re-confirmed)** | NIST pub §1, quoted below |
| A published five-rung twin ladder | **assumed not to exist** | **VERIFIED_AT_PUBLISHER — it does** | NIST pub Figure 1 + §2 bullets |
| Top-of-ladder autonomous control is aspirational | project judgement | **VERIFIED_AT_PUBLISHER** | NIST pub §2 ("envisaged to") |
| Gemini/CDBB digital-twin maturity model | unchecked | **VERIFIED_VIA_DOI_REGISTRY — but does not ground our ladder** | Crossref 10.3390/su13158224; see §4 |
| ISO 23247-6 (twin composition), ISO/TR 23247-100:2025 | unknown | **NEW — noted, not pursued** | iso.org catalogue; see §6 |
| A standards-defined *synchronization* maturity ladder | — | **NOT_FOUND** | §4 sweep — absence of evidence, not proof of absence |

---

## 3. ISO 23247 currency

**ISO 23247-5:2026** — *Automation systems and integration — Digital twin framework for manufacturing —
Part 5: Digital thread for digital twin.* Edition 1, published June 2026, 26 pages, ISO/TC 184/SC 4.
Scope per the catalogue: specifies how a digital thread enables creation, connectivity, management and
maintenance of manufacturing digital twins across the product life cycle (design, planning, production,
testing) by defining principles, presenting methodologies, and providing use-case examples.

**Caveat, stated plainly:** a direct fetch of the iso.org catalogue page returned **HTTP 403** — the same
bot-gating pattern Phase 48 documented for the Siemens portals, not a dead link. The title, edition,
date, page count and committee above come from iso.org's own catalogue metadata as surfaced in search;
the **standard's body is paywalled and was not read.** Tagging is therefore
`VERIFIED_AT_PUBLISHER` **for existence, title, edition and date only** — no clause text, no
requirement, and no definition may be attributed to the body of Part 5 on this basis. The corpus note's
existing "ISO body not read" caveat stands and must not be softened.

---

## 4. The maturity sweep

**The NIST publication (primary, read in full for §§1–6).** Shao, Kibira & Frechette, *Digital Twins for
Advanced Manufacturing: The Standardized Approach*, NIST Engineering Laboratory. Figure 1 and the
following §2 bullets define five categories, each with a driving question:

| NIST category | Driving question (verbatim from Figure 1) |
|---|---|
| Descriptive Digital Twin | "What happened or is happening?" |
| Diagnostic Digital Twin | "What's wrong and why is it happening?" |
| Predictive Digital Twin | "What is likely to happen?" |
| Prescriptive Digital Twin | "How can we make it happen?" |
| Intelligent Digital Twin | "How can we automatically achieve our goals?" |

Verbatim passages worth preserving:

- Definition: ISO 23247 *"defines a 'Digital Twin in Manufacturing' as a 'fit for purpose digital
  representation of an observable manufacturing element with synchronization between the element and its
  digital representation.'"*
- One-way sync: *"The airline industry has used Digital Twins to monitor jet engines for many years.
  These types of digital twins use one-way synchronization. They receive data from the physical object
  but do not provide control feedback."*
- The aspirational top rung: *"Intelligent Digital Twins are **envisaged to** control their physical
  counterparts based on the strategies and parameters identified by the prescriptive Digital Twins."*
- Fit-for-purpose is load-bearing: *"The purpose dictates the information content, model fidelity, and
  frequency of synchronization."* — this is the source-grounded reason maturity is a *per-use-case
  declaration*, not a product grade.

**Gemini Principles / CDBB line.** Chen, Xie, Lu, Parlikad, Pitt & Yang, *Gemini Principles-Based Digital
Twin Maturity Model for Asset Management*, **Sustainability 13(15):8224 (2021), MDPI**, DOI
`10.3390/su13158224` — `VERIFIED_VIA_DOI_REGISTRY` (Crossref publisher-deposited metadata; the MDPI HTML
403'd). **It does not ground our ladder, for two reasons:** (a) structurally it is an *assessment rubric*
— three dimensions, nine sub-dimensions, 27 rubrics — not a sequential level ladder; (b) its domain is
built-environment asset management, validated by expert survey and city case studies, not process or
machinery control. Record it as adjacent prior art; do not cite it as the basis of a control-system
maturity claim.

**Sweep result for a standards-defined *synchronization* ladder** (offline → shadow → synchronized →
predictive → closed-loop, as a graded sync property): **NOT_FOUND.** ISO 23247 supplies the
one-way/two-way distinction and the fit-for-purpose principle, but no graded sync scale. Vendor and
analyst ladders (Gartner and similar) are marketing artifacts and were not pursued past identification —
`SECONDARY_ONLY` at absolute best, and not needed given the NIST anchor.

---

## 5. Verdict for the content slice

**PARTIALLY GROUNDED. Split the citation by axis — do not label the whole ladder project vocabulary.**

1. **The functional axis is NIST's and must be cited as such.** The five-rung progression from
   observation to automatic goal-seeking, and its ordering, come from the NIST publication (Figure 1).
   Cite `nist_dt_manufacturing`.
2. **The synchronization axis is this project's contribution and must be labelled as such.** Grading M0–M4
   by *what the data link and state estimation actually do* (no link / one-way / reconciled state /
   validated forward horizon / gated action path) is engineering judgement built on top of NIST's verified
   one-way-vs-two-way distinction. NIST grades by question answered; this project grades by
   synchronization owed. State the difference in the note rather than blurring the two.
3. **Keep the project's level names, and show the NIST mapping beside them.** M1 connected shadow ≈
   Descriptive; M2 synchronized twin ≈ Diagnostic; M3 predictive twin ≈ Predictive; M4 bounded
   closed-loop twin ≈ Prescriptive/Intelligent. M0 offline model sits **below** NIST's scale — NIST's
   ladder presumes a live twin — and that gap should be stated, not papered over.
4. **M4 stays "described, not authorized," and now has external corroboration.** NIST's own top rung is
   *envisaged*, and no register row grants a twin-composed learned output above level 2. Two independent
   reasons, one sourced and one internal. Neither is a permission.
5. **No ceiling moves.** Nothing in 49d supports raising any `max_authority`. `digital_twin_state_sync`
   stays at 2. The NIST ladder is a *functional* description and confers no authority — the same
   distinction 49a drew for capability-versus-authority sources generally.

---

## 6. Noted, not pursued

- **ISO/FDIS 23247-6** — *Part 6: Digital twin composition*, at FDIS stage (iso.org std. 87426). Directly
  relevant to the corpus note's "spine" framing if it publishes; re-check next twin slice.
- **ISO/TR 23247-100:2025** — *Part 100: Use case on management of semiconductor ingot growth process*
  (iso.org std. 90387). A published ISO twin use case in **semiconductor process control** — adjacent to
  the repo's existing `semiconductor_facility/` module. Flagged as a future cross-link candidate; no
  action this slice.
- Neither was read; both are catalogue-metadata sightings only.

---

## 7. What an implementer must not take from this document

- Not a clause-level reading of any ISO 23247 part. The bodies remain unread and paywalled.
- Not an authority argument. A twin that reaches NIST's "Intelligent" category still holds exactly the
  authority the method register assigns its composing models — currently 2, advisory.
- Not a maturity certification scheme. There is no assessment procedure here, and none is implied.
