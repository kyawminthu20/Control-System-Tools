from pathlib import Path

from tools.validate_corpus_quality import check, check_index


def _corpus(root: Path, name: str, body: str) -> None:
    (root / name).write_text("<!--\nAI_READ_ACCESS: ALLOWED\n-->\n\n" + body, encoding="utf-8")


def test_clean_corpus_passes(tmp_path: Path) -> None:
    _corpus(tmp_path, "ok.md", "The ambient range is 5 C to 40 C. See `PL c` to `PL d`.")
    assert check(tmp_path) == []


def test_flags_conversational_artifact(tmp_path: Path) -> None:
    _corpus(tmp_path, "chat.md", "That completes Clause 17. Would you like me to cover the annexes?")
    errors = check(tmp_path)
    assert len(errors) == 1 and "conversational AI artifact" in errors[0]


def test_flags_empty_placeholder(tmp_path: Path) -> None:
    _corpus(tmp_path, "gap.md", "Operates between ** and ** ( to ) depending on class.")
    errors = check(tmp_path)
    assert any("empty placeholder" in error for error in errors)


def test_readme_is_ignored(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("Would you like me to explain this folder?", encoding="utf-8")
    assert check(tmp_path) == []


def _index_corpus(root: Path, index_body: str, files: dict[str, str]) -> Path:
    """Build a minimal standards_intelligence tree with an _index.yaml and files."""
    si = root / "standards_intelligence"
    for rel, body in files.items():
        target = si / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")
    (si / "_index.yaml").write_text(index_body, encoding="utf-8")
    return root


def test_index_clean_passes(tmp_path: Path) -> None:
    _index_corpus(
        tmp_path,
        'standards:\n  us:\n    - folder: "us/nec"\n'
        'guidance_documents:\n  - file: "reference_models/Guide.md"\n',
        {"us/nec/Article100.md": "content", "reference_models/Guide.md": "content"},
    )
    assert check_index(tmp_path) == []


def test_index_flags_folder_missing_on_disk(tmp_path: Path) -> None:
    _index_corpus(
        tmp_path,
        'standards:\n  us:\n    - folder: "us/nec"\n    - folder: "us/ghost"\n',
        {"us/nec/Article100.md": "content"},
    )
    errors = check_index(tmp_path)
    assert len(errors) == 1 and "us/ghost" in errors[0]


def test_index_flags_unindexed_disk_folder(tmp_path: Path) -> None:
    _index_corpus(
        tmp_path,
        'standards:\n  us:\n    - folder: "us/nec"\n',
        {
            "us/nec/Article100.md": "content",
            "international/offshore/ABS_notes.md": "content",
        },
    )
    errors = check_index(tmp_path)
    assert len(errors) == 1 and "international/offshore" in errors[0]


def test_index_flags_case_mismatched_reference(tmp_path: Path) -> None:
    # Must fail even on case-insensitive filesystems (macOS), where a naive
    # Path.exists() would resolve the wrong-case reference.
    _index_corpus(
        tmp_path,
        'guidance_documents:\n  - file: "reference_models/guide_to_safety.md"\n',
        {"reference_models/Guide_To_Safety.md": "content"},
    )
    errors = check_index(tmp_path)
    assert len(errors) == 1 and "guide_to_safety.md" in errors[0]


def test_index_missing_is_reported(tmp_path: Path) -> None:
    (tmp_path / "standards_intelligence").mkdir()
    errors = check_index(tmp_path)
    assert len(errors) == 1 and "_index.yaml" in errors[0]
