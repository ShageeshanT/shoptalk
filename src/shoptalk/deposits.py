def deposit_due(total_amount: float | None, deposit_percent: int = 50) -> float | None:
    if total_amount is None:
        return None
    percent = max(0, min(deposit_percent, 100))
    return round(total_amount * percent / 100, 2)
