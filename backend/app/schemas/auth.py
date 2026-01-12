from pydantic import BaseModel
from app.schemas.user_status import UserStatus

class RegiterRequest (BaseModel):
    email: str
    password: str
    
    
class RegisterResponse(BaseModel):
    status: str
    next_step: str
    user_status: UserStatus