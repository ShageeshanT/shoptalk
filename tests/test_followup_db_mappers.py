from uuid import uuid4

from shoptalk.db_mappers import followup_from_record, followup_to_record
from shoptalk.schemas import FollowUp


def test_followup_mapper_preserves_status_and_title():
    follow_up = FollowUp(business_id=uuid4(), title="Check payment")
    restored = followup_from_record(followup_to_record(follow_up))
    assert restored.title == "Check payment"
    assert restored.status == follow_up.status
