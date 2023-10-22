from sqlalchemy.orm import Session, Union, Dict, Any

from typing import Optional
from fastapi.encoders import jsonable_encoder
from base import CRUDBase
from models.user import User
from schemas.user import UserCreate, UserUpdate

def get_password_hash(): return False
def verify_password(): return False

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    """CRUD class for the User model
    """

    def get_user_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()
    
    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
         email = obj_in.email,   
         password = get_password_hash(obj_in.password),
         full_name = obj_in.full_name,
         is_superuser = obj_in.is_superuser,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update(self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["password"] = hashed_password
        return super().update(db=db, db_obj=db_obj, obj_in=update_data)
    
    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_user_by_email(db, email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active
    
    def is_superuser(self, user: User) -> bool:
        return user.is_superuser