from state import State
from stringGen import generateRandomWord
from main import *
from generator import generateResponseTable
import sys

tempSearched = []
tries = 0
lenSearched = len(searched)
generatedResponseTable = generateResponseTable(searched)
print(generatedResponseTable)


def compareRandomWithSearched(searched, random):
    print('random: ' + random + ' searched: ' + searched)
    global appState

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
                    print('one equal: ' + x)
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
        # print("state partially: " + str(tries))
        # print("tempSearched: " + str)
        compareRandomWithSearched(
            "".join(tempSearched), generateRandomWord(lenSearched)
        )


rerun()
