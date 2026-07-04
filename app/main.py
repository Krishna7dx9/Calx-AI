from fastapi import FastAPI, UploadFile, File
from app.usda_client import search_food
from app.food_detector import detect_food
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("USDA_API_KEY")


@app.get("/nutrition")
def nutrition(food: str):
    return search_food(food, API_KEY)


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

        for food in food_list:
            nutrition_data = search_food(food, API_KEY)

            if "error" not in nutrition_data:
                nutrition_results.append(nutrition_data)

        return {
            "foods": nutrition_results,
            "total_detected": len(food_list),
            "total_found": len(nutrition_results)
        }

    except Exception as exc:
        return {
            "error": "Image processing failed",
            "details": str(exc)
        }