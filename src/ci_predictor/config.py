"""Central place for configuration. Secrets come from environment variables only."""
import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"

load_dotenv(PROJECT_ROOT / ".env")


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(
            f"Missing environment variable {name}. "
            "Copy .env.example to .env and fill it in."
        )
    return value


def get_github_token() -> str:
    return require_env("GITHUB_TOKEN")