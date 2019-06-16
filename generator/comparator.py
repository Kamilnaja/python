from variables import *
from generator import generateResponseTable

def compareRandomWithSearched(searched, random):
    print('compareRandom : searched ' + searched)
    global appState
    temporarySearchedReplacement = []
    print('searched :' + searched)
    if "".join(searched) == generateResponseTable():
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
