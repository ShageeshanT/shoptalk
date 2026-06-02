from datetime import datetime, timedelta, timezone

from shoptalk.response_time import response_minutes, response_time_label


def test_response_minutes_rounds_elapsed_time():
    start = datetime(2026, 1, 1, tzinfo=timezone.utc)
    assert response_minutes(start, start + timedelta(minutes=12, seconds=20)) == 12


def test_response_time_label_buckets_minutes():
    assert response_time_label(3) == "fast"
    assert response_time_label(30) == "normal"
    assert response_time_label(90) == "slow"
