from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CalX AI is running"}

@app.get("/nutrition")
def get_nutrition(food: str):
    return {
        "food": food,
        "calories": "coming soon"
    }