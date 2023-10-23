from pydantic import BaseModel
from typing import Optional


class NoteBase(BaseModel):
    """Schema for notes
    """
    title: Optional[str] = None
    content: Optional[str] = None


class NoteCreate(NoteBase):
    title: str


class NoteUpdate(NoteBase):
    pass


class NoteInDBBase(NoteBase):
    id: int
    title: str

    class Config:
        orm_mode = True
