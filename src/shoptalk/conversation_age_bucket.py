def conversation_age_bucket(hours):
    return "fresh" if hours <= 2 else "same_day" if hours <= 24 else "old"
