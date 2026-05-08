# Deployment

The documentation site is a static MkDocs site and can be deployed on Vercel.
The repository includes a root-level `vercel.json` that selects Vercel's `Other` framework preset, installs the Python documentation dependencies, builds the site with strict MkDocs validation, and publishes the generated `site` directory. Setting the framework preset to `null` is important because this repository has a `pyproject.toml` for its Python CLI package, but the deployed site is static documentation rather than a Python web function.

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

## CLI deployment

If the Vercel CLI is available and authenticated, deploy with:

```bash
vercel --prod
```

If the CLI is not linked yet, run `vercel link` first and select the existing Vercel project or create a new one.


## Troubleshooting `No python entrypoint found`

If Vercel reports `No python entrypoint found`, it is treating the repository as a Python web application instead of a static documentation site. Confirm that the deployment is using the checked-in `vercel.json` and that the project settings do not override the framework preset back to `Python`, `FastAPI`, or `Flask`. The project should use the `Other` framework preset and publish the `site` output directory.
