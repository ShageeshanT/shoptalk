from shoptalk.repository_protocols import BusinessScopedRepository, CreateRepository, GetRepository


def test_repository_protocols_are_importable():
    assert CreateRepository is not None
    assert GetRepository is not None
    assert BusinessScopedRepository is not None
