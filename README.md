# Calx-AI

AI-powered nutrition tracking and calorie estimation system built using an iterative engineering approach. The project evolves from text-based nutrition lookup into AI-driven food recognition and future adaptive calorie estimation.

---

## Current Status

**Current Development Stage:** V3.2 (Active Development)

### Implemented Features

#### V1 — Nutrition Lookup ✅

- Search food using text input
- FatSecret OAuth 2.0 authentication
- FatSecret nutrition API integration
- Detailed nutrition retrieval
- Standardized internal nutrition response
- Environment variable-based API security
- OAuth token caching
- Modular backend architecture
- Error handling
- Automated unit tests

---

#### V2 — AI Food Recognition 🟡

Implemented

- Upload food images
- AI-based food detection using OpenRouter Vision
- Multiple food detection
- Image validation
- External API exception handling
- Request timeout handling
- Reusable service architecture

Pending (after FatSecret migration)

- AI → Nutrition integration
- AI nutrition lookup pipeline

---

#### V3.1 — Multi-Food Nutrition Aggregation 🟡

Implemented

- Detect multiple foods from a single image
- Partial failure handling
- Regression tests
- Package configuration for testing

Pending

- Aggregate nutrition data
- Total calorie calculation using FatSecret nutrition data


## Supported Nutrition Data

Current extracted nutrients:

Reference Serving

• Calories
• Protein
• Carbohydrates
• Fat
• Sugar
• Fiber
• Sodium

Additional Serving Information

• Serving description
• Metric weight
• Serving URL
• Serving size
• Potassium
• Calcium
• Iron
• Vitamin A
• Vitamin C
• Cholesterol
• Saturated fat
• Monounsaturated fat
• Polyunsaturated fat

---

## System Architecture

### Text-Based Nutrition Search

```text
User Input (Food Name)
          ↓
FastAPI Backend
          ↓
FatSecret Client
          ↓
FatSecret foods.search API
          ↓
Best Matching Food
          ↓
FatSecret food.get API
          ↓
Response Normalization
          ↓
Nutrition Response
```

### AI Image Recognition

```text
User Uploads Food Image
            ↓
FastAPI Backend
            ↓
OpenRouter Vision Model
            ↓
Detected Food Names
            ↓
FatSecret Nutrition Engine
            ↓
foods.search
            ↓
food.get
            ↓
Nutrition Normalization
            ↓
Aggregated Nutrition Response
```

---

## Project Structure

```text
Calx-AI
│
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── fatsecret_client.py
│   ├── food_detector.py
│
├── tests
│   ├── test_fatsecret_client.py
│   ├── test_food_detector.py
│   ├── test_main.py
│
├── .env
├── requirements.txt
├── pytest.ini
├── README.md
├── system_architecture.png
```

---

## Tech Stack

### Backend

- Python
- FastAPI
- Requests
- python-dotenv

### AI

- OpenRouter API
- Google Gemma 3 Vision

### Nutrition Data Source

- FatSecret Platform API (OAuth 2.0)

### Development & Testing

- Pytest
- Git
- GitHub
- Swagger UI (OpenAPI)

### Planned Technologies

- Flutter (Mobile Application)
- Supabase
- PostgreSQL
- Advanced Computer Vision Models
- Depth Estimation Models (MiDaS / ARCore / LiDAR)

---

## API Endpoints

### Search Nutrition by Food Name

**Request**

```http
GET /nutrition?food=rice
```

**Example Response**

```json
{
  "food_name": "White Rice",
  "food_id": "4501",
  "food_type": "Generic",
  "food_url": "https://foods.fatsecret.com/calories-nutrition/generic/rice-white-cooked-regular",
  "reference_serving": {
    "description": "100 g",
    "grams": 100,
    "unit": "g",
    "calories": 129,
    "protein": 2.66,
    "fat": 0.28,
    "carbs": 27.90,
    "fiber": 0.40,
    "sugar": 0.05,
    "sodium": 365
  },
  "servings": [
    {
      "serving_description": "100 g",
      "metric_serving_amount": "100.000",
      "metric_serving_unit": "g",
      "calories": "129",
      "protein": "2.66",
      "fat": "0.28",
      "carbohydrate": "27.90",
      "fiber": "0.40",
      "sugar": "0.05",
      "sodium": "365"
    }
  ]
}
```

---

### AI Nutrition Detection from Image

**Request**

```http
POST /upload-image
```

**Response**

```json
{
  "detected_foods": [
    "Rice",
    "Chicken Breast"
  ],
  "total_nutrition": {
    "calories": 521,
    "protein": 34.8,
    "fat": 8.1,
    "carbs": 44.5,
    "fiber": 0.4,
    "sugar": 0.1
  }
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
* Regression testing
* Partial failure handling
* Low coupling design
* Replaceable AI and nutrition provider layers

---

## Future Roadmap

### V3.2 — AI → Nutrition Integration

Planned:

- Connect AI food detection with FatSecret nutrition lookup
- Normalize AI-generated food names
- Improve nutrition search accuracy
- Add search scoring and result ranking

---

### V3.3 — Portion Estimation

Planned:

- Detect serving counts
- Estimate food quantity
- Improve nutrition calculations
- Handle multiple portions of the same food

---

### V3.4 — Weight Estimation

Planned:

- Convert estimated portions into approximate grams
- Use food metadata for scaling
- Improve calorie accuracy
- Prepare backend for 3D volume estimation

---

### V4 — Personalized Nutrition Engine

Planned:

- User authentication
- Personalized calorie goals
- Meal history
- Daily nutrition tracking
- Progress analytics
- Streaks and consistency tracking
- Nutrition insights and recommendations

---

### V5 — Advanced Computer Vision

Planned:

- Food segmentation
- 3D volume estimation
- Depth-based weight estimation
- Adaptive calorie estimation
- Improve portion accuracy

---

### V6 — Production Backend

Planned:

- Cloud deployment
- Scalable backend architecture
- Database optimization
- Caching
- Background jobs
- Monitoring and logging
- API rate limiting
- Production security

---

### V7 — Mobile Application

Planned:

- Flutter application
- Responsive UI
- User profile management
- Cloud synchronization
- Subscription system
- Offline support
- Cross-platform optimization

---

### V8 — Food Ecosystem & Release

Planned:

- Barcode scanning
- OpenFoodFacts integration
- Packaged food support
- Recipe nutrition support
- Restaurant food support
- Play Store publishing

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