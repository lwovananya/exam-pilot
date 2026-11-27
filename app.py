import streamlit as st

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