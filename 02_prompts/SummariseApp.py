from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

st.header("Research tool")

user_input = st.text_input("Enter your prompt:")

if st.button("summarize"):
    result = model.invoke(user_input)
    st.write(result.content)