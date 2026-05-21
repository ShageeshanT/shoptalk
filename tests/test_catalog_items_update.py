from fastapi.testclient import TestClient

from shoptalk.main import app

client = TestClient(app)


def test_catalog_item_can_be_updated() -> None:
    business_response = client.post("/businesses", json={"name": "Catalog Update Bakery"})
    business_id = business_response.json()["id"]
    created = client.post(
        "/catalog-items", json={"business_id": business_id, "name": "Brownie Box", "price": 1200}
    ).json()

    response = client.put(
        f"/catalog-items/{created['id']}",
        json={"business_id": business_id, "name": "Premium Brownie Box", "price": 1500, "available": False},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Premium Brownie Box"
    assert body["price"] == 1500
    assert body["available"] is False
