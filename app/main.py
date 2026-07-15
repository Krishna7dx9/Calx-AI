from fastapi import FastAPI, UploadFile, File
from app.fatsecret_client import search_food
from app.food_detector import detect_food
import os
from dotenv import load_dotenv
from app.portion_estimator import estimate_portions
from app.nutrition_formatter import format_nutrition_response
from app.nutrition_aggregator import aggregate_nutrition

load_dotenv()

app = FastAPI()

@app.get("/nutrition")
def nutrition(food: str):
    nutrition_data = search_food(food)

    if "error" in nutrition_data:
        return nutrition_data

    return format_nutrition_response(nutrition_data)

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):

    # Validate uploaded file
    if not file.content_type or not file.content_type.startswith("image/"):
        return {"error": "Only image files allowed"}

    try:
        image = await file.read()

        detected_foods = detect_food(image)
        portion_estimates = estimate_portions(image, detected_foods)

        if not detected_foods:
            return {"error": "Food not detected"}

        food_list = [
            food.strip()
            for food in detected_foods.split(",")
            if food.strip()
        ]

        nutrition_results = []
        failed_food_count = 0

        for food, portion in zip(food_list, portion_estimates):
            nutrition_data = search_food(food)

            if "error" in nutrition_data:
                failed_food_count += 1
                continue
                
            nutrition_results.append(
                format_nutrition_response(nutrition_data, portion)
            )

        total_nutrition = aggregate_nutrition(nutrition_results)

        return {
            "foods": nutrition_results,
            "total_detected": len(food_list),
            "total_found": len(nutrition_results),
            "total_failed": failed_food_count,

            "total_nutrition": total_nutrition
        }

    except Exception as exc:
        return {
            "error": "Image processing failed",
            "details": str(exc)
        }