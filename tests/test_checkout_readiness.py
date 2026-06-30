from shoptalk.checkout_readiness import checkout_readiness

def test_checkout_readiness():
    assert checkout_readiness(True, True, True) == "ready"
    assert checkout_readiness(True, False, True) == "missing details"
