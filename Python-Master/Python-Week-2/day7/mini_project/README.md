# Mini-Project: CLI Contact Manager

## Objective
Build a modular, command-line Contact Manager application. This project tests your ability to use dictionaries, lists, strings, and standard file I/O over multiple Python files.

## Architecture
- `main.py`: The entry point and command loop.
- `contact_manager.py`: Core logic for adding, searching, and deleting contacts.
- `storage.py`: Functions handling loading/saving contacts to a JSON file.
- `utils/input_handler.py`: Reusable functions for taking and sanitizing user input.
- `utils/validation.py`: Regex or logic to ensure emails/phones are valid.

## Features
1. Add Contact (Name, Phone, Email)
2. View All Contacts (Formatted cleanly)
3. Search Contacts (Substring search on Name)
4. Delete Contact
5. Save/Load automatically on exit/startup.
