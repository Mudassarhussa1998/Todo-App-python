def fetchnote(ids):
    found = False  # Track if at least one note is found
    counter = 0

    try:
        ids = int(ids)  # Ensure ids is an integer
    except ValueError:
        print("Invalid ID format.")
        return

    with open("notes.txt", "r") as file:
        for line in file:  # Read file line by line
            fields = line.strip().split(",")  # Remove spaces and split

            if len(fields) < 4:  # Ensure there's enough data
                continue

            if not fields[0].isdigit():  # Check if the ID is numeric
                continue

            stored_id = int(fields[0])

            if stored_id == ids:
                counter += 1
                print(f"{counter}: {fields[3]} : {fields[1]} : {fields[2]}")  # Print each matching note
                found = True

    if not found:
        print("You have no notes.")
