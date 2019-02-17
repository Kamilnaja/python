# def points(games):
#     result = 0
#     for val in games:
#         res = val.split(':')
#         if res[0] > res[1]:
#             result += 3
#         elif res[0] == res[1]:
#             result += 1
#     return result


# print(
#     points(['1:0', '2:0', '3:0', '4:0', '2:1',
#             '3:1', '4:1', '3:2', '4:2', '4:3'])
# )

# points(['1:0', '2:0', '3:0', '4:0', '2:1',
#         '3:1', '4:1', '3:2', '4:2', '4:3'])

def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)


array1 = [True,  True,  True,  False,
          True,  True,  True,  True,
          True,  False, True,  False,
          True,  False, False, True,
          True,  True,  True,  True,
          False, False, True,  True]

print(count_sheeps(array1) == 17)
print(count_sheeps(array1))
