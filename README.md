# ActualPlate

AI-powered nutrition tracking and calorie estimation system built using an iterative engineering approach. The project evolves from text-based nutrition lookup into AI-driven food recognition and future adaptive calorie estimation.

---

## Current Status

**Current Development Stage:** V3.3 (Active Development)

### Implemented Features

#### V1 — Nutrition Lookup ✅

- Search food using text input
- FatSecret OAuth 2.0 authentication
- FatSecret nutrition API integration
- Detailed nutrition retrieval
- Standardized internal nutrition response format
- Environment variable-based API security
- OAuth token caching
- Modular backend architecture
- Error handling
- Automated unit tests

---

#### V2 — AI Food Recognition ✅

Implemented

- Upload food images
- AI-based food detection using OpenRouter Vision
- Multiple food detection from a single image
- Image validation
- External API exception handling
- Request timeout handling
- Reusable AI service architecture
- AI-to-nutrition pipeline integration
- Automatic nutrition lookup for detected foods

---

#### V3.1 — Multi-Food Nutrition Aggregation ✅

Implemented

- Detect multiple foods from a single image
- Partial nutrition lookup failure handling
- Nutrition response formatting
- Separate nutrition aggregation module
- Total calorie and nutrient calculation using FatSecret nutrition data
- Regression tests
- Package configuration for testing

---


## Supported Nutrition Data

The system currently extracts and processes nutrition information from FatSecret API responses.

### Core Nutrition Data

Reference Serving:

• Calories  
• Protein  
• Carbohydrates  
• Fat  
• Sugar  
• Fiber  
• Sodium  

### Additional Nutrition Metadata

Available from nutrition providers:

• Serving description  
• Metric weight  
• Serving size  
• Serving URL  
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
Selected Food Result
          ↓
FatSecret food.get API
          ↓
Response Normalization
          ↓
Formatted Nutrition Response
```

### AI Food Recognition and Nutrition Pipeline

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
Food Search and Nutrition Retrieval
            ↓
Nutrition Formatter
            ↓
Nutrition Aggregator
            ↓
Total Calories and Nutrient Breakdown
```

### Future Computer Vision Pipeline

```text
Food Image
      ↓
OpenRouter Vision
      ↓
Detected Food Names
      ↓
Grounding DINO (Food Localization)
      ↓
SAM2 (Food Segmentation)
      ↓
Portion Estimation
      ↓
Weight Estimation
      ↓
Nutrition Calculation
```


---

## Project Structure

```text
ActualPlate
│
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── fatsecret_client.py
│   ├── food_detector.py
│   ├── nutrition_formatter.py
│   ├── nutrition_aggregator.py
│   ├── portion_estimator.py
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
---

## Tech Stack

### Backend

- Python
- FastAPI
- Requests
- python-dotenv

### AI

Implemented:

- OpenRouter API
- Google Gemma 3 Vision

Planned:

- Grounding DINO (Food Localization)
- SAM2 (Food Segmentation)
- Depth Estimation Models (Depth Anything / MiDaS)
- ARCore / LiDAR-based depth features

### Nutrition Data Source

- FatSecret Platform API (OAuth 2.0)

### Development & Testing

- Pytest
- Git
- GitHub
- Swagger UI (OpenAPI)

### Planned Application Technologies

- Flutter (Mobile Application)
- Supabase
- PostgreSQL

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
  "portion": null,
  "nutrition": {
    "calories": 129,
    "protein": 2.66,
    "fat": 0.28,
    "carbs": 27.90,
    "fiber": 0.40,
    "sugar": 0.05,
    "sodium": 365
  }
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
  "foods": [
    {
      "food_name": "Chicken Breast",
      "food_id": "12345",
      "portion": {
        "food_name": "chicken breast",
        "portion_ratio": 1.0,
        "confidence": null,
        "method": "placeholder"
      },
      "nutrition": {
        "calories": 165,
        "protein": 31,
        "fat": 3.6,
        "carbs": 0,
        "fiber": 0,
        "sugar": 0,
        "sodium": 74
      }
    }
  ],
  "total_detected": 1,
  "total_found": 1,
  "total_failed": 0,
  "total_nutrition": {
    "calories": 165,
    "protein": 31,
    "fat": 3.6,
    "carbs": 0,
    "sugar": 0,
    "fiber": 0
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
* Separate AI detection and nutrition services
* Nutrition response formatting layer
* Independent nutrition aggregation module
* Incremental feature development
* Regression testing
* Partial failure handling
* Low coupling design
* Replaceable AI and nutrition provider layers
* Scalable architecture for future computer vision improvements

---

## Future Roadmap

### V3.3 — Computer Vision Based Portion Estimation

Current:

- Basic placeholder portion module implemented
- Uses default portion ratio (1.0)
- No visual estimation performed yet

Planned:

- Food localization using Grounding DINO
- Food segmentation using SAM2
- Estimate food area from segmentation masks
- Convert visual area into portion ratio
- Improve nutrition calculation accuracy

---

### V3.4 — Weight Estimation

Planned:

- Convert visual portions into approximate grams
- Use food metadata and density information
- Improve calorie estimation accuracy
- Prepare pipeline for depth-based volume estimation

---

### V4 — Depth and 3D Food Understanding

Planned:

- Depth estimation models (Depth Anything / MiDaS)
- Volume estimation from RGB images
- Depth-assisted portion calculation
- ARCore / LiDAR support for compatible devices
- Improved weight estimation accuracy

---

### V5 — Personalized Nutrition Engine

Planned:

- User authentication
- Personalized calorie goals
- Meal history
- Daily nutrition tracking
- Progress analytics
- Streaks and consistency tracking
- Nutrition insights and recommendations

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

---

## Run Locally

Clone the repository:

```bash
git clone https://github.com/Krishna7dx9/ActualPlate.git
```

Navigate to the project directory:

```bash
cd ActualPlate
```

Create and activate virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root and add required API credentials:

```env
FATSECRET_CLIENT_ID=your_client_id
FATSECRET_CLIENT_SECRET=your_client_secret
OPENROUTER_API_KEY=your_api_key
```

Start server:

```bash
uvicorn app.main:app --reload
```

Open API documentation:

```text
http://localhost:8000/docs
```

---

## Design Philosophy

The system follows an iterative engineering approach:

* Start with a minimal working product
* Build modular and reusable components
* Separate AI, nutrition, and processing layers
* Extend functionality without replacing existing architecture
* Improve accuracy progressively through better models
* Design components for scalability and future production requirements