'''
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes  
import uvicorn
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
import os
from dotenv import load_dotenv

from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="mistral")

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]="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"

app = FastAPI(
	title="Langchain Server",
	version="1.0",
	description="A simple API Server"
)

add_routes(
	app,
	llm,
	path="/openai"
)

## Ollama mistral
#llm=Ollama(model="mistral")
prompt1=ChatPromptTemplate.from_template("write me an essay about {topic} with 100 words")

add_routes(
	app,
	prompt1|llm,
	path="/essay"
)

if __name__=="__main__":
	uvicorn.run(app,host="127.0.0.1",port=8000)

'''


from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes  
import uvicorn
from langchain_ollama import OllamaLLM
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up LangChain API Tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"

# Initialize FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# Initialize LLM model
llm = OllamaLLM(model="mistral")

# Add base LLM route
add_routes(app, llm, path="/openai")

# Define prompt template for essay generation
prompt1 = ChatPromptTemplate.from_template("{topic}")

# Add essay generation route
add_routes(app, prompt1 | llm, path="/essay")

# Run FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)






















