def customer_note_prompt(customer_name: str, last_order: str | None = None) -> str:
    name = customer_name.strip() or "this customer"
    if last_order:
        return f"Note anything important about {name}'s {last_order} order."
    return f"Note anything important about {name}."
