from shoptalk.customer_priority_label import customer_priority_label

def test_customer_priority_label_thresholds():
    assert customer_priority_label(80) == "High priority"
    assert customer_priority_label(50) == "Medium priority"
    assert customer_priority_label(20) == "Low priority"

def test_customer_priority_label_invalid_score():
    assert customer_priority_label("nope") == "Watch"
