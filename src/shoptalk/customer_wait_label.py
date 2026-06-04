def customer_wait_label(minutes_waiting: int) -> str:
    if minutes_waiting < 15:
        return "fresh"
    if minutes_waiting < 60:
        return "waiting"
    if minutes_waiting < 240:
        return "late"
    return "overdue"
