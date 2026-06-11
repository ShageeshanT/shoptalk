    from shoptalk.approval_friction_label import classify_approval_friction


    def test_classify_approval_friction_labels_key_states():
        assert classify_approval_friction(-1) == 'Clean'
assert classify_approval_friction(1) == 'Minor edits'
assert classify_approval_friction(3) == 'Needs rewrite'
