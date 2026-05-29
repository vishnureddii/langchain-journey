import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
 
load_dotenv()
 
# Page config
st.set_page_config(page_title="AI Chatbot",
                   page_icon="🤖")
st.title("🤖 AI Chatbot")
 
# Initialize chat history
# This is the KEY concept
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
 
# Initialize model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7
)
 
# Display chat history
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)
 
# Chat input
user_input = st.chat_input("Type your message...")
 
if user_input:
    # Add user message to history
    st.session_state.chat_history.append(
        HumanMessage(content=user_input)
    )
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.invoke(
                st.session_state.chat_history
            )
            st.write(response.content)
    
    # Add AI response to history
    st.session_state.chat_history.append(
        AIMessage(content=response.content)
    )
if st.button("🧹 Clear History"):
    st.session_state.history = []
    st.rerun()
