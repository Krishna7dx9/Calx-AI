from fastapi import FastAPI
from app.usda_client import search_food
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("USDA_API_KEY")


@app.get("/nutrition")
def nutrition(food: str):
    data = search_food(food, API_KEY)
    return data