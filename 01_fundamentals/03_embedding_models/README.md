# Embedding Models + Semantic Search
 
Most important section — embeddings are
the foundation of RAG pipelines.
 
## What I Built
1. Gemini Embedding Model implementation
2. HuggingFace Embedding Model
3. Local Embedding Model understanding
4. Semantic Search using Cosine Similarity
5. Document Similarity Application
 
## What Are Embeddings
Text converted to numerical vectors
that capture semantic meaning.
 
"King" and "Queen" → similar vectors
"King" and "Database" → different vectors
 
## Cosine Similarity
Measures angle between two vectors
→ 1.0 = identical meaning
→ 0.0 = completely different
→ Used in semantic search to find
   most relevant documents
 
## Why This Matters
This is the core of RAG:
User query → embedding →
find similar document embeddings →
retrieve relevant context →
LLM generates answer
 
## Models Used
- Google Gemini Embeddings
- HuggingFace sentence-transformers
- Local embedding model
 
## Real World Application Built
Document Similarity App:
→ Input two documents
→ Converts both to embeddings
→ Calculates cosine similarity score
→ Returns similarity percentage
→ Foundation of document search systems
