# ActualPlate

AI-powered nutrition tracking and calorie estimation system built using a modular, service-based architecture. The project evolves from text-based nutrition lookup into AI-driven food recognition, multi-food nutrition analysis, and future adaptive calorie estimation using computer vision and depth-based technologies.

## Why ActualPlate?

Most nutrition apps (MyFitnessPal, Cronometer) estimate portions in 2D. ActualPlate uses:
- **Depth Anything V2** for 3D reconstruction
- **SAM2** for precise food segmentation  
- **Density mapping** for weight estimation

Result: More accurate calorie estimation than 2D-only competitors.

---

## Repository & Links

- **GitHub**: https://github.com/Krishna7dx9/ActualPlate
- **LinkedIn**: https://www.linkedin.com/in/krishna-sharma-software-engineer/

---

## Current Status

**Current Development Stage:** V3.3 (Active Development)

### Implemented Features

#### V1 — Nutrition Lookup ✅

Implemented:

- Search food using text input
- FatSecret OAuth 2.0 authentication
- FatSecret nutrition API integration
- Detailed nutrition retrieval
- Standardized internal nutrition response format
- Environment variable-based API security
- OAuth token caching
- Error handling
- Automated unit tests

---

#### V2 — AI Food Recognition ✅

Implemented:

- Upload food images
- AI-based food detection using OpenRouter Vision
- Multiple food detection from a single image
- Image validation
- External API exception handling
- Request timeout handling
- Reusable AI recognition service
- AI-to-nutrition pipeline integration
- Automatic nutrition lookup for detected foods

---

#### V3.1 — Multi-Food Nutrition Aggregation ✅

Implemented:

- Detect multiple foods from a single image
- Partial nutrition lookup failure handling
- Nutrition response formatting
- Separate nutrition aggregation module
- Total calorie and nutrient calculation using FatSecret nutrition data
- Regression tests
- Package configuration for testing

---

## Supported Nutrition Data

The system extracts, normalizes, and processes nutrition information from external nutrition providers. Currently, FatSecret Platform API is used as the primary nutrition data source.

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
• Metric serving amount  
• Serving unit  
• Serving size information  
• Food ID  
• Food URL  
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

### Current Backend Architecture (Implemented)

```text
Client (Web / Mobile)
          │
          ▼
     FastAPI Backend
          │
          ▼
   API Routing Layer
          │
          ▼
   ┌───────────────────────────────┐
   │        Service Layer          │
   ├───────────────────────────────┤
   │                               │
   │  Vision Service               │
   │      │                        │
   │      ▼                        │
   │  OpenRouter Vision            │
   │      │                        │
   │      ▼                        │
   │  Food Recognition             │
   │                               │
   │  Nutrition Service            │
   │      │                        │
   │      ▼                        │
   │  FatSecret Provider           │
   │      │                        │
   │      ▼                        │
   │  Nutrition Retrieval          │
   │                               │
   │  Processing Layer             │
   │      │                        │
   │      ▼                        │
   │  Nutrition Formatter          │
   │      │                        │
   │      ▼                        │
   │  Nutrition Aggregator         │
   └───────────────────────────────┘
          │
          ▼
  Standardized Nutrition Response
```

### Future AI Computer Vision Pipeline

```text
Food Image
     │
     ▼
Vision Recognition
(OpenRouter Vision)
     │
     ▼
Food Recognition
     │
     ▼
Grounding DINO
(Food Localization)
     │
     ▼
SAM2
(Food Segmentation)
     │
     ▼
Segmentation Masks
     │
     ▼
Depth Estimation
(Depth Anything / MiDaS)
     │
     ▼
3D Volume Estimation
     │
     ▼
Weight Estimation
(Food Density Models)
     │
     ▼
Nutrition Engine
(FatSecret + Portion Scaling)
     │
     ▼
Adaptive Calorie Estimation
```

### Future Production Architecture

```text
Flutter Mobile App
          │
          ▼
      API Gateway
          │
          ▼
     FastAPI Backend
          │
          ▼
   ┌──────────────────────────────┐
   │      Backend Services        │
   ├──────────────────────────────┤
   │                              │
   │ Authentication               │
   │ Nutrition Service            │
   │ Vision Service               │
   │ User Service                 │
   │ Analytics                    │
   │                              │
   └──────────────────────────────┘
          │
          ├──────────────► PostgreSQL
          │
          ├──────────────► Object Storage
          │
          └──────────────► AI Inference Workers
                               │
                               ▼
                     Dedicated Cloud GPU
                               │
                               ▼
        Vision • Detection • Segmentation • Depth
                               │
                               ▼
                    Nutrition Intelligence
```

---

## Project Structure

