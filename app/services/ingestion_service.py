from app.services.document_loader import load_document
from app.rag.chunking import split_text
from app.rag.vector_store import create_vector_store

def ingest_document(file_path:str):
    text=load_document(file_path)
    chunks=split_text(text)
    vector_store=create_vector_store(
        chunks,
        source=file_path,
        source_type="uploaded_file",
    )
    return vector_store

