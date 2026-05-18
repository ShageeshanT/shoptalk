from uuid import UUID

from shoptalk.schemas import CatalogItemCreate, CatalogItemRecord
from shoptalk.storage import InMemoryStore

catalog_items: InMemoryStore[CatalogItemRecord] = InMemoryStore()


def create_catalog_item(payload: CatalogItemCreate) -> CatalogItemRecord:
    item = CatalogItemRecord(**payload.model_dump())
    catalog_items.add(item)
    return item


def list_catalog_items(business_id: UUID, available_only: bool = True) -> list[CatalogItemRecord]:
    items = [item for item in catalog_items.list() if item.business_id == business_id]
    if available_only:
        items = [item for item in items if item.available]
    return items
