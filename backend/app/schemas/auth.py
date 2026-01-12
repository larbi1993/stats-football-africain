from pydantic import BaseModel, EmailStr
from app.schemas.user_status import UserStatus

class RegiterRequest (BaseModel):
    email: EmailStr
    password: str
    
    
class RegisterResponse(BaseModel):
    status: str
    next_step: str
    user_status: UserStatus
    
    
class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user_status: UserStatus
