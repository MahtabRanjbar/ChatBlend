import os
import json
import streamlit as st
import openai
from groq import Groq
from typing import List, Dict, Any

def get_openai_response(
    chat_history: List[Dict[str, str]], 
    mode: str = "Friendly", 
    language: str = "English",
    api_key: str = ""
) -> str:
    """
    Generate a response using OpenAI GPT-4.

    Args:
        chat_history (List[Dict[str, str]]): The history of chat messages.
        mode (str): The mode of the assistant (Friendly, Professional, Technical).
        language (str): The response language.
        api_key (str): The OpenAI API key.

    Returns:
        str: The assistant's response.
    """
    try:
        system_prompt = {
            "Friendly": "You are a friendly and helpful assistant.",
            "Professional": "You are a professional and concise assistant.",
            "Technical": "You are a highly technical and precise assistant."
        }[mode]

        language_prompt = f"Respond in {language}." if language != "English" else ""

        openai.api_key = api_key

        response = openai.chat.Completion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"{system_prompt} {language_prompt}"},
                *chat_history
            ]
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def get_llama_response(
    chat_history: List[Dict[str, str]], 
    mode: str = "Friendly", 
    language: str = "English"
) -> str:
    """
    Generate a response using Llama 3.1 via Groq.

    Args:
        chat_history (List[Dict[str, str]]): The history of chat messages.
        mode (str): The mode of the assistant (Friendly, Professional, Technical).
        language (str): The response language.

    Returns:
        str: The assistant's response.
    """
    try:
        system_prompt = {
            "Friendly": "You are a friendly and helpful assistant.",
            "Professional": "You are a professional and concise assistant.",
            "Technical": "You are a highly technical and precise assistant."
        }[mode]

        language_prompt = f"Respond in {language}." if language != "English" else ""

        groq_client = Groq()

        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": f"{system_prompt} {language_prompt}"},
                *chat_history
            ]
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def save_chat(chat_history: List[Dict[str, Any]]) -> None:
    """
    Save chat history to a JSON file.

    Args:
        chat_history (List[Dict[str, Any]]): The chat history to save.

    Returns:
        None
    """
    try:
        with open("chat_history.json", "w") as file:
            json.dump(chat_history, file)
    except Exception as e:
        st.error(f"Failed to save chat history: {str(e)}")

def load_chat_history() -> List[Dict[str, Any]]:
    """
    Load chat history from a JSON file.

    Returns:
        List[Dict[str, Any]]: The loaded chat history.
    """
    try:
        if os.path.exists("chat_history.json"):
            with open("chat_history.json", "r") as file:
                return json.load(file)
    except Exception as e:
        st.error(f"Failed to load chat history: {str(e)}")
    return []

def export_chat_history(chat_history: List[Dict[str, Any]]) -> None:
    """
    Export chat history as a downloadable JSON file.

    Args:
        chat_history (List[Dict[str, Any]]): The chat history to export.

    Returns:
        None
    """
    file_name = "chat_history.json"
    try:
        with open(file_name, "w") as file:
            json.dump(chat_history, file)
        st.sidebar.download_button(
            label="Download Chat History",
            data=open(file_name, "rb").read(),
            file_name=file_name,
            mime="application/json"
        )
    except Exception as e:
        st.error(f"Failed to export chat history: {str(e)}")
