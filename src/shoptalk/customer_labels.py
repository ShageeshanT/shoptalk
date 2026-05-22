from shoptalk.schemas import Customer


def customer_display_label(customer: Customer) -> str:
    if customer.phone:
        return f"{customer.name} ({customer.phone})"
    if customer.channel_id:
        return f"{customer.name} ({customer.channel}:{customer.channel_id})"
    return customer.name
