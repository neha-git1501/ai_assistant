from typing import List
from pathlib import Path
from langchain_core.documents import Document
from langchain_community.document_loaders import (
TextLoader,
PyPDFLoader,
Docx2txtLoader,
UnstructuredExcelLoader,
)

def create_documents(
        chunks: list[str],
        source: str,
        source_type: str,
)->list[Document]:
    """
    Convert text chunks into LangChain Documents with metadata.
    """
    return [
        Document(
            page_content=chunk,
            metadata={
                "source": source,
                "source_type": source_type
            },
        )
        for chunk in chunks
    ]