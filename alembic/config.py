"""Configuration from environment."""

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    _env = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(_env)
except ImportError:
    pass


def get_project_id() -> str:
    value = os.environ.get("GOOGLE_CLOUD_PROJECT")
    if not value:
        raise ValueError(
            "Set GOOGLE_CLOUD_PROJECT (or run gcloud config set project YOUR_PROJECT)"
        )
    return value


def get_location() -> str:
    return os.environ.get("VERTEX_LOCATION", "us-central1")


def get_model_id() -> str:
    return os.environ.get("VERTEX_MODEL", "gemini-1.5-flash")
