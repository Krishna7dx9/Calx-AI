from fastapi import FastAPI, UploadFile, File
from app.usda_client import search_food
from app.service import detect_food
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

app = FastAPI()

# Read USDA API key from environment
API_KEY = os.getenv("USDA_API_KEY")


# Existing nutrition endpoint
@app.get("/nutrition")
def nutrition(food: str):
    data = search_food(food, API_KEY)
    return data


# New image upload endpoint
@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):

    detected_food = detect_food(file.filename)

    data = search_food(
        detected_food,
        API_KEY
    )

    return data