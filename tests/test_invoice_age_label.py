from shoptalk.invoice_age_label import classify_invoice_age


def test_classify_invoice_age_labels_key_states():
    assert classify_invoice_age(2) == "Fresh invoice"
    assert classify_invoice_age(3) == "Invoice aging"
    assert classify_invoice_age(10) == "Invoice overdue"
