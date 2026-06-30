from shoptalk.discount_guard_label import discount_guard_label


def test_discount_guard_label():
    assert discount_guard_label(30) == "too_deep"
