# Extension Guide

## Low-friction YAML workflow

Use `data/templates/new-construct-template.yaml` and generate Turtle with:

```bash
python scripts/generate_construct.py data/templates/new-construct-template.yaml
```

The generator is useful for non-programmer contributors who can comfortably edit YAML but not OWL syntax.

## Manual extension workflow

1. Choose the correct module.
2. Add a stable IRI.
3. Add `rdfs:label` and `skos:definition`.
4. Add `skos:scopeNote` when the boundary needs explanation.
5. Add class restrictions that support reuse and querying.
6. Update example data, queries, SHACL, docs, and tests as needed.

## Templates

- `data/templates/new-case-template.ttl`
- `data/templates/new-control-template.ttl`
- `data/templates/new-red-flag-template.ttl`
