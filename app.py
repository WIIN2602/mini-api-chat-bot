from fastapi import FastAPI, HTTPException
from chatbot import Chatbot

app = FastAPI()
chatbot = Chatbot()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Chatbot API"}


@app.post("/ask/")
def ask_question(question: str, context: str):
    """
    รับคำถามและเนื้อหา แล้วส่งคำตอบกลับ
    """
    if not question or not context:
        raise HTTPException(
            status_code=400, detail="Question and context must be provided")

    answer = chatbot.ask(question, context)
    return {"question": question, "context": context, "answer": answer}
