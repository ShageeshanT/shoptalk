from __future__ import annotations


def message_cleanup_score(duplicate_messages, spam_signals, has_order_signal) -> int:
    score = min(duplicate_messages * 12, 36) + min(spam_signals * 18, 36)
    if not has_order_signal:
        score += 20
    return min(score, 100)
