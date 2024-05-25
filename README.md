# Eventra Recommendations Backend

A project to serve event objects and recieve user preferences

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