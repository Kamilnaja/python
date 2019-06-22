from state import State
from comparator import Comparator
from generator import Generator


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

