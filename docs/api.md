# API

## CLI

The `corruptpm` CLI supports:

- `corruptpm validate`
- `corruptpm query <query-file>`
- `corruptpm list-classes`
- `corruptpm list-properties`
- `corruptpm export --format jsonld`
- `corruptpm visualize`
- `corruptpm catalog`
- `corruptpm generate-construct <yaml-file>`

## Python package

Key modules:

- `corruptpm/config.py`
- `corruptpm/loader.py`
- `corruptpm/validate.py`
- `corruptpm/query.py`
- `corruptpm/export.py`
- `corruptpm/generator.py`

Typical usage:

```python
from corruptpm.loader import load_project_graph
from corruptpm.validate import validate_project

graph = load_project_graph(include_examples=True)
result = validate_project(include_examples=True)
print(result.conforms)
```
