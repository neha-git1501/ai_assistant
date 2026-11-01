from pydantic import BaseModel
from starlette import status


class UploadResponse(BaseModel):
    status: str
    session_id: str
    filename: str
    content_type: str|None
    size: int
    path: str

