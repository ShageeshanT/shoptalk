def onboarding_checklist(has_catalog: bool, has_payment_details: bool, has_business_hours: bool) -> list[str]:
    tasks = []
    if not has_catalog:
        tasks.append("add_catalog")
    if not has_payment_details:
        tasks.append("add_payment_details")
    if not has_business_hours:
        tasks.append("set_business_hours")
    return tasks


def onboarding_complete(has_catalog: bool, has_payment_details: bool, has_business_hours: bool) -> bool:
    return not onboarding_checklist(has_catalog, has_payment_details, has_business_hours)
