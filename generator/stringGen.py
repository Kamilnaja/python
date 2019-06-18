import random
from main import searched

def generateRandomWord(searchedLen=len(searched)):
    letters = []
    for x in range(searchedLen):
        randomLetter = random.randint(97, 122)
        letters.append(chr(randomLetter))
    return ",".join(letters).replace(",", "")

