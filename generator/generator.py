import random

def generateRandomWord(searchedLen):
    letters = []
    for x in range(searchedLen):
        randomLetter = random.randrange(97, 122)
        letters.append(chr(randomLetter))
    return ",".join(letters).replace(",", "")


def generateResponseTable(searched):
    resTable = []
    for x in searched:
        resTable.append('_')
    return ''.join(resTable)
