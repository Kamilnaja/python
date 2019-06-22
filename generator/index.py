from state import State
from generator import Generator


class Comparator:
    temporarySearchedReplacement = ""

    @staticmethod
    def compareRandomWithSearched(searched, random):
        print("random: " + random + " searched: " + searched)

        if "".join(searched) == Generator.generateResponseTable(searched):
            return [State.ALL_EQUALS, False]
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

            # App.searchedTemp =

            return [State.PARTIALY_EQUAL, temporarySearchedReplacement]


class App:
    searchedTemp = ""

    def __init__(self):
        self.searched = "wodka czysta"
        self.appState = State.NONE_EQUAL
        self.tries = 0

    def rerun(self):
        self.tries = self.tries + 1
        if self.appState == State.ALL_EQUALS:
            print("Good Job monkeys! finded!")
            print(" tries " + str(self.tries))
            exit()

        if self.appState == State.NONE_EQUAL:
            res = Comparator.compareRandomWithSearched(
                self.searched, Generator.generateRandomWord(len(self.searched))
            )
            self.appState = res[0]
            App.searchedTemp = res[1]

            app.rerun()

        if self.appState == State.PARTIALY_EQUAL:
            res = Comparator.compareRandomWithSearched(
                "".join(App.searchedTemp),
                Generator.generateRandomWord(len(self.searched)),
            )
            self.appState = res[0]
            App.searchedTemp = res[1]
            app.rerun()


app = App()
app.rerun()

