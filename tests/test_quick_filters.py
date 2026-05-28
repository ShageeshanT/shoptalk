from shoptalk.quick_filters import quick_filter_label


def test_known_quick_filter_label():
    assert quick_filter_label("needs_reply") == "Needs reply"


def test_unknown_quick_filter_label():
    assert quick_filter_label("custom_filter") == "Custom Filter"
