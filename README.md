# ShopTalk

Turn customer chats into orders, payments, and follow-ups.

ShopTalk is an AI sales desk for WhatsApp-first small businesses. It helps owners understand messy customer messages, draft better replies, extract order details, track pending payments, and remember follow-ups without surrendering their customer relationships to a soulless chatbot.

The first version focuses on a manual web MVP: paste a customer message, get structured order insights, a suggested reply, and a follow-up plan. WhatsApp and Telegram integrations can be added later once the core workflow is proven with real businesses.

## Why ShopTalk exists

Small businesses often run their entire sales operation through chat.

A single WhatsApp inbox can contain:

- New product inquiries
- Custom orders
- Payment promises
- Delivery questions
- Angry customers
- Refund requests
- People who said “I’ll confirm tonight” and then vanished into the fog

Most owners do not need a fully autonomous chatbot. They need a fast assistant that keeps them in control.

ShopTalk turns chat chaos into a simple workflow:

1. Understand the customer message
2. Suggest a useful reply
3. Extract order details
4. Save the customer and order
5. Create follow-ups before money disappears into the abyss

## Core idea

Customer message:

> Hi, can I order a 1kg chocolate cake for Saturday evening with Happy Birthday Amaya written on it?

ShopTalk extracts:

```json
{
  "intent": "new_order",
  "urgency": "normal",
  "product": "chocolate cake",
  "quantity": 1,
  "size": "1kg",
  "needed_by": "Saturday evening",
  "custom_text": "Happy Birthday Amaya",
  "payment_status": "unknown",
  "follow_up_needed": true
}
```

Suggested reply:

> Hi! Yes, we can make a 1kg chocolate cake for Saturday evening with “Happy Birthday Amaya” written on it. Would you like pickup or delivery?

## MVP scope

The first MVP is intentionally simple.

### Included

- Business setup
- Manual customer message analyzer
- AI intent and urgency detection
- Suggested reply generation
- Order detail extraction
- Customer records
- Order tracking
- Follow-up tracking
- Dashboard for pending work

### Not included yet

- Full WhatsApp Business API integration
- Unofficial WhatsApp automation
- Inventory management
- Accounting
- Team inbox
- Mobile app
- Giant analytics dashboard that nobody asked for

## Product modules

### Message Analyzer

Paste a customer message and receive:

- Intent
- Urgency
- Sentiment
- Extracted order details
- Payment signal
- Follow-up recommendation
- Suggested reply

### Customers

Track customers with:

- Name
- Phone or channel ID
- Notes
- Last message
- Linked orders
- Pending follow-ups

### Orders

Simple order board with statuses:

- New inquiry
- Confirmed
- Payment pending
- Paid
- Preparing
- Ready
- Delivered
- Cancelled

### Follow-ups

Track things like:

- Ask customer for confirmation
- Remind customer about payment
- Check delivery status
- Send catalog
- Confirm pickup time

## Target users

ShopTalk is designed for small businesses that sell through messaging apps:

- Home bakers
- Clothing sellers
- Salons
- Florists
- Repair shops
- Rental businesses
- Local service providers
- Instagram and WhatsApp sellers

The first recommended niche is home bakers because their messages usually contain clear order fields like product, size, date, custom text, pickup, delivery, and deposit.

## Technical direction

Recommended production stack:

- Frontend: Next.js, Tailwind CSS
- Backend: FastAPI
- Database: PostgreSQL
- Queue: Redis with RQ or Celery
- AI: structured JSON extraction through an LLM provider
- Deployment: Railway for the MVP

This repository starts with a lightweight Python-first backend plan so the product logic can be developed and tested quickly before UI and integrations become complicated.

## Planned architecture

```text
Customer message
      |
      v
Channel adapter
manual paste / Telegram / WhatsApp later
      |
      v
Message normalization
      |
      v
AI analysis pipeline
intent, urgency, sentiment, order extraction, reply draft
      |
      v
Database
customers, messages, orders, follow-ups, suggestions
      |
      v
Owner dashboard
review, edit, save, reply, follow up
```

## Data model draft

### businesses

- id
- name
- owner_id
- business_type
- timezone
- tone
- currency

### customers

- id
- business_id
- name
- phone
- channel
- notes
- last_message_at

### messages

- id
- business_id
- customer_id
- channel
- direction
- text
- ai_intent
- urgency
- created_at

### orders

- id
- business_id
- customer_id
- title
- status
- payment_status
- total_amount
- delivery_date
- notes

### followups

- id
- business_id
- customer_id
- order_id
- title
- due_at
- status

### ai_suggestions

- id
- message_id
- suggested_reply
- extracted_json
- confidence

## Roadmap

### Phase 1: Manual MVP

- Create backend models
- Add message analyzer endpoint
- Add structured AI extraction
- Save customers, orders, and follow-ups
- Build simple dashboard

### Phase 2: Workflow MVP

- Order board
- Follow-up list
- Daily summary
- Business tone settings
- Message history

### Phase 3: Telegram prototype

- Telegram bot for forwarding/pasting customer messages
- Bot returns analysis and suggested reply
- Save order or follow-up from bot actions

### Phase 4: WhatsApp integration

- Add official WhatsApp Business Cloud API support
- Keep human approval for important outgoing messages
- Sync incoming messages into ShopTalk

### Phase 5: Paid pilot

- Test with 3 to 5 real small businesses
- Measure reply time, missed follow-ups, and order tracking usefulness
- Refine niche-specific extraction templates

## Development principles

- Human approval first
- Channel-agnostic architecture
- Simple workflows before heavy integrations
- Useful over flashy
- Real business pain over startup theatre

## Status

Early planning and foundation stage.

## License

MIT


## Current MVP API

ShopTalk now includes endpoints for:

- message analysis and reply drafting
- business and customer setup
- order tracking
- follow-up tracking
- seller tasks
- dashboard metrics
- demo seed data

Run locally with:

```bash
uvicorn shoptalk.main:app --reload
```

## API notes

See `docs/API_OVERVIEW.md` for the current endpoint map and the main seller workflow.


## Persistence status

ShopTalk now includes the first SQL persistence layer using SQLAlchemy. It covers core seller records and keeps database access behind repositories so the API can move toward durable storage without rewriting product logic.
