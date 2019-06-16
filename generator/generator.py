import random

def generateRandomWord(searchedLen):
    for x in range(searchedLen):
        randomLetter = random.randint(65, 90)
        print(chr(randomLetter).lower())
