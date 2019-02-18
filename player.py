import json
import itertools


class Player:
    def __init__(self, letters):
        self.letters = letters

    # check every with dictionary
    def readDict(self):
        jsonData = open('dict.json').read()

    with open('dict.json') as f:
        data = json.load(f)

    print(data["words"][0])

    def checkWordWithDictionary(self):
        return "stub"

    # create combination from current letters
    def combine(self):
        return list(itertools.permutations(self.letters))

    def evaluateScore(self):
        return "evaluate score"
