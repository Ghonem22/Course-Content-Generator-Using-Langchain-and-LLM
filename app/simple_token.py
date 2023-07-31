from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException

security = HTTPBearer()
class Token(BaseModel):
    access_token: str


STATIC_TOKEN = "jhsdfjnhu6798sdvbui78adc7"

# Middleware to check the token in the incoming request
async def validate_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not credentials.scheme == "Bearer":
        raise HTTPException(status_code=403, detail="Invalid authentication scheme")
    if not credentials.credentials == STATIC_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")
    return credentials.credentials
