from shoptalk.seller_alerts import SellerAlert
from shoptalk.seller_alert_summary import summarize_seller_alerts


def test_summarizes_alert_counts_and_strongest_level():
    summary = summarize_seller_alerts(
        [
            SellerAlert("warning", "Time sensitive chat", "Need today"),
            SellerAlert("danger", "Customer needs attention", "Refund please"),
            SellerAlert("info", "FYI", "Customer asked for size chart"),
            None,
        ]
    )

    assert summary == {
        "total": 3,
        "danger": 1,
        "warning": 1,
        "info": 1,
        "strongest": "danger",
    }


def test_returns_clear_summary_when_no_alerts():
    assert summarize_seller_alerts([None]) == {
        "total": 0,
        "danger": 0,
        "warning": 0,
        "info": 0,
        "strongest": "clear",
    }
