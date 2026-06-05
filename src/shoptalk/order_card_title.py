from __future__ import annotations

def order_card_title(title: str, customer: str | None=None) -> str:
    clean=title.strip() or "Untitled order"
    return f"{clean} · {customer}" if customer else clean