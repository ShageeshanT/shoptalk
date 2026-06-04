from shoptalk.followup_due_copy import followup_due_copy


def test_followup_due_copy():
    assert followup_due_copy("Kamal", "payment pending") == "Follow up with Kamal: payment pending."


def test_followup_due_copy_defaults():
    assert followup_due_copy("", "") == "Follow up with customer: pending conversation."
