import re
import random


def createuser():
    name = input("Enter your full Name: \n").strip()
    email = input("Enter your Email: \n").strip()
    phone_number = input("Enter your Phone Number: \n (Should not be smaller than 11 digits) \n").strip()
    password = input(
        "Enter Password:  \n (Must have first Upper case character, special character, greater than 5 characters, and a number) \n").strip()
    confirm_password = input("Enter Confirm Password: \n").strip()

    ID = random.randint(1000, 9999)

    try:
        with open("User.txt", "r") as file:
            Details = file.read()
    except FileNotFoundError:
        Details = ""  # File may not exist yet

    # Check if email is already registered
    for line in Details.splitlines():
        fields = line.split(",")
        if len(fields) >= 2 and fields[0] == email:
            print("This email is already registered. Please use another one.")
            return

    # Ensure ID uniqueness
    stored_IDs = {int(line.split(",")[2]) for line in Details.splitlines() if line.strip()}
    while ID in stored_IDs:
        ID = random.randint(1000, 9999)

    if not validate_email(email):
        print("Invalid email format.")
        return

    if not check_password(password, confirm_password):
        return

    if not check_phone_no(phone_number):
        return

    data = [email, password, str(ID), phone_number, name]

    with open("User.txt", "a") as file:
        file.write(",".join(data) + "\n")

    print("User registered successfully!")


def validate_email(email: str) -> bool:
    """Validates email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def check_password(password: str, confirm_password: str) -> bool:
    """Validates password security rules."""
    if password != confirm_password:
        print("Passwords do not match.")
        return False
    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return False
    if password[0].islower():
        print("Password must start with an uppercase letter.")
        return False
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        return False
    if not any(char in "!@#$%^&*()_+" for char in password):
        print("Password must contain at least one special character (!@#$%^&*()_+).")
        return False
    return True


def check_phone_no(phone: str) -> bool:
    """Validates phone number format."""
    if not phone.isdigit():
        print("Phone number must contain only digits.")
        return False
    if len(phone) < 11:
        print("Phone number should be at least 11 digits long.")
        return False
    return True
