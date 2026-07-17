#!/usr/bin/env python3
"""Validate the canonical AI-method register and publish Jekyll data.

The ``.yml`` source files use JSON syntax, which is a strict YAML subset. This
keeps the validation and generation path dependency-free while remaining
directly consumable by Jekyll.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "control-standards" / "rag" / "design_framework" / "ai_integration"
DESTINATION = ROOT / "docs" / "_data" / "ai_methods"
DATA_FILES = ("methods.yml", "sources.yml")

REQUIRED_METHOD_FIELDS = {
    "id",
    "method",
    "family",
    "does",
    "example",
    "layer",
    "deterministic_alternative",
    "justified_when",
    "poor_fit_when",
    "data_requirement",
    "max_authority",
    "authority_basis",
    "validation_required",
    "failure_modes",
    "safety_independence",
    "evidence_strength",
    "maturity",
    "sources",
    # Phase 50.13 selector-classification vocabulary (validated, never inferred in page JS).
    "method_class",
    "decision_type",
    "data_availability",
    "safety_relevance",
}
ALLOWED_MATURITY = {"research", "piloted", "industrially routine"}
ALLOWED_STRENGTH = {
    "peer-reviewed",
    "standards body",
    "preprint",
    "engineering judgement",
    "mixed",
}
ALLOWED_METHOD_CLASS = {"deterministic", "learned", "hybrid"}
ALLOWED_DECISION_TYPE = {
    "regulatory-control",
    "state-estimation",
    "monitoring-detection",
    "prediction-simulation",
    "perception",
    "engineering-support",
    "data-transport",
}
ALLOWED_DATA_AVAILABILITY = {
    "none-or-spec",
    "commissioning-tests",
    "operating-history",
    "labelled-examples",
    "pretrained-plus-context",
}
ALLOWED_SAFETY_RELEVANCE = {"safety-related", "safety-adjacent", "non-safety"}


def _load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path}: invalid register data: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{path}: root must be an object")
    return value


def validate(source: Path = SOURCE) -> list[str]:
    """Return human-readable validation errors for a register source tree."""
    errors: list[str] = []
    try:
        methods_doc = _load(source / "methods.yml")
        sources_doc = _load(source / "sources.yml")
    except ValueError as exc:
        return [str(exc)]

    for name, doc in (("methods.yml", methods_doc), ("sources.yml", sources_doc)):
        if doc.get("AI_READ_ACCESS") != "ALLOWED":
            errors.append(f"{name}: AI_READ_ACCESS must be ALLOWED")
        if doc.get("CONTENT_CLASS") != "RAG_APPROVED":
            errors.append(f"{name}: CONTENT_CLASS must be RAG_APPROVED")
        if doc.get("STATUS") != "DRAFT":
            errors.append(f"{name}: AI-generated register data must remain DRAFT")

    source_rows = sources_doc.get("sources")
    if not isinstance(source_rows, list):
        errors.append("sources.yml: sources must be a list")
        source_rows = []
    source_ids = {row.get("id") for row in source_rows if isinstance(row, dict)}
    if None in source_ids:
        errors.append("sources.yml: every source requires an id")
        source_ids.discard(None)
    if len(source_ids) != len(source_rows):
        errors.append("sources.yml: source ids must be unique")

    methods = methods_doc.get("methods")
    if not isinstance(methods, list):
        return errors + ["methods.yml: methods must be a list"]
    if not 40 <= len(methods) <= 60:
        errors.append(f"methods.yml: expected 40-60 methods, found {len(methods)}")

    seen: set[str] = set()
    for index, method in enumerate(methods, start=1):
        label = f"methods.yml method #{index}"
        if not isinstance(method, dict):
            errors.append(f"{label}: row must be an object")
            continue
        method_id = method.get("id")
        label = f"methods.yml {method_id or f'method #{index}'}"
        missing = REQUIRED_METHOD_FIELDS - method.keys()
        if missing:
            errors.append(f"{label}: missing {', '.join(sorted(missing))}")
        if not isinstance(method_id, str) or not method_id:
            errors.append(f"{label}: id must be a non-empty string")
        elif method_id in seen:
            errors.append(f"{label}: duplicate id")
        else:
            seen.add(method_id)
        authority = method.get("max_authority")
        if authority != "Planned" and (
            not isinstance(authority, int) or isinstance(authority, bool) or not 0 <= authority <= 5
        ):
            errors.append(f"{label}: max_authority must be 0-5 or Planned")
        if method.get("maturity") not in ALLOWED_MATURITY:
            errors.append(f"{label}: invalid maturity")
        if method.get("evidence_strength") not in ALLOWED_STRENGTH:
            errors.append(f"{label}: invalid evidence_strength")

        # Phase 50.13 selector vocabulary — membership checks.
        method_class = method.get("method_class")
        safety_relevance = method.get("safety_relevance")
        data_availability = method.get("data_availability")
        if method_class not in ALLOWED_METHOD_CLASS:
            errors.append(f"{label}: invalid method_class")
        if method.get("decision_type") not in ALLOWED_DECISION_TYPE:
            errors.append(f"{label}: invalid decision_type")
        if data_availability not in ALLOWED_DATA_AVAILABILITY:
            errors.append(f"{label}: invalid data_availability")
        if safety_relevance not in ALLOWED_SAFETY_RELEVANCE:
            errors.append(f"{label}: invalid safety_relevance")

        # Cross-field invariants (Phase 50.13). These encode the register's governing
        # architecture: a safety-related output must be deterministic and verifiable, and
        # cannot ride on an undetermined authority ceiling.
        if safety_relevance == "safety-related":
            if method_class != "deterministic":
                errors.append(
                    f"{label}: safety-related methods must be deterministic "
                    f"(method_class is {method_class!r})"
                )
            if authority == "Planned":
                errors.append(
                    f"{label}: safety-related methods cannot have Planned max_authority"
                )
        if data_availability == "pretrained-plus-context":
            if method_class != "learned":
                errors.append(
                    f"{label}: pretrained-plus-context requires method_class 'learned'"
                )
            if safety_relevance == "safety-related":
                errors.append(
                    f"{label}: pretrained-plus-context cannot be safety-related"
                )

        refs = method.get("sources")
        if not isinstance(refs, list) or not refs:
            errors.append(f"{label}: sources must be a non-empty list")
        else:
            unknown = sorted(set(refs) - source_ids)
            if unknown:
                errors.append(f"{label}: unknown sources {', '.join(unknown)}")
    return errors


def generate(source: Path = SOURCE, destination: Path = DESTINATION) -> list[str]:
    """Validate and copy canonical register data to the Jekyll data tree."""
    errors = validate(source)
    if errors:
        return errors
    destination.mkdir(parents=True, exist_ok=True)
    expected = set(DATA_FILES)
    for stale in destination.glob("*.yml"):
        if stale.name not in expected:
            stale.unlink()
    for name in DATA_FILES:
        shutil.copyfile(source / name, destination / name)
    return []


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate without publishing")
    args = parser.parse_args(argv)
    errors = validate() if args.check else generate()
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    print("AI method register is valid" + ("" if args.check else " and generated"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
