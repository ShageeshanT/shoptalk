from enum import StrEnum
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ApprovalStatus(StrEnum):
    DRAFT = "draft"
    APPROVED = "approved"
    REJECTED = "rejected"


class ApprovalDraft(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    customer_id: UUID | None = None
    message: str = Field(..., min_length=1)
    status: ApprovalStatus = ApprovalStatus.DRAFT


def approve_draft(draft: ApprovalDraft) -> ApprovalDraft:
    return draft.model_copy(update={"status": ApprovalStatus.APPROVED})


def reject_draft(draft: ApprovalDraft) -> ApprovalDraft:
    return draft.model_copy(update={"status": ApprovalStatus.REJECTED})
