from __future__ import annotations

def search_empty_state(query: str) -> str:
    return f"No results for {query.strip()}" if query.strip() else "Search customers, orders, or messages"