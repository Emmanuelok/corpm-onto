# Getting Started

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev,docs]"
```

## Validate

```bash
corruptpm validate
```

## Query

```bash
corruptpm query queries/cq01_corruption_risks_by_phase.sparql
```

## Export

```bash
corruptpm export --format jsonld --output build/corruptpm.jsonld
```

## Generate helper artifacts

```bash
corruptpm catalog
corruptpm visualize
```

