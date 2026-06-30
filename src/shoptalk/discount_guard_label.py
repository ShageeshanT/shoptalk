def discount_guard_label(percent):
    return "safe" if percent <= 10 else "manager_review" if percent <= 25 else "too_deep"
