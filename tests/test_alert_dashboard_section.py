from shoptalk.alert_dashboard_section import alert_dashboard_section
from shoptalk.seller_alerts import SellerAlert


def test_builds_sorted_dashboard_section_with_summary():
    info = SellerAlert("info", "FYI", "Size chart")
    danger = SellerAlert("danger", "Risk", "Refund")

    section = alert_dashboard_section([info, danger])

    assert section["summary"]["strongest"] == "danger"
    assert section["queue_label"] == "watch"
    assert [card["level"] for card in section["cards"]] == ["danger", "info"]


def test_builds_clear_section_without_alerts():
    section = alert_dashboard_section([])

    assert section["summary"]["strongest"] == "clear"
    assert section["queue_label"] == "clear"
    assert section["cards"] == []
