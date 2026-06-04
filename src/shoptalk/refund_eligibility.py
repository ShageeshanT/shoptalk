def refund_eligibility(hours_until_delivery: int, already_prepared: bool) -> str:
    if already_prepared:
        return "review_required"
    if hours_until_delivery >= 24:
        return "eligible"
    if hours_until_delivery >= 6:
        return "partial_review"
    return "unlikely"
