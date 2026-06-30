from __future__ import annotations

def order_summary_line(title: str, total: float) -> str:
    return f"{title.strip()}: LKR {total:,.2f}"
