from shoptalk.db_models import Base, FollowUpRecord


def test_followup_table_is_registered():
    assert "follow_ups" in Base.metadata.tables
    assert FollowUpRecord.__tablename__ == "follow_ups"
