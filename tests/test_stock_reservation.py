from shoptalk.stock_reservation import stock_reservation_status


def test_stock_reservation_reserved():
    assert stock_reservation_status(2, 5) == "reserved"


def test_stock_reservation_partial():
    assert stock_reservation_status(7, 5) == "partial_only"
