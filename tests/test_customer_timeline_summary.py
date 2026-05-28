from shoptalk.customer_timeline_summary import timeline_summary


def test_timeline_summary_returns_latest_events():
    assert timeline_summary(["a", "b", "c", "d"], 2) == ["c", "d"]


def test_timeline_summary_handles_zero_limit():
    assert timeline_summary(["a"], 0) == []
