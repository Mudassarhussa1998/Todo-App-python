def Addnote(ids):
    NoteName = input("Enter Note Name: ").strip()
    NoteDescription = input("Enter the note you want to add: ").strip()

    if not NoteName or not NoteDescription:
        print("Note name and description cannot be empty!")
        return

    Note = [str(ids), NoteName, NoteDescription]

    with open("notes.txt", "a") as file:
        file.write(",".join(Note) + "\n")

    print("Note added successfully!")
