from pydantic import BaseModel
from app.schemas.document_type import DocumentType
from app.schemas.user_status import UserStatus



class VerificationSubmitRequest(BaseModel):
    document_type: DocumentType  # ex: "passport" ou "driver_license"
    note: str | None = None

class VerificationSubmitResponse(BaseModel):
    status: str
    message: str
    user_status: UserStatus
