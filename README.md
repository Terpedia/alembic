# Alembic

Google Vertex AI interface for [Terpedia](https://terpedia.com). Use Gemini and other Vertex models for Terpedia workflows (chat, generation, embeddings).

## Prerequisites

- Python 3.10+
- [Google Cloud project](https://console.cloud.google.com/) with Vertex AI API enabled and billing enabled
- [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials) (e.g. `gcloud auth application-default login`)

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Configure via environment variables (or `.env`):

| Variable | Description |
|----------|-------------|
| `GOOGLE_CLOUD_PROJECT` | Your GCP project ID |
| `VERTEX_LOCATION` | Region (default: `us-central1`) |

## Usage

### Python

```python
from alembic import VertexClient

client = VertexClient()
response = client.generate("Explain terpenes in cannabis.")
print(response)
```

### CLI

```bash
python -m alembic "Your prompt here"
```

## Development

```bash
pip install -e .
python -m alembic "Test prompt"
```

## License

Proprietary – Terpedia.
