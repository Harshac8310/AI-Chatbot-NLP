import streamlit as st
from src.chatbot import get_response


# Page configuration
st.set_page_config(
    page_title="NovaTech Student Support",
    page_icon="🤖",
    layout="centered"
)


# Title
st.title("🤖 NovaTech Student Support Chatbot")
st.caption("Your virtual assistant for college-related information")


# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

    # Initial bot message
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hello! Welcome to NovaTech Institute. How can I help you?"
    })


# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat input
user_input = st.chat_input("Ask me about NovaTech...")


if user_input:

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })


    # Generate response
    response = get_response(user_input)


    # Display bot response
    with st.chat_message("assistant"):
        st.write(response)


    # Store bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })