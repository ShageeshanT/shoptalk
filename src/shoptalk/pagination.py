from dataclasses import dataclass
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar('T')


@dataclass(frozen=True)
class PageResult[T]:
    items: list[T]
    total: int
    limit: int
    offset: int


def paginate(items: Sequence[T], limit: int = 50, offset: int = 0) -> PageResult[T]:
    safe_limit = max(1, min(limit, 100))
    safe_offset = max(0, offset)
    return PageResult(
        items=list(items)[safe_offset:safe_offset + safe_limit],
        total=len(items),
        limit=safe_limit,
        offset=safe_offset,
    )
