    from shoptalk.sales_goal_label import classify_sales_goal


    def test_classify_sales_goal_labels_key_states():
        assert classify_sales_goal(-1) == 'Behind'
assert classify_sales_goal(50) == 'Tracking'
assert classify_sales_goal(100) == 'Hit'
