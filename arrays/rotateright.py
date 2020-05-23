


def rotate(nums, k):
    rotated = [0] * len(nums)
    n = len(nums)
    for x in range(0, k):
        rotated[x] = nums[n-k+x]
    for x in range(k, n):
        rotated[x] = nums[x-k]

    return  rotated

arr = [1,2,3,4,5,6,7]
r = rotate(arr, 3)