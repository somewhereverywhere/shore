from openai import OpenAI
from fastapi import FastAPI, HTTPException
from enum import Enum
from pydantic import BaseModel
import os
from prompt import tone_guides, product_guides
from fastapi.responses import JSONResponse
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

class Tone(str, Enum):
    friendly = "Friendly"
    professional = "Professional"
    fun_quirky = "Fun & Quirky"
    technical = "Technical"
    luxury = "Luxury"
    minimalist = "Minimalist"

class ProductType(str, Enum):
    clothing = "Clothing"
    electronics = "Electronics"
    food_beverage = "Food & Beverage"
    home_appliances = "Home Appliances"
    beauty_wellness = "Beauty & Wellness"
    health_fitness = "Health & Fitness"
    technology = "Technology"
    services = "Services"

class CopyRequest(BaseModel):
    brand_name: str
    product_type: ProductType
    product_description: str
    tone: Tone

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Your FastAPI backend is working! 🎉"}

@app.post("/generate-copy")
def generate_brand_copy(data: CopyRequest):
    tone_instructions = tone_guides.get(data.tone, "")
    product_instructions = product_guides.get(data.product_type, "")

    prompt = f"""
You are an expert brand copywriter with a deep understanding of marketing psychology, emotional storytelling, and creative advertising.
Your task is to generate brand copy assets for a brand called "{data.brand_name}" that sells products in the {data.product_type} category.
Specifically, the brand offers: {data.product_description}.

Instructions:
- Generate:
  - A slogan
  - A poster caption
  - An ad copy
  - A social media post
  - 5 creative hashtags
  - 2 mini mood board ideas (describing visual style, colors, vibes)

Guidelines:
- {tone_instructions}
- {product_instructions}
- Copy must feel original, energetic, and highly engaging.
- Avoid clichés and generic language.

**Format the entire output as a strict valid JSON object:**

{{
  "slogan": "...",
  "poster_caption": "...",
  "ad_copy": "...",
  "social_media_post": "...",
  "hashtags": ["...", "...", "...", "...", "..."],
  "moodboards": ["...", "..."]
}}

Only output the JSON. No explanations, no markdown formatting.
"""
    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-nemo:free",
            messages=[{"role": "user", "content": prompt}]
        )
        content = response.choices[0].message.content.strip()
        json_output = json.loads(content)

        return JSONResponse(content=json_output)

    except Exception as e:
        print(f"Error generating content: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to generate content: {str(e)}")
