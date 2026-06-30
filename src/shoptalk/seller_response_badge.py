def seller_response_badge(minutes):
    return "instant" if minutes <= 5 else "fast" if minutes <= 30 else "slow"
