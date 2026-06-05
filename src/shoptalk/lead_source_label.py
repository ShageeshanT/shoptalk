from __future__ import annotations

def lead_source_label(source: str | None) -> str:
    return source.replace("_", " ").title() if source else "Unknown source"