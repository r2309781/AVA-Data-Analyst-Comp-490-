from fpdf import FPDF
import streamlit as st
from dotenv import load_dotenv
from io import BytesIO
from google import genai
import os

st.title("📄 Welcome to Reports!")

load_dotenv()

def create_pdf():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("⚠️ GOOGLE_API_KEY not found. Please set it in your .env file.")
        st.stop()

    client = genai.Client(api_key=api_key)

    prompt = "Generate a brief report summary about sales performance."
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # Gemini response format (new SDK)
    try:
        text = response.text  # Works in most versions
    except:
        text = response.candidates[0].content.parts[0].text

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)  # 🟢 Prevents overflow
    pdf.set_font("Arial", size=12)

    # Add wrapped text safely
    pdf.multi_cell(0, 8, text)

    pdf_bytes = pdf.output(dest="S")
    return BytesIO(pdf_bytes)

if st.button("Generate PDF Report"):
    with st.spinner("Generating Report..."):
        pdf_data = create_pdf()

    st.download_button(
        label="⬇️ Download PDF",
        data=pdf_data,
        file_name="Sample_Report.pdf",
        mime="application/pdf"
    )
    st.success("✅ Report has been created! Click above to download.")
