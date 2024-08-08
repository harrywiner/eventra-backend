from sqlalchemy.orm import Session
from . import models, schemas

def get_events(db: Session, limit: int = 10, offset: int = 0):
    return db.query(models.Event).offset(offset).limit(limit).all()

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(id=event.id, title=event.title, description=event.description, presenter=event.presenter, date=event.date, location=event.location, image_url=event.image_url)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_preferences(db: Session, limit: int = 10, offset: int = 0):
    return db.query(models.Preference).offset(offset).limit(limit).all()

def create_preference(db: Session, preferences: list):
    created_preferences = []
    for preference in preferences:
        db_preference = models.Preference(
            eventId=preference.eventId,
            liked=preference.liked
        )
        db.add(db_preference)
        db.commit()
        db.refresh(db_preference)
        created_preferences.append(preference)
    return created_preferences

def get_labelled_events(db: Session):
    results = db.query(
    models.Event.id.label('event_id'),
    models.Event.title,
    models.Event.description,
    models.Event.presenter,
    models.Event.date,
    models.Event.location,
    models.Event.image_url,
    models.Preference.id.label('preference_id'),
    models.Preference.liked).join(models.Preference, models.Event.id == models.Preference.eventId).all()  

    events_with_preferences = [
            {
                "event_id": row.event_id,
                "title": row.title,
                "description": row.description,
                "presenter": row.presenter,
                "date": row.date,
                "location": row.location,
                "image_url": row.image_url,
                "preference_id": row.preference_id,
                "liked": row.liked
            }
            for row in results
        ]

    return events_with_preferences
