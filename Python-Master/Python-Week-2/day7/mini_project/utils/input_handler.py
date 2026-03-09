# Input handling utilities
from .validation import is_valid_email, is_valid_phone

def get_menu_choice(min_val, max_val):
    while True:
        try:
            choice = int(input("Select an option: "))
            if min_val <= choice <= max_val:
                return choice
            print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_contact_details():
    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return None
        
    phone = input("Enter Phone: ").strip()
    if phone and not is_valid_phone(phone):
        print("Invalid phone format.")
        return None
        
    email = input("Enter Email: ").strip()
    if email and not is_valid_email(email):
        print("Invalid email format.")
        return None
        
    return name, phone, email
