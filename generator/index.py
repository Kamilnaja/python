from state import State
from generator import generateRandomWord, generateResponseTable
from main import *
import sys

tempSearched = []
tries = 0
lenSearched = len(searched)
generatedResponseTable = generateResponseTable(searched)


def compareRandomWithSearched(searched, random):
    global appState
    print("random: " + random + " searched: " + searched)

    if "".join(searched) == generatedResponseTable:
        appState = State.ALL_EQUALS
        rerun()
    else:
        temporarySearchedReplacement = []
        randomIterator = iter(random)

        for x in searched:
            if x == "_":
                temporarySearchedReplacement.append("_")
            else:
                if x == next(randomIterator):
                    print("random: " + random + " searched: " + searched)
                    print("equal: " + x)
                    temporarySearchedReplacement.append("_")
                else:
                    temporarySearchedReplacement.append(x)

        global tempSearched
        tempSearched = temporarySearchedReplacement
        appState = State.PARTIALY_EQUAL
        rerun()


def rerun():
    global tries
    tries = tries + 1

    if appState == State.ALL_EQUALS:
        print("Good Job monkeys! finded!")
        print(" tries " + str(tries))
        exit()

    if appState == State.NONE_EQUAL:
        print("state none equal")
        compareRandomWithSearched(searched, generateRandomWord(lenSearched))

    if appState == State.PARTIALY_EQUAL:  # generate with
        compareRandomWithSearched(
            "".join(tempSearched), generateRandomWord(lenSearched)
        )


rerun()
