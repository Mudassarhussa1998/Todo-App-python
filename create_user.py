import re

def createuser():
    name = input("Enter your full Name: \n").strip()
    email = input("Enter your Email: \n").strip()
    phone_number = input("Enter your Phone Number: \n (Should not be smaller than 11 number) \n").strip()
    password = input("Enter Password:  \n (Must have first Upper case character , special character , greater than 5 character and number) \n").strip()
    confirm_password = input("Enter Confirm Password: \n").strip()
    
    if not validate_email(email):
        print("Invalid email format.")
        return
    
    if not check_password(password, confirm_password):
        return
    
    if not check_phone_no(phone_number):
        return
       
    data = [email , password , phone_number , name ]
    
    with open("User.txt", "a") as file:
        file.write(",".join(data) + "\n") 
    
    print("User registered successfully!")

def validate_email(email: str) -> bool:
    """Validates email format."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def check_password(password: str, confirm_password: str) -> bool:
    """Validates password security rules."""
    if password != confirm_password:
        print("Passwords do not match.")
        return False
    if len(password) < 5:
        print("Password must be at least 5 characters long.")
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
    if len(phone) < 10:
        print("Phone number should be at least 10 digits long.")
        return False
    return True