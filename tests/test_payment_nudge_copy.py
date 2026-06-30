from shoptalk.payment_nudge_copy import payment_nudge_copy

def test_payment_nudge_copy():
    assert payment_nudge_copy("Nima").startswith("Hi Nima")
