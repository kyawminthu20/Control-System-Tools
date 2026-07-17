import json
from pathlib import Path

from tools.generate_ai_method_register import generate, validate


def _write_register(root: Path, methods: list[dict], sources: list[dict]) -> None:
    metadata = {"AI_READ_ACCESS": "ALLOWED", "CONTENT_CLASS": "RAG_APPROVED", "STATUS": "DRAFT"}
    (root / "methods.yml").write_text(json.dumps({**metadata, "methods": methods}))
    (root / "sources.yml").write_text(json.dumps({**metadata, "sources": sources}))


def _method(index: int) -> dict:
    return {
        "id": f"method_{index}", "method": f"Method {index}", "family": "estimation",
        "does": "Estimates a state.", "example": "Estimating tank level from noisy sensors.",
        "layer": "edge", "deterministic_alternative": "Observer",
        "justified_when": "Validated evidence supports it.", "poor_fit_when": "Inputs are unobservable.",
        "data_requirement": "Representative labelled data.", "max_authority": 2,
        "authority_basis": "Conservative advisory ceiling.", "validation_required": "Held-out tests.",
        "failure_modes": "Drift.", "safety_independence": "Independent protection remains effective.",
        "evidence_strength": "engineering judgement", "maturity": "piloted", "sources": ["source"],
        "method_class": "deterministic", "decision_type": "state-estimation",
        "data_availability": "commissioning-tests", "safety_relevance": "safety-adjacent",
    }


def test_valid_register_generates_exact_files(tmp_path: Path) -> None:
    source = tmp_path / "source"; destination = tmp_path / "destination"; source.mkdir()
    _write_register(source, [_method(i) for i in range(40)], [{"id": "source", "title": "Source"}])
    assert generate(source, destination) == []
    assert (destination / "methods.yml").read_bytes() == (source / "methods.yml").read_bytes()


def test_register_requires_40_to_60_methods(tmp_path: Path) -> None:
    tmp_path.mkdir(exist_ok=True)
    _write_register(tmp_path, [_method(1)], [{"id": "source"}])
    assert any("expected 40-60" in error for error in validate(tmp_path))


def test_register_rejects_unknown_source(tmp_path: Path) -> None:
    methods = [_method(i) for i in range(40)]; methods[0]["sources"] = ["missing"]
    _write_register(tmp_path, methods, [{"id": "source"}])
    assert any("unknown sources missing" in error for error in validate(tmp_path))


def test_register_rejects_invalid_authority(tmp_path: Path) -> None:
    methods = [_method(i) for i in range(40)]; methods[0]["max_authority"] = 6
    _write_register(tmp_path, methods, [{"id": "source"}])
    assert any("max_authority" in error for error in validate(tmp_path))


def test_register_requires_example(tmp_path: Path) -> None:
    methods = [_method(i) for i in range(40)]; del methods[0]["example"]
    _write_register(tmp_path, methods, [{"id": "source"}])
    assert any("example" in error for error in validate(tmp_path))


# --- Phase 50.13 selector-classification vocabulary --------------------------

def test_register_requires_classification_fields(tmp_path: Path) -> None:
    methods = [_method(i) for i in range(40)]; del methods[0]["safety_relevance"]
    _write_register(tmp_path, methods, [{"id": "source"}])
    assert any("safety_relevance" in error for error in validate(tmp_path))


def test_register_rejects_invalid_method_class(tmp_path: Path) -> None:
    methods = [_method(i) for i in range(40)]; methods[0]["method_class"] = "magic"
    _write_register(tmp_path, methods, [{"id": "source"}])
    assert any("invalid method_class" in error for error in validate(tmp_path))


def test_register_rejects_invalid_decision_type(tmp_path: Path) -> None:
    methods = [_method(i) for i in range(40)]; methods[0]["decision_type"] = "guessing"
    _write_register(tmp_path, methods, [{"id": "source"}])
    assert any("invalid decision_type" in error for error in validate(tmp_path))


def test_register_rejects_invalid_data_availability(tmp_path: Path) -> None:
    methods = [_method(i) for i in range(40)]; methods[0]["data_availability"] = "vibes"
    _write_register(tmp_path, methods, [{"id": "source"}])
    assert any("invalid data_availability" in error for error in validate(tmp_path))


def test_safety_related_must_be_deterministic(tmp_path: Path) -> None:
    # Invariant 1 — the load-bearing guardrail: no learned method may be safety-related.
    methods = [_method(i) for i in range(40)]
    methods[0]["method_class"] = "learned"
    methods[0]["safety_relevance"] = "safety-related"
    _write_register(tmp_path, methods, [{"id": "source"}])
    assert any("safety-related methods must be deterministic" in e for e in validate(tmp_path))


def test_safety_related_cannot_have_planned_authority(tmp_path: Path) -> None:
    # Invariant 2 — a protective-layer claim cannot ride on an undetermined ceiling.
    methods = [_method(i) for i in range(40)]
    methods[0]["safety_relevance"] = "safety-related"  # deterministic already
    methods[0]["max_authority"] = "Planned"
    _write_register(tmp_path, methods, [{"id": "source"}])
    assert any("cannot have Planned max_authority" in e for e in validate(tmp_path))


def test_pretrained_context_requires_learned_and_not_safety_related(tmp_path: Path) -> None:
    # Invariant 3.
    methods = [_method(i) for i in range(40)]
    methods[0]["data_availability"] = "pretrained-plus-context"  # method_class is deterministic
    _write_register(tmp_path, methods, [{"id": "source"}])
    assert any("pretrained-plus-context requires method_class 'learned'" in e for e in validate(tmp_path))


def test_canonical_register_satisfies_classification_invariants() -> None:
    # The real 42-row register must pass every 50.13 rule (regression guard on the backfill).
    source = Path("control-standards/rag/design_framework/ai_integration")
    assert validate(source) == []
