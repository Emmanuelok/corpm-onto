# Validation Guide

Validation is performed with `pyshacl` using `shapes/corruptpm-shapes.ttl`.

Current checks include:

- every corruption event has at least one act, phase, actor, and impact
- ontology classes carry labels and definitions
- every project actor instance has a label
- synthetic cases contain `caseName` and `description`
- indicators used in instance data carry a `confidenceScore`
- score properties remain within documented numeric ranges

Run:

```bash
corruptpm validate
python scripts/validate_all.py
```
