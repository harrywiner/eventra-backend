from fastapi import FastAPI, Query

from .database import get_events

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Boozer"}

@app.get("/events/")
def read_events(limit: int = Query(default=10, ge=1, le=10), offset: int = Query(default=0, ge=0, le=10)):
    return {"limit": limit, "offset": offset, "events": get_events(limit, offset)}