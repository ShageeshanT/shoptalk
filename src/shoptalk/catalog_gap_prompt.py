def catalog_gap_prompt(item_name: str) -> str:
    item = item_name.strip() or "this item"
    return f"Add price, availability, and delivery notes for {item}."
