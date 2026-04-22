# Ontology Overview

## Architecture

The ontology is modular and centred on `cpm:CorruptionEvent`. Core modules define reusable classes and properties, while specialised modules describe lifecycle phases, contract stages, actors, corrupt acts, controls, indicators, impacts, and cases.

## Design principles

- Event-centred rather than taxonomy-only
- Reusable across project management domains
- Specialised for public procurement, infrastructure, construction, engineering, and AEC contexts
- Extensible through templates and generated Turtle snippets
- Compatible with knowledge graph workflows and Protégé-style OWL tooling

## Main modules

- `ontology/corruptpm-core.ttl`
- `ontology/corruptpm-lifecycle.ttl`
- `ontology/corruptpm-contractual-cycle.ttl`
- `ontology/corruptpm-actors.ttl`
- `ontology/corruptpm-corrupt-acts.ttl`
- `ontology/corruptpm-controls.ttl`
- `ontology/corruptpm-indicators.ttl`
- `ontology/corruptpm-cases.ttl`

## Corruption-event model

The key modelling pattern links:

`CorruptionEvent -> CorruptAct -> ProjectPhase/ContractStage -> Impact`

and augments that chain with:

- actors and roles
- causes and vulnerabilities
- red flags and indicators
- controls and barriers
- evidence and case studies
