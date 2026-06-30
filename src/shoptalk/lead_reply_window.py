def lead_reply_window(minutes):
    return "now" if minutes <= 15 else "today" if minutes <= 240 else "later"
