



def search(nums, target):
    if nums == None or len(nums) == 0:
        return -1
    left = 0
    right = len(nums) -1

    while left< right:
        mid = int(left + (right-left)/2)
        if nums[mid] > nums[right]:
            left = mid +1
        else:
            right = mid

    start = left
    left = 0
    right = len(nums) - 1

    if target >= nums[start] and target <= nums[right]:
        left = start
    else:
        right = start

    while left <= right:
        mid = int(left + (right-left)/2)
        if nums[mid] == target:
            return  mid
        if nums[mid] < target:
            left = mid +1
        else:
            right = mid -1
    return -1



nums = [7,0,1,2,3,4,5,6]
target = 5
print("The array contains the value {} at index {} ".format(target, search(nums, target)))