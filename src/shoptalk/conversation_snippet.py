from __future__ import annotations

def conversation_snippet(text: str, limit: int=80) -> str:
    clean=" ".join(text.split())
    return clean if len(clean)<=limit else clean[:limit-1]+"…"