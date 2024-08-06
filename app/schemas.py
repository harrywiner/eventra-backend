# app/schemas.py
from pydantic import BaseModel

class EventBase(BaseModel):
    id: int
    title: str
    description: str
    presenter: str
    date: str
    location: str
    image_url: str

class EventCreate(EventBase):
    pass

class Event(EventBase):
    class ConfigDict:
        from_attributes = True

class PreferenceBase(BaseModel):
    eventId: int
    liked: bool

class PreferenceCreate(PreferenceBase):
    pass

class Preference(PreferenceBase):
    id: int

    class Config:
        from_attributes = True