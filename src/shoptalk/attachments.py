from typing import Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class MessageAttachment(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    kind: Literal['image', 'audio', 'document']
    url: str
    caption: str | None = None


def has_voice_note(attachments: list[MessageAttachment]) -> bool:
    return any(item.kind == 'audio' for item in attachments)
