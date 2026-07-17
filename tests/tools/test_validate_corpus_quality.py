from pathlib import Path

from tools.validate_corpus_quality import check


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
