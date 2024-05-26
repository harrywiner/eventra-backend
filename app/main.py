from fastapi import FastAPI, Query, Depends

from sqlalchemy.orm import Session

from .database import get_db 
from .crud import get_events

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Boozer"}

@app.get("/events/")
def read_events(limit: int = Query(default=10, ge=1, le=100), offset: int = Query(default=0, ge=0, le=100), db: Session = Depends(get_db)):
    return {"limit": limit, "offset": offset, "events": get_events(db, limit, offset)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)