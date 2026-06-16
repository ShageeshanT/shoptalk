"""Service for matching customer product requests against the business catalog."""

from __future__ import annotations

import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class CatalogItem:
    """A product in the business catalog."""

    id: str
    name: str
    description: str
    price: float | None
    available: bool = True


@dataclass
class MatchResult:
    """Result of a catalog match operation."""

    item: CatalogItem | None
    score: float  # 0.0 = no match, 1.0 = exact match
    matched_name: str


class CatalogService:
    """Matches free-text product descriptions against a business catalog.

    Uses simple token overlap scoring. Phase 3 will upgrade this to
    embedding-based semantic search.
    """

    def match(self, query: str, catalog: list[CatalogItem]) -> MatchResult:
        """Find the best matching catalog item for a query string.

        Args:
            query: Free-text product description from the customer message.
            catalog: List of available catalog items.

        Returns:
            MatchResult with the best match and a confidence score.
        """
        if not catalog:
            return MatchResult(item=None, score=0.0, matched_name=query)

        query_tokens = set(query.lower().split())
        best_item: CatalogItem | None = None
        best_score = 0.0

        for item in catalog:
            if not item.available:
                continue
            item_tokens = set(item.name.lower().split())
            if not item_tokens:
                continue
            overlap = len(query_tokens & item_tokens)
            score = overlap / max(len(query_tokens), len(item_tokens))
            if score > best_score:
                best_score = score
                best_item = item

        return MatchResult(
            item=best_item,
            score=best_score,
            matched_name=best_item.name if best_item else query,
        )
