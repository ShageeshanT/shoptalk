    from shoptalk.task_age_label import classify_task_age


    def test_classify_task_age_labels_key_states():
        assert classify_task_age(-1) == 'New'
assert classify_task_age(3) == 'Open'
assert classify_task_age(30) == 'Stale'
