from uuid import UUID

from shoptalk.enums import FollowUpStatus, OrderStatus
from shoptalk.schemas import DailyBrief
from shoptalk.state import state


def daily_brief(business_id: UUID | None = None) -> DailyBrief:
    orders = state.orders.list()
    follow_ups = state.follow_ups.list()
    messages = state.messages.list()
    if business_id is not None:
        orders = [order for order in orders if order.business_id == business_id]
        follow_ups = [follow_up for follow_up in follow_ups if follow_up.business_id == business_id]
        messages = [message for message in messages if message.business_id == business_id]

    open_orders = sum(1 for order in orders if order.status not in {OrderStatus.DELIVERED, OrderStatus.CANCELLED})
    pending_follow_ups = sum(1 for follow_up in follow_ups if follow_up.status == FollowUpStatus.PENDING)
    urgent_messages = sum(1 for message in messages if "urgent" in message.text.lower())

    actions: list[str] = []
    if pending_follow_ups:
        actions.append(f"Review {pending_follow_ups} pending follow-up(s).")
    if open_orders:
        actions.append(f"Check {open_orders} open order(s) before promising delivery times.")
    if urgent_messages:
        actions.append(f"Handle {urgent_messages} urgent customer message(s) first.")
    if not actions:
        actions.append("No urgent sales desk actions right now.")

    return DailyBrief(
        business_id=business_id,
        open_orders=open_orders,
        pending_follow_ups=pending_follow_ups,
        urgent_messages=urgent_messages,
        suggested_actions=actions,
    )
