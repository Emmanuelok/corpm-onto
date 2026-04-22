from corruptpm.loader import load_project_graph
from tests.conftest import ROOT


def test_sparql_queries_run_without_syntax_errors() -> None:
    graph = load_project_graph(root=ROOT, include_examples=True)
    for query_path in sorted((ROOT / "queries").glob("*.sparql")):
        result = graph.query(query_path.read_text(encoding="utf-8"))
        assert result is not None, query_path.name

