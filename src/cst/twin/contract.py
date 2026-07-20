"""The digital-twin data contract, as an executable check.

The corpus note ``control-standards/rag/design_framework/ai_integration/
digital_twin.md`` §5 specifies what a payload crossing the device-communication
seam must carry so that a non-learned gate can *evaluate* it: identity,
timestamps, quality, model provenance, a freshness bound, and — the three that
make gating possible at all — the requested authority level, the action type,
and the audit fields.

This module turns that prose into ``FIELD_SPECS`` and validates payloads against
it. It deliberately **reports only and never acts**: the gate that clamps or
vetoes a proposal is plant-side engineering with its own integrity requirements,
not a Python library. A clean result here means "this proposal is well-formed
enough to be judged", never "this proposal is safe".
"""

from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

from cst.common.cite import Citation

#: The highest authority level the corpus ladder defines. Level 5 (direct
#: learned control) is not assigned to any learned twin output, so a payload
#: requesting it is always flagged regardless of the configured ceiling.
MAX_AUTHORITY_LEVEL = 5

#: Values permitted for ``value_kind``. The corpus is explicit that a prediction
#: must never silently read as a measurement (§3 step 5), which is why this is a
#: closed vocabulary rather than free text.
VALUE_KINDS = ("measured", "derived", "predicted")

CITATIONS = (
    Citation(
        standard="Control System Tools corpus",
        clause="design_framework/ai_integration/digital_twin.md §5",
        note="the data contract this module enforces field-for-field",
    ),
    Citation(
        standard="ISO 23247",
        clause="Digital twin framework for manufacturing (via NIST publication)",
        note="device-communication domain is the seam a payload crosses; ISO body not read",
    ),
    Citation(
        standard="NIST SP 800-82",
        clause="Rev. 3",
        note="OT security placement for the seam — read-only by default, least privilege",
    ),
)


@dataclass(frozen=True)
class FieldSpec:
    """One field of the twin data contract.

    ``types`` is the tuple of acceptable Python types; ``description`` states
    what the field contributes to gating, in the corpus note's own terms.
    """

    name: str
    types: tuple[type, ...]
    required: bool
    description: str
    allowed: tuple[str, ...] = ()

    @property
    def type_names(self) -> str:
        return "/".join(t.__name__ for t in self.types)


# Ordered as the corpus note lists them: identity, timestamps and quality,
# value, model provenance, freshness and health, then the gating fields.
FIELD_SPECS: tuple[FieldSpec, ...] = (
    FieldSpec("asset_id", (str,), True, "which physical asset the payload speaks for"),
    FieldSpec("signal_id", (str,), True, "which signal or inferred quantity"),
    FieldSpec(
        "correlation_id", (str,), True,
        "ties proposal, decision, and audit record together",
    ),
    FieldSpec(
        "source_timestamp", (int, float), True,
        "when the underlying observation was taken (epoch seconds)",
    ),
    FieldSpec(
        "inference_timestamp", (int, float), True,
        "when the model produced this output (epoch seconds)",
    ),
    FieldSpec("input_quality", (str,), True, "quality of the data the model consumed"),
    FieldSpec("output_quality", (str,), True, "quality the model claims for its output"),
    FieldSpec("value", (int, float, str, bool), True, "the payload's primary result"),
    FieldSpec(
        "value_kind", (str,), True,
        "measured, derived, or predicted — a prediction must never read as a measurement",
        allowed=VALUE_KINDS,
    ),
    FieldSpec("model_name", (str,), True, "which model produced the value"),
    FieldSpec("model_version", (str,), True, "which version of it"),
    FieldSpec(
        "feature_pipeline_version", (str,), True,
        "the feature pipeline is part of the model's identity",
    ),
    FieldSpec("calibration_version", (str,), True, "which calibration the value rests on"),
    FieldSpec(
        "valid_until", (int, float), True,
        "freshness bound (epoch seconds) — past this, the proposal is stale by construction",
    ),
    FieldSpec("sync_state", (str,), True, "the twin's synchronization state at inference time"),
    FieldSpec("service_health", (str,), True, "health of the service producing the payload"),
    FieldSpec("fallback_state", (str,), True, "what the plant falls back to if this is rejected"),
    FieldSpec(
        "requested_authority", (int,), True,
        f"authority level 0-{MAX_AUTHORITY_LEVEL} the proposal asks for — the gate's primary input",
    ),
    FieldSpec("action_type", (str,), True, "what the proposal would do if accepted"),
    # Optional: carried when meaningful, absent when not applicable.
    FieldSpec("uncertainty", (int, float), False, "uncertainty on the value, in its own units"),
    FieldSpec("confidence", (int, float), False, "model confidence, where the family defines one"),
    FieldSpec("prediction_horizon_s", (int, float), False, "how far ahead a prediction reaches"),
    FieldSpec("value_class", (str,), False, "class label, for classification outputs"),
    FieldSpec("acknowledged", (bool,), False, "whether the gate accepted the proposal"),
    FieldSpec("rejection_reason", (str,), False, "why the gate rejected it, if it did"),
    FieldSpec("audit_identity", (str,), False, "who or what committed the decision"),
)

