import random
# class for getting new letters


class Bag:
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e']
        print(self.letters.__len__())

    def getLetters(self, count):
        return self.letters[random.randrange(0, self.letters.__len__())]

    def removeLetters(self, letter):
        return self.letters
