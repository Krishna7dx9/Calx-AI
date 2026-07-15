def estimate_portions(image, detected_foods):
    """
    Returns portion estimates for each detected food.
    Currently returns 1.0 serving for every food.
    """

    food_list = [
        food.strip()
        for food in detected_foods.split(",")
        if food.strip()
    ]

    portions = []

    for food in food_list:
        portions.append({
            "food_name": food,
            "portion_ratio": 1.0,
            "confidence": 1.0,
        })

    return portions