from __future__ import annotations

def promo_readiness_score(stock_ready: int, margin_ok: int, audience_fit: int) -> int:
    raw_score = stock_ready * 10 + margin_ok * 8 + audience_fit * 7
    return max(0, min(100, int(raw_score)))
