# 🧠 AI Brand Copy Generator

A fullstack GenAI web application that generates creative and tailored brand copy using LLMs. It produces slogans, poster captions, ad copy, social media posts, hashtags, and moodboard ideas — all in one click.

## 🚀 Live Demo

🔗 [Try the app here](https://shore-brand-copy.vercel.app)

---

## 💡 Features

- 🎨 Generates brand copy based on product type, tone, and description.
- ✨ Includes slogans, ad copy, poster captions, social media posts, hashtags, and visual moodboard suggestions.
- ⚙️ Built with OpenRouter's Mistral model via Groq API.
- 🧠 Prompt-engineered responses formatted in clean JSON.
- 🌐 Fully deployed with:
  - **Frontend**: [Vercel's V0](https://v0.dev/)
  - **Backend**: FastAPI hosted on [Render](https://render.com)

---

## 📦 Tech Stack

| Layer        | Tools Used                                  |
|--------------|---------------------------------------------|
| Frontend     | Vercel V0, React, Tailwind CSS              |
| Backend      | FastAPI, Python                             |
| AI/LLM       | Mistral (via Groq API & OpenRouter)         |
| Deployment   | Vercel (frontend), Render (backend)         |
| Dev Tools    |  pycharm,GitHub                             |

---

## 📄 API Endpoint

- **POST** `/generate-copy`  
  Request body:
  ```json
  {
    "brand_name": "GlowUp",
    "tone": "Friendly",
    "product_type": "Beauty & Wellness",
    "product_description": "All-natural face serum made from organic botanicals",
    "content_type": "Ad Copy"
  }
