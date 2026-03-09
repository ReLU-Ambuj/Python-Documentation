# CLI Contact Manager Entry Point
from contact_manager import ContactManager
from utils.input_handler import get_menu_choice, get_contact_details

def main():
    print("Welcome to Contact Manager v1.0")
    manager = ContactManager()
    
    while True:
        print("\n--- Menu ---")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = get_menu_choice(1, 5)
        
        if choice == 1:
            manager.view_contacts()
        elif choice == 2:
            details = get_contact_details()
            if details:
                manager.add_contact(*details)
        elif choice == 3:
            query = input("Enter name to search: ")
            manager.search_contacts(query)
        elif choice == 4:
            name = input("Enter exact name to delete: ")
            manager.delete_contact(name)
        elif choice == 5:
            manager.save()
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
