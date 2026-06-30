from __future__ import annotations

def followup_prompt_copy(topic: str) -> str:
    clean = topic.strip() or "the order"
    return f"Could you confirm {clean}?"
