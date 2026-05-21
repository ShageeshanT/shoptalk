# ShopTalk MVP Status

Updated for the current backend batch.

## Working backend capabilities

- Business, customer, order, task, follow-up, catalog, message, approval, checkout, briefing, dashboard, health, ingestion, and timeline APIs.
- Rule-based message analysis for early home baker and chat commerce flows.
- Seller-facing message summaries and reply drafts.
- Human approval queue with edit, approve, reject, and filtering support.
- Channel message ingestion with duplicate protection for external message IDs.
- Customer timelines that combine messages, orders, and follow-ups.
- Catalog item creation, updates, availability filtering, and search.
- Checkout draft generation with payment instructions.
- Dashboard and health endpoints for operator visibility.

## Still needed before a private beta

- Persistent database storage instead of in-memory repositories.
- Seller dashboard UI for the full workflow.
- Real channel adapter integration, starting with a WhatsApp/Baileys bridge or official WhatsApp Cloud path.
- Authentication and owner/business access control.
- Production AI extraction behind a provider boundary.
- Deployment configuration, environment validation, and operational logging.

## Current product posture

The backend is now a usable workflow skeleton for the core sales desk loop, but it is not production-ready until persistence, auth, UI, and real messaging delivery are in place.
