from corruptpm.export import generate_mermaid_overview
from corruptpm.loader import load_project_graph
from corruptpm.config import load_config


def main() -> None:
    config = load_config()
    graph = load_project_graph(include_examples=False)
    config.paths.visualization_output.write_text(generate_mermaid_overview(graph), encoding="utf-8")
    print(config.paths.visualization_output)


if __name__ == "__main__":
    main()

