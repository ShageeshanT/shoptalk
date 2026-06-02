from shoptalk.delivery_window_copy import delivery_window_copy


def test_delivery_window_copy_includes_window():
    assert delivery_window_copy("Saturday", "2pm-4pm") == "Delivery is planned for Saturday during 2pm-4pm."


def test_delivery_window_copy_handles_missing_date():
    assert delivery_window_copy(None) == "Delivery timing is not confirmed yet."
