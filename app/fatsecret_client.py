import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("FATSECRET_CLIENT_ID") or ""
CLIENT_SECRET = os.getenv("FATSECRET_CLIENT_SECRET") or ""

if not CLIENT_ID or not CLIENT_SECRET:
    raise RuntimeError(
        "FATSECRET_CLIENT_ID and FATSECRET_CLIENT_SECRET must be set."
    )

TOKEN_URL = "https://oauth.fatsecret.com/connect/token"
SEARCH_URL = "https://platform.fatsecret.com/rest/server.api"

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

# FatSecret REST API endpoint
SEARCH_URL = "https://platform.fatsecret.com/rest/server.api"


def search_food(food_name):
    """
    Search a food inside FatSecret.

    Input:
        "rice"

    Output:
        Nutrition information of the best matching food.
    """

    # -----------------------------
    # STEP 1
    # Get OAuth token
    # -----------------------------
    token = get_access_token()

    # -----------------------------
    # STEP 2
    # Call FatSecret Search API
    # -----------------------------
    response = requests.get(
        SEARCH_URL,
        headers={
            # OAuth Bearer token
            "Authorization": f"Bearer {token}"
        },
        params={
            # FatSecret search endpoint
            "method": "foods.search",

            # Food detected by AI
            "search_expression": food_name,

            # JSON response
            "format": "json",

            # Only best result
            "max_results": 1,
        },
        timeout=10
    )

    if response.status_code != 200:
        return {
            "error": "Search failed",
            "details": response.text
        }

    data = response.json()

    # -----------------------------
    # STEP 3
    # Extract foods section
    # -----------------------------
    # DEBUG: Remove after verifying the API response
    print(response.json())  
    
    foods = data.get("foods", {}).get("food")

    if not foods:
        return {
            "error": "Food not found"
        }

    # FatSecret returns
    #
    # list
    # when multiple foods exist
    #
    # dict
    # when only one food exists

    if isinstance(foods, list):
        food = foods[0]
    else:
        food = foods

    # Return raw response for now.
    # We'll normalize it in the next commit.
    return food