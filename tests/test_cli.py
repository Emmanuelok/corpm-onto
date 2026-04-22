import runpy

from click.testing import CliRunner

from corruptpm.cli import main
from tests.conftest import ROOT


def test_cli_validate_command_works(monkeypatch) -> None:
    runner = CliRunner()
    monkeypatch.chdir(ROOT)
    result = runner.invoke(main, ["validate"])
    assert result.exit_code == 0, result.output


def test_construct_catalog_generation_script_works(monkeypatch) -> None:
    monkeypatch.chdir(ROOT)
    runpy.run_path((ROOT / "scripts" / "generate_construct_catalog.py").as_posix(), run_name="__main__")
    catalog_path = ROOT / "docs" / "construct-catalog.md"
    assert catalog_path.exists()
    assert "# Construct Catalog" in catalog_path.read_text(encoding="utf-8")

