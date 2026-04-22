from corruptpm.export import generate_construct_catalog_markdown
from corruptpm.loader import load_project_graph
from corruptpm.config import load_config


def main() -> None:
    config = load_config()
    graph = load_project_graph(include_examples=False)
    config.paths.catalog_output.write_text(generate_construct_catalog_markdown(graph), encoding="utf-8")
    print(config.paths.catalog_output)


if __name__ == "__main__":
    main()

