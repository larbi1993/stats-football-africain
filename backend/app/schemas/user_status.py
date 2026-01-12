from enum import Enum

class UserStatus (str, Enum):
    EN_ATTENTE = "EN_ATTENTE"
    VERIFIE = "VERIFIE"
    REFUSE = "REFUSE"
    SUSPENDU = "SUSPENDU"