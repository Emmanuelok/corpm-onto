import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_vercel_config_uses_static_mkdocs_build() -> None:
    config = json.loads((ROOT / "vercel.json").read_text(encoding="utf-8"))

    assert config["framework"] is None
    assert "mkdocs build --strict" in config["buildCommand"]
    assert config["outputDirectory"] == "site"
