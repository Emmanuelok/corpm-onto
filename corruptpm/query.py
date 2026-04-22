from __future__ import annotations

from pathlib import Path
from typing import Iterable

from rdflib import Graph, Literal, URIRef
from rdflib.query import Result

from corruptpm.config import load_config
from corruptpm.loader import load_project_graph


def resolve_query_path(query_path: str | Path, root: Path | None = None) -> Path:
    path = Path(query_path)
    if path.is_absolute():
        return path
    config = load_config(root)
    direct = (config.paths.root / path).resolve()
    if direct.exists():
        return direct
    return (config.paths.queries_dir / path).resolve()


def load_query_text(query_path: str | Path, root: Path | None = None) -> str:
    resolved = resolve_query_path(query_path, root=root)
    return resolved.read_text(encoding="utf-8")


def run_query(
    query_path: str | Path,
    *,
    root: Path | None = None,
    include_examples: bool = True,
    materialize_rdfs: bool = False,
) -> Result:
    graph = load_project_graph(root=root, include_examples=include_examples, materialize_rdfs=materialize_rdfs)
    query_text = load_query_text(query_path, root=root)
    return graph.query(query_text)


def _term_to_text(term: object) -> str:
    if term is None:
        return ""
    if isinstance(term, URIRef):
        return str(term)
    if isinstance(term, Literal):
        return str(term)
    return str(term)


def result_to_rows(result: Result) -> tuple[list[str], list[list[str]]]:
    headers = [str(item) for item in result.vars]
    rows = [[_term_to_text(cell) for cell in row] for row in result]
    return headers, rows


def render_table(headers: Iterable[str], rows: Iterable[Iterable[str]]) -> str:
    headers = list(headers)
    rows = [list(row) for row in rows]
    if not headers:
        return ""
    widths = [len(header) for header in headers]
    for row in rows:
        for index, cell in enumerate(row):
            widths[index] = max(widths[index], len(cell))
    lines = [
        " | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)),
        "-+-".join("-" * width for width in widths),
    ]
    for row in rows:
        lines.append(" | ".join(cell.ljust(widths[index]) for index, cell in enumerate(row)))
    return "\n".join(lines)

