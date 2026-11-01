from fastapi import FastAPI

from app.routers.health import router as health_router
from app.routers.upload import router as upload_router
from app.routers.chat import router as chat_router

app = FastAPI(
    title="EnterpriseAIAssistant",
    description="Enterprise GenAI and Agentic AI Platform",
    version="1.0.0",
)
app.include_router(health_router)
app.include_router(upload_router)
app.include_router(chat_router)

@app.get("/")
async def root():
    return {"message": "Enterprise AI platform is running successfully"}
