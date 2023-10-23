import secrets
from pydantic import BaseSettings


class Settings(BaseSettings):

    """Configuration class for managing application wide settings
    """
    SECRET_KEY: str = secrets.token_urlsafe(32)
    TOKEN_EXPIRE_MINUTES: int = 60
    


setttings = Settings()
