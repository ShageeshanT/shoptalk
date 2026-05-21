from enum import StrEnum
from uuid import UUID, uuid4

from shoptalk.date_utils import utc_now

from pydantic import BaseModel, Field


class ApprovalStatus(StrEnum):
    DRAFT = "draft"
    APPROVED = "approved"
    REJECTED = "rejected"


class ApprovalDraft(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    customer_id: UUID | None = None
    business_id: UUID | None = None
    message: str = Field(..., min_length=1)
    edited_message: str | None = None
    status: ApprovalStatus = ApprovalStatus.DRAFT
    created_at: str = Field(default_factory=lambda: utc_now().isoformat())
    updated_at: str = Field(default_factory=lambda: utc_now().isoformat())


def approve_draft(draft: ApprovalDraft) -> ApprovalDraft:
    return draft.model_copy(update={"status": ApprovalStatus.APPROVED, "updated_at": utc_now().isoformat()})


def reject_draft(draft: ApprovalDraft) -> ApprovalDraft:
    return draft.model_copy(update={"status": ApprovalStatus.REJECTED, "updated_at": utc_now().isoformat()})


def edit_draft(draft: ApprovalDraft, message: str) -> ApprovalDraft:
    return draft.model_copy(update={"edited_message": message, "updated_at": utc_now().isoformat()})
