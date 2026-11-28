import streamlit as st
from pypdf import PdfReader

st.title("📚 ExamPilot")

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

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    st.write(text)