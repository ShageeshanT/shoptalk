from shoptalk.alert_dashboard_view import alert_dashboard_view
from shoptalk.seller_alerts import SellerAlert


def test_adds_empty_state_to_clear_dashboard_view():
    view = alert_dashboard_view([])

    assert view["empty_state"] == "No urgent chats right now. Keep selling, tiny chaos goblin contained."
    assert view["cards"] == []


def test_hides_empty_state_when_alert_cards_exist():
    view = alert_dashboard_view([SellerAlert("danger", "Risk", "Refund")])

    assert view["empty_state"] is None
    assert view["cards"][0]["level"] == "danger"
