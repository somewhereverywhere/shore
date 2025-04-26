import os


tone_guides = {
    "Friendly": "tone_guides/friendly.md",
    "Professional": "tone_guides/professional_tone.md",
    "Fun & Quirky": "tone_guides/fun_quirky_tone.md",
    "Technical": "tone_guides/technical_tone.md",
    "Luxury": "tone_guides/luxury.md",
    "Minimalist": "tone_guides/minimalist.md",

}


product_guides = {
    "Clothing": "product_guides/clothing_product.md",
    "Electronics": "product_guides/electronics_product.md",
    "Food & Beverage": "product_guides/food_beverage_product.md",
    "Home Appliances": "product_guides/home_appliances_product.md",
    "Beauty & Wellness": "product_guides/beauty_wellness_product.md",
    "Health & Fitness": "product_guides/health_fitness_product.md",
    "Technology": "product_guides/technology_product.md",
    "Services": "product_guides/services_product.md",

}



def load_guides():
    for filename in os.listdir("tone_guides"):
        if filename.endswith(".md"):
            tone_name = filename.replace("_tone.md", "").replace("_", " ").title()
            with open(os.path.join("tone_guides", filename), 'r', encoding='utf-8') as f:
                tone_guides[tone_name] = f.read()

    for filename in os.listdir("product_guides"):
        if filename.endswith(".md"):
            product_name = filename.replace("_product.md", "").replace("_", " ").title()
            with open(os.path.join("product_guides", filename), 'r', encoding='utf-8') as f:
                product_guides[product_name] = f.read()


load_guides()

