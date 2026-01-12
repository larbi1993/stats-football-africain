from fastapi import APIRouter
from app.schemas.user_status import UserStatus

router= APIRouter(prefix="/verification", tags=["verification"])

@router.get("/status")
def status():
    return {"user_status" : UserStatus.EN_ATTENTE}