from shoptalk.checkout_blocker_label import checkout_blocker_label


def test_checkout_blocker_label():
    assert checkout_blocker_label(["address"]) == "needs_address"
