from resources.item import *

def test_get_item(client):
    response = client.get("items/Chicken Platter")

    assert response.status_code == 200
    assert response.json == {
        "id": 1,
        "title": "Python for Dummies"
    }