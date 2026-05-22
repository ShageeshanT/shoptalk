# ShopTalk Architecture

ShopTalk keeps product logic separate from channel adapters.

## Layers

1. Channel adapters receive WhatsApp, Telegram, Instagram, or manual messages.
2. Normalization converts raw events into internal customer messages.
3. Analysis extracts intent, urgency, order details, and reply drafts.
4. Repositories persist businesses, customers, orders, messages, and follow-ups.
5. Seller workflows expose review queues, approvals, dashboard metrics, and exports.

The MVP still uses in-memory repositories so the sales loop can move quickly. The next backend milestone is replacing those repositories with durable database-backed storage without changing route handlers.
