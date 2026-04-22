# AGENTS.md

Instructions for future Codex agents, automated maintainers, and code review agents working in this repository.

## Core maintenance rules

1. Preserve ontology consistency across modules, shapes, queries, examples, docs, and tests.
2. Never add unsupported real-world corruption allegations.
3. Mark unsourced examples as synthetic, and keep synthetic examples clearly synthetic.
4. Always update SHACL shapes when adding new required ontology constraints.
5. Always add or update tests when changing ontology modules, loader logic, validation logic, example data, or CLI behaviour.
6. Always run `pytest` and ontology validation before finalising work.
7. Keep labels, definitions, and scope notes clear, specific, and free of unexplained abbreviations.
8. Use stable IRIs. Avoid renaming existing IRIs without a migration plan and documentation update.
9. Avoid duplicate classes or near-duplicate concepts with overlapping meanings.
10. Maintain the modular structure. Add concepts to the right module rather than turning the master file into a monolith.
11. Keep [README.md](README.md) and docs synchronised with ontology and CLI changes.
12. Treat ontology validation failures as high priority.
13. Treat broken competency queries as high priority.
14. In reviews, explicitly check for missing labels, missing definitions, inconsistent ranges or domains, invalid Turtle syntax, unsupported claims, and failing tests.

## Repository-specific modelling guidance

- Prefer event-centred modelling over flat taxonomies.
- Keep the actor -> role -> vulnerability -> act -> impact -> control chain explicit where possible.
- Use subclass restrictions to encode reusable domain knowledge that competency queries can inspect.
- Keep control categories, barriers, and objectives distinguishable.
- Use `cpm:sourceReference` for provenance and `cpm:description` for explanatory case text.
- When adding instance data, give every actor a label and every indicator used in instance data a `confidenceScore`.

## Extension workflow

- Use [data/templates/new-construct-template.yaml](data/templates/new-construct-template.yaml) and [scripts/generate_construct.py](scripts/generate_construct.py) for low-friction extensions.
- If a new construct changes the competency-question surface, add or update a SPARQL query.
- If a new construct changes required metadata, update SHACL and tests in the same change.
