import random


def Addnote(userid):
    ids = random.randint(1000, 9999)
    while True:
        NoteName = input("Enter Note Name: ").strip()
        if not NoteName:
            print("Note name cannot be empty! Please try again.")
            continue

        NoteDescription = input("Enter the note you want to add: ").strip()
        if not NoteDescription:
            print("Note description cannot be empty! Please try again.")
            continue

        break

    try:
        with open("notes.txt", "r") as file:
            existing_notes = {int(line.split(",")[0]) for line in file if line.strip()}
    except FileNotFoundError:
        existing_notes = set()  # File does not exist yet

    # Ensure unique ID only if needed
    if ids in existing_notes:
        while ids in existing_notes:
            ids = random.randint(1000, 9999)

    with open("notes.txt", "a") as file:
        file.write(f"{userid},{NoteName},{NoteDescription},{ids}\n")

    print("Note added successfully!")
