def handoff_reason(is_angry: bool, asks_discount: bool, payment_issue: bool) -> str:
    if is_angry:
        return "angry_customer"
    if payment_issue:
        return "payment_issue"
    if asks_discount:
        return "discount_request"
    return "no_handoff_needed"
