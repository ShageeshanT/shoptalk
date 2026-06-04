def seller_daily_digest(new_messages: int, open_orders: int, due_followups: int) -> str:
    parts = []
    if new_messages > 0:
        parts.append(f"{new_messages} new message{'s' if new_messages != 1 else ''}")
    if open_orders > 0:
        parts.append(f"{open_orders} open order{'s' if open_orders != 1 else ''}")
    if due_followups > 0:
        parts.append(f"{due_followups} follow-up{'s' if due_followups != 1 else ''} due")
    if not parts:
        return "All quiet. No customer action needed right now."
    return "Today: " + ", ".join(parts) + "."
