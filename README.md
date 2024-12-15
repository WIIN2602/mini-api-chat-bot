# Chatbot API
This is a simple chatbot API built using FastAPI and Hugging Face Transformers.

## How to Use
1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `uvicorn app:app --reload`
3. Access the API at `http://127.0.0.1:8000/docs`

## Features
- Answer questions based on the given context
- Built using a pre-trained DistilBERT model from Hugging Face

## Example
**Context:** "OpenAI is an AI research and deployment company. Our mission is to ensure that artificial general intelligence (AGI) benefits all of humanity."

**Question:** "What is OpenAI's mission?"

**Answer:** "ensure that artificial general intelligence (AGI) benefits all of humanity."
