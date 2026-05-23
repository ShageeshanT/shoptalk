from shoptalk.persistence_errors import DuplicateRecordError, PersistenceError, RecordNotFoundError


def test_persistence_errors_share_base_type():
    assert issubclass(DuplicateRecordError, PersistenceError)
    assert issubclass(RecordNotFoundError, PersistenceError)
