def update_note(userid, note_id):
    found = False  # Track if at least one note is found
    updated_lines = []  # Store modified lines

    try:
        userid = int(userid)
        note_id = int(note_id)
    except ValueError:
        print("Invalid ID format.")
        return

    Ans = input("What would you like to update? \n 1. Note Name \n 2. Note Description \n ")
    if Ans == "1":
        updated_name: str = input("Please enter the new note name: \n")
    elif Ans == "2":
        updated_description = input("Please enter the new note description: \n")
    else:
        print("Incorrect input")
        return

    with open("notes.txt", "r") as file:
        for line in file:
            fields = line.strip().split(",")

            if len(fields) < 4:  # Ensure enough data
                updated_lines.append(line)
                continue

            if not fields[0].isdigit() or not fields[3].isdigit():  # Validate numeric IDs
                updated_lines.append(line)
                continue

            stored_id = int(fields[0])
            stored_note_id = int(fields[3])

            if stored_id == userid and stored_note_id == note_id:
                found = True
                if Ans == "1":
                    fields[1] = updated_name  # Update note name
                elif Ans == "2":
                    fields[2] = updated_description  # Update note description

                updated_lines.append(",".join(fields) + "\n")  # Save updated note
            else:
                updated_lines.append(line)  # Keep other lines unchanged

    if found:
        with open("notes.txt", "w") as file:
            file.writelines(updated_lines)  # Write updated content
        print("Note updated successfully.")
    else:
        print("No matching note found.")
