import random
from state import State
from stringGen import generateRandomWord
from main import *

tempSearched = []

def genResTable():
    resTable = []
    for x in searched:
        resTable.append('_')
    return ''.join(resTable)

def compareRandomWithSearched(searched, random):
    print('compareRandom : searched ' + searched)
    global appState
    temporarySearchedReplacement = []
    print('searched :' + searched)
    if "".join(searched) == genResTable():
        appState = State.ALL_EQUALS
        print('Good Job monkeys! finded!')
        return

    searchedIterator = iter(searched)
    randomIterator = iter(random)

    for x in searched:
        print("letter" + " : " + x + ":" + random + " searched : " + searched)
        print('searchedString ' + x)
        if x == '_':
            print('dash')
            temporarySearchedReplacement.append("_")
        else: 
            if next(searchedIterator) == next(randomIterator):
                print("is equal " + x)
                temporarySearchedReplacement.append("_")
            else:  # jeżeli nie znajdzie aktualnie dopasowania żadnego
                temporarySearchedReplacement.append(x)
                print("not found ")

    print("temp " + "".join(temporarySearchedReplacement))
    print("rerun!")
    global tempSearched
    tempSearched = temporarySearchedReplacement
    print(tempSearched)
    print("tempSearchedStr :" + "".join(tempSearched))
    appState = State.PARTIALY_EQUAL
    rerun()


def rerun():
    if appState == State.NONE_EQUAL:
        print("state = " + str(appState))
        print("searched: " + searched)
        compareRandomWithSearched(searched, generateRandomWord())

    elif appState == State.PARTIALY_EQUAL:  # generate with
        print("state = " + str(appState))
        print('tempSearchedStr ' + "".join(tempSearched))
        compareRandomWithSearched("".join(tempSearched), generateRandomWord())

    elif appState == State.ALL_EQUALS:
        print("state = " + str(appState))
        print("We have succesfully generated your string!")
        return


rerun()
