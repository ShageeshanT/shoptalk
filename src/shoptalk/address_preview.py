from __future__ import annotations

def address_preview(address: str | None, limit: int=50) -> str:
    if not address: return "No address"
    clean=" ".join(address.split())
    return clean if len(clean)<=limit else clean[:limit-1]+"…"