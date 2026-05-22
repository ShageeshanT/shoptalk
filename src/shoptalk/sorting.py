from typing import TypeVar

T = TypeVar('T')


def newest_first(items: list[T], field: str = 'created_at') -> list[T]:
    return sorted(items, key=lambda item: getattr(item, field), reverse=True)
