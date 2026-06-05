from __future__ import annotations

def urgency_badge(urgency: str) -> str:
    return {"high":"High priority","normal":"Normal priority","low":"Low priority"}.get(urgency, "Normal priority")