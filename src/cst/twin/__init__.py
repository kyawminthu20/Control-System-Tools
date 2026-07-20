"""Digital-twin integration checks: the data contract and synchronization health.

Both modules report and never act. A clean result means a proposal is
well-formed enough for a non-learned gate to judge, or that telemetry has the
synchronization properties it claims — never that anything is safe or
authorized. Authority lives in the method register
(``control-standards/rag/design_framework/ai_integration/methods.yml``); the
gate that clamps or vetoes is plant-side engineering.
"""

from cst.twin.contract import (
    FIELD_SPECS,
    MAX_AUTHORITY_LEVEL,
    OPTIONAL_FIELDS,
    REQUIRED_FIELDS,
    VALUE_KINDS,
    FieldSpec,
    TwinContractError,
    TwinPayload,
    authority_ceilings,
    load_payload,
    schema,
    validate_payload,
)
from cst.twin.sync_health import Gap, SyncHealth, read_sample_csv, sync_health

__all__ = [
    "FIELD_SPECS",
    "MAX_AUTHORITY_LEVEL",
    "OPTIONAL_FIELDS",
    "REQUIRED_FIELDS",
    "VALUE_KINDS",
    "FieldSpec",
    "Gap",
    "SyncHealth",
    "TwinContractError",
    "TwinPayload",
    "authority_ceilings",
    "load_payload",
    "read_sample_csv",
    "schema",
    "sync_health",
    "validate_payload",
]
