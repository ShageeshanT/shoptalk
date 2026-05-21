from fastapi.testclient import TestClient

from shoptalk.main import app

client = TestClient(app)


def test_catalog_items_can_be_searched_by_name_or_tag() -> None:
    business_response = client.post("/businesses", json={"name": "Catalog Search Bakery"})
    business_id = business_response.json()["id"]
    client.post("/catalog-items", json={"business_id": business_id, "name": "Chocolate Cake", "tags": ["birthday"]})
    client.post("/catalog-items", json={"business_id": business_id, "name": "Vanilla Cupcakes", "tags": ["party"]})

    response = client.get(f"/catalog-items?business_id={business_id}&search=party")

    assert response.status_code == 200
    items = response.json()
    assert len(items) == 1
    assert items[0]["name"] == "Vanilla Cupcakes"
