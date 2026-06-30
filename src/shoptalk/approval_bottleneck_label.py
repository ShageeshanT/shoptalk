"""Compact seller dashboard helper for approval bottleneck."""

from __future__ import annotations


def classify_approval_bottleneck(pending_drafts: int | float) -> str:
    """Return a short seller-facing label for approval bottleneck."""
    return "Clear approvals" if pending_drafts < 3 else "Approval queue" if pending_drafts < 10 else "Approval bottleneck"
