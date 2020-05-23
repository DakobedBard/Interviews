



def minimumAbsDistance(arr):
    if len(arr) == 0:
        return 0
    min_diff = float('inf')
    arr = sorted(arr)
    min_indices = []

    for i in range(len(arr) - 1):
        diff = abs(arr[i]) - arr[i + 1]
        if diff < min_diff:
            min_diff = diff
            min_indices = []
            min_indices.append([i, i + 1])
        elif diff == min_diff:
            min_indices.append([i, i + 1])

    return min_indices

nums = [4,2,1,3]
result = minimumAbsDistance(nums)
print("The minimum distance is {}".format(minimumAbsDistance(nums)))