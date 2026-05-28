from shoptalk.delivery_slots import format_delivery_slot, is_same_day_slot


def test_formats_delivery_slot():
    assert format_delivery_slot("today", "5pm-7pm") == "Today · 5pm-7pm"


def test_detects_same_day_slot():
    assert is_same_day_slot("Tonight")
    assert not is_same_day_slot("Friday")
