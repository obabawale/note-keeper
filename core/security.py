from typing import Union, Any
from datetime import datetime, timedelta
from passlib.context import CryptContext
from core.config import setttings
from jose import jwt

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

ALGORITHM = "HS256"


def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    if not expires_delta:
        expires_delta = timedelta(minutes=setttings.TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    to_encode = {'exp': expire, "sub": subject}
    encoded_jwt = jwt.encode(
        to_encode, setttings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_password_hash(plain_password: str) -> str:
    return pwd_context.hash(plain_password)


def get_password_hash(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
