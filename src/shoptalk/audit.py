from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from shoptalk.date_utils import utc_now


class AuditEvent(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    actor: str = 'seller'
    action: str
    resource_type: str
    resource_id: UUID | None = None
    created_at: datetime = Field(default_factory=utc_now)


def audit_label(event: AuditEvent) -> str:
    return f"{event.actor}:{event.action}:{event.resource_type}"
