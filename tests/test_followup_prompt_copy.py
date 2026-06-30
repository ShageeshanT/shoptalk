from shoptalk.followup_prompt_copy import followup_prompt_copy

def test_followup_prompt_copy():
    assert followup_prompt_copy("pickup") == "Could you confirm pickup?"
