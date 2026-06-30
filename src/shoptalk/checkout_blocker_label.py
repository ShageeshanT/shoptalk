def checkout_blocker_label(missing_fields):
    return "ready" if not missing_fields else "needs_" + missing_fields[0]
