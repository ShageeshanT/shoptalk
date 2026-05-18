from uuid import UUID

from shoptalk.schemas import CustomerProfile
from shoptalk.state import state


def build_customer_profile(customer_id: UUID) -> CustomerProfile | None:
    customer = state.customers.get(customer_id)
    if customer is None:
        return None

    orders = [order for order in state.orders.list() if order.customer_id == customer_id]
    follow_ups = [follow_up for follow_up in state.followups.list() if follow_up.customer_id == customer_id]
    messages = [message for message in state.messages.list() if message.customer_id == customer_id]

    return CustomerProfile(
        customer=customer,
        orders=orders,
        follow_ups=follow_ups,
        messages=sorted(messages, key=lambda message: message.received_at),
    )
