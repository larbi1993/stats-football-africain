from pydantic import BaseModel, EmailStr
from app.schemas.user_status import UserStatus

class RegiterRequest (BaseModel):
    email: EmailStr
    password: str
    
    
class RegisterResponse(BaseModel):
    status: str
    next_step: str
    user_status: UserStatus