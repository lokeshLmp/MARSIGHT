# MARSIGHT

AI-powered planetary terrain intelligence and mission-planning research platform using open planetary data and Python-based scientific computing.

## Current deployment

The repository currently deploys a FastAPI foundation. The terrain-processing, NASA data-ingestion, and interactive frontend layers described in the architecture are still under development; this API does not claim those features are operational.

### Run locally

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open:
- API root: http://127.0.0.1:8000/
- Health: http://127.0.0.1:8000/health
- Interactive API docs: http://127.0.0.1:8000/docs

## Deploy on Render

A `render.yaml` Blueprint is included. In Render, choose **New + → Blueprint**, connect this repository, and deploy the `marsight-api` service. Render will install the Python requirements and start the FastAPI application.

## Planned architecture

NASA data → data processing → terrain intelligence → FastAPI → interactive frontend.

See [system design](docs/architecture/system-design.md), [NASA dataset research](docs/data-sources/nasa-datasets.md), and the [development plan](docs/development-plan.md).

## Safety and limitations

MARSIGHT is a research and educational decision-support prototype. It is not certified for astronaut navigation, operational mission planning, or mission safety. Candidate datasets and scientific methods must be verified before implementation.
