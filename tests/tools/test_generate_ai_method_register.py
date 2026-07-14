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
        "does": "Estimates a state.", "layer": "edge", "deterministic_alternative": "Observer",
        "justified_when": "Validated evidence supports it.", "poor_fit_when": "Inputs are unobservable.",
        "data_requirement": "Representative labelled data.", "max_authority": 2,
        "authority_basis": "Conservative advisory ceiling.", "validation_required": "Held-out tests.",
        "failure_modes": "Drift.", "safety_independence": "Independent protection remains effective.",
        "evidence_strength": "engineering judgement", "maturity": "piloted", "sources": ["source"]
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
