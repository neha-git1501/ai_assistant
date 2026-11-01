from app.rag.embedding import embeddings
vector = embeddings.embed_query(
    "Why IMS registration failed?"
)
print(type(vector))
print(len(vector))
print(vector[:10])