from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os
import tomllib


CONFIG_FILE_NAME = "corruptpm.toml"


@dataclass(frozen=True)
class NamespaceConfig:
    base_iri: str
    prefix: str
    provisional: bool


@dataclass(frozen=True)
class PathConfig:
    root: Path
    master_ontology: Path
    shapes: Path
    examples_dir: Path
    queries_dir: Path
    catalog_output: Path
    visualization_output: Path


@dataclass(frozen=True)
class ValidationConfig:
    risk_score_min: float
    risk_score_max: float
    normalized_score_min: float
    normalized_score_max: float


@dataclass(frozen=True)
class ProjectConfig:
    namespace: NamespaceConfig
    paths: PathConfig
    validation: ValidationConfig


def find_repo_root(start: Path | None = None) -> Path:
    env_root = os.environ.get("CORRUPTPM_ROOT")
    if env_root:
        root = Path(env_root).expanduser().resolve()
        if (root / CONFIG_FILE_NAME).exists():
            return root
    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / CONFIG_FILE_NAME).exists():
            return candidate
    raise FileNotFoundError(f"Could not locate {CONFIG_FILE_NAME} from {current}")


def load_config(root: Path | None = None) -> ProjectConfig:
    repo_root = find_repo_root(root)
    with (repo_root / CONFIG_FILE_NAME).open("rb") as handle:
        raw = tomllib.load(handle)
    namespace = NamespaceConfig(**raw["namespace"])
    paths = PathConfig(
        root=repo_root,
        master_ontology=(repo_root / raw["paths"]["master_ontology"]).resolve(),
        shapes=(repo_root / raw["paths"]["shapes"]).resolve(),
        examples_dir=(repo_root / raw["paths"]["examples_dir"]).resolve(),
        queries_dir=(repo_root / raw["paths"]["queries_dir"]).resolve(),
        catalog_output=(repo_root / raw["paths"]["catalog_output"]).resolve(),
        visualization_output=(repo_root / raw["paths"]["visualization_output"]).resolve(),
    )
    validation = ValidationConfig(**raw["validation"])
    return ProjectConfig(namespace=namespace, paths=paths, validation=validation)

