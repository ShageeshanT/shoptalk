def payment_confirmation_copy(customer_name: str | None = None) -> str:
    name = customer_name.strip() if customer_name else "there"
    return f"Hi {name}, payment received. We will keep your order moving and update you soon."


def payment_reminder_copy(amount: float | None = None, currency: str = "LKR") -> str:
    if amount is None:
        return "Quick reminder: payment is still pending for your order."
    return f"Quick reminder: {currency} {amount:,.0f} is still pending for your order."
