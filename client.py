'''
import requests
import streamlit as st

# Function to call FastAPI
def get_ollama_response(input_text):
    response = requests.post(  # Fixed 'request.post' to 'requests.post'
        "http://127.0.0.1:8000/essay/invoke",
        json={'input': {'topic': input_text}}
    )
    
    if response.status_code == 200:
        return response.json().get('output', 'No response received')
    else:
        return f"Error: {response.status_code}, {response.text}"

# Streamlit UI
st.title('Langchain Demo With mistral API')

# User input
input_text = st.text_input("Write an essay on:")

# Ensure input is provided before calling API
if input_text:
    result = get_ollama_response(input_text)
    st.write(result)
'''

import requests
import streamlit as st

# Function to call FastAPI
def get_ollama_response(input_text):
    url = "http://127.0.0.1:8000/essay/invoke"  # Fixed endpoint URL
    payload = {"input": {"topic": input_text}}  # Corrected JSON structure
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an error for failed requests
        return response.json().get("output", "No response received")
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Streamlit UI
st.title("Langchain Demo With mistral API")

# User input
input_text = st.text_input("search anything:")

# Ensure input is provided before calling API
if input_text:
    result = get_ollama_response(input_text)
    st.write(result)