_SPECS_BY_NAME = {spec.name: spec for spec in FIELD_SPECS}
REQUIRED_FIELDS = tuple(spec.name for spec in FIELD_SPECS if spec.required)
OPTIONAL_FIELDS = tuple(spec.name for spec in FIELD_SPECS if not spec.required)


class TwinContractError(ValueError):
    """Raised when a payload does not satisfy the contract.

    Carries every problem, not just the first, so a caller fixing a payload
    sees the whole list in one pass.
    """

    def __init__(self, problems: Sequence[str]) -> None:
        self.problems = list(problems)
        joined = "\n  - ".join(self.problems)
        super().__init__(f"{len(self.problems)} contract problem(s):\n  - {joined}")


def _check_type(spec: FieldSpec, value: object) -> str | None:
    """Return a problem string if *value* does not fit *spec*, else None."""
    # bool is a subclass of int, so an unguarded isinstance check would let
    # True satisfy an int field (and requested_authority=True read as 1).
    if bool not in spec.types and isinstance(value, bool):
        return (
            f'field "{spec.name}" is a boolean; expected {spec.type_names} '
            f"(a boolean here is almost always an encoding mistake)"
        )
    if not isinstance(value, spec.types):
        return (
            f'field "{spec.name}" has type {type(value).__name__}; '
            f"expected {spec.type_names} — {spec.description}"
        )
    if spec.allowed and value not in spec.allowed:
        return (
            f'field "{spec.name}" is {value!r}; expected one of '
            f"{', '.join(repr(a) for a in spec.allowed)} — {spec.description}"
        )
    return None


def validate_payload(
    data: Mapping[str, object],
    *,
    authority_ceiling: int | None = None,
    now: float | None = None,
) -> list[str]:
    """Return every contract violation in *data* as a message naming its field.

    An empty list means the payload is well-formed enough for a gate to judge —
    it is **not** a safety verdict.

    ``authority_ceiling`` is the maximum authority the caller's register row
    permits for this method; pass it to have the requested level checked against
    it. ``now`` (epoch seconds) is compared against ``valid_until`` for the
    staleness check; pass it explicitly so the check is deterministic in tests
    and reproducible in audits.
    """
    problems: list[str] = []

    for spec in FIELD_SPECS:
        if spec.name not in data:
            if spec.required:
                problems.append(
                    f'missing required contract field "{spec.name}" — {spec.description}'
                )
            continue
        problem = _check_type(spec, data[spec.name])
        if problem:
            problems.append(problem)

    unknown = sorted(set(data) - set(_SPECS_BY_NAME))
    problems.extend(
        f'unknown field "{name}" is not part of the contract — a gate cannot '
        f"interpret it, so it must not carry meaning"
        for name in unknown
    )

    src = data.get("source_timestamp")
    inf = data.get("inference_timestamp")
    if isinstance(src, (int, float)) and isinstance(inf, (int, float)):
        if not isinstance(src, bool) and not isinstance(inf, bool) and inf < src:
            problems.append(
                f"inference_timestamp ({inf:g}) precedes source_timestamp ({src:g}) — "
                f"a model cannot infer from an observation it has not seen"
            )

    level = data.get("requested_authority")
    if isinstance(level, int) and not isinstance(level, bool):
        if not 0 <= level <= MAX_AUTHORITY_LEVEL:
            problems.append(
                f"requested_authority {level} is outside the ladder "
                f"(0-{MAX_AUTHORITY_LEVEL})"
            )
        elif level == MAX_AUTHORITY_LEVEL:
            # Independent of any configured ceiling: the corpus ladder assigns
            # level 5 to no learned twin output at all.
            problems.append(
                f"requested_authority {MAX_AUTHORITY_LEVEL} (direct learned control) is not "
                f"assigned to any learned twin output — no evidence case supports it"
            )
        elif authority_ceiling is not None and level > authority_ceiling:
            problems.append(
                f"requested_authority {level} exceeds the register ceiling "
                f"{authority_ceiling} for this method"
            )

    valid_until = data.get("valid_until")
    if now is not None and isinstance(valid_until, (int, float)) and not isinstance(valid_until, bool):
        if now > valid_until:
            problems.append(
                f"payload is stale: valid_until {valid_until:g} passed at {now:g} "
                f"({now - valid_until:g} s late) — a gate must reject it"
            )

    return problems


