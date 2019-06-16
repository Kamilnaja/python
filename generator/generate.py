from generator import generateRandomWord

searchedString = "lorem"
states = ("NOT_FOUND", "ONE_OK", "ALL_OK")
state = ""

if state == states[0]:  # none found
    print("not found")
elif state == states[1]:  # one ok
    print("one ok, searching")
elif state == states[2]:  # all ok
    print("we have found the searched string!")



generateRandomWord(len(searchedString))
