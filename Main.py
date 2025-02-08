from create_user import createuser
from login_user import login

def main():
    var = int(input("Enter what you want to do: \n 1. For Login \n 2. For Signup \n 3. Exit \n"))
    if var == 1:
        login()
        print("You are login")
    elif var == 2:
        createuser()
        print("user created")
    elif var == 3:
        print("Good Bye .................")
        return 0
    else:
        print("incorrect input \n Try again")
        main()

main()