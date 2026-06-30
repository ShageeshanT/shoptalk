from shoptalk.seller_dashboard_hint import build_seller_dashboard_hint


def test_seller_dashboard_hint():
    assert build_seller_dashboard_hint(3, 2) == "3 open orders, 2 pending replies"
