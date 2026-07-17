<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Interfaces, edge inference, and the result contract

Corpus source for the site's Interfaces & Handshakes page. It records where a learned service sits on
the network, why high-rate inference belongs at the edge, and how its result should cross into the
control system. Claims trace to the OPC UA specification parts retrieved in the Phase 49a sprint, to
NIST SP 800-82 Rev. 3, and to the MQTT Sparkplug specification; where a claim is version-dependent it
says "verify against your version."

## 1. The rule

Analyse the fast signal **where it is measured**, and send the verdict — not the waveform — across the
network. Perform high-rate acquisition and inference at the source, then publish the lower-rate result
with its class or estimate, confidence or uncertainty, model version, timestamp, quality, and
freshness.

## 2. Why: the four constraints — not "the protocol is too slow"

A common but **incorrect** claim is that "kHz signals cannot go through OPC UA." As a protocol claim
this is false: OPC UA PubSub/UADP over TSN has been measured at a 250 µs cycle (4 kHz) with
sub-microsecond jitter — the protocol is not the bottleneck. The edge-inference conclusion instead
rests on four constraints:

1. **Server sampling floor.** OPC UA Part 4 makes sampling *best-effort*: the server returns a
   `revisedSamplingInterval` it can actually meet, and Part 5 defines `MinSupportedSampleRate`. The
   specification anticipates a server-imposed floor. Some embedded OPC UA servers on PLCs impose a
   minimum sampling interval on the order of tens to hundreds of milliseconds — two to three orders of
   magnitude short of kHz. (Verify the floor for your device.)
2. **Decoupled source and aliasing — the decisive one, and it is spec-level.** Part 4 states the
   server *"provides access to a decoupled system and therefore has no knowledge of the data update
   logic."* **You cannot reconstruct a waveform by oversampling a tag whose source updates once per
   PLC scan** — you alias it.
3. **The historian is a compressor, not a recorder.** Deadband and swinging-door compression decimate
   by design; a feature pipeline reading archives gets decimated data.
4. **Segmentation.** Pushing a kHz stream across the IT/OT boundary means widening a conduit that
   NIST SP 800-82 Rev. 3 guidance says to keep narrow.

The conclusion — **inference on high-rate signals belongs at the edge; only the result crosses into
SCADA** — follows from these four, not from protocol speed.

## 3. Neither OPC UA nor Sparkplug gives an AI result a standard meaning

You must define and test the application contract explicitly. What the transports do and do not give:

- **OPC UA.** There is **no AI/ML companion specification** for inference results (verify against the
  current companion-spec list, which grows over time). A `DataValue` has a fixed set of fields and its
  quality is a coarse `StatusCode`, not a confidence number. What OPC UA *does* provide: custom
  **Structured DataTypes** — the sanctioned way to define a `ModelResult` structure; the
  `Uncertain_*` status codes (e.g. `Uncertain_LastUsableValue`) as an idiomatic "model degraded /
  inputs missing" channel; `SourceTimestamp` for freshness; and **Part 9 Alarms & Conditions**, which
  is the correct construct for an AI advisory that requires human acknowledgement.
- **MQTT Sparkplug B.** Metrics carry **arbitrary per-metric properties** (used today for engineering
  units and range limits), so a result's confidence, model version, and freshness can travel as metric
  properties without a bespoke type. Publisher liveness is managed by **birth/death certificates**
  (NBIRTH/NDEATH, DBIRTH/DDEATH), so a subscriber can detect a dead publisher. As with OPC UA, none of
  this assigns an AI result a standard *meaning* or *authority* — that remains the application's job.

## 4. Write-authority separation

This is the strongest, fully spec-backed part of the interface story. OPC UA separates read from write,
and the well-known **Observer** role (browse / read / subscribe, **no write**) maps exactly onto an
edge inference service that publishes results and must never write setpoints. Sparkplug B has no
equivalent role construct — the same separation is a **convention you must enforce** (broker ACLs,
topic namespacing), not a guarantee you inherit.

An edge inference service should therefore be **publish-only** with respect to control: it emits a
result contract; a separate, verifiable layer decides whether to act on it.

## 5. The result contract

Publish a compact, self-describing result, not a raw stream. A minimal payload:

```json
{
  "result":        "bearing_outer_race_fault",
  "confidence":    0.87,
  "model_version": "vib-cnn 2.3.1",
  "timestamp_utc": "2026-07-16T09:41:07Z",
  "quality":       "GOOD",
  "freshness_ms":  250
}
```

Two optional fields strengthen it: a **training-set identifier** makes drift auditable, and an explicit
**authority tag** lets the consumer enforce the register's ceiling at the point of use. Publishing a
compact result also crosses zone boundaries on terms a raw waveform stream does not.

## 6. The cybersecurity boundary

Place the AI service inside the existing OT security zones and conduits. **NIST SP 800-82 Rev. 3**
supports edge-local computation and read-only monitoring as a distinct, lower-impact class; keep the
service **read-only by default and least-privilege**, and do not widen a conduit to carry a raw stream.
(Cite NIST SP 800-82r3 for this placement; specific IEC 62443 clause numbers were not verified and are
not asserted.)

## Sources

- OPC UA Parts 1/3/4/5/9/18 — OPC Foundation (retrieved in the Phase 49a sprint): best-effort sampling
  and `MinSupportedSampleRate`; decoupled-source statement; no AI/ML companion spec; `Uncertain_*`
  status; Part 9 Alarms & Conditions; read/write separation and the Observer role.
- MQTT Sparkplug specification — per-metric properties; NBIRTH/NDEATH and DBIRTH/DDEATH liveness
  (verify against your Sparkplug version).
- NIST SP 800-82 Rev. 3 — Guide to Operational Technology Security (edge-local, read-only, segmentation).
- OPC UA PubSub/UADP over TSN — 250 µs cycle measurement (basis for the "protocol is not the bottleneck"
  correction).

## Changelog

- 2026-07-17 — Slice C corpus note drafted from the Phase 49a interface findings. The 49a note's
  "Sparkplug first-class STALE quality" claim was **not** confirmed against the specification during
  Slice C and was replaced with the verified birth/death-certificate liveness mechanism. Review pending.
