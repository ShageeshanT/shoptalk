from shoptalk.approval_labels import approval_label


def test_approval_label_known_values():
    assert approval_label("reply") == "Reply draft"
    assert approval_label("order") == "Order draft"


def test_approval_label_default():
    assert approval_label("unknown") == "Review item"
