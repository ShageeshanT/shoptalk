from shoptalk.daily_sales_snapshot import daily_sales_snapshot


def test_daily_sales_snapshot_quiet():
    assert daily_sales_snapshot(0, 0, 0)["status"] == "quiet"


def test_daily_sales_snapshot_needs_collection():
    assert daily_sales_snapshot(5000, 1, 2)["status"] == "needs_collection"
