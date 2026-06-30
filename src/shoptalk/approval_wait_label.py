def approval_wait_label(hours):
    return "new" if hours < 1 else "waiting" if hours < 8 else "stale"
