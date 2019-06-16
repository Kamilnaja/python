def find_uniq(arr):
    # your code here
    for item in arr:
        if arr.count(item) == 1:
            return item;

arr = [ 1, 1, 1, 2, 1, 1 ]
arr2 = [1,1,1, 0.5]
print( find_uniq(arr2))