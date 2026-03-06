# Problem Understanding Service – Dockerfile
# Build: docker build -t problem-understanding-service .
# Run:   docker run -p 8000:8000 --env-file .env problem-understanding-service

FROM python:3.11-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Dependencies first (cache layer)
COPY pyproject.toml ./
RUN uv sync --no-dev --no-install-project

# Application
COPY app/ ./app/
COPY main.py ./

# Non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

ENV PATH="/app/.venv/bin:$PATH" PYTHONPATH="/app"
EXPOSE 8000

CMD ["python", "main.py"]
