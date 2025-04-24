import streamlit as st
import ollama

from prompt import tone_guides,product_guides



def generate_brand_copy(brand_name, tone, content_type, product_type,product_description ):
    tone_instructions = tone_guides.get(tone, "")
    product_instructions = product_guides.get(product_type, "")
    prompt = f"""

You are an expert brand copywriter with a deep understanding of marketing psychology, emotional storytelling, and creative advertising.
Your task is to generate a {content_type} for a brand called "{brand_name}" that sells products in the {product_type} category.
create 5 creative hashtags relevant to the brand and {tone_instructions} (short, catchy, 1-3 words each)
and 3 mini mood board ideas describing the visual style using {product_instructions} (colors, vibes, visual elements).
Specifically, the brand offers: {product_description},{product_instructions}
Write in a {tone} tone,{tone_instructions} 

The copy should:
- Feel highly original, catchy, and relatable to the brand’s target audience
- Match the emotional depth and energy of the selected tone
- Be aligned with the brand’s values, unique selling points, and market positioning
- Strictly avoid clichés and generic language
If content type is:
- "Poster Caption" ➔ Keep it short, visually inspiring, and immediately impactful
- "Slogan" ➔ Make it punchy, memorable, and under 10 words
- "Ad Copy" ➔ Highlight 2–3 key benefits concisely with a soft call-to-action
- "Social Media Post" ➔ Make it engaging, friendly, and designed to encourage shares or comments
Use persuasive techniques subtly (emotional hooks, storytelling fragments, vivid imagery) if appropriate.
Only output the generated copy — **no explanations, no extra text**.
Your goal is to create branded copy that feels tailor-made and instantly usable in professional marketing campaigns.


"""

    response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']



def main():
    st.set_page_config(page_title="AI Brand Copy and Poster Generator", page_icon="✨")
    st.title("Welcome to Shore")

    brand_name = st.text_input("What is the name of your brand:")
    product_type = st.selectbox("Select Product Type:",["Clothing", "Electronics", "Food & Beverage", "Home Appliances", "Beauty & Wellness",
                                 "Health & Fitness", "Technology", "Services"])
    product_description = st.text_area("Briefly describe your product(s):", height=100)
    content_type = st.selectbox("Select Content Type:", ["Slogan", "Ad Copy", "Social Media Post", "Poster Caption"])
    tone = st.selectbox("Select the Tone:", ["Friendly", "Professional", "Fun & Quirky", "Technical", "Luxury","Minimalist"])

    if st.button("Generate Copy ✨"):
        if brand_name:
            with st.spinner("Generating your brand copy..."):
                generated_text = generate_brand_copy(brand_name, tone, content_type,product_type,product_description )
            st.subheader("Generated Output:")
            st.text_area("Your AI-Generated Copy:", value=generated_text, height=200)
        else:
            st.warning("Please enter your brand name first!")


if __name__ == "__main__":
    main()
