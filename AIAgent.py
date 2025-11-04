from google import genai
from dotenv import load_dotenv
import streamlit as st
import os

# --- Load .env file (for local dev)
load_dotenv()

# --- Initialize Gemini client
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("⚠️ GOOGLE_API_KEY not found. Please set it in your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

# --- Streamlit UI
st.title("💬 Data Analyst")

# Example input
prompt = st.text_area("Ask something:", "")

if st.button("Generate"):
    with st.spinner("Thinking..."):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
    st.success("✅ Response:")
    st.write(response.text)
