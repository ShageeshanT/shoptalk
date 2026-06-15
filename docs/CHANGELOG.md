# Changelog

All notable changes to ShopTalk are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
ShopTalk uses [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

### Added
- CONTRIBUTING.md with full developer setup guide
- ROADMAP.md with phased delivery plan
- GitHub issue and PR templates
- README badges and Quick Start section

---

## [0.2.0] — 2026-06

### Added
- SQL persistence layer using SQLAlchemy for businesses, customers, orders, messages, and follow-ups
- Database health and readiness check endpoints (`GET /database/health`, `GET /database/readiness`)
- Database snapshot and count helpers
- Idempotent demo seed endpoint
- Filtered SQL queries for orders, customers, messages, and follow-ups
- Masked database diagnostics for safe logging
- Readiness checks on startup

### Changed
- Repositories now support both in-memory and SQL backends without changing route handlers
- Storage documentation updated to reflect persistence boundary

---

## [0.1.0] — 2026-05

### Added
- FastAPI application entry point with health check
- Message analysis endpoint (`POST /messages/analyze`)
- Intent and urgency detection (rule-based placeholder)
- Suggested reply generation
- Order detail extraction from customer messages
- Business setup endpoints (`POST /businesses`, `GET /businesses/{id}`)
- Customer management (`POST /customers`, `GET /customers`)
- Order tracking with status pipeline (`POST /orders`, `PATCH /orders/{id}`)
- Follow-up tracking (`POST /follow-ups`, `GET /follow-ups`)
- Seller task management
- Daily briefing endpoint (`GET /briefing/daily`)
- Sales funnel summary (`GET /sales/funnel`)
- Dashboard metrics endpoint
- In-memory repository for all core entities
- Pydantic schemas for all request and response models
- Channel normalization utilities
- Phone number cleanup helpers
- Money parsing utilities
- Delivery detection logic
- Reply template system with tone adjustment
- Safety and audit helpers
- SLA tracking helpers
- Health report generation
- Catalog item management and matching
- Checkout draft generation
- Conversation thread endpoint
- Message search endpoint
- Utility modules: address completion, approval friction, basket health, bulk order labels
- Private beta documentation
- Architecture documentation

### Technical
- Python 3.11+ with `pyproject.toml` packaging
- FastAPI with automatic OpenAPI docs at `/docs`
- Pydantic v2 for data validation
- UUID-based entity identifiers
- Timezone-aware timestamps throughout

---

## [0.0.1] — 2026-04

### Added
- Initial project scaffold
- README with product vision and roadmap
- Architecture documentation
- API overview documentation
- MIT license
