# from state import State
# from index import Comparator
# from generator import Generator


# class App:
#     def __init__(self):
#         self.searched = "wodka czysta"
#         self.appState = State.NONE_EQUAL
#         self.tries = 0

#     def rerun(self):
#         self.tries = self.tries + 1
#         if self.appState == State.ALL_EQUALS:
#             print("Good Job monkeys! finded!")
#             print(" tries " + str(self.tries))
#             exit()

#         if self.appState == State.NONE_EQUAL:
#             self.appState = Comparator.compareRandomWithSearched(
#                 self.searched, Generator.generateRandomWord(len(self.searched))
#             )
#             app.rerun()

#         if self.appState == State.PARTIALY_EQUAL:
#             self.appState = Comparator.compareRandomWithSearched(
#                 "".join(tempSearched), Generator.generateRandomWord(len(self.searched))
#             )
#             app.rerun()


# app = App()
# app.rerun()

