"""Sanity check: is my token valid, how much rate limit do I have,
and what does one workflow-run record look like?

Usage:  python scripts/check_github.py
"""
import json
import sys

import requests

from ci_predictor.config import get_github_token

API = "https://api.github.com"
REPO = "pytest-dev/pytest"


def main() -> None:
    headers = {
        "Authorization": f"Bearer {get_github_token()}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    # 1) Rate limit (this call is free)
    r = requests.get(f"{API}/rate_limit", headers=headers, timeout=30)
    if r.status_code == 401:
        sys.exit("401 Unauthorized: token is wrong or expired. Check your .env file.")
    r.raise_for_status()
    core = r.json()["resources"]["core"]
    print(f"Rate limit: {core['remaining']}/{core['limit']} requests left this hour")

    # 2) One CI workflow run
    r = requests.get(
        f"{API}/repos/{REPO}/actions/runs",
        headers=headers,
        params={"per_page": 1},
        timeout=30,
    )
    r.raise_for_status()
    body = r.json()
    print(f"{REPO}: {body['total_count']} workflow runs reported by GitHub")

    run = body["workflow_runs"][0]
    keep = ["id", "name", "event", "status", "conclusion", "head_sha",
            "run_attempt", "created_at", "updated_at"]
    print(json.dumps({k: run.get(k) for k in keep}, indent=2))


if __name__ == "__main__":
    main()