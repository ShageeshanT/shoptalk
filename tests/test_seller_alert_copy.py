from shoptalk.seller_alert_copy import seller_alert_cta
from shoptalk.seller_alerts import SellerAlert


def test_returns_safe_copy_when_no_alert_exists():
    assert seller_alert_cta(None) == "No urgent action needed."


def test_returns_danger_next_action_copy():
    alert = SellerAlert("danger", "Customer needs attention", "Refund request")
    assert seller_alert_cta(alert) == "Reply now and resolve the risk before taking new orders."


def test_returns_warning_next_action_copy():
    alert = SellerAlert("warning", "Time sensitive chat", "Need today")
    assert seller_alert_cta(alert) == "Check timing and confirm the next step with the customer."


def test_returns_neutral_copy_for_info_alerts():
    alert = SellerAlert("info", "Review later", "Asked for colour chart")
    assert seller_alert_cta(alert) == "Review when the current queue is stable."
