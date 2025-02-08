def deletenote(userid, noteid):
    found = False  # Track if at least one note is found
    updated_lines = []  # Store modified lines

    try:
        userid = int(userid)
        noteid = int(noteid)
    except ValueError:
        print("Invalid ID format.")
        return

    with open("notes.txt", "r") as file:
        for line in file:
            fields = line.strip().split(",")  # Remove spaces and split

            if len(fields) < 4:  # Ensure there's enough data
                updated_lines.append(line)  # Keep unchanged lines
                continue

            if not fields[0].isdigit() or not fields[3].isdigit():  # Validate user ID and note ID
                updated_lines.append(line)
                continue

            stored_id = int(fields[0])
            stored_noteid = int(fields[3])

            if stored_id == userid and stored_noteid == noteid:
                print(f"Note {noteid} deleted for User {userid}")
                found = True
                continue  # Skip this line (delete it)

            updated_lines.append(line)  # Keep other lines unchanged

    if found:
        with open("notes.txt", "w") as file:
            file.writelines(updated_lines)  # Write updated content
        print("Note deleted successfully.")
    else:
        print("No matching note found.")
