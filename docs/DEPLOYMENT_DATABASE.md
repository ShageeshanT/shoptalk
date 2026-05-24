# Deployment Database Notes

ShopTalk can run with SQLite for local demos, but hosted sellers should use PostgreSQL.

## Environment

Set `DATABASE_URL` to the deployed database connection string. Keep credentials outside commits and logs.

## Readiness checks

- `/database/health` verifies a basic SQL round trip.
- `/database/readiness` checks that required core tables exist.

## Before beta

Add migration management, backups, and seller scoped access checks before handling real customer conversations.
