# Storage

ShopTalk uses repository boundaries to avoid tying the product workflow to one database implementation.

## Local development

- SQLite is supported for fast local runs and demos.
- The default local path is `data/shoptalk.sqlite3`.
- Tests use in-memory SQLite databases.

## Production direction

- PostgreSQL should become the hosted production database.
- Alembic migrations should manage schema changes.
- Seller and business authorization must be enforced before persisted records are exposed through the API.
