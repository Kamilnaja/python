from app import App

def start():
    print("Please enter searched sentence", end=" ")
    searchedSentence = input()
    app = App(searchedSentence)
    app.rerun()


start()
