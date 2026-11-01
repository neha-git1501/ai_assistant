from langchain_huggingface import HuggingFaceEmbeddings

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
def create_embeddings(texts: list[str])->list[list[float]]:
    vectors = embeddings.embed_documents(texts)
    return vectors

def create_query_embeddings(texts: str)->list[float]:
    return embeddings.embed_query(texts)

