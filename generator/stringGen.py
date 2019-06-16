import random
from main import searched

def generateRandomWord(searchedLen=len(searched)):
    # print('searched len :' + str(len(searchedString)))
    letters = []
    for x in range(searchedLen):
        randomLetter = random.randint(65, 90)
        letters.append(chr(randomLetter).lower())
    return ",".join(letters).replace(",", "")

