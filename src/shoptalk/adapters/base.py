from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from shoptalk.date_utils import utc_now


class InboundMessage(BaseModel):
    channel: str
    conversation_id: str
    sender_id: str
    text: str
    business_id: UUID | None = None
    customer_id: UUID | None = None
    received_at: datetime = Field(default_factory=utc_now)


class OutboundMessage(BaseModel):
    channel: str
    conversation_id: str
    recipient_id: str
    text: str
    business_id: UUID | None = None
    customer_id: UUID | None = None


class SendResult(BaseModel):
    accepted: bool
    channel: str
    conversation_id: str
    provider_message_id: str | None = None
    reason: str | None = None
