def message_followup_flag(text):
    return any(word in text.lower() for word in ("remind", "follow up", "later"))
