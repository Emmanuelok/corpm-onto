# Contributing

Thanks for contributing to `corruptpm-ontology`.

## Before you start

Read [AGENTS.md](AGENTS.md) and [README.md](README.md). This repository treats ontology consistency, validation, and provenance as first-class maintenance concerns.

## Proposing a new class

1. Choose the correct module under [ontology](ontology).
2. Reuse an existing concept if one already captures the meaning.
3. Add `rdfs:label` and `skos:definition`.
4. Add `skos:scopeNote` when the boundary or intended usage is likely to be misunderstood.
5. Add meaningful relationships such as linked phases, controls, risk factors, or impacts.
6. Update docs, queries, and tests if the new class changes project behaviour or user-facing outputs.

## Proposing a new corrupt act

1. Start from the closest parent under [ontology/corruptpm-corrupt-acts.ttl](ontology/corruptpm-corrupt-acts.ttl).
2. Link the act to phases, stages, red flags, controls, impacts, and decision points where appropriate.
3. Avoid duplicate or overly vague act names.
4. Add or update a query or example that shows why the new class matters.

## Proposing a new red flag

1. Add the class in [ontology/corruptpm-indicators.ttl](ontology/corruptpm-indicators.ttl).
2. Explain what the signal suggests and what it does not prove.
3. Link it to at least one risk factor, act, or lifecycle context when you have a defensible modelling reason.
4. Update example data or queries if the red flag supports a competency question.

## Proposing a new control

1. Add the class in [ontology/corruptpm-controls.ttl](ontology/corruptpm-controls.ttl) or an extension file.
2. State whether the control is preventive, detective, corrective, punitive, digital, governance, contractual, or another category.
3. Link it to one or more control objectives and barriers where appropriate.
4. Update SHACL if the new control introduces required metadata or structural expectations.

## Adding a synthetic case

1. Copy [data/templates/new-case-template.ttl](data/templates/new-case-template.ttl).
2. Keep the case explicitly synthetic in the label, case name, or scope note.
3. Include `caseName`, `description`, at least one corruption event, one corrupt act, one phase, one actor, and one impact.
4. Add `confidenceScore` values for indicators and red flags used in instance data.
5. Run validation and tests before opening the pull request.

## Adding a real case with citations

1. Do not add a real case unless you have reliable source references.
2. Add provenance using `cpm:sourceReference`.
3. Avoid defamatory phrasing and do not overstate certainty.
4. Clearly distinguish documented facts, allegations, findings, and inferred analytical links.
5. Expect maintainers to review real-case additions with extra care.

## Running validation

```bash
corruptpm validate
python scripts/validate_all.py
pytest
```

## Opening a pull request

1. Explain what changed and why.
2. Mention affected modules, shapes, queries, examples, and docs.
3. Confirm validation and tests passed.
4. Call out any modelling assumptions or unresolved questions.
