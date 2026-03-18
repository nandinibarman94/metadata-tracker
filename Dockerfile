# Using Python slim image
FROM python:3.14-slim

# Setting working directory
WORKDIR /metadata-tracker

# Installing SQLite
RUN apt-get update && apt-get install -y sqlite3

# Installing Poetry
RUN python -m pip install poetry

# Setting Poetry environment variables
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_VIRTUAL_ENVS_IN_PROJECT=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PYTHONPATH=/metadata-tracker/src

# Copying dependency files
COPY pyproject.toml poetry.lock poetry.toml* ./

# Installing dependencies
RUN poetry install --no-root && rm -rf "$POETRY_CACHE_DIR"

# Copying application code
COPY . .