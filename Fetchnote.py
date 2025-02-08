from numpy.core.defchararray import isnumeric

def fetchnote(ids: int):
    found = False  # Track if at least one note is found
    counter = 0
    with open("notes.txt", "r") as file:
        for line in file:  # Read file line by line
            fields = line.strip().split(",")  # Remove spaces and split

            counter += 1

            if len(fields) < 1:  # Ensure there's data
                continue

            if not isnumeric(fields[0]):
                continue
            stored_id = int(fields[0])

            if stored_id == ids:
                print( f"Note no: {counter} \n {fields[3]} {fields[1]} {fields[2]} " )  # Print each matching note
                found = True


    if not found:
        print("You have no notes.")