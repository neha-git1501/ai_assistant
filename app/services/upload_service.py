from pathlib import Path
from typing import Annotated
from fastapi import UploadFile,File
from app.rag.chunking import split_text
from app.rag.vector_store import create_vector_store
from app.services.document_loader import load_document

BASE_UPLOAD_DIR = Path("uploads")
CHUNK_SIZE = 1024*1024
ALLOWED_EXTENSIONS = {
    ".txt",
    ".log"
}
MAX_FILE_SIZE = 10 * 1024 * 1024
async def save_upload(
        file:UploadFile,
        session_id:str,
) -> dict:
    if not file.filename:
        raise ValueError("filename is required")
    filename=Path(file.filename).name
    extension=Path(file.filename).suffix.lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(
            f'Unsupported file type:{extension}'
        )
    session_dir = BASE_UPLOAD_DIR / session_id
    session_dir.mkdir(
        parents=True,
        exist_ok=True
    )
    target_path = session_dir / filename
    total_size = 0
    try:
        with target_path.open("wb") as buffer:
            while chunk := await file.read(CHUNK_SIZE):
                total_size += len(chunk)
                if total_size > MAX_FILE_SIZE:
                    raise ValueError(
                        "File size exceeds the allowed limit"
                    )
                buffer.write(chunk)
    except Exception:
        target_path.unlink(missing_ok=True)
        raise
    return {
        "filename": filename,
        "content_type": file.content_type,
        "size": total_size,
        "path": str(target_path),
    }


def ingest_uploaded_file(file_path:str)->dict:
    text = load_document(file_path)
    chunks = split_text(text)
    print("="*60)
    print("Chunks Created:", len(chunks))
    print("="*60)
    for chunk in chunks:
        print(chunk)
    if not chunks:
        raise ValueError(
            "Uploaded file contains no readable text."
        )
    vector_store = create_vector_store(chunks)
    return {
        "chunks" : len(chunks),
        "vector_store_created" : True
    }