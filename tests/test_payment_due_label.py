from shoptalk.payment_due_label import payment_due_label

def test_payment_due_label():
    assert payment_due_label(True,2)=="Payment due in 2 day(s)"