from shoptalk.customer_language_label import label_customer_language


def test_customer_language_label():
    assert label_customer_language("ayubowan friend") == "sinhala"
