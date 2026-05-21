from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from shoptalk.message_tagging import tag_messages
from shoptalk.schemas import ConversationMessage, ConversationMessageOut, MessageTag
from shoptalk.state import state

router = APIRouter(prefix="/messages", tags=["messages"])


@router.post("", response_model=ConversationMessageOut, status_code=status.HTTP_201_CREATED)
def create_message(payload: ConversationMessage) -> ConversationMessageOut:
    if state.businesses.get(payload.business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")
    if payload.customer_id is not None and state.customers.get(payload.customer_id) is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    message = ConversationMessageOut(**payload.model_dump())
    state.messages.add(message)
    return message


@router.get("", response_model=list[ConversationMessageOut])
def list_messages(
    business_id: UUID | None = None,
    customer_id: UUID | None = None,
    search: str | None = None,
    limit: int = 50,
) -> list[ConversationMessageOut]:
    messages = state.messages.list()
    if business_id is not None:
        messages = [message for message in messages if message.business_id == business_id]
    if customer_id is not None:
        messages = [message for message in messages if message.customer_id == customer_id]
    if search:
        query = search.lower().strip()
        messages = [message for message in messages if query in message.text.lower()]
    return messages[-limit:]


@router.get("/tags", response_model=list[MessageTag])
def list_message_tags(business_id: UUID | None = None) -> list[MessageTag]:
    if business_id is not None and state.businesses.get(business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return tag_messages(state.messages.list(), business_id=business_id)
