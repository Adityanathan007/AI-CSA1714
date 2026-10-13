def vacuum_cleaner(room):
    for position in room:
        if room[position] == "Dirty":
            print("Cleaning room", position)
            room[position] = "Clean"
        else:
            print("Room", position, "is already clean")

    print("All rooms are clean!")

room = {"A": "Dirty", "B": "Dirty"}
vacuum_cleaner(room)
