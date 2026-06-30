from shoptalk.payment_method_hint import payment_method_hint


def test_payment_method_hint():
    assert payment_method_hint("Bank transfer done") == "bank"
