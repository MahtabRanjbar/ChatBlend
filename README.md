
# ChatBlend

## Overview

**ChatBlend** is a simple chatbot app that allows users to switch between two advanced language models: **GPT-4 (OpenAI)** and **Llama 3.1 (Groq)**. Built with Streamlit, ChatBlend offers a user-friendly interface where you can select your conversation style and language, making it easy to interact with AI in the way that suits you best.

## Features

- **Model Selection**: Choose between GPT-4 (OpenAI) and Llama 3.1 (Groq) to power your chatbot.
- **Multiple Assistant Modes**: Customize the bot's personality with Friendly, Professional, or Technical modes.
- **Multi-Language Support**: Get responses in English, Spanish, French, or German.
- **Chat History Management**: Save, load, and export chat histories for future reference.
- **Secure API Key Handling**: API keys are managed securely, with the OpenAI key being user-provided and the Groq key stored in an environment file.

## Getting Started

### Prerequisites

- **Python 3.8+**
- **Streamlit**
- **OpenAI Account** (for GPT-4 usage)
- **Groq API Key** (for Llama 3.1 usage)

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/MahtabRanjbar/ChatBlend.git
    cd ChatBlend
    ```


2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
    - Create a `.env` file in the root directory of the project and add your Groq API key.
    ```bash
    GROQ_API_KEY=your_groq_api_key_here
    ```
    - If using GPT-4, you will be prompted to enter your OpenAI API key in the app.

### Running the Application

1. **Start the Streamlit App**:
    ```bash
    streamlit run streamlit_app.py
    ```

2. **Access the App**:
    - Open your web browser and navigate to `http://localhost:8501` to interact with the chatbot.

## Usage

### Model Selection

- **GPT-4 (OpenAI)**: Choose this model if you want to leverage OpenAI's advanced GPT-4 capabilities. You will need to provide your OpenAI API key when prompted.
- **Llama 3.1 (Groq)**: Select this model to use Groq's Llama 3.1 model. The API key is securely fetched from your `.env` file.

### Chat History

- **Save Chat History**: The chat history is automatically saved to a JSON file (`chat_history.json`).
- **Load Chat History**: Previous chat histories are loaded automatically when the app starts.
- **Export Chat History**: Use the export button in the sidebar to download the current chat history as a JSON file.

### Modes and Language

- **Assistant Modes**: Select the desired mode (Friendly, Professional, Technical) to adjust the chatbot's tone and response style.
- **Language**: Choose from English, Spanish, French, or German for the chatbot's responses.



## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

