"""Small seller-facing helper for approval friction label."""

from __future__ import annotations


def classify_approval_friction(edits: int | float | bool) -> str:
    """Return a compact dashboard label for approval friction label."""
    return "Clean" if edits <= 0 else "Minor edits" if edits <= 2 else "Needs rewrite"
