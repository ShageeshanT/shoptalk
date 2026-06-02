from shoptalk.refund_policy_copy import refund_policy_copy


def test_refund_policy_copy_for_early_status():
    assert "before preparation" in refund_policy_copy("new_inquiry")


def test_refund_policy_copy_for_in_progress_status():
    assert "limited" in refund_policy_copy("ready")
