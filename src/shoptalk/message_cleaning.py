"""Message cleanup helpers for noisy chat input."""

from __future__ import annotations


def clean_message_text(text: str) -> str:
    """Normalize whitespace while preserving message wording."""

    return " ".join(text.replace("\n", " ").split())


def is_empty_message(text: str) -> bool:
    """Return whether text is empty after cleanup."""

    return clean_message_text(text) == ""
