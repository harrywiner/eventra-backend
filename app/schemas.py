# app/schemas.py
from pydantic import BaseModel

class EventBase(BaseModel):
    id: int
    title: str
    description: str
    date: str
    location: str
    image_url: str

class EventCreate(EventBase):
    pass

class Event(EventBase):
    class ConfigDict:
        from_attributes = True