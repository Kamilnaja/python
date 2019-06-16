from functools import reduce
def find(n):
    div = []
    for x in range(1, n + 1):
        if (x % 3 == 0 or x % 5 == 0):
            div.append(x)        
    return reduce((lambda x, y: x + y), div)

print(find(10))
print(find(5))