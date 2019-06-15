
nums = [0, 'operation', 0]

def setupValues(val, numVal):
    if val == numVal:
        nums[2] = val
    if isinstance(val, str):
        nums[0] = numVal
        nums[1] = val
    

def zero(val=0):
    return setupValues(val, 0)


def one(val=1):
    setupValues(val, 1)
    
def two(val=2):
    setupValues(val, 2)

def three(val=3):
    setupValues(val, 3)

def four(val=3):
    setupValues(val, 4)

def five(val=5):
    setupValues(val, 5)

def six(val=6):
    setupValues(val, 6)

def seven(val=7):
    setupValues(val, 7)

def eight(val=8):
    setupValues(val, 8)

def nine(val=9):
    setupValues(val, 9)

def plus(val=0):
    return '+'

def minus(val):
    return "-"

def times(val):
    return '*'

def divided_by(val):
    return "/"

# one(plus(one()))
# print(nums[0], nums[1], nums[2], 'one one')
# strToCalculate = ','.join([str(x) for x in nums]).replace(',', '')
# print(eval(strToCalculate))


# zero(plus(zero()))
# print(nums[0], nums[1], nums[2], 'zero zero')
# strToCalculate = ','.join([str(x) for x in nums]).replace(',', '')
# print(eval(strToCalculate))

# two(plus(one()))
# print(nums[0], nums[1], nums[2], 'two one')
# strToCalculate = ','.join([str(x) for x in nums]).replace(',', '')
# print(eval(strToCalculate))


# two(plus(three()))
# print(nums[0], nums[1], nums[2], 'two three')
# strToCalculate = ','.join([str(x) for x in nums]).replace(',', '')
# print(eval(strToCalculate))


# nine(divided_by(five()))
# print(nums[0], nums[1], nums[2], 'nine five')
# strToCalculate = ','.join([str(x) for x in nums]).replace(',', '')
# print(eval(strToCalculate))

# seven(times(five()))
print(zero(plus(zero())))