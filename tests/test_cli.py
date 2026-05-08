import runpy
import subprocess
import sys

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


def test_validate_all_script_works_when_executed_directly() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_all.py")],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Conforms: True" in result.stdout
