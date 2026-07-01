from __future__ import annotations


def catalog_gap_score(missing_photos, missing_prices, customer_asks) -> int:
    score = min(missing_photos * 8, 32) + min(missing_prices * 10, 30)
    if customer_asks >= 5:
        score += 25
    elif customer_asks > 0:
        score += 10
    return min(score, 100)
