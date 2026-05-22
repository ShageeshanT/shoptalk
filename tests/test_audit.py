from shoptalk.audit import AuditEvent, audit_label


def test_audit_label_combines_actor_action_and_resource() -> None:
    event = AuditEvent(action="created", resource_type="order")
    assert audit_label(event) == "seller:created:order"
