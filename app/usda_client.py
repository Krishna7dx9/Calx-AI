import requests

BASE_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"


def search_food(food_name, api_key):
    response = requests.get(
        BASE_URL,
        params={
            "query": food_name,
            "api_key": api_key,
            "pageSize": 1
        },
        timeout=10
    )

    data = response.json()

    if "foods" not in data or len(data["foods"]) == 0:
        return {"error": "Food not found"}

    food = data["foods"][0]

    nutrients = {}

    for item in food.get("foodNutrients", []):
        name = item.get("nutrientName")
        value = item.get("value", 0)

        if name == "Energy":
            nutrients["calories"] = value

        elif name == "Protein":
            nutrients["protein"] = value

        elif name == "Carbohydrate, by difference":
            nutrients["carbs"] = value

        elif name == "Total lipid (fat)":
            nutrients["fat"] = value

        elif name == "Fiber, total dietary":
            nutrients["fiber"] = value

        elif name == "Total Sugars":
            nutrients["sugar"] = value

    return {
        "food": food["description"],
        **nutrients
    }