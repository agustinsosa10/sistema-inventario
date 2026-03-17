import bcrypt
from jose import jwt
from datetime import datetime, timedelta, timezone
from app.core.config import settings


def get_password_hash(password: str) -> str:
    pwd_clean = str(password).strip().encode("utf-8")
    return bcrypt.hashpw(pwd_clean, bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.strip().encode("utf-8"), hashed_password.encode("utf-8")
    )


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
