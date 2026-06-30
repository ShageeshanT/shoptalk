from shoptalk.payment_receipt_label import label_payment_receipt


def test_payment_receipt_label():
    assert label_payment_receipt(True) == "received"
