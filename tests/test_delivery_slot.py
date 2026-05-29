from datetime import datetime

from shoptalk.delivery_slot import delivery_slot_label, delivery_slot_summary


def test_delivery_slot_label_buckets_times() -> None:
    assert delivery_slot_label(None) == "delivery_not_set"
    assert delivery_slot_label(datetime(2026, 5, 29, 9, 30)) == "morning_delivery"
    assert delivery_slot_label(datetime(2026, 5, 29, 14, 30)) == "afternoon_delivery"
    assert delivery_slot_label(datetime(2026, 5, 29, 19, 30)) == "evening_delivery"
    assert delivery_slot_label(datetime(2026, 5, 29, 23, 30)) == "late_delivery"


def test_delivery_slot_summary_is_readable() -> None:
    assert delivery_slot_summary(datetime(2026, 5, 29, 19, 30)) == "evening delivery"
