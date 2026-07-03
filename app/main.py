from fastapi import FastAPI, UploadFile, File
from app.usda_client import search_food
import os
from dotenv import load_dotenv
from app.food_detector import detect_food

# Load variables from .env file
load_dotenv()

app = FastAPI()

# Read USDA API key from environment
API_KEY = os.getenv("USDA_API_KEY")


# nutrition endpoint
@app.get("/nutrition")
def nutrition(food: str):
    data = search_food(food, API_KEY)
    return data


# image upload endpoint
@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):

    # Check whether uploaded file is image
    if not file.content_type or not file.content_type.startswith("image/"):
        return {"error": "Only image files allowed"}

    image = await file.read()

    food_name = detect_food(image)

    nutrition_data = search_food(food_name, API_KEY)

    return nutrition_data