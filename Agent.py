# app.py
from google import genai
from google.genai import types
from dotenv import load_dotenv
import streamlit as st
import os

# ---------- Setup ----------
st.set_page_config(page_title="Gemini Chatbot", page_icon="💬", layout="centered")
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("⚠️ Set GOOGLE_API_KEY (or GEMINI_API_KEY) in your .env.")
    st.stop()

client = genai.Client(api_key=api_key)
MODEL_NAME = "gemini-2.5-flash"

st.title("💬 Data Analyst Chatbot")

# ---------- Chat history ----------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your chatbot. Ask me anything."}
    ]

# Render history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- Helper to convert history ----------
def to_contents(history):
    out = []
    for m in history:
        part = types.Part.from_text(text=m["content"])  # use keyword argument
        if m["role"] == "user":
            out.append(types.UserContent(parts=[part]))
        else:
            out.append(types.ModelContent(parts=[part]))
    return out


# ---------- Input ----------
user_text = st.chat_input("Type your message…")

if user_text:
    # Save & show user message
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    # Build full typed contents for context and call Gemini (non-streaming for reliability)
    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking…"):
                resp = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=to_contents(st.session_state.messages),
                )
            reply = (resp.text or "").strip() or "…"
        except Exception as e:
            reply = f"Request failed: {e}"

        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
