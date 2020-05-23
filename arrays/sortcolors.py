def sortColors(nums):
    if not nums:
        return nums
    start =0
    end = len(nums) - 1
    n = 0
    while n <= end:
        if nums[n] == 0 and n > start:
            nums[start], nums[n] = nums[n], nums[start]
            start += 1
        elif nums[n] == 2:
            nums[end], nums[n] = nums[n], nums[end]
            end -= 1
        else:
            n += 1


nums = [1,0,2]
sortColors(nums)