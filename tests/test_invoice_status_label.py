from shoptalk.invoice_status_label import invoice_status_label

def test_invoice_status_label_known_values():
    assert invoice_status_label('sent') == 'Invoice sent'
    assert invoice_status_label('paid') == 'Invoice paid'
    assert invoice_status_label('overdue') == 'Invoice overdue'

def test_invoice_status_label_unknown_value():
    assert invoice_status_label("") == 'Invoice draft'
