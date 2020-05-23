

def rotateArray(arr,k):
    n = len(arr)
    rotated = [0] * n
    for x in range(0, n-k):
        rotated[x] = arr[x+k]
    for x in range(n - k, n):
        rotated[x] = arr[x-(n-k)]
    return rotated




arr = [1,2,3,4,5,6]



b = rotateArray(arr, 4)
    # for x in range(n-k, n):


arr = [33,47,70,37,8,53,13,93,71,72,51,100,60,87,97]
b = rotateArray(arr, 13)