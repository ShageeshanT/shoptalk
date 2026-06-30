from shoptalk.approval_wait_label import approval_wait_label


def test_approval_wait_label():
    assert approval_wait_label(9) == "stale"
