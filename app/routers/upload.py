from pathlib import Path
from uuid import uuid4
from fastapi import APIRouter, File, HTTPException, UploadFile, status
from app.services.upload_service import save_upload
from app.models.upload import UploadResponse
from app.services.upload_service import ingest_uploaded_file

router = APIRouter(
    prefix="/api",
    tags=["upload"],
)
@router.post(
    "/upload",
    response_model=UploadResponse,
    status_code=status.HTTP_201_CREATED
)
async def upload_file(
        file: UploadFile=File(...)
) -> UploadResponse:
    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Filename is required",
        )
    session_id = str(uuid4())
    try:
        result = await save_upload(
            file=file,
            session_id=session_id,
        )

        ingestion_result = ingest_uploaded_file(
            result["path"]
        )
        return UploadResponse(
            status="success",
            session_id=session_id,
            filename=result["filename"],
            content_type=result["content_type"],
            size=result["size"],
            path=result["path"],
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(exc)}",
        )
