from shoptalk.alert_resolution_status import alert_resolution_status


def test_resolved_alert_status_wins():
    assert alert_resolution_status(True, waiting_on_customer=True) == "resolved"


def test_waiting_on_customer_status():
    assert alert_resolution_status(False, waiting_on_customer=True) == "waiting_on_customer"


def test_open_alert_needs_seller_reply():
    assert alert_resolution_status(False) == "needs_seller_reply"
