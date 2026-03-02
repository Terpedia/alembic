# Alembic

Use **GCP Vertex AI Workbench (Vertex notebooks)** for [Terpedia](https://terpedia.com). This repo provides the Terpedia-facing client and starter material to run Jupyter notebooks on Vertex with access to Gemini and other Vertex AI services.

## What’s in this repo

- **`alembic`** – Python package to call Vertex AI (Gemini, etc.) from code or from inside a Vertex notebook.
- **`notebooks/`** – Starter notebooks and instructions for running analyses in Vertex AI Workbench.

## Prerequisites

- A [Google Cloud project](https://console.cloud.google.com/) with:
  - **Vertex AI API** and **Notebooks API** enabled  
  - Billing enabled  
- Permissions to create and use Vertex AI Workbench instances (e.g. Notebooks Admin).

## Using Vertex notebooks (Workbench)

1. **Create a notebook instance**  
   - [Console](https://console.cloud.google.com/vertex-ai/workbench): Vertex AI → Workbench → **Create instance**.  
   - Or with gcloud (set `PROJECT` and `LOCATION`, e.g. `us-central1`):
     ```bash
     gcloud notebooks instances create terpedia-notebook \
       --project=$PROJECT \
       --location=$LOCATION \
       --machine-type=n1-standard-4 \
       --vm-image-project=deeplearning-platform-release \
       --vm-image-family=common-cpu-notebooks-debian-12
     ```
2. **Open Jupyter**  
   In the console, click the instance → **Open JupyterLab** (or the link from the gcloud output).
3. **Use this repo in the notebook**  
   In a terminal inside JupyterLab:
   ```bash
   git clone https://github.com/Terpedia/alembic.git
   cd alembic
   pip install -r requirements.txt
   pip install -e .
   ```
   Then in a notebook, set your project (and optionally region) and use the client:
   ```python
   import os
   os.environ["GOOGLE_CLOUD_PROJECT"] = "your-gcp-project"
   # os.environ["VERTEX_LOCATION"] = "us-central1"  # optional

   from alembic import VertexClient
   client = VertexClient()
   print(client.generate("Explain terpenes in cannabis."))
   ```

In a Vertex notebook, Application Default Credentials are usually already set, so you typically only need to set `GOOGLE_CLOUD_PROJECT` (and optionally `VERTEX_LOCATION`).

## Using locally (optional)

You can also run the same client on your machine (e.g. for scripts or local notebooks):

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

Set project and auth:

```bash
export GOOGLE_CLOUD_PROJECT=your-gcp-project
gcloud auth application-default login
```

**CLI:**

```bash
python -m alembic "Your prompt here"
```

**Python:**

```python
from alembic import VertexClient
client = VertexClient()
response = client.generate("Explain terpenes in cannabis.")
print(response)
```

## Configuration

| Variable | Description |
|----------|-------------|
| `GOOGLE_CLOUD_PROJECT` | GCP project ID (required) |
| `VERTEX_LOCATION` | Vertex region (default: `us-central1`) |
| `VERTEX_MODEL` | Model ID (default: `gemini-1.5-flash`) |

## License

Proprietary – Terpedia.
