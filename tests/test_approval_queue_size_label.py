from shoptalk.approval_queue_size_label import label_approval_queue_size


def test_approval_queue_size_label():
    assert label_approval_queue_size(10) == "busy"
