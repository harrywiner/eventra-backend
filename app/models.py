from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    date = Column(String)
    location = Column(String)
    image_url = Column(String)
    preferences = relationship("Preference", back_populates="event")

class Preference(Base):
    __tablename__ = "preferences"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    eventId = Column(Integer, ForeignKey('events.id'), nullable=False)
    liked = Column(Boolean)

    event = relationship("Event", back_populates="preferences")