import itertools
import json
import re

# Check, if you can made anagram from given letters, that exists in dictionary
class Anagramer:
    def __init__(self, letters):
        self.letters = letters

    def readDict(self):
        return json.load(open("dict.json"))["words"]

    def anagrame(self):
        perms = list(itertools.permutations(self.letters))
        r = map(lambda item: re.sub("[^a-z]", "", str(item)), perms)
        for word in r:
            if word in self.readDict():
                return word
        return "not found"


letters = ["m", "o", "r", "l", "e"]
letters2 = ["t", "w", "d", "e", "l", "i", "k", "e", "n"]
an = Anagramer(letters2)
print(" You are searching for " + an.anagrame())