@dataclass(frozen=True)
class TwinPayload:
    """A contract-valid payload, with the required fields as attributes.

    Build one with :meth:`from_mapping`; optional fields are exposed through
    :attr:`extras` rather than as attributes, so adding an optional field to the
    contract never changes this class's shape.
    """

    asset_id: str
    signal_id: str
    correlation_id: str
    source_timestamp: float
    inference_timestamp: float
    input_quality: str
    output_quality: str
    value: object
    value_kind: str
    model_name: str
    model_version: str
    feature_pipeline_version: str
    calibration_version: str
    valid_until: float
    sync_state: str
    service_health: str
    fallback_state: str
    requested_authority: int
    action_type: str
    extras: Mapping[str, object]

    @classmethod
    def from_mapping(
        cls,
        data: Mapping[str, object],
        *,
        authority_ceiling: int | None = None,
        now: float | None = None,
    ) -> "TwinPayload":
        """Validate *data* and build a payload, or raise :class:`TwinContractError`."""
        problems = validate_payload(data, authority_ceiling=authority_ceiling, now=now)
        if problems:
            raise TwinContractError(problems)
        return cls(
            **{name: data[name] for name in REQUIRED_FIELDS},
            extras={k: v for k, v in data.items() if k in OPTIONAL_FIELDS},
        )


def load_payload(path: str | Path) -> dict[str, object]:
    """Read a JSON payload file, with the file named in any parse error."""
    p = Path(path)
    try:
        text = p.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"payload file not found: {p}") from None
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"{p} is not valid JSON: {exc.msg} (line {exc.lineno}, column {exc.colno})"
        ) from None
    if not isinstance(data, dict):
        raise ValueError(
            f"{p} holds a {type(data).__name__}; a twin payload must be a JSON object"
        )
    return data


def authority_ceilings(register_path: str | Path) -> dict[str, int]:
    """Map method id to ``max_authority`` from the AI method register.

    Rows whose ceiling is not an integer — ``Planned``, above all — are
    **excluded**: no ceiling has been established for them, which is a different
    thing from a ceiling of zero, and silently treating it as zero would let a
    caller believe a limit had been decided when it has not.

    The path is required rather than defaulted, so a result is always traceable
    to the register file it came from. ``methods.yml`` is JSON-as-YAML, so the
    stdlib JSON parser reads it and no YAML dependency is needed.
    """
    p = Path(register_path)
    try:
        text = p.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"method register not found: {p}") from None
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"{p} is not parseable as JSON-as-YAML: {exc.msg} "
            f"(line {exc.lineno}, column {exc.colno})"
        ) from None

    rows = parsed.get("methods") if isinstance(parsed, dict) else parsed
    if not isinstance(rows, list):
        raise ValueError(f"{p} does not hold a list of method rows")

    ceilings: dict[str, int] = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        method_id = row.get("id")
        ceiling = row.get("max_authority")
        if isinstance(method_id, str) and isinstance(ceiling, int) and not isinstance(ceiling, bool):
            ceilings[method_id] = ceiling
    return ceilings


def schema() -> dict[str, object]:
    """Return the contract as a JSON Schema (draft 2020-12).

    Generated from :data:`FIELD_SPECS` so the published schema and the validator
    above cannot drift: there is one definition of the contract, and this is a
    view of it.
    """
    json_types = {
        str: "string",
        bool: "boolean",
        int: "integer",
        float: "number",
    }
    properties: dict[str, object] = {}
    for spec in FIELD_SPECS:
        names = [json_types[t] for t in spec.types]
        # An integer is a valid number; listing both is noise in the schema.
        if "number" in names and "integer" in names:
            names.remove("integer")
        prop: dict[str, object] = {
            "type": names[0] if len(names) == 1 else names,
            "description": spec.description,
        }
        if spec.allowed:
            prop["enum"] = list(spec.allowed)
        if spec.name == "requested_authority":
            prop["minimum"] = 0
            prop["maximum"] = MAX_AUTHORITY_LEVEL
        properties[spec.name] = prop

    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "Digital-twin data contract",
        "description": (
            "Payload crossing the device-communication seam between a digital twin "
            "and a control system. Structural validity only — satisfying this schema "
            "means a non-learned gate can evaluate the proposal, never that the "
            "proposal is safe or authorized."
        ),
        "type": "object",
        "additionalProperties": False,
        "required": list(REQUIRED_FIELDS),
        "properties": properties,
    }
