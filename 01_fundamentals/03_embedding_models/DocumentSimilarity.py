from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv

from sklearn.metrics.pairwise import cosine_similarity

import numpy as np

load_dotenv()

model = GoogleGenerativeAIEmbeddings (model = "gemini-embedding-001", output_dimensionality=300)

document = [
"Sachin Tendulkar is known as the 'God of Cricket'.",
"Virat Kohli is one of the best modern-day batsmen.",
"MS Dhoni is one of the greatest captains in cricket history.",
"Joe Root is a top batsman from England.",
"Kane Williamson is a famous cricketer from New Zealand." ]

query = "tell me about sachin"

doc_embeddings =  model.embed_documents(document)
query_embeddings = model.embed_query(query)
scores = cosine_similarity([query_embeddings], doc_embeddings)[0]

index, score = (sorted(list(enumerate(scores)), key = lambda x:x[1]))[-1]

print(query)
print (document[index])
print("similarity is:",score)