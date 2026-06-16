# ShopTalk Architecture

## Overview

ShopTalk is a FastAPI application that sits between messaging channels (WhatsApp, Telegram)
and a seller's order management workflow. It uses OpenAI to parse unstructured customer
messages into structured order data and generates suggested replies.

## High-Level Data Flow

```
Customer (WhatsApp/Telegram)
        |
        v
  Channel Adapter          <- normalises platform-specific payloads
        |
        v
  Analysis Service         <- calls OpenAI, returns structured intent
        |
        v
  Order / Customer Repo    <- persists data to PostgreSQL via SQLAlchemy
        |
        v
  Dashboard / Briefing     <- seller views pending orders and follow-ups
```

## Layer Responsibilities

| Layer | Location | Responsibility |
|-------|----------|----------------|
| Routes | `src/shoptalk/routes/` | HTTP request/response, input validation |
| Services | `src/shoptalk/services/` | Business logic, AI calls |
| Repositories | `src/shoptalk/repositories/` | Database queries, no business logic |
| Models | `src/shoptalk/models/` | SQLAlchemy ORM table definitions |
| Schemas | `src/shoptalk/schemas/` | Pydantic request/response contracts |
| Channels | `src/shoptalk/channels/` | Platform-specific webhook adapters |

## Key Design Decisions

### Async-first
All route handlers and service methods are `async`. SQLAlchemy is used with
`asyncpg` in production and `aiosqlite` in development.

### Dependency injection
FastAPI's `Depends()` system is used throughout. `get_settings()` and
`get_db_session()` are the two primary dependencies.

### Stateless API
The API is stateless. All state lives in the database. This makes horizontal
scaling straightforward — run multiple uvicorn workers or containers behind
a load balancer.

### AI as a service
OpenAI is called only in `AnalysisService`. If the API key is missing or the
call fails, a safe fallback response is returned so the system degrades
gracefully rather than erroring.

## Database Schema

```
customers
  id, business_id, phone, name, channel, is_active, notes, created_at, updated_at

orders
  id, business_id, customer_id, product, quantity, size, price,
  status, needed_by, delivery_address, notes, raw_message, created_at, updated_at

followups
  id, business_id, customer_id, order_id, reason, due_at,
  completed, completed_at, notes, created_at
```

## Future Phases

See [ROADMAP.md](ROADMAP.md) for the full plan. Upcoming architectural additions:

- **Phase 3**: Product catalog with fuzzy matching
- **Phase 4**: Telegram channel adapter
- **Phase 5**: WhatsApp Business API webhook handler
- **Phase 6**: Multi-tenant business isolation with row-level security
