from pandasai.llm.local_llm import LocalLLM
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from dotenv import load_dotenv
import os

load_dotenv()
api_base = os.getenv('API_BASE')

model = LocalLLM(
    api_base= "http://localhost:11434/v1",
    model="llama3"
)

st.title("Excel Data Analyzer")

st.subheader(":blue[1. Upload your excel sheet.]")
st.subheader(":blue[2. Ask questions and get visualizations from your data.]")

uploaded_file = st.file_uploader("Upload File", type=['csv'])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head(5))

    df = SmartDataframe(data, config={"llm": model})
    prompt = st.text_area("Ask questions to your data:")

    if st.button("Sumbit"):
        if prompt:
            with st.spinner("Generating your response..."):
                st.write(df.chat(prompt))
