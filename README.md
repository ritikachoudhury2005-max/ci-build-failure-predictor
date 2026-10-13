# CI Build Failure Predictor
Predicts whether a GitHub PR's CI build will fail, at PR-open time.

## Setup
1. `python -m venv .venv`
2. `.venv\Scripts\Activate.ps1`
3. `pip install -e .`
4. Copy `.env.example` to `.env` and add your `GITHUB_TOKEN`