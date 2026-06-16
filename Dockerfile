# Stage 1: build dependencies
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml ./
RUN pip install --upgrade pip && pip install --no-cache-dir -e .

# Stage 2: runtime image
FROM python:3.12-slim AS runtime

WORKDIR /app

# Create non-root user
RUN addgroup --system shoptalk && adduser --system --ingroup shoptalk shoptalk

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY src/ ./src/
COPY alembic/ ./alembic/
COPY alembic.ini ./

USER shoptalk

EXPOSE 8000

CMD ["uvicorn", "shoptalk.main:app", "--host", "0.0.0.0", "--port", "8000"]
