from shoptalk.approval_bottleneck_label import classify_approval_bottleneck


def test_classify_approval_bottleneck_labels_key_states():
    assert classify_approval_bottleneck(2) == "Clear approvals"
    assert classify_approval_bottleneck(3) == "Approval queue"
    assert classify_approval_bottleneck(10) == "Approval bottleneck"
