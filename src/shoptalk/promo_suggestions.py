def promo_suggestion(stock_level: str, repeat_customer: bool = False) -> str:
    if repeat_customer:
        return "Offer a small loyalty discount or bundle upgrade."
    if stock_level == "low_stock":
        return "Avoid discounting scarce items; suggest alternatives instead."
    if stock_level == "in_stock":
        return "Suggest a bundle to increase order value."
    return "Do not promote unavailable items."
