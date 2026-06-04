def followup_due_copy(customer_name: str, reason: str) -> str:
    name = customer_name.strip() or "customer"
    why = reason.strip() or "pending conversation"
    return f"Follow up with {name}: {why}."
