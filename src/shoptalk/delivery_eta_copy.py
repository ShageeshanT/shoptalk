def delivery_eta_copy(window_label: str, location: str | None = None) -> str:
    window = window_label.strip() or "the agreed delivery window"
    if location and location.strip():
        return f"Delivery is planned for {window} to {location.strip()}."
    return f"Delivery is planned for {window}."
