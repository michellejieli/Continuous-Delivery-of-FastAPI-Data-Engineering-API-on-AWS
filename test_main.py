from fastapi.testclient import TestClient
from main import app


def test_root():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Need recipe ideas?"}


def test_recipe_avocado():
    with TestClient(app) as client:
        response = client.get("/recipe/avocado")
        assert response.status_code == 200
        assert response.json() == {
            "ingredients": [
                "avocado",
                "avocados",
                "avocado oil",
                "hass avocados",
                "hass avocado",
                "ripe avocados",
                "large avocados",
                "medium avocado",
                "haas avocados",
                "california avocado",
                "california avocados",
                "small avocados",
                "small avocado",
                "fresh avocado",
                "avocado leaves",
                "florida avocado",
                "fresh california avocado, ripe",
                "fresh california avocados, ripe",
                "fresh california avocados",
                "large california avocados",
                "large california avocado",
                "olivado avocado oil",
                "fresh california avocado",
                "baby avocados",
                "wholly avocado",
                "la tourangelle avocado oil",
                "mission avocados",
                "california haas avocados",
                "fuerte avocado",
                "jumbo avocado",
                "farm rich avocado slices",
                "hidden valley® original ranch® avocado dressing",
                "spectrum avocado oil",
            ],
            "searches": [
                "avocado",
                "avocado salad",
                "chicken avocado",
                "avocado sauce",
                "avocado tomato",
                "avocado sandwich",
                "avocado low carb",
                "avocado onion tomato dip",
                "cold avocado soup",
                "avocado artichoke",
            ],
        }
