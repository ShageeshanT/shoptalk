from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from shoptalk.approval import ApprovalDraft, approve_draft, reject_draft
from shoptalk.state import state

router = APIRouter(prefix="/approvals", tags=["approvals"])


@router.post("", response_model=ApprovalDraft, status_code=status.HTTP_201_CREATED)
def create_approval_draft(payload: ApprovalDraft) -> ApprovalDraft:
    return state.approvals.add(payload)


@router.get("", response_model=list[ApprovalDraft])
def list_approval_drafts() -> list[ApprovalDraft]:
    return state.approvals.list()


@router.post("/{draft_id}/approve", response_model=ApprovalDraft)
def approve_approval_draft(draft_id: UUID) -> ApprovalDraft:
    draft = state.approvals.get(draft_id)
    if draft is None:
        raise HTTPException(status_code=404, detail="Approval draft not found")
    updated = approve_draft(draft)
    state.approvals.add(updated)
    return updated


@router.post("/{draft_id}/reject", response_model=ApprovalDraft)
def reject_approval_draft(draft_id: UUID) -> ApprovalDraft:
    draft = state.approvals.get(draft_id)
    if draft is None:
        raise HTTPException(status_code=404, detail="Approval draft not found")
    updated = reject_draft(draft)
    state.approvals.add(updated)
    return updated
