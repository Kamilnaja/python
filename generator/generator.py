import random

def generateRandomWord(searchedLen):
    letters = []
    for _ in range(searchedLen):
        aciiStart = 97
        asciiEnd = 122 + 1 # because of exclusive randrange
        randomLetter = random.randrange(aciiStart, asciiEnd + 1) 
        # replace 124 with space
        if randomLetter == 123:
            randomLetter = 32
        letters.append(chr(randomLetter))
    return ",".join(letters).replace(",", "")


def generateResponseTable(searched):
    resTable = []
    for _ in searched:
        resTable.append('_')
    return ''.join(resTable)
