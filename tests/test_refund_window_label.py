from shoptalk.refund_window_label import refund_window_label


def test_refund_window_label():
    assert refund_window_label(10) == "review"
