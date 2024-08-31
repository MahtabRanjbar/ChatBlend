import os
import streamlit as st
from dotenv import load_dotenv
from utils import (
    get_openai_response, 
    get_llama_response, 
    export_chat_history, 
    save_chat, 
    load_chat_history
)

# Load environment variables
load_dotenv()

# Streamlit configuration
st.set_page_config(
    page_title="Multi-Model ChatBot",
    page_icon="🤖",
    layout="centered"
)

st.title("💬 Multi-Model ChatBot")

# Sidebar Configuration for Model Selection
st.sidebar.header("Settings")
model_choice = st.sidebar.selectbox(
    "Choose the Model",
    options=["GPT-4 (OpenAI)", "Llama 3.1 (Groq)"],
    index=0
)

# Show OpenAI API Key input only if GPT-4 is selected
if model_choice == "GPT-4 (OpenAI)":
    openai_api_key = st.sidebar.text_input(
        "OpenAI API Key",
        value="",
        type="password"
    )
else:
    openai_api_key = None  # No need for OpenAI API key when using Llama

mode = st.sidebar.selectbox(
    "Assistant Mode",
    options=["Friendly", "Professional", "Technical"],
    index=0
)

language = st.sidebar.selectbox(
    "Response Language",
    options=["English", "Spanish", "French", "German"],
    index=0
)

# Load chat history from the session or file
if "chat_history" not in st.session_state:
    st.session_state.chat_history = load_chat_history()

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input(f"Ask the {model_choice} model...")

if user_input:
    # Add user input to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    try:
        # Generate assistant response based on the selected model
        if model_choice == "GPT-4 (OpenAI)":
            if not openai_api_key:
                st.error("Please provide an OpenAI API Key.")
            else:
                assistant_response = get_openai_response(
                    chat_history=st.session_state.chat_history, 
                    mode=mode, 
                    language=language,
                    api_key=openai_api_key
                )
        elif model_choice == "Llama 3.1 (Groq)":
            assistant_response = get_llama_response(
                chat_history=st.session_state.chat_history, 
                mode=mode, 
                language=language
            )
        
        # Append the assistant response to the chat history and display it
        if assistant_response:
            st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
            with st.chat_message("assistant"):
                st.markdown(assistant_response)

    except Exception as e:
        st.error(f"Error generating response: {str(e)}")

    # Save the updated chat history
    save_chat(st.session_state.chat_history)

# Export chat option
if st.sidebar.button("Export Chat History"):
    export_chat_history(st.session_state.chat_history)
    st.sidebar.success("Chat history exported successfully!")
