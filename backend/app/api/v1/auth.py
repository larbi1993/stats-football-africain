from fastapi import APIRouter
from app.schemas.user_status import UserStatus
from app.schemas.auth import RegisterResponse, RegiterRequest

router = APIRouter (prefix="/auth", tags=["auth"])

@router.get("/me")
def me():
    return {
        "email" : "larbi9320@gmail.com",
        "user_status" : UserStatus.EN_ATTENTE
    }
    
@router.post("/register", response_model=RegisterResponse)
def register(payload: RegiterRequest):
    return RegisterResponse (
        status = "ok" ,
        next_step = "upload_documents",
        user_status=UserStatus.EN_ATTENTE,
    )