# Core Manager Logic
from storage import load_contacts, save_contacts

class ContactManager:
    def __init__(self):
        self.contacts = load_contacts() # Expected format: { "Name": {"phone": "...", "email": "..."} }
        
    def add_contact(self, name, phone, email):
        self.contacts[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' added successfully.")
        
    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
            
        for name, info in self.contacts.items():
            print(f"Name: {name} | Phone: {info.get('phone')} | Email: {info.get('email')}")
            
    def search_contacts(self, query):
        found = False
        query = query.lower()
        for name, info in self.contacts.items():
            if query in name.lower():
                print(f"Match: {name} - {info}")
                found = True
        if not found:
            print("No matches found.")
            
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted '{name}'.")
        else:
            print(f"Contact '{name}' not found.")
            
    def save(self):
        save_contacts(self.contacts)
