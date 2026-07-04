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

        # temporary for V3 step-by-step
        return {
            "detected_foods": detected_foods
        }

    except Exception as exc:
        return {
            "error": "Image processing failed",
            "details": str(exc)
        }