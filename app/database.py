import json

def get_events(limit: int = 10, offset: int = 0):
    with open("data/dummy.json", "r") as file:
        events = json.load(file)
    return events[offset:offset+limit]