from shoptalk.customer_profile_badge import customer_profile_badge


def test_customer_profile_badge_vip():
    assert customer_profile_badge(10, 0) == "vip"


def test_customer_profile_badge_lead():
    assert customer_profile_badge(0, 0) == "lead"
