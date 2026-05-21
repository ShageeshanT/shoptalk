from uuid import UUID

from shoptalk.schemas import CustomerTimeline, CustomerTimelineEvent
from shoptalk.state import state


def build_customer_timeline(customer_id: UUID) -> CustomerTimeline:
    events: list[CustomerTimelineEvent] = []

    for message in state.messages.filter_by(customer_id=customer_id):
        events.append(
            CustomerTimelineEvent(
                id=message.id,
                event_type="message",
                title=f"{message.sender.value.title()} message",
                occurred_at=message.received_at,
                detail=message.text,
            )
        )

    for order in state.orders.filter_by(customer_id=customer_id):
        events.append(
            CustomerTimelineEvent(
                id=order.id,
                event_type="order",
                title=order.title,
                occurred_at=order.created_at,
                detail=order.status.value,
            )
        )

    for follow_up in state.follow_ups.filter_by(customer_id=customer_id):
        events.append(
            CustomerTimelineEvent(
                id=follow_up.id,
                event_type="follow_up",
                title=follow_up.title,
                occurred_at=follow_up.due_at or follow_up.created_at,
                detail=follow_up.status.value,
            )
        )

    events.sort(key=lambda event: event.occurred_at)
    return CustomerTimeline(customer_id=customer_id, events=events)
