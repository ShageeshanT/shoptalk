# ShopTalk API Reference

Interactive docs available at `/docs` when the server is running.

---

## Health

### `GET /health`

Returns the application health status.

**Response**
```json
{"status": "ok", "version": "0.1.0"}
```

---

## Message Analysis

### `POST /analyze`

Analyze a raw customer message and extract structured intent, urgency, order details, and a suggested reply.

**Request body**
```json
{
  "business_id": "biz_123",
  "customer_id": "cust_456",
  "raw_message": "Hi, can I order a 1kg chocolate cake for Saturday?"
}
```

**Response**
```json
{
  "intent": "new_order",
  "urgency": "normal",
  "sentiment": "positive",
  "product": "chocolate cake",
  "quantity": 1,
  "size": "1kg",
  "needed_by": "Saturday",
  "follow_up_needed": true,
  "suggested_reply": "Hi! Yes, we can do a 1kg chocolate cake for Saturday. Pickup or delivery?"
}
```

---

## Customers

- `POST /customers` — Create a new customer record.
- `GET /customers/{customer_id}` — Retrieve a customer by ID.
- `GET /customers` — List all customers. Supports `?business_id=` filter.

---

## Orders

- `POST /orders` — Create a new order.
- `GET /orders/{order_id}` — Retrieve an order by ID.
- `PATCH /orders/{order_id}/status` — Update order status.

Valid statuses: `pending`, `confirmed`, `in_progress`, `ready`, `delivered`, `cancelled`.

- `GET /orders` — List orders. Supports `?business_id=`, `?status=`, `?customer_id=` filters.

---

## Follow-ups

- `POST /followups` — Create a follow-up reminder.
- `GET /followups/due` — List follow-ups due today or overdue.
- `PATCH /followups/{followup_id}/complete` — Mark a follow-up as completed.

---

## Dashboard

- `GET /dashboard/briefing` — Daily briefing: pending orders, due follow-ups, recent messages.
- `GET /dashboard/funnel` — Sales funnel summary: leads to confirmed to delivered.

---

## Catalog

- `POST /catalog/items` — Add a product to the business catalog.
- `GET /catalog/items` — List catalog items for a business.
- `POST /catalog/match` — Match a free-text product description against the catalog.

---

## Errors

All errors follow this format:

```json
{"detail": "Human-readable error message"}
```

Common HTTP status codes: `400` Invalid request, `404` Not found, `422` Validation error, `500` Server error.
