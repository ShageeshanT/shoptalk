from shoptalk.onboarding_checklist import onboarding_checklist, onboarding_complete


def test_onboarding_checklist_lists_missing_setup():
    assert onboarding_checklist(False, True, False) == ["add_catalog", "set_business_hours"]


def test_onboarding_complete_when_all_setup_exists():
    assert onboarding_complete(True, True, True) is True
