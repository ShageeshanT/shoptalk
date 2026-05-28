from __future__ import annotations


def compact_whatsapp_text(text: str) -> str:
    return " ".join(text.split())


def format_order_update(customer_name: str, order_title: str, status: str) -> str:
    name = customer_name.strip() or "there"
    title = compact_whatsapp_text(order_title)
    return f"Hi {name}, quick update: your {title} order is now {status}."


def format_payment_instruction(amount: float, method: str) -> str:
    return f"Please pay LKR {amount:,.0f} via {method.strip()}. Send the receipt here once done."
