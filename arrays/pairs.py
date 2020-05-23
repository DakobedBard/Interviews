'''
How many pairs of elements have a difference equal to the target value




'''

arr = [1,5,3,4,2]
target = 2

def npairs(k, arr):
    a = set(arr)
    b = set(x + k for x in arr)

    return len(a&b)

print("The number of overlap is " + str(npairs(2, arr)))