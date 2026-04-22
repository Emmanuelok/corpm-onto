from __future__ import annotations

from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import url2pathname

from owlrl import DeductiveClosure, RDFS_Semantics
from rdflib import Graph
from rdflib.namespace import OWL

from corruptpm.config import load_config


def _guess_format(path: Path) -> str:
    if path.suffix.lower() in {".ttl", ".turtle"}:
        return "turtle"
    if path.suffix.lower() in {".jsonld", ".json"}:
        return "json-ld"
    return "xml"


def _resolve_import(current_file: Path, imported_iri: str) -> Path | None:
    resolved = urljoin(current_file.resolve().as_uri(), imported_iri)
    parsed = urlparse(resolved)
    if parsed.scheme != "file":
        return None
    return Path(url2pathname(parsed.path)).resolve()


def _load_with_imports(graph: Graph, path: Path, visited: set[Path]) -> None:
    resolved = path.resolve()
    if resolved in visited:
        return
    temp = Graph()
    temp.parse(resolved.as_posix(), format=_guess_format(resolved))
    graph += temp
    visited.add(resolved)
    for imported in temp.objects(None, OWL.imports):
        imported_path = _resolve_import(resolved, str(imported))
        if imported_path and imported_path.exists():
            _load_with_imports(graph, imported_path, visited)


def load_ontology_graph(root: Path | None = None, *, materialize_rdfs: bool = False) -> Graph:
    config = load_config(root)
    graph = Graph()
    graph.bind(config.namespace.prefix, config.namespace.base_iri)
    _load_with_imports(graph, config.paths.master_ontology, set())
    if materialize_rdfs:
        DeductiveClosure(RDFS_Semantics).expand(graph)
    return graph


def load_shapes_graph(root: Path | None = None) -> Graph:
    config = load_config(root)
    graph = Graph()
    graph.parse(config.paths.shapes.as_posix(), format=_guess_format(config.paths.shapes))
    return graph


def load_example_graph(root: Path | None = None) -> Graph:
    config = load_config(root)
    graph = Graph()
    for path in sorted(config.paths.examples_dir.glob("*.ttl")):
        graph.parse(path.as_posix(), format=_guess_format(path))
    return graph


def load_project_graph(
    root: Path | None = None,
    *,
    include_examples: bool = True,
    materialize_rdfs: bool = False,
) -> Graph:
    graph = load_ontology_graph(root=root, materialize_rdfs=False)
    if include_examples:
        graph += load_example_graph(root=root)
    if materialize_rdfs:
        DeductiveClosure(RDFS_Semantics).expand(graph)
    return graph


def load_ontology_module_paths(root: Path | None = None) -> list[Path]:
    config = load_config(root)
    ontology_dir = config.paths.master_ontology.parent
    return sorted(path for path in ontology_dir.glob("*.ttl") if path.name != config.paths.master_ontology.name)

