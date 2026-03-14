def test_work_dirs_has_converted():
    from tools.fe_study.common import WORK_DIRS
    assert "converted" in WORK_DIRS
    assert WORK_DIRS["converted"] == "_converted"


def test_infer_family_doc():
    from tools.fe_study.common import infer_family
    from pathlib import Path
    assert infer_family(Path("planning/FE_Study/How to/SomePLC.doc")) == "howto_doc"


def test_infer_priority_howto_doc():
    from tools.fe_study.common import infer_priority
    assert infer_priority("howto_doc") == "P2"


def test_convert_doc_to_docx_no_soffice(tmp_path, monkeypatch):
    """Returns None when soffice is not on PATH."""
    import shutil
    from tools.fe_study.common import convert_doc_to_docx
    monkeypatch.setattr(shutil, "which", lambda _: None)
    result = convert_doc_to_docx(tmp_path / "fake.doc", tmp_path / "out")
    assert result is None


def test_convert_doc_to_docx_nonzero_exit(tmp_path, monkeypatch):
    """Returns None when soffice exits non-zero."""
    import shutil, subprocess
    from tools.fe_study.common import convert_doc_to_docx
    monkeypatch.setattr(shutil, "which", lambda _: "/usr/bin/soffice")
    monkeypatch.setattr(
        subprocess, "run",
        lambda *a, **kw: type("R", (), {"returncode": 1})(),
    )
    result = convert_doc_to_docx(tmp_path / "fake.doc", tmp_path / "out")
    assert result is None


def test_convert_doc_to_docx_timeout(tmp_path, monkeypatch):
    """Returns None on TimeoutExpired."""
    import shutil, subprocess
    from tools.fe_study.common import convert_doc_to_docx
    monkeypatch.setattr(shutil, "which", lambda _: "/usr/bin/soffice")
    def raise_timeout(*a, **kw):
        raise subprocess.TimeoutExpired(cmd="soffice", timeout=60)
    monkeypatch.setattr(subprocess, "run", raise_timeout)
    result = convert_doc_to_docx(tmp_path / "fake.doc", tmp_path / "out")
    assert result is None


def test_convert_doc_to_docx_success(tmp_path, monkeypatch):
    """Returns .docx path when conversion succeeds and file exists."""
    import shutil, subprocess
    from tools.fe_study.common import convert_doc_to_docx
    monkeypatch.setattr(shutil, "which", lambda _: "/usr/bin/soffice")
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    docx_path = out_dir / "fake.docx"
    docx_path.touch()
    monkeypatch.setattr(
        subprocess, "run",
        lambda *a, **kw: type("R", (), {"returncode": 0})(),
    )
    result = convert_doc_to_docx(tmp_path / "fake.doc", out_dir)
    assert result == docx_path


def test_converted_docx_path(tmp_path):
    from tools.fe_study.common import converted_docx_path
    source_root = tmp_path / "FE_Study"
    source_path = source_root / "How to" / "PLC Guide.doc"
    result = converted_docx_path(source_root, source_path)
    assert result == source_root / "_converted" / "How to" / "PLC Guide.docx"
