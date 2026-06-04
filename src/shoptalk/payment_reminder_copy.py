def payment_reminder_copy(amount_due: float, due_label: str = "today") -> str:
    if amount_due <= 0:
        return "No payment is due right now."
    return f"Gentle reminder: Rs {amount_due:,.2f} is due {due_label}."
