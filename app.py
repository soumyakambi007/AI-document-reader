import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API Key
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("GOOGLE_API_KEY not found in the .env file.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.6-flash")

st.set_page_config(page_title="Fake News Detector")
st.title("📰 Fake News Detector (AI)")
st.write("Paste a news article or claim below. The AI will estimate whether it appears real or fake and explain why.")

news = st.text_area("Enter the news or claim")

if st.button("Check News"):
    if news.strip() == "":
        st.warning("Please enter some text.")
    else:
        prompt = f"""
You are a fake news detection assistant.

Analyze the following news or claim.

News:
{news}

Respond in this format:

Prediction: REAL / LIKELY REAL / FAKE / LIKELY FAKE

Reason:
- Point 1
- Point 2
- Point 3

Mention that the result is an AI assessment and should be verified with trusted news sources.
"""

        try:
            response = model.generate_content(prompt)
            st.subheader("Result")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")