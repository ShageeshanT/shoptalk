from shoptalk.currency_label import currency_label

def test_currency_label():
    assert currency_label("lkr") == "Rs"
    assert currency_label("aud") == "AUD"