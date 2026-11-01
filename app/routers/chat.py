from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.query_service import ask_question

router = APIRouter(
    prefix="/api",
    tags=["chat"],
)
class ChatRequest(BaseModel):
    question: str

class Source(BaseModel):
    source: str
    source_type: str

class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]

@router.post(
    "/chat",
    response_model=ChatResponse,
)
async def chat(request: ChatRequest)->ChatResponse:
    question = request.question.strip()
    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty.",
        )
    response = ask_question(question)
    return ChatResponse(
        answer=response["answer"],
        sources=response["sources"]
    )