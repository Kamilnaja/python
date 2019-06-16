import random
from enum import Enum


class State(Enum):
    NOT_FOUND = 0  # no match between searched and generated
    FOUND = 1  # found one or more
    ALL_EQUALS = 2  # all ok
    STR_GENERATED = 3
    NONE_EQUAL = 4  # none match
    PARTIALY_EQUAL = 5  # some match


searchedString = "lorem"
state = State.NONE_EQUAL
currentSearchedLen = len(searchedString)
tempRandomStr = ""


def generateRandomWord(searchedLen=len(searchedString)):
    letters = []
    for x in range(searchedLen):
        randomLetter = random.randint(65, 90)
        letters.append(chr(randomLetter).lower())
    return ','.join(letters).replace(',', '')


def compareRandomWithSearched(random, searched):
    print(random)
    print(searched)


if state == State.NONE_EQUAL:
    tempRandomStr = generateRandomWord()  # generate without params
    compareRandomWithSearched(searchedString, tempRandomStr)
elif state == State.ALL_EQUALS:  # generate with
    generateRandomWord(5)
elif state == State.ALL_EQUALS:
    print("We have succesfully generated your string!")
