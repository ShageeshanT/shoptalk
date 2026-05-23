# ShopTalk API Overview

ShopTalk exposes a small sales desk API for WhatsApp-first sellers. The current MVP is intentionally in-memory so product flows can be tested before database wiring is locked in.

## Core flows

1. Create a business and customers.
2. Ingest customer messages.
3. Analyze intent and urgency.
4. Create orders, follow-ups, tasks, and reply drafts.
5. Review dashboard, daily briefing, and sales funnel summaries.

## Useful endpoints

- `POST /businesses` creates seller profiles.
- `POST /customers` stores customers by channel.
- `POST /messages` records customer, seller, or assistant messages.
- `GET /threads` returns a chronological conversation thread.
- `POST /catalog-items` stores sellable products.
- `POST /catalog/match` matches message text against a catalog payload.
- `POST /orders` tracks order pipeline status.
- `GET /checkout/orders/{order_id}/draft` creates a manual payment instruction draft.
- `GET /briefing/daily` returns daily seller priorities.
- `GET /sales/funnel` summarizes order pipeline counts.
- `GET /search/messages` searches stored customer messages.

## Human-in-the-loop rule

ShopTalk can draft replies and payment instructions, but seller approval remains the default before anything is sent to a customer. Tiny businesses need speed, not a rogue chatbot with a payment link and main-character syndrome.


## Persistence boundary

The API is gaining a SQL repository layer so endpoint logic can move from process memory to durable seller data. Current repository coverage includes businesses, customers, orders, conversation messages, and follow ups.
