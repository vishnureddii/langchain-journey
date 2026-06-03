from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "LangChain App is running on Vercel!"}
