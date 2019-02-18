import itertools
import json

jsonData = open('dict.json').read()

letters = ['a', 'g', 'a']

with open('dict.json') as f:
    data = json.load(f)

print(data["words"][0])


def check():
    return "checking"
