import secrets
from pydantic import BaseSettings, validator, PostgresDsn
from typing import Optional, Dict, Any


class Settings(BaseSettings):

    """Configuration class for managing application wide settings
    """
    SECRET_KEY: str = secrets.token_urlsafe(32)
    TOKEN_EXPIRE_MINUTES: int = 60
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )


setttings = Settings()
