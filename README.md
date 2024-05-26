# Eventra Recommendations Backend

A project to serve event objects and receive user preferences  

## Usage

Setup virtual environment 

Mac/Linux
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Running

Locally
```bash
uvicorn app.main:app --reload
```

Initialising DB
```bash
python3 -m app.init_db
```

## .env
```bash
DB_URL=postgresql://user:@localhost/eventra
```