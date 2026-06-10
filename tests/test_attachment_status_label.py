from shoptalk.attachment_status_label import attachment_status_label

def test_attachment_status_label_thresholds():
    assert attachment_status_label(3) == 'Many attachments'
    assert attachment_status_label(1) == 'Has attachment'
    assert attachment_status_label(0) == 'No attachments'

def test_attachment_status_label_invalid_value():
    assert attachment_status_label("bad") == 'No attachments'