```text
ActualPlate
│
├── backend
│   ├── app
│   │   └── main.py
│   ├── models
│   ├── routes
│   ├── services
│   └── utils
│
├── nutrition
│   ├── providers
│   │   └── fatsecret_client.py
│   ├── utils
│   ├── nutrition_formatter.py
│   └── nutrition_aggregator.py
│
├── vision_service
│   ├── recognition
│   │   └── food_recognition.py
│   ├── portion
│   │   └── portion_estimator.py
│   ├── detection
│   ├── segmentation
│   ├── depth
│   ├── weight
│   ├── lidar
│   ├── pipelines
│   └── utils
│
├── tests
│   ├── test_fatsecret_client.py
│   ├── test_food_recognition.py
│   └── test_main.py
│
├── docs
├── .env
├── requirements.txt
├── pytest.ini
├── README.md
└── system_architecture.png
```

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
- Google Gemma 3 27B IT (via OpenRouter)

Planned:

- Grounding DINO (Food Localization)
- SAM2 (Food Segmentation)
- Depth Anything / MiDaS (Depth Estimation)
- ARCore / LiDAR (Supported Devices)

### Nutrition Data

- FatSecret Platform API (OAuth 2.0) — Free Tier (Unlimited)

### Development & Testing

- Pytest
- Git
- GitHub
- Swagger UI (OpenAPI)

### Infrastructure

- Google Cloud (Startup Credits)
- PostgreSQL
- Object Storage
- Serverless Functions

### Client Application

Planned:

- Flutter

---

## Deployment Strategy

Computer vision models (Grounding DINO, SAM2, Depth Anything V2) deployment phases:

**Current:** `INFERENCE_ENV = "colab"`
- Google Colab (Free GPU for development & testing)

**Next Phase:** `INFERENCE_ENV = "serverless"`
- Google Cloud Run (Cost-optimized when MVP is ready)

**Scale Phase:** `INFERENCE_ENV = "dedicated_gpu"`
- Google Cloud GPUs (Dedicated inference when demand justifies, using startup credits)

**Future Phase:** `INFERENCE_ENV = "self_hosted"`
- On-premise GPU (When traffic warrants self-hosting)

Change single environment variable to switch deployment target. All model inference abstracted through unified interface.

---

## API Endpoints

### Search Nutrition by Food Name

Retrieves nutrition information for a food item using the FatSecret Platform API.

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
  "nutrition": {
    "calories": 129,
    "protein": 2.66,
    "fat": 0.28,
    "carbohydrate": 27.9,
    "fiber": 0.4,
    "sugar": 0.05,
    "sodium": 365
  }
}
```

---

### AI Nutrition Detection from Image

Detects foods from an uploaded image and returns nutrition information for each detected item.

**Request**

```http
POST /upload-image
Content-Type: multipart/form-data
```

**Example Response**

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
        "carbohydrate": 0,
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
    "carbohydrate": 0,
    "fiber": 0,
    "sugar": 0,
    "sodium": 74
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
* Unified inference interface for seamless model deployment switching

---

## Future Roadmap

### V3.3 — AI Portion Estimation

Current

- Placeholder portion estimation module
- Fixed portion ratio (1.0)
- Nutrition pipeline ready for future estimation models

Planned

- Grounding DINO for food localization
- SAM2 for food segmentation
- Portion estimation from segmentation masks
- Dynamic portion scaling
- Improved calorie estimation

---

### V3.4 — Weight & Volume Estimation

Planned

- Depth estimation using Depth Anything / MiDaS
- 3D food volume estimation
- Food density mapping
- Weight estimation in grams
- Adaptive nutrition calculation

---

### V4 — Intelligent Nutrition Engine

Planned

- Personalized calorie goals
- Meal history
- Daily nutrition tracking
- Nutrition analytics
- Progress insights
- Recommendation engine

---

### V5 — User Platform & Backend

Planned

- User authentication
- PostgreSQL database
- Backend API deployment
- Object storage
- Background workers
- API caching
- Monitoring & logging
- Rate limiting
- Production security
- Subscription system
- Daily streaks

---

### V6 — Food Ecosystem & Design

Planned

- Figma UI/UX design
- Barcode scanning
- Recipe nutrition analysis
- Meal planning
- AI nutrition recommendations

---

### V7 — Mobile Application

Planned

- Flutter application
- Cross-platform support
- Cloud synchronization
- Offline mode

---

### V8 — Production Release

Planned

- Play Store release
- Performance optimization
- Scalability improvements
- User feedback iteration
- Continuous model improvements

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
INFERENCE_ENV=colab
```

Start server:

```bash
uvicorn backend.app.main:app --reload
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
* Abstract infrastructure to enable seamless deployment transitions