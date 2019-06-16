import random
from main import searchedString

def generateRandomWord(searchedLen=len(searchedString)):
    # print('searched len :' + str(len(searchedString)))
    letters = []
    for x in range(searchedLen):
        randomLetter = random.randint(65, 90)
        letters.append(chr(randomLetter).lower())
    return ",".join(letters).replace(",", "")

