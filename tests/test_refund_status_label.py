from shoptalk.refund_status_label import refund_status_label

def test_refund_status_label():
    assert refund_status_label(True)=="Refund eligible"