from shoptalk.seller_tasks import seller_tasks


def test_seller_tasks_ordering():
    assert seller_tasks(True, True, True) == ["reply_to_customer", "collect_payment", "confirm_delivery"]


def test_seller_tasks_empty():
    assert seller_tasks(False, False, False) == []
