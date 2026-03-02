# Vertex notebooks for Terpedia

Notebooks in this folder are meant to be run in **GCP Vertex AI Workbench**. See the [main README](../README.md) for:

- How to create a Vertex AI Workbench instance
- How to clone this repo and install `alembic` inside the notebook environment
- Env vars: `GOOGLE_CLOUD_PROJECT`, `VERTEX_LOCATION`, `VERTEX_MODEL`

## Quick start inside a Vertex notebook

1. In JupyterLab, open a terminal and run:
   ```bash
   git clone https://github.com/Terpedia/alembic.git && cd alembic && pip install -r requirements.txt && pip install -e .
   ```
2. In a new notebook:
   ```python
   import os
   os.environ["GOOGLE_CLOUD_PROJECT"] = "your-project-id"
   from alembic import VertexClient
   VertexClient().generate("Explain terpenes.")
   ```

Add new `.ipynb` files here as you build Terpedia workflows (e.g. data prep, model calls, reporting).
