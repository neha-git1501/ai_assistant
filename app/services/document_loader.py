from pathlib import Path
def load_document(file_path: str)->str:
    path = Path(file_path)
    extension = path.suffix.lower()
    if extension in [".txt",".log"]:
        return path.read_text(
            encoding = "utf-8",
            errors = "ignore"
        )
    raise ValueError(
        f"Unsupported file format: {extension}"
    )