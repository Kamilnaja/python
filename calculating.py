nums = [0, "operation", 0]
operators = ['*', '//', '+', '-']

def setupValues(val, numVal):
    if val == numVal:
        nums[2] = val
    if val in operators:
        nums[0] = numVal
        nums[1] = val
        return eval(printParsed())

def printParsed():
    return ','.join(str(e) for e in nums).replace(',', '')

def zero(val=0):
    return setupValues(val, 0)


def one(val=1):
    return setupValues(val, 1)
    

def two(val=2):
    return setupValues(val, 2)
    

def three(val=3):
    return setupValues(val, 3)

def four(val=4):
    return setupValues(val, 4)
    

def five(val=5):
    return setupValues(val, 5)
    

def six(val=6):
    return setupValues(val, 6)
    

def seven(val=7):
    return setupValues(val, 7)
    

def eight(val=8):
    return setupValues(val, 8)
    

def nine(val=9):
    return setupValues(val, 9)
    

def plus(val=0):
    return "+"

def minus(val):
    return "-"


def times(val):
    return "*"


def divided_by(val):
    return "//"

print(zero(plus(zero())))
print(zero(plus(one())))
print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(seven(divided_by(nine())))
