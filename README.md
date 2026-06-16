# ShopTalk

[![CI](https://github.com/ShageeshanT/shoptalk/actions/workflows/ci.yml/badge.svg)](https://github.com/ShageeshanT/shoptalk/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **ShopTalk** turns WhatsApp customer messages into structured orders — so small business owners spend less time typing and more time baking, sewing, or building.

## Features

- **AI message analysis** — Extracts intent, product, quantity, urgency, and sentiment from raw customer messages
- **Order lifecycle tracking** — Manage orders from `pending` through `delivered` with a simple status API
- **Customer management** — Auto-creates customer records from phone numbers; supports notes and history
- **Follow-up reminders** — Never forget to call a customer back
- **Daily briefing** — One endpoint gives you everything you need to start the day
- **Channel-agnostic** — WhatsApp adapter included; Telegram coming in Phase 4
- **Product catalog matching** — Fuzzy-matches customer descriptions to your catalog items

## Quick Start

```bash
git clone https://github.com/ShageeshanT/shoptalk.git
cd shoptalk
python -m venv .venv && source .venv/bin/activate
pip install -e .
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
uvicorn shoptalk.main:app --reload
```

Then open `http://127.0.0.1:8000/docs` for the interactive API explorer.

## Project Status

ShopTalk is in active development. See [ROADMAP.md](docs/ROADMAP.md) for the full plan.

| Phase | Status | Description |
|-------|--------|-------------|
| 1 | ✅ Done | Core message analysis and order tracking |
| 2 | 🔄 In progress | Dashboard, follow-ups, seller auth |
| 3 | 📋 Planned | Product catalog with semantic search |
| 4 | 📋 Planned | Telegram channel adapter |
| 5 | 📋 Planned | WhatsApp Business API send integration |
| 6 | 📋 Planned | Multi-tenant support |

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [API Reference](docs/API.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Roadmap](docs/ROADMAP.md)
- [Contributing](CONTRIBUTING.md)

## License

MIT — see [LICENSE](LICENSE).
