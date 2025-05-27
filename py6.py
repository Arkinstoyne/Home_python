from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException
import jwt

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            token = credentials.credentials
            try:
                payload = jwt.decode(token, "YOUR_SECRET_KEY", algorithms=["HS256"])
                return payload  # Возвращаем payload токена
            except jwt.ExpiredSignatureError:
                raise HTTPException(status_code=403, detail="Token expired.")
            except jwt.InvalidTokenError:
                raise HTTPException(status_code=403, detail="Invalid token.")
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")