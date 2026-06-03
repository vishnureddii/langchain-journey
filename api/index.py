from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "LangChain App is running on Vercel!"}
    
# ✅ handle favicon (VERY IMPORTANT for Vercel)
@app.get("/favicon.ico")
def favicon():
    return JSONResponse(content={}, status_code=204)

