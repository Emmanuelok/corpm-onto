from __future__ import annotations

from pathlib import Path

import click

from corruptpm.config import load_config
from corruptpm.export import (
    generate_construct_catalog_markdown,
    generate_mermaid_overview,
    list_named_classes,
    list_properties,
    serialize_graph,
)
from corruptpm.generator import generate_construct_from_yaml
from corruptpm.loader import load_project_graph
from corruptpm.query import render_table, result_to_rows, run_query
from corruptpm.validate import validate_project


@click.group()
def main() -> None:
    """CLI for the corruptpm ontology project."""


@main.command()
@click.option("--no-examples", is_flag=True, help="Validate the ontology without loading example data.")
def validate(no_examples: bool) -> None:
    """Run SHACL validation."""
    result = validate_project(include_examples=not no_examples)
    click.echo(result.report_text.strip())
    if not result.conforms:
        raise SystemExit(1)


@main.command()
@click.argument("query_path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option("--no-examples", is_flag=True, help="Run the query against ontology only.")
def query(query_path: Path, no_examples: bool) -> None:
    """Run a SPARQL query file."""
    result = run_query(query_path, include_examples=not no_examples)
    headers, rows = result_to_rows(result)
    click.echo(render_table(headers, rows))


@main.command("list-classes")
def list_classes_command() -> None:
    """List named OWL classes."""
    graph = load_project_graph(include_examples=False)
    for uri in list_named_classes(graph):
        click.echo(str(uri))


@main.command("list-properties")
@click.option("--kind", type=click.Choice(["all", "object", "data"]), default="all")
def list_properties_command(kind: str) -> None:
    """List ontology properties."""
    graph = load_project_graph(include_examples=False)
    for uri in list_properties(graph, kind=kind):
        click.echo(str(uri))


@main.command()
@click.option("--format", "output_format", type=click.Choice(["turtle", "jsonld", "xml"]), default="jsonld")
@click.option("--output", type=click.Path(dir_okay=False, path_type=Path))
@click.option("--no-examples", is_flag=True, help="Export the ontology without example data.")
def export(output_format: str, output: Path | None, no_examples: bool) -> None:
    """Serialize the graph."""
    graph = load_project_graph(include_examples=not no_examples)
    payload = serialize_graph(graph, output_format)
    if output:
        output.write_text(payload, encoding="utf-8")
        click.echo(str(output))
        return
    click.echo(payload)


@main.command()
@click.option("--output", type=click.Path(dir_okay=False, path_type=Path))
def visualize(output: Path | None) -> None:
    """Generate a Mermaid overview."""
    config = load_config()
    graph = load_project_graph(include_examples=False)
    content = generate_mermaid_overview(graph)
    target = output or config.paths.visualization_output
    target.write_text(content, encoding="utf-8")
    click.echo(str(target))


@main.command()
@click.option("--output", type=click.Path(dir_okay=False, path_type=Path))
def catalog(output: Path | None) -> None:
    """Generate the construct catalog."""
    config = load_config()
    graph = load_project_graph(include_examples=False)
    content = generate_construct_catalog_markdown(graph)
    target = output or config.paths.catalog_output
    target.write_text(content, encoding="utf-8")
    click.echo(str(target))


@main.command("generate-construct")
@click.argument("yaml_path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option("--output", type=click.Path(dir_okay=False, path_type=Path))
def generate_construct_command(yaml_path: Path, output: Path | None) -> None:
    """Generate Turtle from a YAML construct template."""
    _, ttl = generate_construct_from_yaml(yaml_path, output_path=output)
    if output:
        click.echo(str(output))
        return
    click.echo(ttl)

