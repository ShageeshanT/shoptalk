from datetime import datetime


def response_minutes(received_at: datetime, replied_at: datetime) -> int:
    seconds = max((replied_at - received_at).total_seconds(), 0)
    return round(seconds / 60)


def response_time_label(minutes: int) -> str:
    if minutes <= 5:
        return "fast"
    if minutes <= 60:
        return "normal"
    return "slow"
