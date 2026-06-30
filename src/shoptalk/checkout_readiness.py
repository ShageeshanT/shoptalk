from __future__ import annotations

def checkout_readiness(has_items: bool, has_total: bool, has_contact: bool) -> str:
    return "ready" if has_items and has_total and has_contact else "missing details"
