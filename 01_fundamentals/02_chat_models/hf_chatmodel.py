from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="Text-Generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("what is the capital of delhi?")
print(result)