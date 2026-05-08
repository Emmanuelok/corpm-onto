# Deployment

The documentation site is a static MkDocs site and can be deployed on Vercel.
The repository includes a root-level `vercel.json` that selects Vercel's `Other` framework preset, installs the Python documentation dependencies, builds the site with strict MkDocs validation, and publishes the generated `site` directory. Because some Vercel projects continue to apply the Python preset when a repository contains `pyproject.toml`, the repository also declares `tool.vercel.entrypoint = "app.py"` and includes a small WSGI fallback that serves the built static site if Vercel insists on using the Python runtime.

## Local pre-deployment checks

Run these checks before publishing a new deployment:

```bash
pytest
python scripts/validate_all.py
python -m mkdocs build --strict --site-dir site
```

The validation script loads the ontology, SHACL shapes, and synthetic examples from the repository root so it works when called directly from the command line or from automation.

## Vercel settings

When importing the project into Vercel, use the repository root as the project root. The checked-in Vercel configuration supplies the deployment preset and commands:

- Framework preset: `Other` (`"framework": null` in `vercel.json`)
- Install command: `python -m pip install --upgrade pip && python -m pip install -e '.[docs]'`
- Build command: `python -m mkdocs build --strict --site-dir site`
- Output directory: `site`
- Python fallback entrypoint: `app.py` via `tool.vercel.entrypoint` in `pyproject.toml`

## CLI deployment

If the Vercel CLI is available and authenticated, deploy with:

```bash
vercel --prod
```

If the CLI is not linked yet, run `vercel link` first and select the existing Vercel project or create a new one.


## Troubleshooting `No python entrypoint found`

If Vercel reports `No python entrypoint found`, it is treating the repository as a Python web application instead of only a static documentation site. The repository now includes two protections against this: `vercel.json` selects the `Other` framework preset, and `pyproject.toml` declares `tool.vercel.entrypoint = "app.py"`. If the error persists, confirm the deployment is using the latest commit and that Vercel project settings do not override the build command, output directory, or root directory.
