from fastapi import FastAPI, Query, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from .database import get_db 
from .crud import get_events, get_preferences

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Whether to allow credentials (cookies, authorization headers, etc.)
    allow_methods=["*"],  # List of allowed HTTP methods
    allow_headers=["*"],  # List of allowed headers
)

@app.get("/")
def read_root():
    return {"Hello": "Boozer"}

@app.get("/events/")
def read_events(limit: int = Query(default=10, ge=1, le=100), offset: int = Query(default=0, ge=0, le=100), db: Session = Depends(get_db)):
    return {"limit": limit, "offset": offset, "events": get_events(db, limit, offset)}

@app.get("/preferences/")
def read_preferences(limit: int = Query(default=10, ge=1, le=100), offset: int = Query(default=0, ge=0, le=100), db: Session = Depends(get_db)):
    return {"limit": limit, "offset": offset, "preferences": get_preferences(db, limit, offset)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)