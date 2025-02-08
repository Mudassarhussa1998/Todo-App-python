from Fetchnote import fetchnote
from AddNote import Addnote
from DeleteNote import deletenote
from UpdateNote import update_note

def get_note_id() -> int :
    note_id = int(input("Enter note id : "))
    return note_id

def home(user_id):
    print("index no : Note id : Note Title : Note Content ")
    fetchnote(user_id)
    print("\n--------------------------------------------------------\n")
    option = input("What would you like to do? \n 1. Add a Note \n 2. Delete a Note \n 3. Update Note \n 4. Logout \n 5. Exit \n")
    if option == "1":
        Addnote(user_id)
        home(user_id)
    elif option == "2":
        note_id = get_note_id()
        deletenote(user_id , note_id)
        home(user_id)
    elif option == "3":
        note_id = get_note_id()
        update_note(user_id , note_id)
        home(user_id)
    elif option == "4":
        print("Thank you for using this application. Goodbye")
        return 0
    elif option == "5":
        exit()
    else:
        print("Invalid option")
        home(user_id)
