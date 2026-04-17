from sqlalchemy.orm import Session
from models import User

def create_user(db: Session, name:str, email:str):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session,):
    return db.query(User).all()

def update_user(db: Session, user_id: int, name: str = None, email: str = None):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return None

    if name is not None:
        db_user.name = name
    if email is not None:
        db_user.email = email

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return None

    db.delete(db_user)
    db.commit()
    return db_user
