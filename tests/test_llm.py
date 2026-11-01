from app.llm.ollama_service import llm
response=llm.invoke(
    "Explain RAG in one sentence."
)
print(response.content)