from shoptalk.metrics_delta import percentage_delta, trend_label


def test_percentage_delta() -> None:
    assert percentage_delta(150, 100) == 50
    assert percentage_delta(75, 100) == -25
    assert percentage_delta(10, 0) is None


def test_trend_label() -> None:
    assert trend_label(10, 0) == "new_activity"
    assert trend_label(0, 0) == "no_activity"
    assert trend_label(12, 10) == "up"
    assert trend_label(8, 10) == "down"
    assert trend_label(10, 10) == "flat"
