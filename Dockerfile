# Using Python slim image
FROM python:3-slim

# Setting working directory
WORKDIR /app

# Installing SQLite
RUN apt-get update && apt-get install -y sqlite3

# Installing Poetry
RUN python -m pip install poetry

# Setting Poetry environment variables
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_VIRTUAL_ENVS_IN_PROJECT=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PYTHONPATH=/app/src

# Copy dependency files
COPY pyproject.toml poetry.lock poetry.toml* ./

# Install dependencies
RUN poetry install --no-root && rm -rf "$POETRY_CACHE_DIR"

# Copy application code
COPY . /app

# Start an interactive shell
CMD ["bash"]