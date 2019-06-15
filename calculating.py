nums = [0, "operation", 0]
operators = ['*', '/', '+', '-']

def setupValues(val, numVal):
    if val == numVal:
        nums[2] = val
    if val in operators:
        nums[0] = numVal
        nums[1] = val

def printParsed():
    return ','.join(str(e) for e in nums).replace(',', '')

def zero(val=0):
    setupValues(val, 0)
    if val in operators:
        return eval(printParsed())

def one(val=1):
    setupValues(val, 1)
    if val in operators:
        return eval(printParsed())


def two(val=2):
    setupValues(val, 2)
    if val in operators:
        return eval(printParsed())


def three(val=3):
    setupValues(val, 3)
    if val in operators:
        return eval(printParsed())


def four(val=4):
    setupValues(val, 4)
    if val in operators:
        return eval(printParsed())


def five(val=5):
    setupValues(val, 5)
    if val in operators:
        return eval(printParsed())


def six(val=6):
    setupValues(val, 6)
    if val in operators:
        return eval(printParsed())


def seven(val=7):
    setupValues(val, 7)
    if val in operators:
        return eval(printParsed())


def eight(val=8):
    setupValues(val, 8)
    if val in operators:
        return eval(printParsed())


def nine(val=9):
    setupValues(val, 9)
    if val in operators:
        return eval(printParsed())


def plus(val=0):
    return "+"

def minus(val):
    return "-"


def times(val):
    return "*"


def divided_by(val):
    return "/"

print(zero(plus(zero())))
print(zero(plus(one())))
print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(seven(divided_by(nine())))