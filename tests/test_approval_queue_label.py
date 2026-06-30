from shoptalk.approval_queue_label import approval_queue_label

def test_approval_queue_label():
    assert approval_queue_label(0) == "clear"
    assert approval_queue_label(8) == "busy"
