from shoptalk.db_models import Base, BusinessRecord, CustomerRecord, OrderRecord


def test_core_tables_are_registered():
    assert {"businesses", "customers", "orders"}.issubset(Base.metadata.tables)
    assert BusinessRecord.__tablename__ == "businesses"
    assert CustomerRecord.__tablename__ == "customers"
    assert OrderRecord.__tablename__ == "orders"
