from typing import Optional
from sqlalchemy.orm import Session
from models.note import Note
from base import CRUDBase

from schemas.note import NoteCreate, NoteUpdate


class CRUDNote(CRUDBase[Note, NoteCreate, NoteUpdate]):

    def get_note_by_title(self, db: Session, *, title: str) -> Optional[Note]:
        """Get a note by its title
        """
        return db.query(self.model).filter(title=title).first()
