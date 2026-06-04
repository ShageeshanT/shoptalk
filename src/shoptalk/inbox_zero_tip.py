def inbox_zero_tip(open_threads: int, overdue_threads: int) -> str:
    if open_threads <= 0:
        return "Inbox is clear."
    if overdue_threads > 0:
        return "Start with overdue customer threads."
    return "Reply to the oldest open customer thread first."
