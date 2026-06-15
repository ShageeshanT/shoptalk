# ShopTalk Roadmap

This document describes the planned delivery phases for ShopTalk.

---

## Phase 1 — Manual MVP ✅ Complete

**Goal:** Prove the core workflow with a simple API before building UI or integrations.

### Deliverables

- [x] FastAPI backend with health check
- [x] Message analysis endpoint (intent, urgency, sentiment, order extraction)
- [x] Suggested reply generation
- [x] Business and customer management
- [x] Order tracking with status pipeline
- [x] Follow-up tracking
- [x] Daily briefing endpoint
- [x] Sales funnel summary
- [x] In-memory repository layer
- [x] Pydantic schemas for all entities
- [x] Channel normalization utilities
- [x] Catalog item management and matching
- [x] Checkout draft generation

---

## Phase 2 — Persistence & Stability 🚧 In Progress

**Goal:** Replace in-memory storage with durable SQL persistence and harden the API.

### Deliverables

- [x] SQLAlchemy models for all core entities
- [x] SQL repositories for businesses, customers, orders, messages, follow-ups
- [x] Database health and readiness endpoints
- [x] Idempotent demo seed data
- [ ] Database migrations with Alembic
- [ ] PostgreSQL support (currently SQLite)
- [ ] Environment-based configuration
- [ ] Structured logging
- [ ] Rate limiting on public endpoints
- [ ] API key authentication for seller endpoints

---

## Phase 3 — Seller Dashboard

**Goal:** Give sellers a simple web UI to manage their sales desk without touching the API directly.

### Deliverables

- [ ] Next.js frontend scaffold
- [ ] Login with magic link or simple password
- [ ] Message paste and analyze UI
- [ ] Order board (Kanban-style status columns)
- [ ] Follow-up list with due dates
- [ ] Customer profile pages
- [ ] Daily briefing view
- [ ] Business settings (tone, timezone, currency)
- [ ] Catalog management UI

---

## Phase 4 — Telegram Integration

**Goal:** Let sellers forward customer messages from Telegram directly into ShopTalk.

### Deliverables

- [ ] Telegram bot setup
- [ ] Forward or paste customer message to bot
- [ ] Bot returns intent, urgency, and suggested reply
- [ ] Inline buttons to save order or create follow-up
- [ ] Seller approval before any reply is sent

---

## Phase 5 — WhatsApp Integration

**Goal:** Connect ShopTalk to the official WhatsApp Business Cloud API.

### Deliverables

- [ ] WhatsApp Business Cloud API webhook receiver
- [ ] Incoming message normalization
- [ ] Automatic intent analysis on new messages
- [ ] Seller notification for high-urgency messages
- [ ] Human-approved reply sending
- [ ] Message thread sync
- [ ] Read receipt tracking

---

## Phase 6 — Paid Pilot

**Goal:** Test with 3–5 real small businesses and validate product-market fit.

### Deliverables

- [ ] Onboarding flow for new sellers
- [ ] Niche-specific extraction templates (home bakers, clothing sellers, salons)
- [ ] Usage analytics (reply time, missed follow-ups, order conversion)
- [ ] Feedback collection mechanism
- [ ] Pricing model validation
- [ ] Support documentation

---

## Design Principles

These principles guide every phase:

1. **Human approval first** — ShopTalk drafts, sellers decide.
2. **Channel-agnostic** — The core logic works regardless of whether the message came from WhatsApp, Telegram, or a manual paste.
3. **Simple workflows before heavy integrations** — Prove the workflow before automating it.
4. **Useful over flashy** — Every feature must solve a real problem for a real seller.
5. **Real business pain over startup theatre** — No vanity metrics, no unnecessary complexity.

---

## Out of Scope (for now)

- Inventory management
- Accounting or invoicing
- Team inbox with multiple agents
- Mobile app
- Autonomous reply sending without seller approval
- Multi-language support (English first)
