import random
from state import State
from stringGen import generateRandomWord
from main import *
from generator import generateResponseTable
import sys

sys.setrecursionlimit(400000)
tempSearched = []
tries = 0
lenSearched = len(searched)

def compareRandomWithSearched(searched, random):
    global appState

    if "".join(searched) == generateResponseTable(searched):
        appState = State.ALL_EQUALS
        rerun()
        return

    temporarySearchedReplacement = []
    searchedIterator = iter(searched)
    randomIterator = iter(random)

    for x in searched:
        if x == "_":
            temporarySearchedReplacement.append("_")
        else:
            if next(searchedIterator) == next(randomIterator):
                temporarySearchedReplacement.append("_")
            else:  # jeżeli nie znajdzie aktualnie dopasowania żadnego
                temporarySearchedReplacement.append(x)

    global tempSearched
    tempSearched = temporarySearchedReplacement
    appState = State.PARTIALY_EQUAL
    rerun()
    return


def rerun():
    global tries
    tries = tries + 1
    
    if appState == State.NONE_EQUAL:
        print("state none equal")
        compareRandomWithSearched(searched, generateRandomWord(lenSearched))

    elif appState == State.PARTIALY_EQUAL:  # generate with
        print("state partially: " + str(tries))
        compareRandomWithSearched(
            "".join(tempSearched), generateRandomWord(lenSearched)
        )

    elif appState == State.ALL_EQUALS:
        print("state all")
        print("Good Job monkeys! finded!")
        print(" tries " + str(tries))


rerun()
