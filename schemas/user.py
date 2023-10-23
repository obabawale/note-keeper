from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):

    """
    User class schema
    """

    email: Optional[EmailStr]
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    full_name = Optional[str] = None


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: Optional[str]


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
