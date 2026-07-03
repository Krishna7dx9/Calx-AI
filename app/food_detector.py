from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def detect_food(image_bytes):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            "Tell only the food name from this image. Return one word only.",
            types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/jpeg"
            )
        ]
    )

    return response.text.strip() if response.text else "unknown"