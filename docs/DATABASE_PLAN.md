# Database Plan

ShopTalk is moving from in-memory storage toward a SQL persistence layer. The first production target is SQLite for local demos and PostgreSQL for hosted sellers.

## Current boundary

- SQLAlchemy models cover businesses, customers, orders, messages, and follow ups.
- Repository classes keep route handlers away from raw SQL.
- Runtime database helpers initialize tables for local development.

## Next steps

1. Replace in-memory route dependencies with repository injection.
2. Add Alembic migrations before hosted beta usage.
3. Add PostgreSQL connection settings for Railway.
4. Add seller scoped authorization before exposing persisted records.
