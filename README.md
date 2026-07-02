# Calx-AI

AI-powered nutrition tracking and calorie estimation system built incrementally from nutrition search to adaptive image-based calorie estimation.

## Current Status

Current version: **V1 — Text-based Nutrition Lookup**

Implemented:

* Food search using text input
* USDA FoodData Central API integration
* Nutrition extraction
* Secure API key handling with `.env`
* Modular FastAPI backend
* Error handling for missing food results

Extracted nutrients:

* Calories
* Protein
* Carbohydrates
* Fat
* Sugar
* Fiber

---

## System Architecture

User Input

↓

FastAPI Backend

↓

USDA Client Layer

↓

USDA FoodData Central API

↓

Processed Nutrition Response

---

## Tech Stack

Backend:

* Python
* FastAPI
* Requests
* Python-dotenv

Nutrition Source:

* USDA FoodData Central API

Future:

* Flutter
* Computer Vision
* Supabase

---

## Sample API Request

```bash
GET /nutrition?food=rice
```

Sample Response:

```json
{
  "food":"RICE",
  "protein":3.47,
  "fat":2.43,
  "carbs":26.4,
  "calories":139,
  "sugar":1.39,
  "fiber":1.4
}
```

---

## Roadmap

🟢 V1 — Text-based nutrition lookup ✓

🟡 V2 — AI food image recognition

🟠 V3 — Portion estimation

🔴 V4 — Adaptive depth-based calorie estimation

---

## Future Vision

CalX-AI will evolve into a system capable of:

* Food recognition from images
* Portion estimation
* Multi-food detection
* Personalized nutrition tracking
* Adaptive depth estimation using device capabilities

---

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start server:

```bash
uvicorn app.main:app --reload
```

Open API documentation:

```bash
http://localhost:8000/docs
```