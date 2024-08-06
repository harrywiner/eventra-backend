# app/init_db.py
import csv
from sqlalchemy.orm import Session
from .database import engine, Base, SessionLocal
from .models import Event
from .crud import create_event
import json


def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Read CSV file
    # with open('data/ronnie_scotts_100.csv', 'r') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         event = Event(**row)
    #         create_event(db, event)
    #     db.commit()
    # db.close()

    # Open and read the JSON file
    with open('data/edinburgh_200.json', 'r') as json_file:
        data = json.load(json_file)

    # Create an event object from the JSON data
    for d in data:
        event = Event(**d)
        create_event(db, event)
    db.commit()
    db.close()

if __name__ == '__main__':
    init_db()