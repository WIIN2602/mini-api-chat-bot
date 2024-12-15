from transformers import pipeline


class Chatbot:
    def __init__(self):
        # ใช้โมเดล Pre-trained สำหรับตอบคำถามทั่วไป
        self.qa_pipeline = pipeline(
            "question-answering", model="distilbert-base-cased-distilled-squad")

    def ask(self, question: str, context: str) -> str:
        """
        ตอบคำถามจากคำถาม (question) และเนื้อหา (context)
        """
        try:
            result = self.qa_pipeline(question=question, context=context)
            return result['answer']
        except Exception as e:
            return f"Error: {str(e)}"
