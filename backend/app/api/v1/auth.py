from fastapi import APIRouter
from app.schemas.user_status import UserStatus

router = APIRouter (prefix="/auth", tags=["auth"])

@router.get("/me")
def me():
    return {
        "email" : "larbi9320@gmail.com",
        "user_status" : UserStatus.EN_ATTENTE
    }