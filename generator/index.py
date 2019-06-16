import random
from state import State
from stringGen import generateRandomWord
from main import *

tempSearchedStr = []


def compareRandomWithSearched(searched, random):
    global appState
    if searched == "_____":
        appState = State.ALL_EQUALS

    searchedIterator = iter(searched)
    randomIterator = iter(random)
    for x in searchedString:
        if next(searchedIterator) == next(randomIterator):
            # print("equal letter" + ": " + x + ":" + random + " searched : " + searched)
            tempSearchedStr.append("_")
        else:  # jeżeli nie znajdzie aktualnie dopasowania żadnego
            tempSearchedStr.append(x)
            print("not found ")

    print(tempSearchedStr)
    appState = State.PARTIALY_EQUAL
    print("rerun!")
    rerun()


def rerun():
    if appState == State.NONE_EQUAL:
        print("state = " + str(appState))
        print("searched: " + searchedString)
        compareRandomWithSearched(searchedString, generateRandomWord())

    elif appState == State.PARTIALY_EQUAL:  # generate with
        print("state = " + str(appState))

        compareRandomWithSearched(
            ",".join(tempSearchedStr).replace(",", ""), generateRandomWord()
        )

    elif appState == State.ALL_EQUALS:
        print("state = " + str(appState))
        print("We have succesfully generated your string!")
        return


rerun()
