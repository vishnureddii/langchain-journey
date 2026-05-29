from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")

st.header("Research paper Tool")
paper_input = st.selectbox("Select a Research A paper", ["Attention all you need",
"Language Models are Unsupervised Multitask Learners", "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
])

style_input = st.selectbox("Select Explanation Style",["Beginner-Friendly", "Technical","code-oriented"])

length_input = st.selectbox("Select Explanation style",["Short Description", "Medium Description",
                                                        "Long Description"])

template = PromptTemplate(template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematical Details:
- Include relevant mathematical equations if present in the paper.
- Explain the mathematical concepts using simple, intuitive code snippets where applicable.

2. Analogies:
- Use relatable analogies to simplify complex ideas.

If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables= ['paper_input','style_input','length_input']
)

prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input': length_input
})

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
