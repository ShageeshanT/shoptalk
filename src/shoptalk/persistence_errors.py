class PersistenceError(RuntimeError):
    """Base error for persistence boundary failures."""


class DuplicateRecordError(PersistenceError):
    """Raised when a unique external identifier is reused."""


class RecordNotFoundError(PersistenceError):
    """Raised when a requested persisted record cannot be found."""
