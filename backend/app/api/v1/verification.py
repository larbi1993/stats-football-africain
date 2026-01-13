from fastapi import APIRouter
from app.schemas.user_status import UserStatus
from app.schemas.verification import VerificationSubmitRequest, VerificationSubmitResponse

router = APIRouter(prefix="/verification", tags=["verification"])

@router.get("/status")
def status():
    return {"user_status": UserStatus.EN_ATTENTE}

@router.post("/submit", response_model=VerificationSubmitResponse)
def submit(payload: VerificationSubmitRequest):
    return VerificationSubmitResponse(
        status="ok",
        message=f"Verification request received (document_type={payload.document_type})",
        user_status=UserStatus.EN_ATTENTE,
    )
