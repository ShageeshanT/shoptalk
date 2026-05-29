from shoptalk.approval import ApprovalDraft, ApprovalStatus
from shoptalk.approval_summary import approval_status_counts, pending_approval_messages


def test_approval_status_counts_include_all_statuses() -> None:
    drafts = [
        ApprovalDraft(message="A"),
        ApprovalDraft(message="B", status=ApprovalStatus.APPROVED),
    ]

    assert approval_status_counts(drafts) == {"draft": 1, "approved": 1, "rejected": 0}


def test_pending_approval_messages_use_edited_message_and_limit() -> None:
    drafts = [
        ApprovalDraft(message="Original", edited_message="Edited"),
        ApprovalDraft(message="Second"),
        ApprovalDraft(message="Approved", status=ApprovalStatus.APPROVED),
    ]

    assert pending_approval_messages(drafts, limit=1) == ["Edited"]
