from fastapi import FastAPI
from app.usda_client import search_food

app = FastAPI()

API_KEY = "cEmlpRnULNQBraiZEF1WTpKZjKDdZwsAqGwG8jtx"

@app.get("/nutrition")
def nutrition(food: str):
    data = search_food(food, API_KEY)
    return data