# Storage handling (JSON)
import json
import os

FILE_PATH = "contacts.json"

def load_contacts():
    if not os.path.exists(FILE_PATH):
        return {}
        
    try:
        with open(FILE_PATH, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading contacts: {e}")
        return {}

def save_contacts(contacts):
    try:
        with open(FILE_PATH, 'w') as f:
            json.dump(contacts, f, indent=4)
    except Exception as e:
        print(f"Error saving contacts: {e}")
