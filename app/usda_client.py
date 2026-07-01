import requests

BASE_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

def search_food(food_name, api_key):
    response = requests.get(
        BASE_URL,
        params={
            "query": food_name,
            "api_key": api_key,
            "pageSize": 1  
        }
    )

    data = response.json()

    if "foods" in data and len(data["foods"]) > 0:
        return data["foods"][0]   # take only first result

    return {}