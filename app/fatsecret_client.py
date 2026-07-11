import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("FATSECRET_CLIENT_ID")
CLIENT_SECRET = os.getenv("FATSECRET_CLIENT_SECRET")

if not CLIENT_ID or not CLIENT_SECRET:
    raise RuntimeError(
        "FATSECRET_CLIENT_ID and FATSECRET_CLIENT_SECRET must be set."
    )

TOKEN_URL = "https://oauth.fatsecret.com/connect/token"

_access_token = None
_token_expiry = 0


def get_access_token():
    global _access_token, _token_expiry

    current_time = time.time()

    # Return cached token if still valid
    if _access_token and current_time < _token_expiry:
        return _access_token

    response = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "client_credentials",
            "scope": "basic"
        },
        auth=(CLIENT_ID, CLIENT_SECRET),
        timeout=10
    )

    if response.status_code != 200:
        raise Exception(
            f"Failed to get access token: {response.status_code} {response.text}"
        )

    data = response.json()

    _access_token = data["access_token"]

    # Refresh 60 seconds before expiry
    _token_expiry = current_time + data["expires_in"] - 60

    return _access_token