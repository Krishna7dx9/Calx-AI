from fastapi import FastAPI, UploadFile, File
from app.fatsecret_client import search_food
from app.food_detector import detect_food
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/nutrition")
def nutrition(food: str):
    return search_food(food)


@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):

    # Validate uploaded file
    if not file.content_type or not file.content_type.startswith("image/"):
        return {"error": "Only image files allowed"}

    try:
        image = await file.read()

        detected_foods = detect_food(image)

        if not detected_foods:
            return {"error": "Food not detected"}

        food_list = [
            food.strip()
            for food in detected_foods.split(",")
            if food.strip()
        ]

        nutrition_results = []
        failed_food_count = 0

        for food in food_list:
            nutrition_data = search_food(food)

            if "error" in nutrition_data:
                failed_food_count += 1
                continue

            nutrition_results.append(nutrition_data)  

        total_calories = 0
        total_protein = 0
        total_fat = 0
        total_carbs = 0
        total_sugar = 0
        total_fiber = 0

        for food in nutrition_results:
            total_calories += food.get("calories", 0)
            total_protein += food.get("protein", 0)
            total_fat += food.get("fat", 0)
            total_carbs += food.get("carbs", 0)
            total_sugar += food.get("sugar", 0)
            total_fiber += food.get("fiber", 0)

        return {
            "foods": nutrition_results,
            "total_detected": len(food_list),
            "total_found": len(nutrition_results),
            "total_failed": failed_food_count,

            "total_nutrition": {
                "calories": round(total_calories, 2),
                "protein": round(total_protein, 2),
                "fat": round(total_fat, 2),
                "carbs": round(total_carbs, 2),
                "sugar": round(total_sugar, 2),
                "fiber": round(total_fiber, 2)
            }
        }

    except Exception as exc:
        return {
            "error": "Image processing failed",
            "details": str(exc)
        }