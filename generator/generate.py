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
appState = State.NONE_EQUAL
currentSearchedLen = len(searchedString)
tempRandomStr = []
tempSearchedStr = []


def generateRandomWord(searchedLen=len(searchedString)):
    letters = []
    for x in range(searchedLen):
        randomLetter = random.randint(65, 90)
        letters.append(chr(randomLetter).lower())
    return ",".join(letters).replace(",", "")


def compareRandomWithSearched(searched, random):
    searchedIterator = iter(searched)
    randomIterator = iter(random)

    for x in searchedString:
        if next(searchedIterator) == next(randomIterator):
            print("equal " + x + random + " searched : " + searched)
            global appState
            appState = State.PARTIALY_EQUAL
            tempSearchedStr.append("_")
            print(tempRandomStr)
            rerun()
        else:
            tempSearchedStr.append(x)
            appState = State.PARTIALY_EQUAL
    print("tempSearchedStr : " + "".join(tempSearchedStr))
    rerun()


def rerun():
    if appState == State.NONE_EQUAL:
        tempRandomStr = generateRandomWord()  # generate without params
        compareRandomWithSearched(searchedString, tempRandomStr)
    elif appState == State.PARTIALY_EQUAL:  # generate with
        print("partially equal")
        generateRandomWord(5)
    elif appState == State.ALL_EQUALS:
        print("We have succesfully generated your string!")


rerun()
