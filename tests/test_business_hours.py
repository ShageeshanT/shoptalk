from datetime import datetime, timezone

from shoptalk.business_hours import is_within_business_hours, reply_window_label


def test_is_within_business_hours_for_colombo_weekday() -> None:
    assert is_within_business_hours(datetime(2026, 5, 29, 5, 0, tzinfo=timezone.utc))


def test_is_within_business_hours_rejects_after_hours_and_sunday() -> None:
    assert not is_within_business_hours(datetime(2026, 5, 29, 15, 0, tzinfo=timezone.utc))
    assert not is_within_business_hours(datetime(2026, 5, 31, 5, 0, tzinfo=timezone.utc))


def test_reply_window_label() -> None:
    assert reply_window_label(datetime(2026, 5, 29, 5, 0, tzinfo=timezone.utc)) == "business_hours"
