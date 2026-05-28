from shoptalk.followup_copy import followup_copy


def test_followup_copy_payment():
    assert "payment" in followup_copy("payment")


def test_followup_copy_delivery():
    assert "delivery" in followup_copy("delivery")


def test_followup_copy_default():
    assert followup_copy("other").startswith("Send a polite")
