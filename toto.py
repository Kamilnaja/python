#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

numbers = range(1, 42)
choosen = []

print("Witamy komisje kontroli gier i zakładów")


def getLots():
    return random.randrange(0, len(numbers))


def getRandom():
    # generate random number
    randNum = getLots()
    print("wylosowana liczba to " + str(numbers[randNum]))
    # put into array
    choosen.append(numbers[getLots()])
    # remove

    del (numbers[randNum])


for i in xrange(5):
    getRandom()

print("dziękujemy za udział w losowaniu")
