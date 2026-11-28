import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai
from config import API_KEY
genai.configure(
    api_key=API_KEY
)

model = genai.GenerativeModel("gemini-3.8-flash")

st.title("Exam-Pilot")

st.write(
    "AI study assistant that turns PDF notes into summaries, quizzes, and study plans."
)

uploaded_file = st.file_uploader(
    "Upload PDF Notes",
    type=["pdf"]
)

if uploaded_file:

    st.success("PDF uploaded successfully!")

    reader = PdfReader(uploaded_file)
    num_pages = len(reader.pages)
    st.info(f"This PDF contains {num_pages} pages.")

    text = ""

    for page in reader.pages:
        text += page.extract_text()
    if st.button("Generate Summary"):
        with st.spinner("Generating summary..."):
            response = model.generate_content(f"Summarize these study notes:\n{text[:3000]}")
            st.subheader("Summary")
            st.write(response.text)

    st.text_area(
    "Extracted Notes",
    text,
    height=500
)