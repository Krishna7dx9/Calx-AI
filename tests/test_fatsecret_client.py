from app.fatsecret_client import get_access_token, search_food

def test_get_access_token():
    token = get_access_token()

    assert token is not None
    assert len(token) > 100

def test_search_food():

    result = search_food("rice")

    assert "food_name" in result