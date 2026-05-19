import re
from uuid import UUID

from shoptalk.schemas import MessageTag, ConversationMessageOut

TAG_PATTERNS = {
    "price": ["price", "cost", "how much", "rate"],
    "delivery": ["deliver", "delivery", "pickup", "collect", "courier"],
    "payment": ["pay", "paid", "payment", "deposit", "bank transfer"],
    "complaint": ["refund", "complain", "wrong", "late", "bad review"],
    "urgent": ["urgent", "asap", "today", "now"],
}


def detect_message_tags(text: str) -> list[str]:
    lowered = text.lower()
    tags: list[str] = []
    for tag, patterns in TAG_PATTERNS.items():
        if any(re.search(rf"\b{re.escape(pattern)}\b", lowered) for pattern in patterns):
            tags.append(tag)
    return tags


def tag_messages(messages: list[ConversationMessageOut], business_id: UUID | None = None) -> list[MessageTag]:
    filtered = [
        message for message in messages if business_id is None or message.business_id == business_id
    ]
    return [
        MessageTag(message_id=message.id, tags=detect_message_tags(message.text))
        for message in filtered
    ]
