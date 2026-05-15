from shoptalk.metrics import business_metrics


def test_business_metrics_returns_expected_keys():
    metrics = business_metrics()
    assert "businesses" in metrics
    assert "open_orders" in metrics
    assert "pending_follow_ups" in metrics
    assert "open_tasks" in metrics
