from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import setttings

engine = create_engine(setttings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
