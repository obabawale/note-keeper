from db.base_class import Base
from sqlalchemy import Column, Integer, String


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,)
    content = Column(String)
