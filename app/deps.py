from fastapi import Depends, HTTPException
from app.auth import decode_token

def get_current_user_role(token: str):
    payload = decode_token(token)
    return payload.get("role")

def role_required(role: str):
    def dependency(token: str = Depends()):
        user_role = get_current_user_role(token)
        if user_role != role:
            raise HTTPException(status_code=403, detail="Forbidden")
    return dependency
