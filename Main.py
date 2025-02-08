from create_user import createuser
from login_user import login
from AddNote import Addnote
from Fetchnote import fetchnote
from DeleteNote import deletenote

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
    elif var == 4:
        Addnote(3212)
    elif var == 5:
        fetchnote(3212)
    elif var == 6:
        deletenote(3212,3646)
    else:
        print("incorrect input \n Try again")
        main()

main()