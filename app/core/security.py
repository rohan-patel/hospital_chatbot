from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

fake_users_db = {
    "admin": {"username": "admin", "role": "Owner", "password": "adminpass"},
    "drsmith": {"username": "drsmith", "role": "Doctor", "password": "doc123"},
    "nursejane": {"username": "nursejane", "role": "Staff", "password": "staff123"}
}

def authenticate_user(username, password):
    user = fake_users_db.get(username)
    if not user or user["password"] != password:
        return None
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return fake_users_db.get(payload.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def role_required(allowed_roles):
    def wrapper(user: dict = Depends(get_current_user)):
        if user["role"] not in allowed_roles:
            raise HTTPException(status_code=403, detail="You don’t have permission to access this module.")
        return user
    return wrapper