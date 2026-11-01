from pathlib import Path
PROJECT_DIR = Path(__file__).resolve().parents[2]
KNOWLEDGE_BASE_DIR = PROJECT_DIR / "knowledge_base"
JIRA_PATH = KNOWLEDGE_BASE_DIR / "jira"
CONFLUENCE_PATH = KNOWLEDGE_BASE_DIR / "confluence"
EXCEL_PATH = KNOWLEDGE_BASE_DIR / "excel"
WORD_PATH = KNOWLEDGE_BASE_DIR / "word"
PDF_PATH = KNOWLEDGE_BASE_DIR / "pdf"
VECTOR_STORE_DIR = PROJECT_DIR / "vector_store"
