# corruptpm-ontology

`corruptpm-ontology` is a GitHub-ready ontology project for modelling corruption in project management across the full project lifecycle, with particular attention to construction, infrastructure, engineering, procurement, and AEC environments.

The repository is designed for researchers, anti-corruption practitioners, project controls teams, auditors, knowledge graph developers, public procurement specialists, and maintainers who need more than a static taxonomy. It combines a modular OWL/RDF ontology, SHACL validation, SPARQL competency questions, synthetic examples, and a Python CLI so the model can be loaded, queried, validated, extended, and reused in real workflows.

## Purpose

In this ontology, corruption in project management is modelled as an event-centred network:

`actor -> role -> vulnerability/opportunity -> corrupt act -> phase/stage/process affected -> impact -> detection/control/response`

This makes it possible to analyse corruption patterns as connected project phenomena rather than as isolated labels.

## Scope

The ontology covers:

- project lifecycle phases
- contractual and procurement stages
- actors and roles
- corrupt acts
- causes, vulnerabilities, and risk factors
- red flags and indicators
- anti-corruption controls and barriers
- impacts, evidence, sanctions, and case studies

The current release is especially detailed for public procurement, infrastructure delivery, engineering, construction, supervision, variation orders, payment certification, and inspection risk. The model remains general enough to reuse in other project management domains.

## Provisional namespace

The default base IRI is:

`https://w3id.org/corruptpm/`

This is provisional unless the project owner configures a permanent redirect. Namespace settings live in [corruptpm.toml](corruptpm.toml). The shipped ontology files use the provisional namespace; if the namespace changes later, update the config and regenerate new extension content with the provided tooling before publishing a revised release.

## Repository structure

```text
corruptpm-ontology/
  corruptpm/                Python package and CLI
  ontology/                 Modular OWL ontology in Turtle
  shapes/                   SHACL validation shapes
  data/examples/            Synthetic example graphs
  data/templates/           Templates for extending the model
  queries/                  SPARQL competency-question queries
  docs/                     User and maintainer documentation
  scripts/                  Utility scripts
  tests/                    Pytest suite
  .github/workflows/        GitHub Actions CI
```

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev,docs]"
```

## Quick start

Validate the ontology and synthetic data:

```bash
corruptpm validate
```

Run a competency question:

```bash
corruptpm query queries/cq01_corruption_risks_by_phase.sparql
```

List ontology classes:

```bash
corruptpm list-classes
```

Export the graph:

```bash
corruptpm export --format jsonld --output build/corruptpm.jsonld
```

Generate a construct catalog:

```bash
corruptpm catalog
```

Generate a Mermaid overview:

```bash
corruptpm visualize
```

## Validation workflow

The validation flow combines:

- ontology module loading through [ontology/corruptpm-master.ttl](ontology/corruptpm-master.ttl)
- SHACL rules in [shapes/corruptpm-shapes.ttl](shapes/corruptpm-shapes.ttl)
- synthetic example data in [data/examples](data/examples)

`corruptpm validate` exits with a non-zero status when validation fails.

## Running competency questions

The [queries](queries) directory contains runnable SPARQL files covering lifecycle risks, procurement corruption, controls, barriers, oversight roles, digital traceability, land acquisition risk, and synthetic case discovery.

Example:

```bash
corruptpm query queries/cq18_red_flags_for_bid_rigging.sparql
```

## Extending the ontology

To add a new construct through YAML:

1. Copy [data/templates/new-construct-template.yaml](data/templates/new-construct-template.yaml).
2. Fill in the ID, type, definition, broader concept, linked phases, stages, red flags, and controls.
3. Generate Turtle:

```bash
python scripts/generate_construct.py data/templates/new-construct-template.yaml
```

To add a new construct manually:

1. Choose the correct ontology module in [ontology](ontology).
2. Add the class with `rdfs:label`, `skos:definition`, and a useful `skos:scopeNote` when needed.
3. Update SHACL if new required constraints are introduced.
4. Add or update example data, queries, and tests.

## Adding a new case

1. Start from [data/templates/new-case-template.ttl](data/templates/new-case-template.ttl).
2. Keep unsourced cases explicitly marked as synthetic.
3. Ensure the case includes `caseName`, `description`, at least one corruption event, at least one corrupt act, one phase, one actor, and one impact.
4. Run validation and tests.

## Documentation

Project documentation lives in [docs](docs) and covers architecture, lifecycle modelling, competency questions, extension workflows, validation, and API usage.

The documentation site is deployable on Vercel with the checked-in [vercel.json](vercel.json). Deployment details and required build settings are documented in [docs/deployment.md](docs/deployment.md).

## Citation

Use the metadata in [CITATION.cff](CITATION.cff). A minimal citation format is also described there.

## Contributing

Contribution guidance is in [CONTRIBUTING.md](CONTRIBUTING.md). Please also read [AGENTS.md](AGENTS.md) before submitting automated edits.

## License

This project is licensed under Apache-2.0. See [LICENSE](LICENSE).

## Ethical use

This repository is intended for research, education, analytics, governance design, and anti-corruption practice. It must not be used to present unsourced allegations as fact. Synthetic cases in this repository are explicitly synthetic and must remain so unless reliable sources are added and reviewed through a documented contribution process.
