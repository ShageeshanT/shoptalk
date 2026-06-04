from shoptalk.refund_eligibility import refund_eligibility


def test_refund_eligibility_eligible():
    assert refund_eligibility(30, False) == "eligible"


def test_refund_eligibility_prepared_requires_review():
    assert refund_eligibility(30, True) == "review_required"
