# Input Validation using String operations / Regex
import re

def is_valid_email(email):
    # Simple regex for email validation
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

def is_valid_phone(phone):
    # Strip spaces, dashes, parentheses
    clean_phone = "".join(c for c in phone if c.isdigit())
    return len(clean_phone) >= 10
