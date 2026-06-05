from shoptalk.invoice_number_label import invoice_number_label

def test_invoice_number_label():
    assert invoice_number_label("INV-1")=="Invoice INV-1"