from __future__ import annotations

from collections import Counter

from shoptalk.approval import ApprovalDraft, ApprovalStatus


def approval_status_counts(drafts: list[ApprovalDraft]) -> dict[str, int]:
    counts = Counter(draft.status.value for draft in drafts)
    return {status.value: counts.get(status.value, 0) for status in ApprovalStatus}


def pending_approval_messages(drafts: list[ApprovalDraft], *, limit: int = 5) -> list[str]:
    return [
        draft.edited_message or draft.message
        for draft in drafts
        if draft.status == ApprovalStatus.DRAFT
    ][:limit]
