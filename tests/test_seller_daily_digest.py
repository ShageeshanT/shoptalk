from shoptalk.seller_daily_digest import seller_daily_digest


def test_seller_daily_digest_empty():
    assert seller_daily_digest(0, 0, 0) == "All quiet. No customer action needed right now."


def test_seller_daily_digest_combines_counts():
    assert seller_daily_digest(2, 1, 3) == "Today: 2 new messages, 1 open order, 3 follow-ups due."
