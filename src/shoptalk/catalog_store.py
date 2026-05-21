from uuid import UUID

from shoptalk.schemas import CatalogItemCreate, CatalogItemRecord
from shoptalk.storage import InMemoryRepository

catalog_items: InMemoryRepository[CatalogItemRecord] = InMemoryRepository()


def create_catalog_item(payload: CatalogItemCreate) -> CatalogItemRecord:
    item = CatalogItemRecord(**payload.model_dump())
    catalog_items.add(item)
    return item


def list_catalog_items(
    business_id: UUID, available_only: bool = True, search: str | None = None
) -> list[CatalogItemRecord]:
    items = [item for item in catalog_items.list() if item.business_id == business_id]
    if available_only:
        items = [item for item in items if item.available]
    if search:
        query = search.lower().strip()
        items = [
            item
            for item in items
            if query in item.name.lower() or any(query in tag.lower() for tag in item.tags)
        ]
    return items


def update_catalog_item(item_id: UUID, payload: CatalogItemCreate) -> CatalogItemRecord | None:
    existing = catalog_items.get(item_id)
    if existing is None:
        return None
    updated = existing.model_copy(update=payload.model_dump())
    catalog_items.add(updated)
    return updated
