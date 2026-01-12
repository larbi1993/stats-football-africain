from pydantic import BaseModel

class VerificationSubmitRequest(BaseModel):
    document_type: str  # ex: "passport" ou "driver_license"
    note: str | None = None

class VerificationSubmitResponse(BaseModel):
    status: str
    message: str
