from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from pyshacl import validate as shacl_validate
from rdflib import Graph

from corruptpm.loader import load_ontology_graph, load_project_graph, load_shapes_graph


@dataclass(frozen=True)
class ValidationResult:
    conforms: bool
    report_text: str
    report_graph: Graph


def validate_project(root: Path | None = None, *, include_examples: bool = True) -> ValidationResult:
    ontology_graph = load_ontology_graph(root=root)
    data_graph = load_project_graph(root=root, include_examples=include_examples)
    shapes_graph = load_shapes_graph(root=root)
    conforms, report_graph, report_text = shacl_validate(
        data_graph=data_graph,
        shacl_graph=shapes_graph,
        ont_graph=ontology_graph,
        inference="rdfs",
        advanced=True,
        meta_shacl=False,
        debug=False,
    )
    return ValidationResult(conforms=bool(conforms), report_text=str(report_text), report_graph=report_graph)

