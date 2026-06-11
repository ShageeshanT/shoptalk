from shoptalk.customer_churn_label import classify_customer_churn


def test_classify_customer_churn_labels_key_states():
    assert classify_customer_churn(-1) == 'Active'
    assert classify_customer_churn(40) == 'Cooling'
    assert classify_customer_churn(100) == 'Churn risk'
