from app.fatsecret_client import get_access_token

def test_get_access_token():
    token = get_access_token()

    assert token is not None
    assert len(token) > 100