from sqlalchemy.orm import Session
from . import models, schemas

def get_events(db: Session, limit: int = 10, offset: int = 0):
    return db.query(models.Event).offset(offset).limit(limit).all()

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(id=event.id, title=event.title, description=event.description, date=event.date, location=event.location, image_url=event.image_url)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
