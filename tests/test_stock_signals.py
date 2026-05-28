from shoptalk.stock_signals import should_warn_low_stock, stock_signal


def test_stock_signal_out_of_stock():
    assert stock_signal(0) == "out_of_stock"


def test_stock_signal_low_stock():
    assert stock_signal(2) == "low_stock"


def test_stock_signal_available():
    assert stock_signal(10) == "available"
    assert not should_warn_low_stock(10)
