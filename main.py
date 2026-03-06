"""
Entry point for the Problem Understanding Service.

Starts the FastAPI application with structured logging and the evaluate-understanding
endpoint. Run with: uv run python main.py (or uvicorn from project root).
"""

import logging
import sys

from fastapi import FastAPI

from app.config.settings import get_settings
from app.interfaces.api.routes import router as evaluate_router

# ----- Structured logging -----
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Problem Understanding Service",
    description="Agente de compreensão de problemas para plataforma de maratonas de programação",
    version="0.1.0",
)

app.include_router(evaluate_router)


@app.get("/health")
def health() -> dict[str, str]:
    """Health check for load balancers and Docker."""
    return {"status": "ok"}


def main() -> None:
    """Run the API server."""
    settings = get_settings()
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.environment == "development",
    )


if __name__ == "__main__":
    main()
