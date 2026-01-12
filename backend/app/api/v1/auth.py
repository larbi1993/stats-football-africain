from fastapi import APIRouter

router = APIRouter (prefix="/auth", tags=["auth"])

@router.get("/me")
def me():
    return {
        "email" : "larbi9320@gmail.com",
        "user_status" : "EN_ATTENTE"
    }