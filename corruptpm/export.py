from __future__ import annotations

from pathlib import Path

from rdflib import Graph, URIRef
from rdflib.namespace import RDF, RDFS, OWL, SKOS

from corruptpm.config import load_config


TOP_LEVEL_CONSTRUCTS = [
    "CorruptionEvent",
    "CorruptAct",
    "Project",
    "ProjectPhase",
    "ContractStage",
    "ProjectActor",
    "ActorRole",
    "Cause",
    "Vulnerability",
    "RiskFactor",
    "RedFlag",
    "Impact",
    "AntiCorruptionControl",
    "ControlObjective",
    "Barrier",
    "Indicator",
    "Evidence",
    "CaseStudy",
    "Jurisdiction",
    "GovernanceInstrument",
    "Sanction",
    "DetectionMechanism",
    "ReportingMechanism",
    "ProcurementMethod",
    "AssetOrResource",
    "DecisionPoint",
    "ProjectManagementProcess",
]


def serialize_graph(graph: Graph, output_format: str) -> str:
    formats = {
        "turtle": "turtle",
        "ttl": "turtle",
        "jsonld": "json-ld",
        "json-ld": "json-ld",
        "xml": "xml",
    }
    selected = formats[output_format.lower()]
    return graph.serialize(format=selected)


def write_serialization(graph: Graph, output_path: Path, output_format: str) -> Path:
    payload = serialize_graph(graph, output_format)
    output_path.write_text(payload, encoding="utf-8")
    return output_path


def _local_name(namespace: str, uri: URIRef) -> str:
    text = str(uri)
    if text.startswith(namespace):
        return text.removeprefix(namespace)
    return text


def generate_construct_catalog_markdown(graph: Graph, root: Path | None = None) -> str:
    config = load_config(root)
    namespace = config.namespace.base_iri
    lines = [
        "# Construct Catalog",
        "",
        "This catalog is generated from the ontology modules and groups direct subclasses under the main construct areas.",
        "",
    ]
    for construct_name in TOP_LEVEL_CONSTRUCTS:
        construct_uri = URIRef(f"{namespace}{construct_name}")
        label = graph.value(construct_uri, RDFS.label) or construct_name
        definition = graph.value(construct_uri, SKOS.definition) or ""
        lines.extend([f"## {label}", "", str(definition), ""])
        subclasses = sorted(
            {
                subclass
                for subclass in graph.subjects(RDFS.subClassOf, construct_uri)
                if isinstance(subclass, URIRef)
            },
            key=lambda item: str(graph.value(item, RDFS.label) or _local_name(namespace, item)),
        )
        if not subclasses:
            lines.extend(["No direct subclasses are currently declared in the published modules.", ""])
            continue
        for subclass in subclasses:
            subclass_label = graph.value(subclass, RDFS.label) or _local_name(namespace, subclass)
            subclass_definition = graph.value(subclass, SKOS.definition) or ""
            lines.append(f"- **{subclass_label}**: {subclass_definition}")
        lines.append("")
    return "\n".join(lines)


def generate_mermaid_overview(graph: Graph, root: Path | None = None) -> str:
    config = load_config(root)
    namespace = config.namespace.base_iri
    lines = [
        "# Ontology Map",
        "",
        "```mermaid",
        "graph TD",
    ]
    for construct_name in TOP_LEVEL_CONSTRUCTS:
        parent_uri = URIRef(f"{namespace}{construct_name}")
        lines.append(f'  {construct_name}["{construct_name}"]')
        subclasses = sorted(
            {
                child
                for child in graph.subjects(RDFS.subClassOf, parent_uri)
                if isinstance(child, URIRef)
            },
            key=lambda item: str(item),
        )[:8]
        for child in subclasses:
            child_name = _local_name(namespace, child).replace("-", "_")
            label = str(graph.value(child, RDFS.label) or _local_name(namespace, child))
            lines.append(f'  {child_name}["{label}"] --> {construct_name}')
    lines.extend(["```", ""])
    return "\n".join(lines)


def list_named_classes(graph: Graph) -> list[URIRef]:
    return sorted(
        {node for node in graph.subjects(RDF.type, OWL.Class) if isinstance(node, URIRef)},
        key=str,
    )


def list_properties(graph: Graph, *, kind: str = "all") -> list[URIRef]:
    allowed_types = {
        "all": {OWL.ObjectProperty, OWL.DatatypeProperty},
        "object": {OWL.ObjectProperty},
        "data": {OWL.DatatypeProperty},
    }[kind]
    nodes: set[URIRef] = set()
    for property_type in allowed_types:
        nodes.update(node for node in graph.subjects(RDF.type, property_type) if isinstance(node, URIRef))
    return sorted(nodes, key=str)

