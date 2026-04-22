from rdflib import Graph

from corruptpm.generator import generate_construct_from_yaml
from tests.conftest import ROOT


def test_construct_generator_outputs_parseable_ttl(tmp_path) -> None:
    input_path = ROOT / "data" / "templates" / "new-construct-template.yaml"
    output_path = tmp_path / "generated-construct.ttl"
    _, ttl = generate_construct_from_yaml(input_path, output_path=output_path, root=ROOT)
    assert "VariationOrderManipulation" in ttl
    graph = Graph()
    graph.parse(data=ttl, format="turtle")
    assert len(graph) > 0

