from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-001", output_dimensionality=32)

doc = ["virat kohli is international reputed player",
       "sachin is known as God of cricket"]

result = model.embed_documents(doc)

print(result)