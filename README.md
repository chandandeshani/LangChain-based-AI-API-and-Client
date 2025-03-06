# LangChain-based AI API and Client

## Description
This project provides a **FastAPI-based server** with **LangChain integration**, allowing users to interact with an AI model via an API and a **Streamlit-based client**. It supports **Mistral and Llama2** models and enables users to generate text responses dynamically.

## Features
- **FastAPI Server** (`api.py`) serving AI-powered responses.
- **Streamlit Client** (`client.py`) for user-friendly interaction.
- **LangChain and Ollama Integration** (`ollama_langchain.py`) with advanced model handling.
- **Predefined Prompt Handling** for essays and general queries.
- **RAG Implementation** (`rag.ipynb`) for retrieval-augmented generation.

## Files Overview
- `api.py` - FastAPI server providing AI-powered API routes.
- `client.py` - Streamlit-based UI to interact with the API.
- `ollama_langchain.py` - LangChain-based implementation using Llama2.
- `rag.ipynb` - Jupyter Notebook implementing a **Retrieval-Augmented Generation (RAG)** approach.
- `requirements.txt` - List of dependencies required to run the project.
- `speech.txt` - Sample text data.

## Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-name>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project
### Start the FastAPI Server
```bash
python api.py
```
The server runs on `http://127.0.0.1:8000/`

### Run the Streamlit Client
```bash
streamlit run client.py
```

## API Endpoints
- `POST /openai` - Basic AI response using **Mistral**.
- `POST /essay/invoke` - Generates an essay on a given topic.

## Notes
- Modify `ollama_langchain.py` to switch models (Llama2 or Mistral).
- RAG implementation (`rag.ipynb`) helps retrieve relevant data for better responses.
