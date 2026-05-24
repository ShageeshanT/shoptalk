# Changelog

## Unreleased

- Added utility modules for channel normalization, phone cleanup, money parsing, delivery detection, and reply templates.
- Added lightweight safety, audit, export, SLA, and health-report helpers.
- Added private beta and architecture documentation for the next ShopTalk milestone.


## Persistence foundation

- Added SQLAlchemy database models for seller core data.
- Added SQLite session helpers and runtime database wiring.
- Added SQL repositories for businesses, customers, orders, messages, and follow ups.
- Added database health checks and storage documentation.


## Database hardening

- Added readiness checks, masked database diagnostics, and database health routes.
- Added filtered SQL queries for orders, customers, messages, and follow ups.
- Added database snapshots, counts, and idempotent demo seeding helpers.
