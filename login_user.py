def login():
    Email = input("Enter your email \n")  # No need for explicit str()
    Password = input("Enter Password \n")

    with open("User.txt", "r") as file:
        Details = file.read()  # Read file contents

    for line in Details.splitlines():  # Iterate over each line
        fields = line.split(",")  # Split into list [email, password, phone, name]
        
        if len(fields) < 2:  # Ensure there's at least email and password
            continue

        stored_email, stored_password = fields[0], fields[1]

        if stored_email == Email:
            if stored_password == Password:
                print("Thanks for logging in!")
                return
            else:
                print("Incorrect Password")
                return

    print("Incorrect Email")
