from shoptalk.schemas import Business, Customer, FollowUp, Order
from shoptalk.state import state


def seed_demo_data() -> None:
    if state.businesses.list():
        return

    business = state.businesses.add(Business(name="Demo Home Bakery"))
    customer = state.customers.add(
        Customer(
            business_id=business.id,
            name="Nimali",
            channel="whatsapp",
            channel_id="demo-customer-1",
            notes="Wants birthday cakes and delivery updates.",
        )
    )
    order = state.orders.add(
        Order(
            business_id=business.id,
            customer_id=customer.id,
            title="1kg chocolate birthday cake",
            total_amount=4500,
            delivery_date="Saturday",
            notes="Ask for final cake text before confirming.",
        )
    )
    state.follow_ups.add(
        FollowUp(
            business_id=business.id,
            customer_id=customer.id,
            order_id=order.id,
            title="Confirm cake text and delivery address",
        )
    )
