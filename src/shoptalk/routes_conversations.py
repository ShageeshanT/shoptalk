from uuid import UUID

from fastapi import APIRouter, HTTPException

from shoptalk.customer_signals import build_customer_signal
from shoptalk.inbox import build_customer_inbox_item
from shoptalk.schemas import ConversationMessageOut, ConversationSummary, InboxItem
from shoptalk.state import state

router = APIRouter(prefix="/conversations", tags=["conversations"])


def _conversation_messages(
    business_id: UUID,
    customer_id: UUID | None = None,
) -> list[ConversationMessageOut]:
    if state.businesses.get(business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")

    messages = [message for message in state.messages.list() if message.business_id == business_id]
    if customer_id is not None:
        if state.customers.get(customer_id) is None:
            raise HTTPException(status_code=404, detail="Customer not found")
        messages = [message for message in messages if message.customer_id == customer_id]
    return sorted(messages, key=lambda message: message.received_at)


@router.get("/summary", response_model=ConversationSummary)
def conversation_summary(business_id: UUID, customer_id: UUID | None = None) -> ConversationSummary:
    messages = _conversation_messages(business_id, customer_id)
    latest = messages[-1] if messages else None
    return ConversationSummary(
        business_id=business_id,
        customer_id=customer_id,
        messages=len(messages),
        customer_messages=sum(message.sender == "customer" for message in messages),
        seller_messages=sum(message.sender == "seller" for message in messages),
        latest_message=latest,
        signal=build_customer_signal(messages),
    )


@router.get("/inbox", response_model=list[InboxItem])
def conversation_inbox(business_id: UUID) -> list[InboxItem]:
    messages = _conversation_messages(business_id)
    items: list[InboxItem] = []
    for customer in state.customers.list_for_business(business_id):
        signal = build_customer_inbox_item(customer.id, messages)
        if signal is not None:
            items.append(InboxItem(customer_id=customer.id, signal=signal))
    return sorted(items, key=lambda item: item.signal.needs_reply, reverse=True)
