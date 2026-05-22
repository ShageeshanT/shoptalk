def catalog_reply(product_hint: str | None = None) -> str:
    product_line = f" for {product_hint}" if product_hint else ''
    return f"Hi! I can send our latest catalog{product_line}. Would you like prices too?"


def payment_reminder(amount: float | None = None) -> str:
    if amount is None:
        return "Hi! Gentle reminder about the pending payment for your order."
    return f"Hi! Gentle reminder about the pending payment of LKR {amount:,.0f} for your order."


def delivery_confirmation(window: str | None = None) -> str:
    suffix = f" around {window}" if window else ''
    return f"Hi! Just confirming your delivery details{suffix}."
