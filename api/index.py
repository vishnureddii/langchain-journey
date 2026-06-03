from fastapi import FastAPI
from Chatbot.Chatbot import get_response   # ✅ corrected import

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Chatbot API running ✅"}

@app.get("/chat")
def chat(query: str):
    try:
        response = get_response(query)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}

@app.get("/favicon.ico")
def favicon():
    return {}
