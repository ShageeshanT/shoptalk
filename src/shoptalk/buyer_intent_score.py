from __future__ import annotations

def buyer_intent_score(buy_words: int, question_count: int, price_mentions: int) -> int:
    raw_score = buy_words * 12 + question_count * 3 + price_mentions * 5
    return max(0, min(100, int(raw_score)))
