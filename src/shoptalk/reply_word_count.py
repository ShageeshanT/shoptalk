from __future__ import annotations

def reply_word_count(text: str) -> int:
    return len([p for p in text.split() if p])