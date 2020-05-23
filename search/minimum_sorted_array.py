

def findMin(nums):
    if len(nums) ==0:return -1
    if len(nums) ==1: return nums[0]

    left = 0
    right = len(nums) - 1

    # This case not rotated
    if nums[left] < nums[right]:
        return nums[0]

    # Binary Search

    while right >= left:
        mid = int(left + (right-left)/2)

        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        if nums[mid] < nums[mid-1]:
            return nums[mid-1]
        if nums[mid] < nums[0]:
            right = mid-1
        else:
            left = mid+1



arr = [3,1,2]
print("The minimum element is {} ".format(findMin(arr)))