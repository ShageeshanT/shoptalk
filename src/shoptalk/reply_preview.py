from __future__ import annotations

def reply_preview(text: str, limit: int=60) -> str:
    clean=" ".join(text.split())
    return clean if len(clean)<=limit else clean[:limit-1].rstrip()+"…"