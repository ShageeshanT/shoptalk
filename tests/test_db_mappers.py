from shoptalk.db_mappers import business_from_record, business_to_record
from shoptalk.schemas import Business


def test_business_mapper_round_trips_core_fields():
    business = Business(name="Kavi Bakes")
    record = business_to_record(business)
    restored = business_from_record(record)
    assert restored.id == business.id
    assert restored.name == "Kavi Bakes"
    assert restored.currency == "LKR"
