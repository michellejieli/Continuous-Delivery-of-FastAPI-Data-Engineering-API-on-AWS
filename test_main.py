from fastapi.testclient import TestClient
from main import app


def test_root():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        # assert response.json() == {"message": "Need recipe ideas?"}


def test_recipe_avocado():
    with TestClient(app) as client:
        response = client.get("/recipe/avocado")
        assert response.status_code == 200
        assert response.json() == {
            "results": [
                {"type": "ingredient", "display": "avocado", "search_value": "avocado"},
                {
                    "type": "ingredient",
                    "display": "avocado toast",
                    "search_value": "avocado toast",
                },
            ]
        }
