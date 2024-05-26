# app/init_db.py
import csv
from sqlalchemy.orm import Session
from .database import engine, Base, SessionLocal
from .models import Event
from .crud import create_event


def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Read CSV file
    with open('data/ronnie_scotts_100.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            event = Event(**row)
            create_event(db, event)
        db.commit()
    db.close()

if __name__ == '__main__':
    init_db()