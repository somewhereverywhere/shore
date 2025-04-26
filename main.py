from openai import OpenAI
from fastapi import FastAPI,HTTPException
from enum import Enum
from pydantic import BaseModel
import os
from prompt import tone_guides,product_guides
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://shore-brand-copy.vercel.app/"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
OPENROUTER_API_KEY=os.getenv("OPENROUTER_API_KEY")

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
    content_type: str
    tone: Tone

@app.get("/health")
def health_check():
    return {"status": "ok"}
@app.get("/")
def root():
    return {"message": "Your FastAPI backend is working! 🎉"}

@app.post("/generate-copy")
def generate_brand_copy(data:CopyRequest):
    tone_instructions = tone_guides.get(data.tone, "")
    product_instructions = product_guides.get(data.product_type, "")
    prompt = f"""

You are an expert brand copywriter with a deep understanding of marketing psychology, emotional storytelling, and creative advertising.
Your task is to generate a {data.content_type} for a brand called "{data.brand_name}" that sells products in the {data.product_type} category.
-create 5 creative hashtags relevant to the brand and {tone_instructions} (short, catchy, 1-3 words each)
-2 mini mood board ideas describing the visual style using {product_instructions} (colors, vibes, visual elements).
Specifically, the brand offers: {data.product_description},product guide:{product_instructions}
Write in a {data.tone} tone,tone guide:{tone_instructions} 

The copy should:
- Feel highly original, catchy, and relatable to the brand’s target audience
- Match the emotional depth and energy of the selected tone
- Be aligned with the brand’s values, unique selling points, and market positioning
- **Strictly avoid clichés and generic language**
If content type is:
- "Poster Caption" ➔ Keep it short, visually inspiring, and immediately impactful
- "Slogan" ➔ Make it punchy, memorable, and under 10 words
- "Ad Copy" ➔ Highlight 2–3 key benefits concisely with a soft call-to-action
- "Social Media Post" ➔ Make it engaging, friendly, and designed to encourage shares or comments.
Use persuasive techniques subtly (emotional hooks, storytelling fragments, vivid imagery) if appropriate.
Only output the generated copy — **no explanations, no extra text**.
Your goal is to create branded copy that feels tailor-made and instantly usable in professional marketing campaigns.
"""
    try:
        response = client.chat.completions.create(
        model="mistralai/mistral-nemo:free",
        messages=[{"role": "user", "content": prompt}]
        )
        return {"result": response.choices[0].message.content.strip()}
    except Exception as e:
        print(f"Error generating content: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to generate content: {str(e)}")
