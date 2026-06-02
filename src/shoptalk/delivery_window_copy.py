def delivery_window_copy(date: str | None, window: str | None = None) -> str:
    if date and window:
        return f"Delivery is planned for {date} during {window}."
    if date:
        return f"Delivery is planned for {date}."
    return "Delivery timing is not confirmed yet."
