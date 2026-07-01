from __future__ import annotations


def catalog_freshness_score(days_since_update, out_of_stock_items, missing_prices) -> int:
    score = 0
    if days_since_update >= 30:
        score += 35
    elif days_since_update >= 7:
        score += 15
    score += min(out_of_stock_items * 8, 32)
    score += min(missing_prices * 8, 24)
    return min(score, 100)
