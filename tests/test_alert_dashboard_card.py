from shoptalk.alert_dashboard_card import alert_dashboard_card
from shoptalk.seller_alerts import SellerAlert


def test_builds_dashboard_card_payload_for_alert():
    alert = SellerAlert("warning", "Time sensitive chat", "Need today")

    assert alert_dashboard_card(alert) == {
        "level": "warning",
        "title": "Time sensitive chat",
        "message": "Need today",
        "cta": "Check timing and confirm the next step with the customer.",
        "sla_minutes": 30,
    }
