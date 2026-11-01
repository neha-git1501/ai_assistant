from pathlib import Path
from app.config.settings import CONFLUENCE_PATH
from app.rag.chunking import split_text
from app.rag.vector_store import create_vector_store

SUPPORTED_EXTENSIONS = {
    ".txt",
    ".log",
    ".pdf",
    ".docx",
    ".csv",
    ".xlsx",
    ".pptx",
    ".html"
}

def update_confluence_vectors() -> None:
    files = list(CONFLUENCE_PATH.glob("*.txt"))
    if not files:
        print("No confluence files found.")
        return
    total_files = 0
    total_chunks = 0
    for file_path in files:
        text = file_path.read_text(
            encoding = "utf-8",
            errors = "ignore"
        )
        if not text.strip():
            continue
        chunks = split_text(text)
        if not chunks:
            continue
        create_vector_store(
            chunks=chunks,
            source=file_path.name,
            source_type="confluence",
        )
        total_files += 1
        total_chunks += len(chunks)
        print(
            f"Indexed: {file_path.name}"
            f"({len(chunks)} chunks)"
        )
    print("="*60)
    print(f"confluence files indexed: {total_files}")
    print(f"confluence chunks indexed: {total_chunks}")
if __name__ == "__main__":
    update_confluence_vectors()