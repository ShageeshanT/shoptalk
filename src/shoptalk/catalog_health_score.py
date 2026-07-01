from __future__ import annotations

def catalog_health_score(active_items: int, missing_photos: int, stale_prices: int) -> int:
    raw_score = active_items * 3 - missing_photos * 5 - stale_prices * 6
    return max(0, min(100, int(raw_score)))
