from shoptalk.alert_sorting import sort_alerts_by_priority
from shoptalk.seller_alerts import SellerAlert


def test_sorts_danger_alerts_before_warning_and_info():
    info = SellerAlert("info", "FYI", "Size chart")
    warning = SellerAlert("warning", "Timing", "Need today")
    danger = SellerAlert("danger", "Risk", "Refund")

    assert sort_alerts_by_priority([info, warning, danger]) == [danger, warning, info]


def test_returns_empty_list_for_empty_input():
    assert sort_alerts_by_priority([]) == []
