from __future__ import annotations

def intent_label(intent: str) -> str:
    return intent.replace("_", " ").title()