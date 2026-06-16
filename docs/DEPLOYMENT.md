# Deployment Guide

## Prerequisites

- Python 3.11+
- PostgreSQL 14+ (recommended for production)
- An OpenAI API key

## Docker (recommended)

```bash
# Build the image
docker build -t shoptalk:latest .

# Run with environment variables
docker run -d \
  --name shoptalk \
  -p 8000:8000 \
  -e OPENAI_API_KEY=sk-... \
  -e DATABASE_URL=postgresql+psycopg2://user:pass@db:5432/shoptalk \
  -e SECRET_KEY=$(openssl rand -hex 32) \
  -e ENVIRONMENT=production \
  shoptalk:latest
```

## Docker Compose

```yaml
version: '3.9'
services:
  api:
    build: .
    ports:
      - '8000:8000'
    env_file: .env
    depends_on:
      - db
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: shoptalk
      POSTGRES_USER: shoptalk
      POSTGRES_PASSWORD: changeme
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

## Bare Metal

```bash
pip install -e .
alembic upgrade head
uvicorn shoptalk.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## Reverse Proxy (nginx)

```nginx
server {
    listen 80;
    server_name api.yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Database Migrations

ShopTalk uses Alembic for schema migrations.

```bash
# Apply all pending migrations
alembic upgrade head

# Create a new migration after model changes
alembic revision --autogenerate -m 'add new column'
```

## Health Check

Once running, verify the service is healthy:

```bash
curl http://your-server:8000/health
```
