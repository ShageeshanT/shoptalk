def eta_label(days_until_delivery: int | None) -> str:
    if days_until_delivery is None:
        return "unscheduled"
    if days_until_delivery < 0:
        return "overdue"
    if days_until_delivery == 0:
        return "today"
    if days_until_delivery <= 2:
        return "soon"
    return "scheduled"
