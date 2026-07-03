# Calx-AI

AI-powered nutrition tracking and calorie estimation system built using an iterative engineering approach. The project evolves from text-based nutrition lookup into AI-driven food recognition and future adaptive calorie estimation.

---

## Current Status

**Current Version:** V2 (MVP)

### Completed Features

#### V1 — Nutrition Search

* Search food using text input
* USDA FoodData Central API integration
* Extract nutrition information
* Environment variable-based API security
* Modular backend structure
* Error handling for missing food data

#### V2 — AI Food Recognition

* Upload food images
* AI-based food detection using Gemini Vision
* Reuse nutrition lookup engine
* Image validation
* External API exception handling
* Request timeout handling
* Clean reusable service architecture

---

## Supported Nutrition Data

Current extracted nutrients:

* Calories
* Protein
* Carbohydrates
* Fat
* Sugar
* Fiber

---

## System Architecture

### Text Search Flow

```text
User Input (Food Name)
        ↓
FastAPI Backend
        ↓
USDA Client Layer
        ↓
USDA FoodData API
        ↓
Processed Nutrition Response
```

### Image Recognition Flow

```text
User Uploads Food Image
            ↓
FastAPI Backend
            ↓
Gemini Vision API
            ↓
Detected Food Name
            ↓
USDA FoodData API
            ↓
Processed Nutrition Response
```

---

## Project Structure

```text
Calx-AI
│
├── app
│   ├── main.py
│   ├── usda_client.py
│   ├── food_detector.py
│
├── .env
├── requirements.txt
├── README.md
├── .gitignore
```

---

## Tech Stack

### Backend

* Python
* FastAPI
* Requests
* Python-dotenv

### AI

* Gemini Vision API

### Nutrition Source

* USDA FoodData Central API

### Development Tools

* Git
* GitHub
* Swagger UI

### Planned Future Stack

* Flutter (mobile app)
* Advanced computer vision models

---

## API Endpoints

### Search nutrition using text

Request:

```bash
GET /nutrition?food=rice
```

Response:

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

### Upload image for AI nutrition detection

Request:

```bash
POST /upload-image
```

Response:

```json
{
    "food":"RICE",
    "protein":6.67,
    "fat":0,
    "carbs":77.8,
    "calories":356,
    "sugar":0,
    "fiber":0
}
```

---

## Engineering Considerations

Current design decisions:

* Modular service separation
* Environment-based secret management
* External API timeout handling
* Input validation
* Error handling
* Reusable nutrition lookup flow
* Incremental feature development

---

## Future Roadmap

### V1 — Text nutrition lookup ✓

### V2 — AI food recognition ✓

### V3 — Portion estimation

Planned:

* Multi-food detection
* Portion estimation
* Convert estimated quantity to grams
* Calculate total nutrition values

### V4 — Adaptive calorie estimation

Planned:

* Depth-enabled estimation
* Device capability detection
* Personalized nutrition tracking
* Food history and analytics

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

---

## Design Philosophy

The system follows an iterative development strategy:

* Start with a minimal working product
* Build reusable components
* Extend functionality without replacing architecture
* Improve accuracy progressively
* Design for scalability