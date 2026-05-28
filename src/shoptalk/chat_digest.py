"""Chat digest helpers for seller summaries."""

from __future__ import annotations


def chat_digest(messages: list[str], limit: int = 2) -> str:
    """Return a compact digest of the latest chat messages."""

    latest = messages[-limit:] if limit > 0 else []
    return " | ".join(latest)
