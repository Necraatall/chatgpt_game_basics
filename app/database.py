from sqlalchemy.orm import Session
from models import Character, Base, engine, SessionLocal

def init_db():
    Base.metadata.create_all(bind=engine)

def add_character(description, image_url):
    db: Session = SessionLocal()
    new_character = Character(description=description, image_url=image_url)
    db.add(new_character)
    db.commit()
    db.close()
