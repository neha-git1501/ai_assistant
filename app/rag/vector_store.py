from pathlib import Path
from langchain_community.vectorstores import FAISS
from app.rag.embedding import embeddings
from app.rag.documents import  create_documents

VECTOR_STORE_DIR = Path(__file__).resolve().parents[2]/"vector_store"
def create_vector_store(
        chunks: list[str],
        source: str="uploaded_file",
        source_type:str="text",
)->FAISS:
    documents = create_documents(
        chunks=chunks,
        source=source,
        source_type=source_type,
    )
    if VECTOR_STORE_DIR.exists():
        vector_store = FAISS.load_local(
            str(VECTOR_STORE_DIR),
            embeddings,
            allow_dangerous_deserialization=True,
        )
        vector_store.add_documents(documents)
    else:
        vector_store = FAISS.from_documents(
        documents=documents,
        embedding=embeddings,
        )
    vector_store.save_local(
        str(VECTOR_STORE_DIR)
    )
    return vector_store
def load_vector_store()->FAISS:
    if not VECTOR_STORE_DIR.exists():
        raise FileNotFoundError(
            "Vector store does not exist. Ingest a document first."
        )
    return FAISS.load_local(
        str(VECTOR_STORE_DIR),
        embeddings,
        allow_dangerous_deserialization=True,
    )