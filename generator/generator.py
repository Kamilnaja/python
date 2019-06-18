import random

def generateRandomWord(searchedLen):
    letters = []
    for x in range(searchedLen):
        randomLetter = random.randint(65, 90)
        letters.append(chr(randomLetter))
    return ",".join(letters).replace(",", "")

def generateResponseTable(searched):
    resTable = []
    for x in searched:
        resTable.append('_')
    return ''.join(resTable)
