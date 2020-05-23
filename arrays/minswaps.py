

def minimumSwaps(arr):

    n = len(arr)
    visited = [0] * n
    tswaps = 0
    for x in range(n):
        i = arr[x]

        cycleLength = 0
        while(arr[i-1]!= i and visited[i-1] != 1):
            visited[i-1] = 1
            i = arr[i-1]
            cycleLength +=1
        if(cycleLength >1):
            tswaps+= cycleLength -1
    return tswaps

arr = [2,1,4,3]
minimumSwaps(arr)

print("The minimum number of swaps to sort in ascending order is " + str(minimumSwaps(arr)))