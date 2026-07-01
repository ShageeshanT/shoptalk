from shoptalk.seller_alert_digest import seller_alert_digest
from shoptalk.seller_alerts import SellerAlert


def test_returns_clear_digest_without_alerts():
    assert seller_alert_digest([None]) == "No active seller alerts."


def test_returns_digest_with_count_strongest_and_next_action():
    digest = seller_alert_digest(
        [
            SellerAlert("warning", "Time sensitive chat", "Need today"),
            SellerAlert("danger", "Customer needs attention", "Refund request"),
        ]
    )

    assert digest == (
        "2 active alerts. Strongest: danger. Next: "
        "Check timing and confirm the next step with the customer."
    )
